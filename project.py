import sys
def calc_avg(x):
    avg = (int(x[2]) + int(x[3])) / 2
    if avg >= 90:
        gra = "A"
    elif avg >= 80:
        gra = "B"
    elif avg >= 70:
        gra = "C"
    elif avg >= 60:
        gra = "D"
    else:
        gra = "F"
    return avg, gra

def show(x):
    title = ["Student ", "Name    ", "Mid", "Final", "Average", "Grade"]
    for i in title:
        print(i, end="\t")
    print("")
    print("-------------------------------------------------------------")
    if x[0]:
        x.sort(key=lambda x: x[4], reverse=True)
        for i in x:
            print(*i, sep="\t")

def search(x):
    id_q = input("Student ID:")
    find = False
    for i in x:
        if id_q == i[0]:
            show([i])
            find = True
    if find == False:
        print("No Such Person")

def changescore(x):
    id_q = input("Student ID:")
    find = False
    for i in x:
        if id_q == i[0]:
            exam_q = input("Mid/Final?").lower()
            if exam_q == "mid":
                mid_q = input("Input new score:")
                if int(mid_q) >=0 and int(mid_q) <=100:
                    show([i])
                    i[2] = mid_q
                    i[4], i[5] = calc_avg(i)
                    print("Score changed.")
                    print(*i, sep = "\t")
            elif exam_q == "final":
                final_q = input("Input new score:")
                if int(final_q) >= 0 and int(final_q) <= 100:
                    show([i])
                    i[3] = mid_q
                    i[4], i[5] = calc_avg(i)
                    print("Score changed.")
                    print(*i, sep="\t")
            find = True
    if find == False:
        print("No Such Person")

def add(x):
    id_q = input("Student ID:")
    find = False
    for i in x:
        if id_q == i[0]:
            print("ALREADY EXISTS")
            find = True
    if find == False:
        name_q = input("Name:")
        mid_q = input("Midterm Score:")
        final_q = input("Final Score:")
        new = []
        new.append(id_q)
        new.append(name_q)
        new.append(mid_q)
        new.append(final_q)
        avg, gra = calc_avg(new)
        new.append(avg)
        new.append(gra)
        x.append(new)
        print("Student added.")

def searchgrade(x):
    gra_q = input("Grade to search:").upper()
    find = False
    possible_q = ["A","B","C","D","F"]
    if gra_q not in possible_q:
        pass
    else:
        temp_list = []
        for i in x:
            if gra_q == i[5]:
                temp_list.append(i)
                find = True
        if find == False:
            print("NO RESULTS")
        else:
            show(temp_list)

def remove(x):
    if not x:
        print("List is empty")
    else:
        id_q = input("Student ID:")
        find = False
        for i in x:
            if id_q == i[0]:
                x.remove(i)
                print("Student removed.")
                find = True
        if find == False:
            print("No Such Person")

def quit(x):
    quit_q = input("Save data?[yes/no]")
    if quit_q == "yes":
        x.sort(key=lambda x: x[4], reverse=True)
        file_name = input("File name:")
        f = open(file_name, "w")
        for i in x:
            f.write(f"{i[0]:<10}\t{i[1]:<15}\t{i[2]:<3}\t{i[3]:<3}\n")
        f.close()
        return True

#-----------------------------------------------------#
# 파일을 연다
if len(sys.argv) == 1:
    f = open("students.txt", "r")
else:
    f = open(sys.argv[1], "r")

# 텍스트를 받을 임시 리스트를 생성한다.
t_list = []
for i in f:
    t_list.append(i)
f.close()

# 임시 리스트의 텍스트 내용을 받아 리스트를 생성한다
s_list = []
for i in t_list:
    s_list.append(i.strip().split("\t"))

# 평균과 등급을 추가한다.
for i in s_list:
    avg, gra = calc_avg(i)
    i.append(avg)
    i.append(gra)

# 프로그램 시행
while True:
    command = input("# ")
    if command == "show":
        show(s_list)
    elif command == "search":
        search(s_list)
    elif command == "changescore":
        changescore(s_list)
    elif command == "add":
        add(s_list)
    elif command == "searchgrade":
        searchgrade(s_list)
    elif command == "remove":
        remove(s_list)
    elif command == "quit":
        quit_q = quit(s_list)
        if quit_q == True:
            break
    else:
        continue
print("프로그램 끝")
