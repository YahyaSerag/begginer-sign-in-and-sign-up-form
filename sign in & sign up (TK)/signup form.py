import ast
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('login')
window.geometry('925x500+300+200')
window.resizable(False,False)

def sign_up():
    username = user.get()
    password = pasw.get()
    confirm_pass = cpw.get()

    if password == confirm_pass:
        try:
            file = open('datasheet', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('datasheet', 'w')
            w = file.write(str(r))

            messagebox.showinfo('signup', 'Sucessfully sign up')
        except:
            file = open('datasheet', 'w')
            pp = str({username:password})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Invalid', ' Both password should match!')


img = PhotoImage(file = 'sign up.png')
Label(window, image=img, bg='white', height=320).place(x=85, y=75)

frame = Frame(window, width=350, height=325, bg='white')
frame.place(x=475, y=75)


heading = Label(frame, text='SIGN UP', fg='#57a1f8', bg='white', font=('C',23,'bold'))
heading.place(x=105, y=30 )

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0,'Username')

user = Entry(frame, width=25, fg='black', border=0, bg= 'white', font= ('Microsoft YaHei UI Light',9))
user.place(x=60, y= 85 )
user.insert(0, 'UserName')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=225, height=2, bg='black').place(x=52, y=105)

def on_enter(e):
    pasw.delete(0,'end')

def on_leave(e):
    name = pasw.get()
    if name == '':
        pasw.insert(0,'Password')

pasw = Entry(frame, width=25, fg='black', border=0, bg= 'white', font= ('Microsoft YaHei UI Light',9))
pasw.place(x=60, y= 130 )
pasw.insert(0, 'Password')
pasw.bind('<FocusIn>', on_enter)
pasw.bind('<FocusOut>', on_leave)

Frame(frame,width=225, height=2, bg='black').place(x=52, y=150)

def on_enter(e):
    cpw.delete(0,'end')

def on_leave(e):
    name = cpw.get()
    if name == '':
        cpw.insert(0,'Confirm password')

cpw = Entry(frame, width=25, fg='black', border=0, bg= 'white', font= ('Microsoft YaHei UI Light',9))
cpw.place(x=60, y= 175 )
cpw.insert(0, 'Confirm password')
cpw.bind('<FocusIn>', on_enter)
cpw.bind('<FocusOut>', on_leave)

Frame(frame,width=225, height=2, bg='black').place(x=52, y=195)

Button(frame, width=31, pady=7, text='sign up', bg='#57a1f8', fg='white', border=0, command=sign_up).place(x=53,y=225)
label = Label(frame,text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light',8))
label.place(x=93, y=270)

signin = Button(frame, width=6, text='sign in', border = 0, bg='white', cursor='hand2', fg= '#57a1f8')
signin.place(x=185, y=270)

window.mainloop()