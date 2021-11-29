def bubble(arr):
    print("SORTED USING BUBBLE SORT METHOD")
    print("ORIGINAL ARRAY :", arr)
    for i in range(len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print("---------------------------------------------")
    print("SORTED IN DESCENDING ORDER : ",end="")
    print(arr)
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print("---------------------------------------------")
    print("SORTED IN ASCENDING ORDER : ",end="")
    print(arr)
    print("---------------------------------------------")
# bubble(b)
def selection(arr):
    pos=0
    print("SORTED USING SELECTION SORT METHOD")
    print("ORIGINAL ARRAY :", arr)
    for i in range(len(arr)-1):
        mn=arr[i]
        for j in range(i+1,len(arr)):
            if arr[j]>mn:
                mn=arr[j]
                pos=j
                arr[i],arr[pos]=arr[pos],arr[i]
    print("---------------------------------------------")
    print("SORTED IN DESCENDING ORDER: ",end="")
    print(arr)
    for i in range(len(arr)-1):
        mx=arr[i]
        for j in range(i+1,len(arr)):
            if arr[j]<mx:
                mx=arr[j]
                pos=j
                arr[i],arr[pos]=arr[pos],arr[i]
    print("---------------------------------------------")
    print("SORTED IN ASCENDING ORDER: ", end="")
    print(arr)
    print("---------------------------------------------")

def insertion(arr):
    print("SORTED USING INSERTION SORT METHOD")
    print("ORIGINAL ARRAY :", arr)
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]<temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    print("---------------------------------------------")
    print("SORTED IN DESCENDING ORDER: ", end="")
    print(arr)
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    print("---------------------------------------------")
    print("SORTED IN ASCENDING ORDER: ", end="")
    print(arr)
    print("---------------------------------------------")




# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(arr, low, high):
	i = (low-1)		 # index of smaller element
	pivot = arr[high]	 # pivot

	for j in range(low, high):

		# If current element is smaller than or
		# equal to pivot
		if arr[j] <= pivot:

			# increment index of smaller element
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:

		# pi is partitioning index, arr[p] is now
		# at right place
		pi = partition(arr, low, high)

		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)


    # This code is contributed by Mohit Kumra
    #This code in improved by https://github.com/anushkrishnav

if __name__ == '__main__':
    arr=[]
    def creat():
        global arr
        arr=[]
        n=int(input("ENTER SIZE OF ARRAY:"))
        print("ENTER ELEMENTS IN ARRAY")
        for i in range(n):
            ele=int(input())
            arr.append(ele)
    while True:
        print("--------------------OPITIONS--------------------")
        print("FOR BUBBLE SORT TYPE 1")
        print("FOR SELECTION SORT TYPE 2")
        print("FOR INSERTION SORT TYPE 3")
        print("FOR QUICK SORT TYPE 4")
        choice=int(input("ENTER YOUR CHOICE: "))
        if choice==1:
            creat()
            bubble(arr)
        elif choice==2:
            creat()
            selection(arr)
        elif choice==3:
            creat()
            insertion(arr)
        elif choice==4:
            creat()
            quickSort(arr,0,len(arr)-1)
            print("Sorted array is:")

            for i in range(len(arr)):
                print("%d" % arr[i],end=" ")
                print("\n\n")
        else:
            break
