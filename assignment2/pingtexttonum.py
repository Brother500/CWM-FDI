import re

open("ping0001.txt", "w").close()

with open("ping0001.log") as f:
    for line in f:
        match = re.search(r'(-?\d+(?:\.\d+)?)\s*[a-zA-Z%]+\s*$', line)
        if match:
            with open("ping0001.txt", "a") as g:
                print(match.group(1), file=g)

