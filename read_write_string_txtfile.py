
example_string = 'Good'
#Read str from file
with open('test.txt', 'r', encoding='utf8') as f:
    content = f.read()
# Write str to file
with open('test.txt', 'w', encoding='utf8') as f:
    f.write(example_string)