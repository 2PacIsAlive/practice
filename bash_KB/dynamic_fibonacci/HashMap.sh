#!/bin/bash

hinit() {
    rm -f /tmp/hashmap.$1
    touch /tmp/hashmap.$1
}

hput() {
    echo "$2 $3" >> /tmp/hashmap.$1
}

hget() {
    unset val
    val=$(grep "^$2 " /tmp/hashmap.$1 | awk '{ print $2 };')
}
