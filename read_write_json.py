import json

st = {'first': 1, 'second': 2, 'third': 3, 'four': 4}

# Write JSON
with open('test.txt', 'w', encoding='utf8') as f:
    json.dump(st , f)
#Read JSON
with open('test.txt', 'r', encoding='utf8') as f:
    a = json.load(f)
