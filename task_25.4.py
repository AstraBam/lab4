import random, string


def generate_password(m):
    x = random.randint(1, m - 2)
    y = random.randint(1, m - x - 1)
    z = m - x - y

    l = []

    i = 0
    while i < x:
        n = random.choice(string.digits)
        if n != '1' and n != '0':
            l.append(n)
            i += 1

    i = 0
    while i < y:
        u = random.choice(string.ascii_uppercase)
        if u != 'I' and u != 'O':
            l.append(u)
            i += 1

    i = 0
    while i < z:
        w = random.choice(string.ascii_lowercase)
        if w != 'l' and w != 'o':
            l.append(w)
            i += 1

    random.shuffle(l)
    return ''.join(l)


def main(n, m):
    list_of_passwords = []
    for i in range(n):
        list_of_passwords.append(generate_password(m))
    return list_of_passwords


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")