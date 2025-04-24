import os
import matplotlib.pyplot as plt
class Student:
    def __init__(self, i, name):
        self.name = name
        self.id = i
        self.grade = 0
    def add_grade(self, grade):
        self.grade += grade
class Grades:
    def __init__(self, name, points, num):
        self.grades = []
        self.name = name
        self.points = points
        self.num = num
    def add_grade(self, grade):
        self.grades.append(grade)
    def get_avg(self):
        grades = self.grades
        total = 0
        for i in grades:
            total += float(i)
        return total/len(grades)
    def get_min(self):
        grades = self.grades
        return min(grades)
    def get_max(self):
        grades = self.grades
        return max(grades)




std = []
assn = []
grades = []
with open("data/students.txt", "r") as file:
    for line in file:
        name = line[3:]
        num = line[:3]
        student = Student(num, name)
        std.append(student)
with open("data/assignments.txt", "r") as file:
    lns = []
    for line in file:
        lns.append(line)
    for i in range(0, len(lns), 3):
        name = lns[i]
        num = lns[i+1]
        pts = int(lns[i+2])
        assignment = Grades(name, pts, num)
        assn.append(assignment)
# def get_count(ls):
#     tot = 0
#     count = 0
#     for i in ls:
#         count += 1
#         tot += i.points
#     print(tot, count)
# get_count(assn)
for filename in os.listdir("data/submissions"):
    with open(f"data/submissions/{filename}", "r") as file:
        txt = file.read()
        stud = txt[:3]
        num = txt[4:(len(txt))-3]
        grade = txt[(len(txt)-2):]
        #print(num, stud, grade)
        for i in assn:
           # print(f"{i.num.strip()} {num.strip()}")
            #print(i.num.strip() == num.strip())
            if i.num.strip() == num.strip():
                #print("Hello")
                i.grades.append(grade)
        for i in std:
            if i.id.strip() == stud.strip():
                for j in assn:
                    if j.num.strip() == num.strip():
                        points = j.points
                        #print(points, "HELLO")
                i.add_grade((int(grade)/1000)*points)
        j = True
        for i in assn:
            #print(i.num)
            if i.num == num:
                #print(i.num)
                #print("NOW NOW NOW NOW")
                i.add_grade(grade)






# assignment = assn[1]
# print(assignment.points)
# print(assignment.num)
# print(assn[2].get_avg())
# i = std[1]
# print(i.name)
# print(i.grade)
# print(i.id)

def main():
    print("1. Student grade\n2. Assignment statistics\n3. Assignment graph\n")
    opt = input("Enter your selection: ")
    if int(opt) == 1:
        name = input("What is the student's name: ")
        good = None
        for i in std:
            if i.name.strip() == name.strip():
                print(f"{i.grade:.0f}%")
                good = 1
        if good is None:
            print("Student not found")
    if int(opt) == 2:
        assignment = input("What is the assignment name: ")
        good = None
        for i in assn:
            if i.name.strip() == assignment.strip():
                print(f"Min: {i.get_min()}")
                print(f"Avg: {i.get_avg():.0f}")
                print(f"Max: {i.get_max()}")
                good = 1
        if good is None:
            print("Assignment not found")
    if int(opt) == 3:
        name = input("What is the assignment name: ")
        assignment = None
        for i in assn:
            if i.name.strip() == name.strip():
                assignment = i
                break
        if assignment is None:
            print("Assignment not found")
        else:
            low = float(assignment.get_min().strip())
            #print(low)
            high = float(assignment.get_max().strip())
            #print(high)
            interval = (high - low) / 10
            two = low + interval
            three = two + interval
            quatre = three + interval
            cinq = quatre + interval
            six = cinq + interval
            sept = six + interval
            huite = sept + interval
            neuf = huite + interval
            #print(low, two, three, quatre, cinq, six, sept, huite, neuf, high)
            #print(assignment.grades)
            plt.hist([int(i) for i in assignment.grades],
                     bins=[low-interval,low, two, three, quatre, cinq, six, sept, huite, neuf, high,high+interval])
            plt.show()

if __name__ == "__main__":
    main()