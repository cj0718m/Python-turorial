from tkinter import *
window = Tk()

photo = PhotoImage(file = "C:\\Users\\cj071\\Downloads\\KakaoTalk_20250506_162627345.gif")
photo = PhotoImage(file = "C:\\Users\\cj071\\Downloads\\KakaoTalk_20250506_162627345.gif")

labe1 = Label(window,image = photo)
label2= Label(window,image = photo)
labe1.pack(side=LEFT)
label2.pack(side=RIGHT)

window.mainloop()