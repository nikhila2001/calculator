
############################### Logical Part ################################
def click(event):
    global input_data
    data = event.widget.cget("text")
    print(data)
    if data== "=":
        if input_data.get().isdigit():
            val = int(input_data.get)
        else:
            try:
                val = eval(input_field.get())
            except Exception as e:
                print(e) 
                val = "Error"

        input_data.set(val)
        input_field.update()

            

        
    elif data == "C":
        input_data.set("")
        input_field.update()

    else:
        input_data.set(input_data.get() + data)
        input_field.update()

        
    
#################################### GUI of calculator ###################################
from tkinter import*
from tkinter import messagebox
from tkinter.font import BOLD
root = Tk()  #parent window
root.geometry("500x450")
root.configure(bg='grey')

root.title("Calci by nik")
font_tuple =  ("Times New Roman",30,"bold")
input_data = StringVar()
input_data.set("")
input_field = Entry(root,fg ="white",font=("Times New Roman",25,"bold"),bg="green",textvariable=input_data )
input_field.pack(fill=X,padx=5,pady=5,ipady=8)
f = Frame(root,bg="green",bd=3,highlightcolor="black",highlightthickness=3,width=300,height=400)
f.pack(padx=3,pady=3,ipady=8,ipadx=3)


b0 = Button(f,bg = "black",fg = "white",font=font_tuple,text = "0")
b0.grid(row=0,column=0,ipadx = 15,ipady = 10,padx =5,pady=4)
b0.bind("<Button -1>",click)

b1 = Button(f,bg = "black",fg = "white",font=font_tuple,text = "1")
b1.grid(row=0,column=1,ipadx = 15,ipady = 10,padx =5,pady=4)
b1.bind("<Button -1>",click)

b2 = Button(f,bg = "black",fg = "white",font=font_tuple,text = "2")
b2.grid(row=0,column=2,ipadx = 15,ipady = 10,padx =5,pady=4)
b2.bind("<Button -1>",click)

b3 = Button(f,bg = "black",fg = "white",font=font_tuple,text = "3")
b3.grid(row=0,column=3,ipadx = 15,ipady = 10,padx =5,pady=4)
b3.bind("<Button -1>",click)

bplus = Button(f,bg = "black",fg = "white",font=font_tuple,text = "+")
bplus.grid(row=0,column=4,ipadx = 15,ipady = 10,padx =5,pady=4)
bplus.bind("<Button -1>",click)

b4 = Button(f,bg = "black",fg = "white",font=font_tuple,text = "4")
b4.grid(row=1,column=0,ipadx = 15,ipady = 10,padx =5,pady=4)
b4.bind("<Button -1>",click)

b5 = Button(f,bg = "black",fg = "white",font=font_tuple,text = "5")
b5.grid(row=1,column=1,ipadx = 15,ipady = 10,padx =5,pady=4)
b5.bind("<Button -1>",click)    

b6 = Button(f,bg = "black",fg = "white",font=font_tuple,text = "6")
b6.grid(row=1,column=2,ipadx = 15,ipady = 10,padx =5,pady=4)
b6.bind("<Button -1>",click)

b7 = Button(f,bg = "black",fg = "white",font=font_tuple,text = "7")
b7.grid(row=1,column=3,ipadx = 15,ipady = 10,padx =5,pady=4)
b7.bind("<Button -1>",click)

bminus = Button(f,bg = "black",fg = "white",font=font_tuple,text = "-")
bminus.grid(row=1,column=4,ipadx = 19,ipady = 10,padx =5,pady=4)
bminus.bind("<Button -1>",click)
b8 = Button(f,bg = "black",fg = "white",font=font_tuple,text = "8")
b8.grid(row=2,column=0,ipadx = 15,ipady = 10,padx =5,pady=4)
b8.bind("<Button -1>",click)

b9 = Button(f,bg = "black",fg = "white",font=font_tuple,text = "9")
b9.grid(row=2,column=1,ipadx = 15,ipady = 10,padx =5,pady=4)
b9.bind("<Button -1>",click)

b00 = Button(f,bg = "black",fg = "white",font = ("Times New Roman",25,"bold"),text="00")
b00.grid(row=2,column=2,ipadx = 15,ipady = 10,padx =11,pady=2)
b00.bind("<Button -1>",click)

bdot = Button(f,bg = "black",fg = "white",font=font_tuple,text = ".")
bdot.grid(row=2,column=3,ipadx = 19,ipady = 10,padx =5,pady=4)
bdot.bind("<Button -1>",click)

bc = Button(f,bg = "black",fg = "white",font=font_tuple,text = "C")
bc.grid(row=2,column=4,ipadx = 15,ipady = 10,padx =8,pady=4)
bc.bind("<Button -1>",click)

bx = Button(f,bg = "black",fg = "white",font=font_tuple,text = "*")
bx.grid(row=3,column=0,ipadx = 15,ipady = 10,padx =5,pady=4)
bx.bind("<Button -1>",click)

bdivide = Button(f,bg = "black",fg = "white",font=font_tuple,text = "/")
bdivide.grid(row=3,column=1,ipadx = 15,ipady = 10,padx =5,pady=4)
bdivide.bind("<Button -1>",click)

bpercent = Button(f,bg = "black",fg = "white",font=font_tuple,text = "%")
bpercent.grid(row=3,column=2,ipadx = 15,ipady = 10,padx =5,pady=4)
bpercent.bind("<Button -1>",click)

b = Button(f,bg = "black",fg = "white",font=font_tuple,text = ",")
b.grid(row=3,column=3,ipadx = 15,ipady = 10,padx =5,pady=4)
b.bind("<Button-1>",click)

bequal = Button(f,bg = "black",fg = "white",font=font_tuple,text = "=")
bequal.grid(row=3,column=4,ipadx = 15,ipady = 10,padx =5,pady=4)
bequal.bind("<Button -1>",click)

root.mainloop()