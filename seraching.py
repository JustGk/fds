def linear_search(arr,n):
    search=int(input("ENTER THE ELEMENT YOU WANT TO SEARCH : "))
    for i in range(n):
        if search==arr[i]:
            print("---------------------------------")
            print("SUCCESSFUL SEARCH")
            print("ELEMENT FOUND AT POSITION {}".format(i+1))
            print("---------------------------------")

            break
        elif search!=arr[i]and i==n-1:
            print("---------------------------------")
            print("UNSUCCESSFUL SEARCH")
            print("---------------------------------")


def bubble_sort():
    global arr
    for i in range(len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


if __name__ == '__main__':
    print("ENTER SIZE OF ARRAY:")
    n=int(input())
    print("ENTER THE ELEMENTS")
    arr=[]
    for i in range(n):
        ele=int(input())
        arr.append(ele)
    while True:
        print("FOR LINEAR SEARCH TYPE 1.")
        print('FOR BINARY SEARCH TYPE 2.')
        choise=int(input("ENTER YOUR CHOISE:"))
        if choise==1:
            linear_search(arr,n)
        elif choise==2:
            bubble_sort()
            search = int(input("ENTER ELEMENT YOU WANT TO SEARCH:"))

            result = binary_search(arr, 0, len(arr) - 1, search)

            if result != -1:
                print("Element is present at position", str(result+1))
            elif result==-1:
                print("Element is not present in array")
        else:
            break
