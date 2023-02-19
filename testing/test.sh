#!/bin/bash

f_countries="./countries.txt"
f_commands="./commands.txt"
declare -a countries=()
declare -a commands=()
counter=0

remove() {
  if [ -f $1 ] ; then
    rm $1
  fi
}

second() {
  
  arr=($@)  
  while read -r line
  do
    arr=($(awk 'FNR > 1 {print $2;}'))
  done < $1
  echo ${arr[*]}
 
}

remove $f_commands
remove $f_countries
python ../main.py help > $f_commands
python ../main.py countries > $f_countries
countries=$(second $f_countries ${countries[@]})
commands=$(second $f_commands ${commands[@]})

echo ${countries[*]}
echo ${commands[*]}
