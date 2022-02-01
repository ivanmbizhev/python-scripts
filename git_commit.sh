#!/bin/bash

# This script is meant only for a local system and can be used to add and commit your changes to the repo. 
# Made by Ibizhev

echo "Current status: "
echo ------------------------------------------
git status
echo ------------------------------------------
echo "Please enter your file: "
read  punkt

echo "Please enter your commit: "
read  commit


git add $punkt && git commit -m "$commit"
