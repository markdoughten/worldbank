#!/bin/bash

countries="./countries.txt"
commands="./commands.txt"

remove () {
    if [ -f "$1" ] ; then
        rm "$1"
    fi
}

remove $commands
remove $countries
python ../main.py help > $commands
python ../main.py countries > $countries

while read -r line
do
  awk '{print $1;}'
done < "$countries"
