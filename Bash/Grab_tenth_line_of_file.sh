# head -n 10| tail -1
# If you give 3 lines in file; it will give last line of file

sed -n '10p' file.txt

# Sed -n option will not print anything unless an explicit request
# to print is found.
# i mentioned the "/p" flag to the substitute command as one way
# to print back on
# <number>p gives command to this function to print the respective line.