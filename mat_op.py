mat1=[]

mat2=[]
mat3=[]
def creat(r,c,r1,c1):
    mat=[]
    global mat2,mat1
    print("enter elements of 1st matrix:",end=" ")
    for i in range(3):#creation of mat1
        b=[]
        for j in range(3):
            insert=0
            b.append(insert)

        mat1.append(b)

    print()
    for i in range(r):#creation of mat2
        b=[]
        for j in range(c):
            insert=0
            b.append(insert)
        mat2.append(b)

    for i in range(r):#inserting elements in mat1
        b=[]
        for j in range(c):
            insert=int(input(f"enter {i}{j} elment of mat1 "))
            b.append(insert)
        mat.append(b)


    mat1=mat
    print("matrix 1 = ",end=" ")
    print()
    for i in range(r):#displaying mat1
        print("| ",end="")

        for j in range(c):
            print(mat1[i][j], end=" ")
        print("|",end="")
        print()

    print(end=" ")
    print()
    mat=[]
    print("enter elements of 2st matrix:", end=" ")
    print()
    for i in range(r1):#inserting elements in mat2
        b=[]
        for j in range(c1):
            insert=int(input(f"enter {i}{j} elment of mat2 "))
            b.append(insert)
        mat.append(b)
    mat2=mat
    print("matrix2 = ",end="")
    print()
    for i in range(r1):#displaying mat2
        print("| ",end="")

        for j in range(c1):
            print(mat2[i][j], end=" ")
        print("|",end="")
        print()
    print(end=" ")


# creat(r,c)
def add(mat1,mat2):#for addition
    # m1=[[1,2,3],[1,2,3],[1,2,3]]
    # m2=[[1,2,3],[1,2,3],[1,2,3]]

    res=[]

    for i in range(r):
        b=[]
        for j in range(c):
            insert=0
            b.append(insert)
        res.append(b)
    for i in range(r):

        for j in range(c):
            res[i][j]=(mat1[i][j]+mat2[i][j])
    print("matrix 1 = ")
    print()
    for i in range(r):#displaying mat1
        print("| ",end="")

        for j in range(c):
            print(mat1[i][j], end=" ")
        print("|",end="")
        print()
    print()
    print("matrix2 = ", end="")
    print()
    for i in range(r1):  # displaying mat2
        print("| ", end="")

        for j in range(c1):
            print(mat2[i][j], end=" ")
        print("|", end="")
        print()
    print(end=" ")
    print("addition of matrices is =",end=" ")
    print()
    for i in range(r):
        print("| ",end="")

        for j in range(c):
            print(res[i][j], end=" ")
        print("|",end="")
        print()
    print(end=" ")
def sub(mat1,mat2):#for subtraction


    res=[]
    print("matrix 1 = ")
    print()
    for i in range(r):  # displaying mat1
        print("| ", end="")

        for j in range(c):
            print(mat1[i][j], end=" ")
        print("|", end="")
        print()
    print()
    print("matrix2 = ", end="")
    print()
    for i in range(r1):  # displaying mat2
        print("| ", end="")

        for j in range(c1):
            print(mat2[i][j], end=" ")
        print("|", end="")
        print()
    print()
    print("subtraction of matrices is =")

    for i in range(r):
        b=[]
        for j in range(c):
            insert=0
            b.append(insert)
        res.append(b)
    for i in range(r):

        for j in range(c):
            res[i][j]=(mat1[i][j]-mat2[i][j])


    for i in range(r):
        print("| ",end="")

        for j in range(c):
            print(res[i][j], end=" ")
        print("|",end="")
        print()
    print(end=" ")


print()
print()
def multi(mat1,mat2):#for multiplication

    res = []

    for i in range(r):
        b = []
        for j in range(c1):
            insert = 0
            b.append(insert)
        res.append(b)

    for i in range(r):
        for j in range(c1):
            for k in range(r1):
                res[i][j]=res[i][j]+(mat1[i][k]*mat2[k][j])#i for row of mat 1
                                                       # k for coloumn of mat1 and row of mat2
                                                       # j for column of mat 2


    for i in range(r):
        print("| ",end="")

        for j in range(c1):
            print(res[i][j], end=" ")
        print("|",end="")
        print()
    print(end=" ")

def transpose(r2,c2):
    global mat3
    mat=[]
    print("enter elements of 1st matrix:", end=" ")
    print()
    for i in range(3):  # creation of mat1
        b = []
        for j in range(3):
            insert = 0
            b.append(insert)

        mat3.append(b)
    for i in range(r2):#inserting elements in mat
        b=[]
        for j in range(c2):
            insert=int(input(f"enter {i}{j} elment of mat "))
            b.append(insert)
        mat.append(b)
    mat3=mat
    res=[]
    for i in range(c2):
        l=[]
        for j in range(r2):
            insert=0
            l.append(insert)
        res.append(l)

    print("original matrix:")
    for i in range(r2):#displaying mat
        print("| ",end="")

        for j in range(c2):
            print(mat3[i][j], end=" ")
        print("|",end="")
        print()
    for i in range(len(mat3)):
        for j in range(len(mat3[0])):
            res[j][i]=mat3[i][j]






    print()
    print("transpose of matrix :")
    for i in range(c2):#displaying mat
        print("| ",end="")

        for j in range(r2):
            print(res[i][j], end=" ")
        print("|",end="")
        print()


run=1
while run:
    print("for creating matrices:0")
    print("for addition of matrices type 1:")
    print("for subtraction of matrices type 2:")
    print("for multiplication of matrices type 3:")
    print("for transpose of matrix type 4:")
    choice=int(input("Enter your choice:"))
    if choice==1:
        if r==r1 and c==c1:
            add(mat1,mat2)
        else:
            print("number of rows and columns of both matrices  are not same")
    elif choice==0:

        r=int(input("enter number of rows of mat1 : "))
        c=int(input("enter number of columns of mat1 : "))
        r1=int(input("enter number of rows of mat2: "))
        c1=int(input("enter number of columns of mat2: "))
        creat(r,c,r1,c1)
    elif choice==2:
        if r==r1 and c==c1:
            sub(mat1,mat2)
        else:
            print("number of rows and columns of both matrices  are not same")

    elif choice==3:
        if c==r1:
            multi(mat1,mat2)
        else:
            print("number of cols of mat1 is not eqaul to number of rows in mat2")
    elif choice==4:
        r2 = int(input("enter number of rows of mat : "))
        c2 = int(input("enter number of columns of mat : "))
        transpose(r2,c2)
    else:
        break