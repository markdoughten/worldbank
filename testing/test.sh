#!/bin/bash

f_countries="./countries.txt"
f_commands="./commands.txt"
declare -a countries=()
declare -a commands=()
counter=0
RANDOM=$$$(date +%s)

echo $RANDOM

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

#remove $f_commands
#remove $f_countries
#python ../ > $f_commands
#python ../main.py countries > $f_countries
countries=$(second $f_countries ${countries[@]})
commands=$(second $f_commands ${commands[@]})


echo ${commands[0]}
echo $RANDOM%${#commands[@]}

select_countries=${countries[ $RANDOM % ${#countries[@]} ]}
select_commands=${commands[$RANDOM % ${#commands[@]}]}

#echo $select_countries
