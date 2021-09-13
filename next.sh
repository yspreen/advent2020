#!/bin/bash

main() {
    ( ! ( [ -f ./.meta ] || [ -f ../.meta ] ) ) && return
    [ "$(cat .meta | head -1)" = 'dir=>DAY' ] && cd ..
    n="$(ls -1 | grep -E '^\d{2}$' | sort | tail -1)"
    n=$((n+1))
    n="$(printf "%02d" $n)"
    aoc -d $n
    cd $n
    cp ../../template.py ./main.py
    code main.py $((n)).md input
}
main