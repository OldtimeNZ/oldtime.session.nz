#!/usr/bin/env python3
# encoding: utf-8

import os
import re
import eyed3
import datetime

today = datetime.date.today()

def slugify(s):
    """
    Simplifies ugly strings into something URL-friendly.
    >>> print slugify("[Some] _ Article's Title--")
    some-articles-title
    """

    # "[Some] _ Article's Title--"
    # "[some] _ article's title--"
    s = s.lower()

    # "[some] _ article's_title--"
    # "[some]___article's_title__"
    for c in [' ', '-', '.', '/']:
        s = s.replace(c, '_')

    # "[some]___article's_title__"
    # "some___articles_title__"
    s = re.sub('\W', '', s)

    # "some___articles_title__"
    # "some   articles title  "
    s = s.replace('_', ' ')

    # "some   articles title  "
    # "some articles title "
    s = re.sub('\s+', ' ', s)

    # "some articles title "
    # "some articles title"
    s = s.strip()

    # "some articles title"
    # "some-articles-title"
    s = s.replace(' ', '-')

    return s


for file in os.listdir("."):
    if file.endswith(".mp3"):

        print (file)
        audiofile = eyed3.load(file)
        artist = audiofile.tag.artist
        title = audiofile.tag.title
        album = audiofile.tag.album
        #print(title)

        mp3File = slugify(title) + '.mp3'
        mdFile = slugify(title) + '.md'

        if (album == None):
            album = 'https://www.youtube.com/user/katiehendersonfiddle'

        with open(mdFile, 'w') as md:
            md.write("""---
title: {0}
titleID: {5}
key:
rhythm:
notes:
date: {1}
location:
tags: cm
repeats:
parts:
regtuneoftheweek:
slowtuneoftheweek:
mp3_file: /mp3/{3}
mp3_source: <a href="{2}">{4}</a>
mp3_licence: "© {4}. All Rights Reserved."
mp3_url: {2}
source: Wellington
abc_source:
abc_url:
abc:

---
""".format(title, today, album, mp3File, artist, mdFile))

        os.rename(file, mp3File)
