## finding second largest,smaller from the array

arr = [3,2,1,2,1,7,7,5]
n = len(arr)

## Brutal Approch:


def largest_element(arr,n):

    largest = arr[0]
    second_largest = -1

    for i in range(n-1,0,-1):
        for j in range(0,i,1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    largest = arr[n-1]

    for element in range(n-2,0,-1):

        if arr[element] != largest:
            second_largest =arr[element]
            break 
        
    print(f"Largest element :{largest}")
    print(f"Second largest element:{second_largest}")

def smallest_element(arr,n):

    smallest = arr[0]
    second_smallest = float('inf')

    for i in range(n-1,0,-1):
        for j in range(0,i,1):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    smallest = arr[n-1]

    for element in range(n-2,0,-1):
        if arr[element] != smallest:
            second_smallest = arr[element]
            break
    print(f"smallest element :{smallest}")
    print(f"Second smallest element:{second_smallest}")

largest_element(arr,n)
smallest_element(arr,n)

## ani T.C. = O(NlogN)

## Better Approch:


def largest_element(arr,n):
    Largest = arr[0]
    Second_largest = -1

    for i in range(n):    
        if arr[i] > Largest:
            Largest = arr[i]

        for j in range(n):
            if arr[j] > Second_largest and arr[j] < Largest:
                Second_largest = arr[j]

    print("Largest:",Largest)
    print("Second Largest:",Second_largest)

def smallest_element(arr,n):
    smallest = arr[0]
    second_smallest = float('inf')

    for i in range(n):
        if arr[i] < smallest:
            smallest = arr[i]

        for j in range(n):
            if arr[j] < second_smallest and arr[j] > smallest:
                second_smallest = arr[j]

    print("Smallest:",smallest)
    print("Second Smallest:",second_smallest)


largest_element(arr,n)
smallest_element(arr,n)

# aa ni T.C. = O(n^2)

### Optimal Approch:

def largest_(arr,n):

    Largest = arr[0]
    Second_largest = -1

    for i in range(n):
        if arr[i] > Largest:
            Second_largest = Largest
            Largest = arr[i]

        elif arr[i] < Largest and arr[i] > Second_largest:
            Second_largest = arr[i]

    print("Largest:",Largest)
    print("Second Largest:",Second_largest)

def smallest_element(arr,n):
    Smallest = arr[0]
    second_smallest = float('inf')

    for i in range(n):
        if arr[i] < Smallest:
            second_smallest = Smallest
            Smallest = arr[i]

        elif arr[i] < Smallest and arr[i] > second_smallest:
            second_smallest = arr[i]

    print("Smallest:",Smallest)
    print("Second Smallest:",second_smallest)
            
largest_(arr,n)
smallest_element(arr,n)
    
    


