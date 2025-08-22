import re
import os
os.system("clear")

files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\b\w+\.txt"
matches = re.findall(pattern, files)
if matches:
  print(matches)
else:
  print("Not found")