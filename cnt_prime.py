import pdb
with open('prime10000.txt', 'r') as file:
    string = file.read()

ct = 0
for idx, c in enumerate(string):
    if c.isnumeric():
        ct += 1
    if ct == 10000:
        print(string[idx - 10:idx + 10])
# pdb.set_trace()
