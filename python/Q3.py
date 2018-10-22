import re

q = input('')
x = q.split(',')
for i in x:
    if (len(i)>5 and len(i)<13):
        if re.search(r'[a-z]', i):
            if re.search(r'[0-9]', i):
                if re.search(r'[A-Z]', i):
                    if re.search(r'[$#@]', i):
                        print(i)
