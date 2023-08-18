Spatial LibriSpeech Schema
==========================

This document describes the metadata schema for Spatial LibriSpeech. The metadata is organised as
columns of a pandas' DataFrame. We first describe how to load the dataframe, and then list all its
columns.

### Loading the metadata

Once you have downloaded any the dataset you can load the dataset with the following command:

```python3
import pandas as pd
metadata = pd.read_parquet("<path_to_dataset>/metadata.parquet")
```

Alternatively, you can download the metadata directly from the internet:

```python3
import pandas as pd
metadata = pd.read_parquet("https://docs-assets.developer.apple.com/ml-research/datasets/spatial-librispeech/v1/metadata.parquet")
```

The rest of this document describes the metadata schema for Spatial LibriSpeech (organised by
columns in the dataframe)


## Sample identification metadata

- `sample_id`
  * Type: `int`
  * Range: [0, 22]
  * Dataloader feature: `spatial_librispeech.Feature.SAMPLE_ID`
  * Numeric identifier for sample. Corresponding audio files will be named `{sample_id:06}.flac`.

- `split`
  * Type: `string`
  * Values: [`train`, `test`]
  * Determines whether current sample belongs to the train or the test set.

- `lite_version`
  * Type: `boolean`
  * If true, current sample is part of the lite version of the dataset.


## Acoustics metadata
- `acoustics/frequency_bins`
  * Type: `numpy.array` of 33 `floats`
  * Unit: hertz
  * Dataloader feature: `spatial_librispeech.Feature.FREQUENCY_BINS`
  * Mean frequency values of the third octave bins used for all acoustic features.

- `acoustics/c50_db`
  * Type: `numpy.array` of 33 `floats`
  * Unit: decibels
  * Dataloader feature: `spatial_librispeech.Feature.C50_DB`
  * Third octave values of speech clarity (C50) in decibels.

- `acoustics/drr_db`
  * Type: `numpy.array` of 33 `floats`
  * Unit: decibels
  * Dataloader feature: `spatial_librispeech.Feature.DRR_DB`
  * Third octave values of direct-to-reverberant-ratio (DRR) in decibels.

- `acoustics/edt_ms`
  * Type: `numpy.array` of 33 `floats`
  * Unit: milliseconds
  * Dataloader feature: `spatial_librispeech.Feature.EDT_MS`
  * Third octave values of early-decay time (EDT) in milliseconds.

- `acoustics/t20_ms`
  * Type: `numpy.array` of 33 `floats`
  * Unit: milliseconds
  * Dataloader feature: `spatial_librispeech.Feature.T20_MS`
  * Third octave values of 20dB decay duration (T20) in milliseconds.

- `acoustics/t30_ms`
  * Type: `numpy.array` of 33 `floats`
  * Unit: milliseconds
  * Dataloader feature: `spatial_librispeech.Feature.T30_MS`
  * Third octave values of 30dB decay duration (T30) in milliseconds.


## Audio information

- `audio_info/duration`
  * Type: `float`
  * Unit: seconds
  * Sample duration in seconds.

- `audio_info/frames`
  * Type: `int`
  * Unit: seconds
  * Number of frames in audio sample. Note sample rate is 16kHz.

- `audio_info/size/ambisonics`
  * Type: `int`
  * Unit: bytes
  * Size of speech ambisonics sample in bytes.

- `audio_info/size/noise_ambisonics`
  * Type: `int`
  * Unit: bytes
  * Size of distractor noise ambisonics sample in bytes.

- `audio_info/checksum/ambisonics`
  * Type: `string`
  * Hexadecimal representation of sha-256 checksum of speech ambisonics sample.

- `audio_info/checksum/noise_ambisonics`
  * Type: `string`
  * Hexadecimal representation of sha-256 checksum of distractor noise ambisonics sample.


## Speech metadata

- `speech/azimuth`
  * Type: `float`
  * Unit: radians
  * Dataloader feature: `spatial_librispeech.Feature.AZIMUTH`
  * Horizontal angle between speech source and microphone array.

- `speech/elevation`
  * Type: `float`
  * Unit: radians
  * Dataloader feature: `spatial_librispeech.Feature.ELEVATION`
  * Vertical angle between speech source and microphone array.

- `speech/distance`
  * Type: `float`
  * Unit: meters
  * Dataloader feature: `spatial_librispeech.Feature.DISTANCE`
  * Distance between speech source and microphone array.

- `speech/speaking_azimuth`
  * Type: `float`
  * Unit: radians
  * Dataloader feature: `spatial_librispeech.Feature.SPEAKING_AZIMUTH`
  * Horizontal rotation of speech source with respect to microphone array. Zero is in direct line of array.

- `speech/speaking_elevation`
  * Type: `float`
  * Unit: radians
  * Dataloader feature: `spatial_librispeech.Feature.SPEAKING_ELEVATION`
  * Vertical rotation of speech source with respect to microphone array. Zero is in direct line of array.

- `speech/mrp`
  * Type: `float`
  * Unit: decibels at random active speech level (dB-ASL)
  * Signal power for speech at mouth reference point (25 mm in front of the lip plane,cf. ITU-T P.58)

- `speech/source_id`
  * Type: `float`
  * Range: [1, 20]
  * Numeric identifier for speech source location in the room.

- `speech/directivity_id`
  * Type: `int`
  * Range: [0, 15]
  * Dataloader feature: `spatial_librispeech.Feature.DIRECTIVITY_ID`
  * Numeric identifier for the different directivity profiles applied to speech.


### Original LibriSpeech metadata

- `speech/librispeech_metadata/book_id"`
  * Type: `int`
  * * Dataloader feature: `spatial_librispeech.Feature.BOOK_ID`
  * Numeric identifier for book being read.

- `speech/librispeech_metadata/chapter_id"`
  * Type: `int`
  * Dataloader feature: `spatial_librispeech.Feature.CHAPTER_ID`
  * Numeric identifier for chapter being read.

- `speech/librispeech_metadata/chapter_title"`
  * Type: `string`
  * Name of chapter being read.

- `speech/librispeech_metadata/project_id"`
  * Type: `int`
  * Dataloader feature: `spatial_librispeech.Feature.PROJECT_ID`
  * Numeric identifier for project being read.

- `speech/librispeech_metadata/project_title"`
  * Type: `string`
  * Name of project being read.

- `speech/librispeech_metadata/reader_id"`
  * Type: `int`
  * Numeric identifier for reader.

- `speech/librispeech_metadata/reader_name"`
  * Type: `string`
  * Name (or alias) of reader.

- `speech/librispeech_metadata/reader_sex"`
  * Type: `string`
  * Dataloader feature: `spatial_librispeech.Feature.READER_SEX`
  * Values: [`m`, `f`]  # TODO: verify these
  * Sex of reader.

- `speech/librispeech_metadata/sequence_number"`
  * Type: `int`
  * Dataloader feature: `spatial_librispeech.Feature.SEQUENCE_NUMBER`
  * Sequence identifier for utterance (will be ordered for same project, book, and chapter).

- `speech/librispeech_metadata/transcription"`
  * Type: `string`
  * Dataloader feature: `spatial_librispeech.Feature.TRANSCRIPTION`
  * Transcription of text being read.

- `speech/librispeech_metadata/subset"`
  * Type: `string`
  * Values: [`train-clean-100`, `train-clean-360`, `test-clean`, `test-other`]
  * Original librispeech subset for utterance.

## Noise metadata

- `noise/azimuth`
  * Type: `float`
  * Unit: radians
  * Dataloader feature: `spatial_librispeech.Feature.NOISE_AZIMUTH`
  * Horizontal angle between distractor noise source and microphone array.

- `noise/elevation`
  * Type: `float`
  * Unit: radians
  * Dataloader feature: `spatial_librispeech.Feature.NOISE_ELEVATION`
  * Vertical angle between distractor noise source and microphone array.

- `noise/distance`
  * Type: `float`
  * Unit: meters
  * Dataloader feature: `spatial_librispeech.Feature.NOISE_DISTANCE`
  * Distance between distractor noise source and microphone array.

- `noise/snr`
  * Type: `float`
  * Unit: decibels
  * Dataloader feature: `spatial_librispeech.Feature.SNR_DB`
  * Signal-to-noise ratio for distractor noise in decibels.

- `noise/source_id`
  * Type: `float`
  * Range: [1, 20]
  * Numeric identifier for distractor noise source location in the room.

- `noise/deep_noise_suppression_metadata/filename`
  * Type: `string`
  * Filename of noise in deep noise suppression.

- `noise/deep_noise_suppression_metadata/is_audioset`
  * Type: `boolean`
  * If true, noise is part of Audioset dataset, otherwise it is part of Freesound dataset.

- `noise/deep_noise_suppression_metadata/is_audioset`
  * Type: `string`
  * Comma-separated labels for noise, for Audioset you may need to consult lookup table.

- `noise/deep_noise_suppression_metadata/youtube_id`
  * Type: `string`
  * Only available for Audioset samples, youtube id of video from where noise was extracted.


## Room metadata

- `room/room_id`
  * Type: `int`
  * Dataloader feature: `spatial_librispeech.Feature.ROOM_ID`
  * Numeric identifier for simulated simulated room.

- `room/floor_area`
  * Type: `float`
  * Unit: squared meters
  * Room's floor surface area.

- `room/surface_area`
  * Type: `float`
  * Unit: squared meters
  * Sum of the area of all surface (floor, walls, ceiling) in the room.

- `room/volume`
  * Type: `float`
  * Unit: cubic meters
  * Room's total volume.
