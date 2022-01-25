#!/bin/bash

echo "Please enter your commit:"
read commit

git add . && git commit -m "$commit"
