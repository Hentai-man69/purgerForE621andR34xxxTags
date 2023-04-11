# purgerForE621andR34xxxTags
Credit to pikaft-e621-posts-downloader by pikaflufftuft and Ruxx by trickerer01 for creating a way to download images with tags

If you download using Ruxx(https://github.com/trickerer01/Ruxx) then the order goes as follows
filerenamer.py, parser.py, purger.py
must have rx option enabled
also removes score thing

If you download using pikaft-e621-posts-downloader (https://github.com/pikaflufftuft/pikaft-e621-posts-downloader) then you only need to run purger.py

blacklist tags is per line ie:
a, b 
a, -b
a and b will be blacklisted if both are in a tag list
a will be blacklisted if a but not b is in a tag list

idk if any of this works and i can't really offer any support on this

know issue and manual fix
if parser script does not work there is an issue with your !tag.txt it would look something like this
filename.png: a b c
d e f

to fix this go to the line without a file name and delete the new line so it looks something like this
filename.png: a b c d e f
or
filename.png: a b c

Also log files are bad so don't rely on them for anything
