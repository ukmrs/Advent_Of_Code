#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Provide day number"
    exit 1
fi

number=$1
input_file="inputs/day${number}"
script_name="solutions/day${number}.py"

if [ ! -d "solutions" ]; then
    mkdir solutions
fi

if [ -f "$script_name" ]; then
    echo "${script_name} already exists. Exiting."
    exit 1
fi

cp day_skelly "$script_name"

if [ ! -d "inputs" ]; then
    mkdir inputs
fi

if [ -f "$input_file" ]; then
    echo "${input_file} already exists. Exiting."
    exit 1
fi

xsel -b > "$input_file"
