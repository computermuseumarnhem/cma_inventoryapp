#!/bin/sh

sizes="200x200 300x300"

for file in *.jpg;
do
    name=${file%%.jpg}
    convert ${name}.jpg ${name}.png

    for size in $sizes
    do
        convert \
            "${name}.png" \
                -scale $size \
                -background none -gravity center -extent $size \
            "${size}/${name}.png"
    done
done
