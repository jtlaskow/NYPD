import re

palindrom = "123321 , 111112 , 124421 , 345678, 111111, 123421"

pal = re.findall(r"(\d)(\d)(\d)\3\2\1", palindrom)
pali = re.search(r"(\d)(\d)(\d)\3\2\1", palindrom)

print(pal, pali)
