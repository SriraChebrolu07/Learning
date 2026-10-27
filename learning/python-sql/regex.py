import re

pattern =r"^9........."
result=re.search(pattern,"7989564525")

print(result.group())