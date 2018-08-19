"""
Turn the following unix pipeline into Python code using generators

$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort |
uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""
import glob
import re

def gen_files(pat):
    return [i for i in glob.glob(pat)]


def gen_lines(files):
    lines = []
    for file in files:
        with open(file, encoding='utf-8') as f:
            lines.extend(f.readlines())
    return lines

def gen_grep(lines, pattern):
    new_lines = []
    for line in lines:
        if re.search(pattern, line):
            new_lines.append(re.sub(pattern, '', line).strip())
        else:
            continue
    new_lines.sort()
    return new_lines


def gen_count(lines):
    lines.sort()
    final_dict = {}
    for line in lines:
        final_dict.setdefault(line,0)
        final_dict[line] += 1
    return sorted([f'{v} {k}' for k,v in final_dict.items()], reverse=True)

if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    grep_lines = gen_grep(lines, '^import ')
    counts = gen_count(grep_lines)
    for count in counts:
        print(count)
