#!/bin/bash
# Generating the Book.txt file 
find ./manuscript -maxdepth 1 -type f | grep --only-matching "[0-9].*md$" | sort --dictionary-order > ./manuscript/Book.txt
