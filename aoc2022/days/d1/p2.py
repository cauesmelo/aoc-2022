from aoc2022.utils.get_lines import get_lines


lines = get_lines("i2.txt")

elfs = [0]

for line in lines:
    if line != "":
        elfs[-1] += int(line)
    else:
        elfs.append(0)

print(sum(sorted(elfs, reverse=True)[:3]))
