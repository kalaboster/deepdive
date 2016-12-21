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
import uuid

with open('story.yaml', 'r') as y:
    story = yaml.load(y)

# if there are chapters then check and create tsv
# This does nothing right now but print.
# I am leaving this as I may not have two options.
# It seems to me only a list is needed.
# I don't want to think of the right words now
# That don't include chapter.
if 'chapter' in story:

    for key, value in story['chapter'].iteritems():

        print(key, value)

# Read in the short story and make into one tsv.
if 'short' in story:

    short = ""

    with open(story['short']) as f:

        for line in f:

            if not line.startswith("#"):

                short = short + line.strip() + "\\n"

    with open("story.tsv", "w") as tsv:

        print("Print story.tsv files of the story: " + story['short'])

        tsv.write(str(uuid.uuid4()) + "\t" + short)
