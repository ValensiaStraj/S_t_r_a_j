from tkinter import *
from tkinter import ttk

def form(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2
 
def prime(x1,y1,x2,y2,x3,y3):
    an = form(x1, y1, x2, y2)
    tun = form(x1, y1, x3, y3)
    drune = form(x2, y2, x3, y3)
    ps = [an, tun, drune]
    ps.sort()
    if ps[0] + ps[1]  == ps[2]:
        return 'True'
    else:
        return 'False'

def delet():
    try:
        data_A_x.delete(0,END)
        data_A_y.delete(0,END)
        data_B_x.delete(0,END)
        data_B_y.delete(0,END)
        data_C_x.delete(0,END)
        data_C_y.delete(0,END)    
        w.delete(treug)
        w.delete(l_lbl1)
        w.delete(l_lbl_p)
        w.delete(v_A)
        w.delete(v_B)
        w.delete(v_C)
    except:
        raise Exception('Удалять то еще нечего)')

def sq():
    global treug, l_lbl1, l_lbl_p, v_A, v_B, v_C
    x1,y1,x2,y2,x3,y3 = map(int,(data_A_x.get(),data_A_y.get(),data_B_x.get(),data_B_y.get(),data_C_x.get(),data_C_y.get()))
    a = abs( x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2) ) / 2
    prim_prov = prime(x1,y1,x2,y2,x3,y3)

    with open('area.txt','w') as arf, open('truefalse.txt','w') as tff:
        arf.write(str(a))
        tff.write(prim_prov)

    # треугольник
    points = ([x1+50,700-y1],[x2+50,700-y2],[x3+50,700-y3])
    treug = w.create_polygon(points, fill = 'white',outline = 'blue', width = 1)

    # вершина A треугольника
    v_A = w.create_text(x1+50-10,700-y1-10, 
                  text="A",
                  justify=CENTER, font="Verdana 10",fill="blue")
    # вершина B треугольника
    v_B = w.create_text(x2+50-10,700-y2-10, 
                  text="B",
                  justify=CENTER, font="Verdana 10",fill="blue")
    # вершина C треугольника
    v_C = w.create_text(x3+50-10,700-y3-10, 
                  text="C",
                  justify=CENTER, font="Verdana 10",fill="blue")

    # площадь треугольника
    lbl1 = ttk.Label(root,font = 'Verdana 10', 
                    background = 'white', text = 'Площадь треугольника ABC = {a}'.format(a = a))
    l_lbl1 = w.create_window(50, 830, anchor=NW, window=lbl1, width=300, height=20)
    
    if prim_prov == 'True':
        b = 'Треугольник прямоугольный'
    else:
        b = 'Тип треугольника неопределен'

    lbl_p = ttk.Label(root,font = 'Verdana 10', 
                    background = 'white', text = b)
    l_lbl_p = w.create_window(50, 860, anchor=NW, window=lbl_p, width=300, height=20)

root = Tk()
root.title("Площадь треугольника")
root.resizable(False, False)
w = Canvas(root, width=650, height=900, bg = 'white')
w.pack()

lbl_info = ttk.Label(root,font = 'Verdana 10', 
                background = 'white', text = 'Расчет площади треугольника ABC по координатам')
w.create_window(50, 50, anchor=NW, window=lbl_info, width=600, height=20)

lbl_input_ABC = ttk.Label(root,font = 'Verdana 10', 
                background = 'white', text = 'Введите значения вершин: A=                   B=                  C=')
w.create_window(50, 100, anchor=NW, window=lbl_input_ABC, width=600, height=20)

# ввод значений вершин треугольника
data_A_x = ttk.Entry()
w.create_window(265, 100, anchor=NW, window=data_A_x, width=30, height=20)
data_A_y = ttk.Entry()
w.create_window(300, 100, anchor=NW, window=data_A_y, width=30, height=20)

data_B_x = ttk.Entry()
w.create_window(380, 100, anchor=NW, window=data_B_x, width=30, height=20)
data_B_y = ttk.Entry()
w.create_window(415, 100, anchor=NW, window=data_B_y, width=30, height=20)

data_C_x = ttk.Entry()
w.create_window(490, 100, anchor=NW, window=data_C_x, width=30, height=20)
data_C_y = ttk.Entry()
w.create_window(525, 100, anchor=NW, window=data_C_y, width=30, height=20)

btn_sq = ttk.Button(text = 'Площадь', command = sq)
w.create_window(460, 130, anchor=NW, window=btn_sq, width=120, height=40)

btn_del = ttk.Button(text = 'Удалить', command = delet)
w.create_window(300, 130, anchor=NW, window=btn_del, width=120, height=40)

# Оси координат X, Y
w.create_line(50,700,50,200, fill='black',
                width=2, arrow=LAST,
                arrowshape="5 20 10")

w.create_line(50,700,600,700, fill='black',
                width=2, arrow=LAST,
                arrowshape="5 20 10")

# Значения Оси X
for k in range(0,550,50):
    w.create_text(50+k, 730, 
                  text=k,
                  justify=CENTER, font="Verdana 10",fill="blue")

 # Значения Оси Y
for k in range(50,550,50):
    w.create_text(20, 700-k, 
                  text=k,
                  justify=CENTER, font="Verdana 10",fill="blue")
   
mainloop()
