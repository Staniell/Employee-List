from tkinter import *

emp_number = 201915000
class Selection:
    def __init__(self, root):

        with open("Employeelist.txt",'a') as f:
            print('')

        
        values = {"1":"CEO","2":'Manager',"3":'Assistant',"4":'Secretary','6':"Staff"}
        programs = ["Accounting","Human Resources",'Sales and Marketing','Manufacturing',"Admin"]

        var2 = IntVar()
        var1 = IntVar()
        root.title("Employee List")


        self.canvas = Canvas(root, height = 600, width = 700, bg = 'light grey')
        self.canvas.pack()
        self.canvas3 = Canvas(root, height = 70, width = 700, bg = 'grey')
        self.canvas3.place(x = 0,y=0)
        self.canvas.create_text(330, 170, fill = "black", text = "Result",font="Georgia")
        self.canvas1 = Canvas(root, height = 300, width = 240, bg = 'white')
        self.canvas1.place(x = 300, y = 180)
       
       

        #Title
        self.title = Label(root, text="Employee List",bg = 'light grey',fg='black')
        self.title.config(font=("Georgia",28))
        self.title.place(x=120, y=10)

        #Employee number
        self.num = Label(root, text = 'Employee Number',bg = 'light grey',fg='black')
        self.num.config(font=("Georgia",16))
        self.num.place(x=300, y=95)


        #Last Name and First Name
        self.fname = Label(root, text = 'Last Name',bg = 'light grey',fg='black')
        self.fname.config(font=("Georgia",16))
        self.fname.place(x=14, y=90)

        self.lname = Label(root, text = 'First Name',bg = 'light grey',fg='black')
        self.lname.config(font=("Georgia",16))
        self.lname.place(x=14, y=120)

        #Gender
        self.gender = Label(root, text = 'Gender',bg = 'light grey',fg='black')
        self.gender.config(font=("Georgia",14))
        self.gender.place(x=14, y=155)

        #Interests
        self.interests = Label(root, text = 'Position',bg = 'light grey',fg='black')
        self.interests.config(font=("Georgia",16))
        self.interests.place(x=14, y=190)

        #Programs
        self.programs = Label(root, text = 'Program',bg = 'light grey',fg='black')
        self.programs.config(font=("Georgia",16))
        self.programs.place(x=150, y=190)

        #Radio Buttons
        def Add_Employee():
            q = interest()
            self.canvas1.delete('all')
            if self.name.get() == '' or self.name2.get() == '' or gender() == None:
                self.canvas1.create_text(90, 25, fill = "black", text = "Please fill out every information first.",font = ('Verdana',12), width = 200, tag = 'erase')
            else:
                with open("Employeelist.txt",'r') as f:
                    u = f.readlines()
                    for i in u:
                        if i.split(',')[0] == str(emp_number):
                            self.canvas1.create_text(100, 65, fill = "black", text = "Employee number already exists!\n\nPlease Select 'New' Button to generate a new number.",font = ('Verdana',12), width = 200, tag = 'erase')
                            with open('Employeenumber.txt','w') as f:
                                f.write(str(emp_number))
                            break
                    else:
                        self.canvas1.create_text(100, 105, fill = "black", text = f"\nEmployee number:\n{emp_number}\nLast Name: {self.name.get()}\nFirst Name: {self.name2.get()}\nGender: {gender()}\nPosition: {interest()}\nDepartment: {self.listbox.get(ACTIVE)}\n\nStudent Information Successfully Added!",font = ('Verdana',12), width = 200, tag = 'erase')
                        with open("Employeelist.txt",'a') as f:
                            f.write(f"{emp_number},{self.name.get()},{self.name2.get()},{self.listbox.get(ACTIVE)},{gender()},{q};\n")
            

        def New():
            global emp_number
            with open('Employeelist.txt', 'r') as s:
                a = s.readlines()
            if len(a) > 1:
                with open('Employeelist.txt','r') as f:
                    file = f.readline()
                    for la in f:
                        pass
                        x = la.split(',')[0]
                    emp_number = int(x)
            
            self.canvas1.delete('all')
            self.name.delete(0, 'end')
            self.student_num.delete(0, 'end')
            self.name2.delete(0, 'end')
            self.radiom.deselect()
            self.radiof.deselect()
        

            emp_number +=1

            with open('Employeenumber.txt','w') as f:
                f.write(str(emp_number))



        def gender():
            try:
                if var2.get() == 1:
                    return 'Male'
                elif var2.get() == 2:
                    return 'Female'
            except:
                return None

        def interest():
            values = {"1":"CEO","2":'Manager',"3":'Assistant',"4":'Secretary','6':"Staff"}
            newval = {v:k for k,v in values.items()}
            try:
                s = values[str(var1.get())]
                x = newval[s]
                z = values[x]
                return z
            except:
                return None

        def Search():
            self.canvas1.delete('all')
            with open("Employeelist.txt", 'r') as f:
                x = f.readlines()
            for i in x:
                if str(self.student_num.get()) == str(i.split(',')[0]):
                    self.canvas1.create_text(100, 120, fill = "black", text = f"Employee number: {i.split(',')[0]}\n\nLast Name: {i.split(',')[1]}\n\nFirst Name: {i.split(',')[2]}\n\nGender: {i.split(',')[4]}\n\nPosition: {i.split(',')[5].replace(';',' ')}\nDepartment: {i.split(',')[3]}", font = ('Verdana',12),width = 200, tag = 'erase')
                    break
            else:   
                self.canvas1.create_text(100, 35, fill = "black", text = f"Employee number Does not Exist...", font = ('Verdana',12),width = 200, tag = 'erase')

        def Deletez():
            h = 0
            self.canvas1.delete('all')
            with open("Employeelist.txt", 'r') as f:
                x = f.readlines()
            with open('Employeelist.txt', 'w') as f:
                for i in x:
                    if str(self.student_num.get()) == str(i.split(',')[0]):
                        h +=1
                        pass
                    else:
                        f.write(i)
            if h == 1:
                self.canvas1.create_text(100, 35, fill = "black", text = f"Employee Information Successfully Deleted!",font = ('Verdana',12), width = 200, tag = 'erase')

            else:
                self.canvas1.create_text(100, 35, fill = "black", text = f"Employee number Does not Exist...",font = ('Verdana',12), width = 200, tag = 'erase')

        self.Add_button = Button(root, text="Save", command=Add_Employee)
        self.Add_button.place(x=228, y=450)

        self.New_button = Button(root, text = "New", command=New)
        self.New_button.place(x=190, y = 450)

        self.student_num = StringVar()
        self.student_num = Entry(root, width = 40)
        self.student_num.place(x=300, y = 126)

        self.name = StringVar()
        self.name = Entry(textvariable=self.name, width =25)
        self.name.place(x=130, y=97)

        self.name2 = StringVar()
        self.name2 = Entry(root, width =25)
        self.name2.place(x=130, y=126)


        self.radiom = Radiobutton(root, text = 'Male', variable = var2, value = 1, command=gender)
        self.radiom.place(x=90, y=157)
        self.radiof = Radiobutton(root, text = 'Female', variable = var2, value = 2, command=gender) 
        self.radiof.place(x=150, y=157)


        self.search = Button(root, text = 'Search', command=Search)
        self.search.place(x=500,y=150)

        self.deletex = Button(root, text = "Delete", command=Deletez)
        self.deletex.place(x=450, y = 150)
        


        b = 220
        x = 1
        for key, val in values.items():
            Radiobutton(root, text = val, variable = var1, value = x, command=interest).place(x =20 ,y = b)
            b+=30
            x+=1

        

        self.listbox = Listbox(root, height =14, width = 20)
        self.listbox.place(x=140,y=220)

        for i in programs:
            self.listbox.insert(END, i)
      


     

root = Tk()
root.geometry('600x500')
StudentApp = Selection(root)
root.mainloop()


