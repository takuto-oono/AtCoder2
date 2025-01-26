#!/bin/bash

expected_dir="AtCoder2"
current_dir=$(basename "$PWD")

if [ "$current_dir" != "$expected_dir" ]; then
  echo "Error: Script must be run from a directory named $expected_dir"
  exit 1
fi

dirname=$1

mkdir -p $dirname
cd $dirname

echo "created directory $dirname"

for problem in "a" "b" "c" "d" "e" "f"
do
  mkdir -p $problem
done

echo "created directories a, b, c, d, e, f"

for problem in "a" "b" "c" "d" "e" "f"
do
  if [ ! -f "$problem/main.go" ]; then
      cp ../snippet.go $problem/main.go
      echo "copied snippet.go to $problem/main.go"
  else
      echo "$problem/main.go already exists"
  fi
done

echo "all done"


