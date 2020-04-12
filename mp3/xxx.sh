#!/bin/bash

ARTIST='Katy Davis Henderson'

for i in *.m4a
do
echo "$i"
TITLE=$(echo $i |cut -d '-' -f5 | cut -d'(' -f1 | sed -e 's/^ //' -e 's/ $//')
TUNENAME=$(slugify.sh "$TITLE")
lame -V2 --tt "$TITLE" --ta "$ARTIST" --id3v2-only "$i" "$TUNENAME".mp3
done

