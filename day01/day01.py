def quicksort(A, left, right):
    if left < right:
        pivot_index = partition(A, left, right)
        quicksort(A, left, pivot_index -1)
        quicksort(A, pivot_index + 1, right)
    return A
def partition(A, left, right):
    pivot = A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[right] = A[right], A[i + 1]
    return i + 1
def absolute(a,b):
    x = a-b
    if x < 0:
        x = x * -1
    return x

lines = [[int(word) for word in line.strip().split()] for line in open('input.txt', 'r')]
transposed_lines = [list(x) for x in zip(*lines)]

ax = quicksort(transposed_lines[0], 0, len(transposed_lines[0])-1)
bx = quicksort(transposed_lines[1], 0, len(transposed_lines[1])-1)
i = 0
acum = 0
while i <= len(ax)-1:
    x = absolute(ax[i],bx[i])
    acum = x + acum  
    i = i + 1
print(acum)

def stoopid (A,B):
    total = 0
    for a in A:
        counter = 0
        for b in B:
            if a == b:
                counter = counter + 1
        score = counter * a
        total = total + score
    return counter
print(stoopid(ax,bx))