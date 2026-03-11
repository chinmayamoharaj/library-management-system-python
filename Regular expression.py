 # Using Regular Expressions (re module)

# Regular expressions are powerful for pattern matching.

#  ^\d → matches a digit at the start of the string.

import re

s = "9abc"

if re.match(r'^\d', s):
    print("String starts with a digit")
else:
    print("String does not start with a digit")