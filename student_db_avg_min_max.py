user = int(input("ENTER NUMBER OF STUDENTS IN CLASS : "))
i = 1
marks = []
absent = []
# mark = marks.copy()
print("FOR ABSENT STUDENTS TYPE -1 AS MARKS")
for j in range(user):
    student = int(input("ENTER MARKS OF STUDENT  {} : ".format(i)))
    if student == -1:
        absent.append(i)
    else:
        marks.append(student)

    i += 1

def avg():
    mrk = 0

    for mark in marks:
        mrk += mark
    avg = mrk/(user-len(absent))
    print("AVERAGE SCORE OF THE CLASS IS  {}".format(avg))
def hmax_hmin():
    hmax = 0
    hmin = 100
    for high in marks:
        if high > hmax:
            hmax = high

    for min in marks:
        if min < hmin:
            hmin = min
    print("HIGHEST SCORE OF THE CLASS IS  {}".format(hmax))
    print("--------------------------")
    print("LOWEST SCORE OF THE CLASS IS {}".format(hmin))


print("--------------------------")
# print("--------------------------")
# print("--------------------------")
def abs_nt():
    if len(absent) > 1:
        print("{} STUDENTS WERE ABSENT FOR THE TEST".format(len(absent)))
    elif len(absent) >= 1:
        print("{} STUDENT WAS ABSENT FOR THE TEST".format(len(absent)))
    else:
        print("ALL STUDENTS WERE PRESENT FOR THE TEST")
print("--------------------------")
def freq():
    frq = 0
    frmax = 0
    for ele in marks:
        if marks.count(ele) > frq:
            frq = marks.count(ele)
            frmax = ele
    print("{} IS THE SCORE WITH HIGHEST OCCURING FREQUENCY {}".format(frmax, frq))
########################################
while(1):
    print("FOR AVG TYPE 1")
    print("FOR MAX_MARKS AND MIN_MARKS TYPE 2")
    print("FOR FREQUENCY TYPE 3")
    print("FOR NUMBER OF ABSENT STUDENT TYPE 4")
    choise=int(input())
    if choise==1:
        print("--------------------------")
        avg()
        print("--------------------------")
    elif choise==2:
        print("--------------------------")
        hmax_hmin()
        print("--------------------------")
    elif choise==3:
        print("--------------------------")
        freq()
        print("--------------------------")
    elif choise==4:
        print("--------------------------")
        abs_nt()
        print("--------------------------")
    else:
        print("--------------------------")
        print("TYPE RIGHT CHOICE")
        print("--------------------------")
        break
