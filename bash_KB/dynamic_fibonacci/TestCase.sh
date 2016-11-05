#!/bin/bash

. ./Solution.sh
. ../assert.sh

setup

declare -a answers=(1 1 1 2 3 5 9 13 21 34)

for n in {0..9}; do
    fibonacci $n
    #echo "$answer"
    #echo "${answers[$n]}"
    #echo $answer
    assert "echo $answer" "${answers[$n]}";
done
