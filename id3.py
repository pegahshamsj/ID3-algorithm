import math

train = []
filename = "monks-1.train"
file = open(filename, "r")
for line in file:
    train.append(line.strip().split(' '))


def calculate_entropy(data):
    np = 0
    pp = 0
    n = 0

    for i in data:
        n += 1
        if i[0] == "0":
            np += 1
        elif i[0] == "1":
            pp += 1

    n_p = ((-np)/n)
    p_p = ((-pp)/n)
    entropy = (n_p*math.log(-1*n_p, 2))+(p_p*math.log(-1*p_p, 2))
    return entropy


entropy_all = calculate_entropy(train)


def gain_ratio_a1(data, entropy_):
    np = 0
    pp = 0
    mp = 0
    n = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0

    for i in data:
        n += 1
        if i[1] == "1":
            np += 1
            if i[0] == "0":
                a += 1
            elif i[0] == "1":
                b += 1
        elif i[1] == "2":
            pp += 1
            if i[0] == "0":
                c += 1
            elif i[0] == "1":
                d += 1
        elif i[1] == "3":
            mp += 1
            if i[0] == "0":
                e += 1
            elif i[0] == "1":
                f += 1

    entropy_a1 = ((np / n) * (-1) * (((a / np) * math.log((a / np), 2)) + ((b / np) * math.log((b / np), 2)))) + \
                 ((pp / n) * (-1) * (((c / pp) * math.log((c / pp), 2)) + ((d / pp) * math.log((d / pp), 2)))) + \
                 ((mp / n) * (-1) * (((e / mp) * math.log((e / mp), 2)) + ((f / mp) * math.log((f / mp), 2))))

    gain = (entropy_ - entropy_a1)
    return gain


def gain_ratio_a2(data, entropy_):
    np = 0
    pp = 0
    mp = 0
    n = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0

    for i in data:
        n += 1
        if i[2] == "1":
            np += 1
            if i[0] == "0":
                a += 1
            elif i[0] == "1":
                b += 1
        elif i[2] == "2":
            pp += 1
            if i[0] == "0":
                c += 1
            elif i[0] == "1":
                d += 1
        elif i[2] == "3":
            mp += 1
            if i[0] == "0":
                e += 1
            elif i[0] == "1":
                f += 1

    entropy_a2 = ((np / n) * (-1) * (((a / np) * math.log((a / np), 2)) + ((b / np) * math.log((b / np), 2)))) + \
                 ((pp / n) * (-1) * (((c / pp) * math.log((c / pp), 2)) + ((d / pp) * math.log((d / pp), 2)))) + \
                 ((mp / n) * (-1) * (((e / mp) * math.log((e / mp), 2)) + ((f / mp) * math.log((f / mp), 2))))

    gain = (entropy_ - entropy_a2)
    return gain


def gain_ratio_a3(data, entropy_):
    np = 0
    pp = 0
    n = 0
    a = 0
    b = 0
    c = 0
    d = 0

    for i in data:
        n += 1
        if i[3] == "1":
            np += 1
            if i[0] == "0":
                a += 1
            elif i[0] == "1":
                b += 1
        elif i[3] == "2":
            pp += 1
            if i[0] == "0":
                c += 1
            elif i[0] == "1":
                d += 1

    entropy_a3 = ((np / n) * (-1) * (((a / np) * math.log((a / np), 2)) + ((b / np) * math.log((b / np), 2)))) + \
                 ((pp / n) * (-1) * (((c / pp) * math.log((c / pp), 2)) + ((d / pp) * math.log((d / pp), 2))))

    gain = (entropy_ - entropy_a3)
    return gain


def gain_ratio_a4(data, entropy_):
    np = 0
    pp = 0
    mp = 0
    n = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0

    for i in data:
        n += 1
        if i[4] == "1":
            np += 1
            if i[0] == "0":
                a += 1
            elif i[0] == "1":
                b += 1
        elif i[4] == "2":
            pp += 1
            if i[0] == "0":
                c += 1
            elif i[0] == "1":
                d += 1
        elif i[4] == "3":
            mp += 1
            if i[0] == "0":
                e += 1
            elif i[0] == "1":
                f += 1

    entropy_a4 = ((np / n) * (-1) * (((a / np) * math.log((a / np), 2)) + ((b / np) * math.log((b / np), 2)))) + \
                 ((pp / n) * (-1) * (((c / pp) * math.log((c / pp), 2)) + ((d / pp) * math.log((d / pp), 2)))) + \
                 ((mp / n) * (-1) * (((e / mp) * math.log((e / mp), 2)) + ((f / mp) * math.log((f / mp), 2))))

    gain = (entropy_ - entropy_a4)
    return gain


def gain_ratio_a5(data, entropy_):
    np = 0
    pp = 0
    mp = 0
    n = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0

    for i in data:
        n += 1
        if i[4] == "1":
            np += 1
            if i[0] == "0":
                a += 1
            elif i[0] == "1":
                b += 1
        elif i[4] == "2":
            pp += 1
            if i[0] == "0":
                c += 1
            elif i[0] == "1":
                d += 1
        elif i[4] == "3":
            mp += 1
            if i[0] == "0":
                e += 1
            elif i[0] == "1":
                f += 1

    entropy_a5 = ((np / n) * (-1) * (((a / np) * math.log((a / np), 2)) + ((b / np) * math.log((b / np), 2)))) + \
                 ((pp / n) * (-1) * (((c / pp) * math.log((c / pp), 2)) + ((d / pp) * math.log((d / pp), 2)))) + \
                 ((mp / n) * (-1) * (((e / mp) * math.log((e / mp), 2)) + ((f / mp) * math.log((f / mp), 2))))
    gain = (entropy_ - entropy_a5)
    return gain


def gain_ratio_a6(data, entropy_):
    np = 0
    pp = 0
    n = 0
    a = 0
    b = 0
    c = 0
    d = 0

    for i in data:
        n += 1
        if i[6] == "1":
            np += 1
            if i[0] == "0":
                a += 1
            elif i[0] == "1":
                b += 1
        elif i[6] == "2":
            pp += 1
            if i[0] == "0":
                c += 1
            elif i[0] == "1":
                d += 1

    entropy_a6 = ((np / n) * (-1) * (((a / np) * math.log((a / np), 2)) + ((b / np) * math.log((b / np), 2)))) + \
                 ((pp / n) * (-1) * (((c / pp) * math.log((c / pp), 2)) + ((d / pp) * math.log((d / pp), 2))))
    gain = (entropy_ - entropy_a6)
    return gain


a1 = gain_ratio_a1(train, entropy_all)
a2 = gain_ratio_a2(train, entropy_all)
a3 = gain_ratio_a3(train, entropy_all)
a4 = gain_ratio_a4(train, entropy_all)
a5 = gain_ratio_a5(train, entropy_all)
a6 = gain_ratio_a6(train, entropy_all)

chosen = max(a1, a2, a3, a4, a5, a6)
print(chosen)

