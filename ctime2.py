import unicurses as curses
import keyboard
import locale
import time
import sys
 
 
numbers = {
    0: ('**********',
        '*        *',
        '*        *',
        '*        *',
        '*        *',
        '*        *',
        '*        *',
        '*        *',
        '*        *',
        '*        *',
        '**********'),
    1: ('         *',
        '       * *',
        '     *   *',
        '   *     *',
        ' *       *',
        '         *',
        '         *',
        '         *',
        '         *',
        '         *',
        '         *'),
    2: ('**********',
        '         *',
        '         *',
        '         *',
        '         *',
        '**********',
        '*',
        '*',
        '*',
        '*',
        '**********'),
    3: ('**********',
        '         *',
        '         *',
        '         *',
        '         *',
        '**********',
        '         *',
        '         *',
        '         *',
        '         *',
        '**********'),
    4: ('*        *',
        '*        *',
        '*        *',
        '*        *',
        '*        *',
        '**********',
        '         *',
        '         *',
        '         *',
        '         *',
        '         *'),
    5: ('**********',
        '*',
        '*',
        '*',
        '*',
        '**********',
        '         *',
        '         *',
        '         *',
        '         *',
        '**********'),
    6: ('**********',
        '*',
        '*',
        '*',
        '*',
        '**********',
        '*        *',
        '*        *',
        '*        *',
        '*        *',
        '**********'),
    7: ('**********',
        '        *',
        '      *',
        '    *',
        '  *',
        '*',
        '*',
        '*',
        '*',
        '*',
        '*'),
    8: ('**********',
        '*        *',
        '*        *',
        '*        *',
        '*        *',
        '**********',
        '*        *',
        '*        *',
        '*        *',
        '*        *',
        '**********'),
    9: ('**********',
        '*        *',
        '*        *',
        '*        *',
        '*        *',
        '**********',
        '         *',
        '         *',
        '         *',
        '         *',
        '**********')
}
 
def number(x,y,num):
    '''x,y: координаты вывода цифра на экран; num: цифра 0-9'''
    if num in numbers:
        for i in range(11):
            curses.mvaddstr(y+i,x,numbers[num][i])
    else:
        curses.mvaddstr(y,x,'Неверный формат аргумента "num"')
 
def colon(x,y):
    '''x,y: координаты вывода двоеточие на экран'''    
    curses.mvaddstr(x,y,'*')
    curses.mvaddstr(x+4,y,'*')
 
def main():
    locale.setlocale(locale.LC_ALL,('russian'))
    stdscr=curses.initscr()
    while True:
        curses.clear()
        h=time.strftime('%H')
        m=time.strftime('%M')
        s=time.strftime('%S')
        sec0=int(s[1])
        sec1=int(s[0])
        min0=int(m[1])
        min1=int(m[0])
        hour0=int(h[1])
        hour1=int(h[0])
 
        number(68,0,sec0)
        number(56,0,sec1)
        colon(3,53)
        number(40,0,min0)
        number(28,0,min1)
        colon(3,25)
        number(12,0,hour0)
        number(0,0,hour1)
 
        curses.mvaddstr(12,0,'Для выхода нажмите клавишу "q"')
        curses.refresh()
        if keyboard.is_pressed('q'):
            break
    curses.endwin()
    return 0
 
if __name__ == '__main__':
    sys.exit(main())
