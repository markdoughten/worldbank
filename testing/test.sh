#!/bin/bash

f_countries="./countries.txt"
f_commands="./commands.txt"
declare -a countries=()
declare -a commands=()
declare -a random_countries=()
declare -a random_commands=()
RANDOM=$$$(date +%s)

second() {
  local arr
  arr=($@)  
  while read -r line
  do
    arr=($(awk 'FNR > 1 {print $2;}'))
  done < $1
  echo ${arr[*]}
 
}

random() {
  local arr
  local index
  arr=($@)  
  for index in $(shuf -i 0-$(( ${#arr[@]} - 1 )) -n $1)
  do
      echo ${arr[$index]}
  done
}

#python ../main.py help > $f_commands
#python ../main.py countries > $f_countries
countries=$(second $f_countries ${countries[@]})
commands=$(second $f_commands ${commands[@]})
IFS=' ' read -r -a commands <<< "${commands[0]}"
IFS=' ' read -r -a countries <<< "${countries[0]}"
N=5
random_commands=$(random $N ${commands[@]})
N=3
random_countries=$(random $N ${countries[@]})

echo $random_countries
echo $random_commands
