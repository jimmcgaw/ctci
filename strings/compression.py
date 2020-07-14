#!/usr/bin/env python

# compress a string with repeated characters


def compress_string(s):
    # "aaabbccccccc" => a3b2c6
    # "abc" => "abc"
    compressed = []
    max_repeated = 1
    previous_character = None
    count = 0

    for index, char in enumerate(s):
        if index == 0:
            count += 1
            previous_character = char
            continue

        if index == len(s)-1:
            compressed.append('{}{}'.format(char, count))

        if char == previous_character:
            count += 1
        else:
            compressed.append('{}{}'.format(previous_character, count))
            if max_repeated < count:
                max_repeated = count
            previous_character = char
            count = 1

    if max_repeated == 1:
        return s
    return ''.join(compressed)
