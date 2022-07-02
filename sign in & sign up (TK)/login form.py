from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('login')
root.geometry('925x500+300+200')
root.resizable(False,False)

def sign_in():
    username = user.get()
    password = pasw.get()

    if username == 'admin' and password == '123':
        screen = Toplevel(root)
        screen.title('App')
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen, text='Hello Everyone!', bg='#fff', font=('Microsoft YaHei UI Light',50,'bold')).pack(expand=True)

        screen.mainloop()

    elif username != 'admin' and password != '123':
         messagebox.showerror('Invalid', 'invalid username and password!')

    elif password != '123':
        messagebox.showerror('Invalid','invalid password!')

    elif username != 'admin':
        messagebox.showerror('invalid','invalid username!')

img = PhotoImage(file = 'login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=335, bg='white')
frame.place(x=450, y=50)

heading = Label(frame, text='SIGN IN', fg='#57a1f8', bg='white', font=('C',23,'bold'))
heading.place(x=105, y=30 )

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0,'Username')

user = Entry(frame, width=25, fg='black', border=0, bg= 'white', font= ('Microsoft YaHei UI Light',11))
user.place(x=60, y= 90 )
user.insert(0, 'UserName')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=225, height=2, bg='black').place(x=52, y=115)

def on_enter(e):
    pasw.delete(0,'end')

def on_leave(e):
    name = pasw.get()
    if name == '':
        pasw.insert(0,'Password')

pasw = Entry(frame, width=25, fg='black', border=0, bg= 'white', font= ('Microsoft YaHei UI Light',11))
pasw.place(x=60, y= 140 )
pasw.insert(0, 'Password')
pasw.bind('<FocusIn>', on_enter)
pasw.bind('<FocusOut>', on_leave)

Frame(frame,width=225, height=2, bg='black').place(x=52, y=165)

Button(frame, width=32, pady=7, text='sign in', bg='#57a1f8', fg='white', border=0, command=sign_in).place(x=50,y=200)
lable = Label(frame, text="Don't have an account?",fg='black', bg='white', font=('Microsoft YaHei UI Light',9 ))
lable.place(x=75, y=260)

sign_up = Button(frame, width=6, text='sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=260)




root.mainloop()