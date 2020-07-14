#!/usr/bin/env python

# does a string have all unique characters?

def unique_character_string(s):
    # cannot use additional data structures
    for index, char in enumerate(s):
        for other_index in range(index+1, len(s)):
            other_char = s[other_index]
            if char == other_char:
                return False
    return True
