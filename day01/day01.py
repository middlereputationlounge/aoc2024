lines = [[int(word) for word in line.strip().split()] for line in open('input.txt', 'r')]
print(lines)
transposed_lines = zip(lines)

ax = transposed_lines[0]
print(ax)
bx = transposed_lines[1]
i = 0
acum = 0
while i <= len(ax):
    acum = abs(ax[i] - bx[i])  
    i = i + 1
print(acum)

def sort()