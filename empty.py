#!/usr/local/bin/python
import os

PATH_TRANSCRIPTS = './transcripts'

# iterate over the files in the directory
for transcript in os.listdir(PATH_TRANSCRIPTS):
    path_transcript = os.path.join(PATH_TRANSCRIPTS, transcript)
    if os.path.isfile(path_transcript) and os.path.getsize(path_transcript) == 0:
        print(f'rm {path_transcript}')

