#!/bin/bash

echo "Current status: "
echo ------------------------------------------
git status
echo ------------------------------------------
echo "Please enter your file: "
read  punkt

echo "Please enter your commit: "
read  commit


git add $punkt && git commit -m "$commit"
