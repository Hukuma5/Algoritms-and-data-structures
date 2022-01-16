import sys

def strategy(val):
    res = []
    while val != 0:
        if val == 1 or val == 3:
            res.append('inc')
            val -= 1
        elif val % 2 == 0:
            res.append('dbl')
            val /= 2
        else:
            bin1 = int(val + 1)
            bin2 = int(val - 1)
            ost1 = 0
            ost2 = 0
            count_z1 = 0
            count_z2 = 0
            while ost1 != 1:
                ost1 = bin1 % 2
                bin1 /= 2
                count_z1 += 1
            while ost2 != 1:
                ost2 = bin2 % 2
                bin2 /= 2
                count_z2 += 1
            if count_z1 > count_z2:
                res.append('dec')
                val += 1
            else:
                res.append('inc')
                val -= 1
    return reversed(res)

def print_strategy(val, out):
    for i in val:
        print(i, file=out)

out = sys.stdout
while True:
    try:
        line = input()
        if not line:
            continue
        elif len(line.split()) == 1 and line.split()[0].isdigit() \
                                    and int(line.split()[0]) >= 0:
            print_strategy(strategy(int(line.split()[0])), out)
        else:
            break
    except EOFError:
        sys.exit()
