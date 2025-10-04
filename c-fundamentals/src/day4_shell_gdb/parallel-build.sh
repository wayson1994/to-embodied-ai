#!/bin/bash
cpus=$(nproc)
echo "Using $cpus cores"
find . -maxdepth 1 -name '*.c' -print0 | xargs -0 -P "$cpus" -I {} gcc -Wall -O2 -c {} -o {}.o
gcc *.o -o app