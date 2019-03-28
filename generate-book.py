# Code to generate Book.txt in the right order
# Left as a task for rishi@malhotra.ca who loves python language

# Concepts:
#   Books are usually organized as
#       Part
#           Chapter
#               Section
#                   Sub-section

# == in sequential coding parlance ==
# Following convention over configuration, this code will need to
#   10 Iterate over all files in manuscript folder
#   20 Ignore all with dunder (double underscore), these are not to be used
#   30 Consider all files with naming convention like "*.0 abc.md" to be a Part and put them in a sorted Set
#   40 All files with names like "1.x Abc.md" as Chapters and so on
#   50 The code needs to write these in the right sequence to Book.txt
#   60 Test the output to match this shell command generate-book.sh

# == now implement the same in object oriented fashion ==
