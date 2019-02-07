# comparison between 2 adjacent bubbles
def bubble_sort(a, N):
    # number of rounds or pass is total elements -1
    for i in range(len(a)-1):
        # number of comparisons in each round
        # at the end of each comp, the biggest element
        # will be at the end;
        # Also the comps decrease with increase in the rounds
        for j in range(N-1-i):
            # swapping if a[j] > a[j+1]
            if a[j]>a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a

print('Enter the no of integer')
N = input()
a =[]
print('Enter the array of integers')
for i in range(N):
    try:
        a.append(input())
    except:
        print('Not a valid input')

sorted_pattern = bubble_sort(a, N)
print(sorted_pattern)