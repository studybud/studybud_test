import sys
import os

# get 1st param - input file to remove the duplicates from
input_file = sys.argv[1]
name, ext = os.path.splitext(input_file)
print(f'name: {name}')
print(f'ext: {ext}')

lines_seen = set() # holds lines already seen

# with open(f'rdl_{input_file}', "w") as outfile:
with open(f'{name}_rdl{ext}', "w") as outfile:
    for line in open(input_file, "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
