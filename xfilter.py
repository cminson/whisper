#!/usr/local/bin/python
# 
# Run locally on Mac to filter input files for whisper
#
import json
import os

PATH_CONFIG = './CONFIG00.JSON'
PATH_TOP200 = './TOP200.JSON'
PATH_INPUT = './input/'
PATH_OUTPUT = './output/'

#
# Filter all completed talks
#
list_transcriptions = os.listdir(PATH_OUTPUT)
list_transcriptions = [file_path for file_path in list_transcriptions if '.txt' in file_path]
for path_transcription in list_transcriptions:
    file_name = path_transcription.split('/')[-1]
    file_name = file_name.strip('.txt')
    path_input = PATH_INPUT + file_name
    if os.path.exists(path_input):
        print("Deleting transcribed  mp3: ", path_input)
        os.remove(path_input)

#
exit()

#
# filter all guided meditations
#
list_mp3 = os.listdir(PATH_INPUT)
for file_name in list_mp3:
    if 'guided' in file_name:
        path_mp3 = PATH_INPUT + file_name
        print("Deleting guided meditation mp3: ", path_mp3)
        os.remove(path_mp3)


#
# filter all previous transcriptions
#
print("filtering previously transcribed")
fd = open(PATH_CONFIG,'r')
data  = json.load(fd)
list_transcripts = data['albums'][7]['talks']

for transcript in list_transcripts:
    url = transcript['url']
    file_name = url.split('/')[-1]
    path_filtered_talk = PATH_INPUT + file_name
    if os.path.exists(path_filtered_talk):
        print("Filtering: ", path_filtered_talk)
        os.remove(path_filtered_talk)

#
# filtering top 200 (previously test transcribed)
#
print("filtering top 200")
fd = open(PATH_TOP200,'r')
data  = json.load(fd)
list_talks = data['talks']

for talk in list_talks[0:200]:
    url = talk['url']
    file_name = url.split('/')[-1]
    path_filtered_talk = PATH_INPUT + file_name
    #print(path_filtered_talk)
    if os.path.exists(path_filtered_talk):
        print("Filtering: ", path_filtered_talk)
        os.remove(path_filtered_talk)


