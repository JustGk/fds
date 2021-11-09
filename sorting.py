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
        else:
            break