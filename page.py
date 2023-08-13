from tkinter import *

#####################################################################  Root Method
root = Tk()
root.geometry=('800x600+400+100')
root.configure(bg='powder blue')
root.title('Typing Speed Tester Game')
root.iconbitmap('')
##################################################################### Variables
score = 0
Timeleft = 60
count = 0
sliderWords = ''
#####################################################################  Lable Method
frontLabel = Label(root, text='Welcome To Typing Master', font=('airal', 28, 'bold'), bg='powder blue', fg='red')

frontLabel.place(x=10, y=10)

wordLabel = Label(root,text='Guitar',font=('airal',28,'bold'),bg='powder blue')
wordLabel.place(x=350, y=200)

scoreLable = Label(root,text='Your Score :',font=('airal', 20, 'bold'), bg='Powder Blue',fg='blue')
scoreLable.place(x=10, y=100)

scoreLablecount = Label(root, text='Score', font=('airal', 20, 'bold'), bg='Powder Blue', fg='Blue')
scoreLablecount.place(x=80, y=180)

timerLable = Label(root, text='Time left : ',font=('airal', 20, 'bold'), bg='Powder Blue', fg='Blue')
timerLable.place(x=600, y=100)

timeLableCount = Label(root, text='Time Left', font=('airal', 20, 'bold'), bg='Powder Blue', fg='Blue')
timeLableCount.place(x=680,y =180)

###################################################################### Entry Method
wordEntry = Entry(root,font=('airal',20,'bold'),bd=10,justify='center' )

wordEntry.place(x=250,y=300)
wordEntry.focus_set()


root.mainloop()
