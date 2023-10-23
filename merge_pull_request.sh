#!/bin/bash

number_pr=$(gh pr list --json number --jq ".[].number")

for number in $number_pr; do 
	gh pr merge $number --merge --fill --delete-branch
done


#gh pr diff --name-only 393
