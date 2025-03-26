from tkinter import Tk, Label

root = Tk()
root.geometry('300x200')

# Label with padding
label1 = Label(root, text="Top Padding", bg="lightblue")
label1.pack(pady=(20, 10))  # 20 pixels of padding above, 10 below

label2 = Label(root, text="No Padding", bg="lightgreen")
label2.pack()  # Default padding (none)

label3 = Label(root, text="Bottom Padding", bg="lightcoral")
label3.pack(pady=(0, 30))  # 30 pixels of padding below

root.mainloop()
