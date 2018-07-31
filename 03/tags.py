import itertools
from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

REPLACE_CHARS = str.maketrans('-', ' ')  # forgot to add this
IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags(feed=RSS_FEED):
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    with open(feed) as f:
        tag_list = TAG_HTML.findall(f.read())
    return [tag.translate(REPLACE_CHARS) for tag in tag_list]


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    c = Counter(tags)
    return c.most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (
    already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair
    and continue if not the same"""
    # tag_pairs = product(tags, repeat=2)  # returns the same tag also
    tag_pairs = itertools.combinations(tags, r=2)  # returns unique combos

    for x, y in tag_pairs:
        # don't bother if first letters aren't same - faster
        if x[0] != y[0]:
            continue
        # ensure that pair order constant, not needed if combos
        # x, y = tuple(sorted((x, y)))

        if IDENTICAL > SequenceMatcher(a=x, b=y).ratio() >= SIMILAR:
                yield x, y

    # for pair in product(tags, tags):
    #     # performance enhancements 1.992s -> 0.144s
    #     if pair[0][0] != pair[1][0]:
    #         continue
    #     pair = tuple(sorted(pair))  # set needs hashable type
    #     similarity = SequenceMatcher(None, *pair).ratio()
    #     if SIMILAR < similarity < IDENTICAL:
    #         yield pair


if __name__ == "__main__":
    tags = get_tags('all.rss.xml')
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
