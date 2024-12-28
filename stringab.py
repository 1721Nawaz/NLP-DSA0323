import re


def ends_with_ab(string):
    
    pattern = r'ab$'
    return bool(re.search(pattern, string))
test_strings = ["helloab", "world", "testab", "python"]

for s in test_strings:
    if ends_with_ab(s):
        print(f"'{s}' ends with 'ab'")
    else:
        print(f"'{s}' does not end with 'ab'")
