#!/bin/bash

number_pr=$(gh pr list --json number --jq ".[].number")

for number in $number_pr; do 

	echo $number
done
