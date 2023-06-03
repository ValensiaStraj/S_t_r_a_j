from tkinter import *

### функция обработки события, при нажатии <Enter>
def presnum(event):
    if o_x[4].get().isdigit() and o_y[4].get().isdigit():
        
        x=int(o_x[4].get())-6
        y=int(o_y[4].get())-6
        for i in range(0,10):
            o_x[i].delete(0,END)
            o_x[i].insert(0,x+i+2)

        for i in range(0,10):
            o_y[i].delete(0,END)
            o_y[i].insert(0,y+i+2)
        
        for i in range(0,10):
            for j in range(1,11):
                spv[i][j].delete(0,END)
                spv[i][j].insert(0,(y+i+2)*(x+j+1))

### конструктор окна
window=Tk()
window.title('Pifagor 2.0')
window.geometry("375x215")
window.resizable(0,0)

### формирование заголовков таблицы
lab = Label(text="        ")
lab.grid(row=0,column=0)

o_x=[]
o_y=[]
x=y=0
for i in range(0,10):
    if i==4:bgr='wheat2'
    else: bgr='gray48'
    v=Entry(width=5,bg=bgr)
    o_x.append(v)
    o_x[i].grid(row=0,column=i+1)
    o_x[i].insert(0,x+i+2)

for i in range(0,10):
    if i==4:bgr='wheat2'
    else: bgr='gray48'
    v=Entry(width=5,bg=bgr)
    o_y.append(v)
    o_y[i].grid(row=i+1,column=0)
    o_y[i].insert(0,y+i+2)

### формирование ячеек таблицы   
spv=[]
for i in range(0,10):
    spv.append([i])
    for j in range(1,11):
        if i==4 or j==5:bgr='wheat2'
        else: bgr='ghostwhite'
        v=Entry(width=5,bg=bgr)   
        spv[i].append(v)
        spv[i][j].grid(row=i+1,column=j)
        
### заполнение тыблицы первоначальными данными
for i in range(0,10):
    for j in range(1,11):
        spv[i][j].insert(0,(i+2)*(j+1))

### обработка событий
o_x[4].bind('<KeyRelease>', presnum)
o_y[4].bind('<KeyRelease>', presnum)

###
window.mainloop()
