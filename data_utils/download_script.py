#!pip install pandas fastparquet tqdm requests

import argparse
import pandas as pd
import requests
import os
from tqdm import tqdm
import logging


def download_file(url:str)->bytes:
    """ This function downloads and returns the content of the given url

    Args:
        url (str): the url of the file to be downloaded

    Raises:
        e: The exception that is raised by the request module 

    Returns:
        file_content (bytes): The file content downloaded from the url
    """

    try:
        file_content = requests.get(url, allow_redirects=True).content
        return file_content
    except requests.exceptions.RequestException as e:
        logger.error(f'Failed to download {url}')
        raise e



def save_audio_content(target_file: str, file_content: bytes):
    """This function saves the downloaded content passed via `file_content' in the `target_file'

    Args:
        target_file (str): the target path for the file content to be saved to
        file_content (bytes): the content to be saved
    
    Raises:
        e: the IOError raised by the writing operation
    """
    try:
        with open(target_file, 'wb') as file:
            file.write(file_content)
    except IOError as e:
        logger.error(f'Failed to save {target_file}')
        raise e



def main(args):

    # reading the metadata parquet file
    metadata = pd.read_parquet(args.metadata)
    
    # going through the list of ids, downloading, and saving each file
    for sample_id in tqdm(metadata['sample_id']):
        
        # check to see if the file exists and should be skipped
        target_file = os.path.join(args.target_path, f'{sample_id:06}.flac')
        if os.path.exists(target_file):
            continue
        
        # downloading the file content from url
        url = f"{args.base_url}/ambisonics/{sample_id:06}.flac"
        audio_content = download_file(url)

        # saving the content into the file
        save_audio_content(target_file=target_file, file_content=audio_content)
        
        logger.info(f'Successfully downloaded {url}')

    logger.info(f'Download Complete')


if __name__=='__main__':
    
    # setup the system arg parser
    parser = argparse.ArgumentParser()
    
    # args for establishing dir structure 
    parser.add_argument("--metadata", type=str, required=False,default='../data/metadata.parquet', help="the path to the metada.parquet file")
    parser.add_argument("--target_path", type=str, required=False, default='../data/audio_files', help="the path to the target folder to download the dataset to")
    parser.add_argument("--log_dir", type=str, required=False, default='../logs', help="the target path for logs to be saved")
    

    parser.add_argument("--base_url", type=str, required=False, default='https://docs-assets.developer.apple.com/ml-research/datasets/spatial-librispeech/v1', help="the base url for the SLS dataset")

    args = parser.parse_args()

    # setting up logger
    global logger
    os.makedirs(args.log_dir, exist_ok=True)
    logging.basicConfig(filename=os.path.join(args.log_dir, 'downloader.log'), level=logging.INFO)
    logger = logging.getLogger()
    

    # running the main script 
    main(args=args)