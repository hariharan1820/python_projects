class school:
    def __init__(self,ts):
        print("TOTAL NUMBER OF STUDENT IN SCHOOL=",ts)

class count(school):
    def __init__(self):
        fileA=open(r"C:\Users\My PC\Desktop\python project\sectionA.txt", "r")
        count=len(fileA.readlines())
        print("TOTAL NUMBER OF STUDDENT IN SECTION A =",count)
        fileB = open(r"C:\Users\My PC\Desktop\python project\sectionB.txt", "r")
        count1 =len(fileB.readlines())
        print("TOTAL NUMBER OF STUDDENT IN SECTION B =", count1)

        total=count+count1
        self.total=total
        super().__init__(total)

class student:
    def add(self, section,stulist):
        if section == 'A':
            fileA = open(r"C:\Users\My PC\Desktop\python project\sectionA.txt", "a+")
            fileA.seek(0)
            data = fileA.readlines()
            if str(stulist) + "\n" in data:
                print("student name aleady exist")
            else:
                fileA.write("%s\n" % stulist)
                print('done')
            fileA.close()
            b = count()
        else:
            fileB = open(r"C:\Users\My PC\Desktop\python project\sectionB.txt", "a+")
            fileB.seek(0)
            data = fileB.readlines()
            if str(stulist) + "\n" in data:
                print("student name aleady exist")
            else:
                fileB.write("%s\n" % stulist)
                print('done')
            fileB.close()
            b = count()

    def delete(self, section, stulist1):
        if section == 'A':
            strn=[]
            fileA = open(r"C:\Users\My PC\Desktop\python project\sectionA.txt", "a+")
            temp=open(r"C:\Users\My PC\Desktop\python project\temp.txt", "w+")
            fileA.seek(0)
            for i in fileA.readlines():
                strn.append(i)
            for i in strn:
                if i != str(stulist1)+"\n":
                    temp.write(i)
            fileA.close()
            temp.close()
            import os
            os.remove(r"C:\Users\My PC\Desktop\python project\sectionA.txt")
            os.rename(r"C:\Users\My PC\Desktop\python project\temp.txt", r"C:\Users\My PC\Desktop\python project\sectionA.txt")
            b = count()
        else:
            strn = []
            fileB = open(r"C:\Users\My PC\Desktop\python project\sectionB.txt", "a+")
            temp1 = open(r"C:\Users\My PC\Desktop\python project\temp1.txt", "w+")
            fileB.seek(0)
            for i in fileB.readlines():
                strn.append(i)
            for i in strn:
                if i != str(stulist1) + "\n":
                    temp1.write(i)
            fileB.close()
            temp1.close()
            import os
            os.remove(r"C:\Users\My PC\Desktop\python project\sectionB.txt")
            os.rename(r"C:\Users\My PC\Desktop\python project\temp1.txt",r"C:\Users\My PC\Desktop\python project\sectionB.txt")
            b = count()


print("CHOOSE THE TASK YOU WANT TO DO")
task=(input("1.ADD STUDENT \n2.DELETE STUDENT \n3.STUDENT COUNT\n"))

if task=='1':
    print("ENTER STUDENT DETAILS")
    stuname=input("enter student name")
    stustandard=input("Enter standard")
    stusection=input("Enter section")
    stuage=input("Enter age")
    stulist=[stuname,stustandard,stusection,stuage]
    a = student()
    print(stulist)
    a.add(stusection,stulist)

elif task=='2':
    print("ENTER STUDENT DETAILS TO DELETE")
    stuname = input("enter student name")
    stustandard = input("Enter standard")
    stusection = input("Enter section")
    stuage = input("Enter age")
    stulist = [stuname, stustandard, stusection, stuage]
    a = student()
    print("ENTERED DATA",stulist)
    a.delete(stusection,stulist)
elif task=='3':
    b = count()
else:
    print("ENTER CORRECT TASK TO PERFORM ")




