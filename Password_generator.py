from tkinter import *
import string
import random


def generate():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation
    
    all=small_alphabets+capital_alphabets+numbers+special_characters
    
    password_length=int(length_Box.get())
    
    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))
    
    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))
    
root=Tk()
root.config(bg='#007FFF')
choice=IntVar()
Font=('arial',14,'bold')

#Password generator
passwordLabel=Label(root,text="Password Generator",font='arial',fg='#F5F5DC',bg='#0000EE')
passwordLabel.grid(pady=2)

#weak
weakradioButton=Radiobutton(root,text='weak',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)

#medium
mediumradioButton=Radiobutton(root,text='medium',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)

#strong
strongradioButton=Radiobutton(root,text='strong',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=5)

lengthLabel=Label(root,text="Password Length",font='Font',fg='#F5F5DC',bg='#9A32CD')
lengthLabel.grid(pady=5)


length_Box=Spinbox(root,from_=4,to_=19,width=5)
length_Box.grid(pady=5)

generateButton=Button(root,text='Generate',font=Font,command=generate,fg='#F5F5DC',bg='#9A32CD')
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2)
passwordField.grid(pady=5)


root.mainloop()

