def binarySearch(x):
    a=[i for i in range (10)]
    left_indicator = 0
    right_indicator = len(a) -1
    while True:
        middle_point = (right_indicator + left_indicator) // 2
        if x == a[middle_point]:
            return middle_point
        elif x > a[middle_point]:
            left_indicator = middle_point + 1
        elif x < a[middle_point]:
            right_indicator = middle_point - 1
        if left_indicator > right_indicator:
            return -1

output = binarySearch(11)
print(output)
        
        
    
