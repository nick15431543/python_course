import sys

def cli(lines):
    res = []
    for num, i in enumerate(lines):
        a = str(num + 1) + ' ' + i
        res.append(a)
    return res
    

if __name__ == "__main__":
    args = sys.argv
    lines = []
    if len(args) > 1:
        with open(args[1], 'r') as f:
            lines = f.readlines()
    else:
        for line in sys.stdin:
            lines.append(line)
    res = cli(lines)
    for line in res:
        print(line.rstrip('\n'))