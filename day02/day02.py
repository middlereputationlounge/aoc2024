def turn_to_distances(A):
    distances = []
    counter = 1
    while counter < len(A):
        distances.append(A[counter]-A[counter-1])
        counter = counter + 1
    return distances
lines = []
for line in open('input.txt', 'r'):
    lines.append([int(word) for word in line.split()])
count_safe = 0
for report in lines:
    distances = turn_to_distances(report)
    if all(0 < level < 4 for level in distances) or all(-4 < level < 0 for level in distances):
        count_safe += 1
print(count_safe)