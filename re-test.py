import re

a="asdqapython136e2134123java12312542135asdas"

pat=re.compile(r"Python",re.I)

c1=pat.search(a)
print(c1)