import re
import os
os.system("clear")

text = "+34 688999999 +1 123456789 +123 987654321"
pattern = r"\+?\d{1,3} \d{9}"

"lo.que+sea@shopping.online"
"michael@gov.co.uk"

text = "michael@gov.co.uk"
pattern = r"[\w._%+-]+@[\w.-]+\.[a-zA-z]+"
matches = re.findall(pattern, text)
print(matches)