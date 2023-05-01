#!/usr/local/bin/python
import os
import sys
import json
from os import path
import subprocess


PATH_MP3 = '/Volumes/AudioDharma/AD/TALKS_BACKUP'
PATH_TRANSCRIPT = './transcripts/'
CONFIG_JSON = '/Volumes/AudioDharma/AD/CONFIG00.JSON'

COMMAND = '/Library/Frameworks/Python.framework/Versions/3.10/bin/whisper --verbose False  /Volumes/AudioDharma/AD/TALKS_BACKUP/{} -o ./transcripts'


ARG_MUST_INCLUDE = '.mp3'     # default filter -> accept all mp3s
if len(sys.argv) > 1:
    ARG_MUST_INCLUDE = sys.argv[1]

with open(CONFIG_JSON,'r') as fd:
    list_talks  = json.load(fd)['talks']

for talk in list_talks:
    url = talk['url']
    date = talk['date']

    # tmp filters
    if 'Teacher' in url: continue
    if 'Fronsdal' in url: continue

    # only convert talk if it has ARG_MUST_INCLUDE in date
    if ARG_MUST_INCLUDE not in date: 
        print(f'filtering via {ARG_MUST_INCLUDE}: {url}')
        continue

    file_mp3 = os.path.basename(url)
    file_transcript = file_mp3 + '.txt'
    path_mp3 = os.path.join(PATH_MP3, file_mp3)
    path_transcript = os.path.join(PATH_TRANSCRIPT, file_transcript)

    # don't try to transcribe a non-existent mp3
    if path.exists(path_mp3) == False:
        print(f'skipping: {path_mp3}')
        continue

    #print(path_mp3)
    #print(path_transcript)

    # if transcript already exists, skip it
    if path.exists(path_transcript):
        print(f'skipping: {path_transcript}')
        continue

    # all good.  form the whisper command and execute
    command = COMMAND.format(file_mp3)
    #print(command)
    print("creating transcript: ", path_transcript)
    subprocess.run(command, shell=True)

    # clean up the unneeded files
    path_vtt = path_transcript.replace('.vtt', '')
    path_srt = path_transcript.replace('.srt', '')
    os.remove(path_vtt)
    os.remove(path_srt)

