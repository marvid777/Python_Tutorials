import tkinter as tk

# tkinter._test()

root = tk.Tk()
root.title("Das ist das Hauptfenster")
root.geometry("800x400")
root.minsize(width=250, height=250)
root.maxsize(width=600, height=600)
root.resizable(width=False, height=True)


label1 = tk.Label(root, text="Hallo Martin", bg="green")
label1.pack(side="top", expand=True,  fill="y")

label2 = tk.Label(root, text="Hallo Marie", bg="red")
label2.pack(side="top", expand=True,  fill="both")


root.mainloop()

# print("Textausgabe")

