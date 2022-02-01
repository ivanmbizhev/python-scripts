#!/bin/bash

echo "Please enter the file to add: "
read punkt
echo "Please enter your commit: "
read commit


git add $punkt && git commit -m "$commit"
