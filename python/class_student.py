#display the particular details of the student
class student:
    def __init__(self,name,reg,m1,m2,m3):
        self.name=name
        self.reg=reg
        self.marks1=m1
        self.marks2=m2
        self.marks3=m3
def display(reg):
    for st in s:
        if st.reg==reg:
            print("name=",st.name)
            print("reg no=",st.reg)
            print("marks1=",st.marks1)
            print("marks2=",st.marks2)
            print("marks3=",st.marks3) 
s=[]
n=int(input("enter the number of student"))
for i in range(n):
    name=input("enter the name:")
    reg=int(input("enter the reg no:"))
    marks1=int(input("enter the marks1:"))
    marks2=int(input("enter the marks2:"))
    marks3=int(input("enter the marks3:"))
    st=student(name,reg,marks1,marks2,marks3)
    s.append(st)
k=int(input("enter the reg number of student hows detail needed"))
display(k)


        