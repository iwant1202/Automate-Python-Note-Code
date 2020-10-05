import os

totalSize = 0
for filename in os.listdir('c:\\'):
    if not os.path.isfile(os.path.join('c:\\', filename)):
        continue
    totalSize += os.path.getsize(os.path.join('c:\\', filename))
    print(os.path.join('c:\\', filename))


print(totalSize)
