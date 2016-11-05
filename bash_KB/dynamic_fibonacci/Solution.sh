#!/bin/bash

# pls help :)

. ./HashMap.sh

setup() {
    hinit memo
}

fibonacci() {
    n=$1
    if [ -s /tmp/hashmap.memo ]
    then
        hget memo $n
        if [ "$val" ] 
        then
            answer=$val
        elif [ $n -le 2 ] 
        then
            answer=1
            hput memo $n $answer
        else
            fibonacci $[$(($n - 1))]
            n1=$answer
            fibonacci $[$(($n - 2))]
            n2=$answer
            answer=$(echo $(($n1+$n2)))
            hput memo $n $answer
        fi
    else
        answer=1 
        hput memo $1 $answer
    fi
}

