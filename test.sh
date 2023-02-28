#!/bin/bash

f_countries="./testing/countries.txt"
f_commands="./testing/commands.txt"
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
  for index in $(shuf -i 0-$(( ${#arr[@]} - 1 )) -n 2)
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

i=0
while [[ $i -lt 1 ]]
do 
  random_commands=$(random $N ${commands[@]})
  random_countries=$(random $N ${countries[@]})
  echo $random_countries $random_commands  
  python main.py $random_countries $random_commands
  ((i++))
done  


