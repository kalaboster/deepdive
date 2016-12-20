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


story = ""

print uuid.uuid4()


with open('story.yaml', 'r') as y:
    story = yaml.load(y)

# if there are chapters then check and create tsv
if 'chapter' in story:
    for key, value in story['chapter'].iteritems():
        print(key, value)


if 'short' in story:

    print("This is s short story:")
    print(story['short'])

    with open(story['short']) as f:

        storylines = f.readlines()
        for line in storylines:

            if not line.startswith("#"):
                print "A Line:" + line.strip()
                story = story + "\n\n" + str(line.strip())

print story

with open("story.tsv", "w") as tsv:
    print("What the fuck to I print?")
    print "\t" .join(story)
