import re

text = input("Enter a camelCase string: ")
result = re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower()

print(result)
