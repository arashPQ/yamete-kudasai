from tkinter import *
from playsound import playsound

main = Tk()
main.title("Network ERROR")
main.geometry("250x100")
main.resizable(False, False)



text = Label(main, text="This not important Error.", fg="midnightblue").place(x=10, y=10)
def comm():
    playsound('1.mp3')


def dis():
    pass

main.protocol("WM_DELETE_WINDOW", dis)
button = Button(main, text="Accept and Close", font="arial 12 bold", fg="midnightblue", bg="aqua", command=comm).place(x=30, y=60)
main.mainloop()