

def get_prime_sequence(idx, string):
    s = ''
    for c in string:
        if c.isnumeric():
            s += str(c)

    return s[idx:idx + 5]


if __name__ == '__main__':
    with open('prime10000.txt', 'r') as file:
        string = file.read()
    idx = 0
    print(get_prime_sequence(idx, string))
