#!/usr/bin/env python3
# encoding: utf-8

import os
import sys
import shutil
from mutagen.mp3 import MP3
from slugify import slugify

mp3SrcDir = '/home/asjl/GitHub/oldtime.session.nz/mp3'
#mp3DestDir = '/var/www/html/mp3/' + year
mdDestDir = '/home/asjl/GitHub/oldtime.session.nz/_tunes/NEW/'

if os.path.isdir(mp3SrcDir):
    os.chdir(mp3SrcDir)
    totalMP3 = 0
    goodMP3 = 0
    for fileName in os.listdir('.'):
        print("Processing: " + fileName)
        if fileName.endswith(".mp3"):
            totalMP3 += 1
            audiofile = MP3(fileName)
            try:
                title = str(audiofile["TIT2"])
            except:
                print('"Title" ID3 tag not found')
                print('Add using \'mid3v2 -t "title string" {0}\''.format(fileName))
                continue

            try:
                artist = str(audiofile["TPE1"])
            except:
                print('"Artist" ID3 tag not found')
                print('Add using \'mid3v2 -a "artist name" {0}\''.format(fileName))
                continue

            goodMP3 += 1
            # Rename and move the mp3 file into the production directory
            mp3File = slugify(title) + '.mp3'
            os.rename(fileName, mp3File)

            # Create the mdFile based on the ID3 tags in the mp3 file
            mdFile = slugify(title) + '.md'
            with open(mdDestDir + mdFile, 'w') as md:
                md.write("""---
title: {0}
titleID: {3}
key:
rhythm:
notes:
repeats:
parts:
date: 2020-04-19
mp3_file: /mp3/{1}
mp3_source: {2}
mp3_licence: "© {2}. All Rights Reserved."
mp3_url:
source: Wellington
abc_source:
abc_url:
abc:
---
""".format(title, mp3File, artist, mdFile))

    if totalMP3:
        print("Processed {0} of {1} mp3 files".format(goodMP3, totalMP3))
        if (goodMP3 != totalMP3):
            print("""Fix ID3 tag errors in the mp3 files in '{0}'

Re-run the script.
""".format(mp3SrcDir))
    else:
        print("""No mp3 files left to process in '{0}'
""".format(mp3SrcDir))
else:
    print("""'{0}': no such directory

Create the directory '{0}' and place the mp3 files marked up with the necessary
ID3 tags in that directory.

Re-run the script.
""".format(mp3SrcDir))
