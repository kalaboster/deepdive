#!usr/bin/env python
# 
#######
# Purpose = Read and format story chapter data in on tsv file for this deepdive app.
#######
# This command line tool reads from a configuration 
# files a list of file that are chapters of a story.
#
# Once the files are read the the script publishes them 
# into a tsv list file compatiable with deepdive and 
# a version of a pipeline.
#######
import yaml

with open('story.yaml', 'r') as y:
    story = yaml.load(y)

for key, value in story['chapter'].iteritems():
    print(key, value)



















