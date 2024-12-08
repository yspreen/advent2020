#!/bin/bash

main() {
    ( ! ([ -f ./.meta ] || [ -f ../.meta ])) && return
    [ "$(cat .meta | head -1)" = 'dir=>DAY' ] && cd ..
    n=$(ls -1 | grep -E '^\d{2}$' | sort | tail -1 || echo "00")
    n=$((n + 1))
    aoc -d $n
    cd "$(printf "%02d" $n)"
    cp ../../template.py ./main.py
    code $n.md input main.py
}
main
