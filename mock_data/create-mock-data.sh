#!/bin/bash

while [[ $# -gt 0 ]]; do
  key="$1"

  case $key in
    -o|--output)
      output_file="$2"
      shift
      shift
      ;;
    -a|--append)
      append_file="$2"
      shift
      shift
      ;;
    -s|--seed)
      seed="$2"
      shift
      shift
      ;;
    *)
      printf '%s\n' "Unknown option. Exiting"
      exit 1
      ;;
  esac
done

if [ ! -z $output_file ] && [ ! -z $append_file ]; then
  printf '%s\n' "Provide eiter [append_file] or [output_file], but no both."
  exit 1
elif [ ! -z $append_file ] && [ ! -f "$append_file" ]; then
  printf '%s\n' "File specified to append to does not exist."
  exit 1
elif [ ! -z $output_file ] && [ -f "$output_file" ]; then
  printf '%s\n' "Specified output_file already exist. Choose another name or option to append to file."
  exit 1
elif [ -z $output_file ] && [ -z $append_file ]; then
  printf '%s\n\n' "No output specified. Proceeding to only print results to console."
fi

# If wanting to specify seed for randomization
if [ ! -z $seed ]; then
  RANDOM=$seed;
fi

declare -a gender=( "male" "female" )
declare -a medium=( "mobile" "computer" )
declare -a age=( "child" "adult" )
declare -a videos=( "v0" "v1" "v2" "v3" "v4" "v5" )
declare -a b_bool=( "true" "false" )

get_random_element() {
  arr=("${!1}");
  echo ${arr["$[RANDOM % ${#arr[@]}]"]};
}

count=0
for i in $(seq 0 $(( ${#videos[@]} - 2 )) ); do
  for j in $(seq $(( $i + 1)) $(( ${#videos[@]} - 1 )) ); do
    _age=$(get_random_element "age[@]")
    _medium=$(get_random_element "medium[@]")
    _gender=$(get_random_element "gender[@]")
    _better=$(get_random_element "b_bool[@]")

    res[${count}]=${videos[${i}]}","${videos[${j}]}","${_age}","${_medium}","${_gender}","${_better}
    count=$(( count + 1 ));
  done
done

columns="#V1,V2,Age,Medium,Gender,V1BetterQuality"

if [ ! -z $append_file ] && [ -z $output_file ]; then
  printf '%s\n' "${res[@]}" >> $append_file
elif [ ! -z $output_file ] && [ -z $append_file ]; then
  printf '%s\n' $columns > $output_file
  printf '%s\n' "${res[@]}" >> $output_file
else
  printf '%s\n' $columns
  printf '%s\n' "${res[@]}"
fi
