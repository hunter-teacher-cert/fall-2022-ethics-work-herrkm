import re

def find_name(line):
    pattern = r"(?:(?:Mr|Mrs|Dr)\.? )?(?:(?!Mr|Mrs|Dr)[A-Za-z\-\'\,\"]+ ?)*(?:[A-Z]\. )*(?:(?!Mr|Mrs|Dr)[A-Za-z\-\'\,\"]+ ?)+"
    result = re.findall(pattern,line)

    result = result + re.findall(pattern,line)
    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)

# Characters with diacritics don't match
# Can't find the end of a name if it's followed by another name without a title/prefix
# Any special character not explicitly accounted for will not work