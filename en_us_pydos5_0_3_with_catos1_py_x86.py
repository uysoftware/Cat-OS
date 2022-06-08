from random import*
from time import*
from datetime import*
import os,tkinter
def catos():
    print('Starting boot from pY DOS')
    def allCode():
        def txt1():
            window1 = tkinter.Tk()
            window1.title("CatOS")
            window1.geometry("500x500") 
            dyklb1212=tkinter.Label(window1,text="Welcome to use.")
            dyklb1212.pack()
        window = tkinter.Tk()
        window.title("CatOS1")
        window.geometry("2000x1000")
        def WordTXT():
            window = tkinter.Tk()
            window.title("Word Sky(Unsupported)")
            window.geometry("500x500")
        def shut():
                dyjk2=tkinter.Tk()
                dyjk2.geometry('500x500')
                dyklb12=tkinter.Label(dyjk2,text="Shuting Down…………")
                dyklb12.pack()
        def M106():
            #TK===========================================================
            window=tkinter.Tk()
            window.geometry('500x500')
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
        
            lb1=tkinter.Label(window,text='系统助手')
            lb2=tkinter.Label(window,text='版本：0.1.0纯净版')
            lb3=tkinter.Label(window,text='（翻版必究）')
            def com1():
                times()
                dyj2k=tkinter.Tk()
                dyj2k.geometry('100x100')
                dyklb1=tkinter.Label(dyj2k,text=current_time)
                dyklb1.pack()
            btn1=tkinter.Button(window,text='时钟',command=com1)
            btn2=tkinter.Button(window,text='关机',command=shut)
            lb1.pack()
            lb2.pack()
            lb3.pack()
            btn1.place(x='125',y='150')
            btn2.place(x='375',y='150')
            window.mainloop()
        def firstApp():
            dy1=tkinter.Tk()
            dy1.geometry('500x500')
            dy11=tkinter.Label(dy1,text='CatOS')
            dy11.pack()
            def C():
                dy2=tkinter.Tk()
                dy2.geometry('500x500')
                dy12=tkinter.Label(dy2,text="Local:(5.0MB)")
                dy12.pack()
                btn1l=tkinter.Button(dy2,text='place.txt',command=txt1)
                btn1l.pack()
                def desktop():
                    desktop=tkinter.Tk()
                    desktop.geometry('500x500')
                    desktop.title("C:/desktop")
                    desktop1=tkinter.Label(desktop,text="桌面")
                    desktop1.pack()
                    desktop2=tkinter.Button(desktop,text="系统助手",command=M106)
                    desktop2.pack()
                    desktop3=tkinter.Button(desktop,text="Word Sky",command=WordTXT)
                    desktop3.pack()
                desk2=tkinter.Button(dy2,text="桌面",command=desktop)
                desk2.pack()
            dy123=tkinter.Button(dy1,text="Local:(5.0MB)",command=C)
            dy123.pack()
            def D():
                dy3=tkinter.Tk()
                dy3.geometry('500x500')
                dy123=tkinter.Label(dy3,text="D:(14.7MB)")
                dy123.pack()
            dy123=tkinter.Button(dy1,text="D:(14.7MB)",command=D)
            dy123.pack()
        def btn01():
            dyjk=tkinter.Tk()
            dyjk.geometry('500x500')
            dyjk.title("start")
            dyklb1=tkinter.Label(dyjk,text="Start")
            dyklb1.pack()
            dyklb2=tkinter.Button(dyjk,text="shut down",command=shut)
            dyklb2.pack()
            def All():
                dyjk3=tkinter.Tk()
                dyjk3.geometry('500x500')
                dyklb123=tkinter.Label(dyjk3,text="All Apps")
                dyklb123.pack()
                dyklb32=tkinter.Button(dyjk3,text="         此电脑       ",command=firstApp)
                dyklb32.pack()
                dr2=tkinter.Button(dyjk3,text="CatOS系统助手",command=M106)
                dr2.pack()
                br3=tkinter.Button(dyjk3,text="    Word Sky    ",command=WordTXT)
                br3.pack()
            dyklb3=tkinter.Button(dyjk,text="All Apps",command=All)
            dyklb3.pack()
        bt1=tkinter.Button(window,text="       此电脑     ",command=firstApp)
        bt1.pack()
        bt2=tkinter.Button(window,text=" CatOS系统助手 ",command=M106)
        bt2.pack()
        bt3=tkinter.Button(window,text="    Word Sky    ",command=WordTXT)
        bt3.pack()
        btn1=tkinter.Button(window,text='                start              ',command=btn01)
        btn1.pack()  
        lb1=tkinter.Label(window,text="CatOS\n Copyright©保留所有权利")
        
        lb1.pack()
        btn1.place(x=100,y=750)
        bt1.place(x=100,y=100)
        bt2.place(x=100,y=150)
        bt3.place(x=100,y=200)
        window.mainloop()
    root = tkinter.Tk()
    root.title("CatOS")
    root.geometry("2000x1000")
    e=tkinter.Label(root,text="欢迎使用CatOS V.1.0系统")
    e.pack()
    esktop2=tkinter.Button(root,text="登录Administrator",command=allCode)
   
    esktop2.pack()
    root.mainloop()

def dos():
    while True:
        print("------------------------------------------------")
        print("Pythonix pY-DOS 5 Options Menu:>")
        space1 = "------------------------------------------------"
        print(space1)
        print("Command Prompt:>")
        space2 = "                                                "
        print(space2)
        print("1.About")
        print(space1)
        print("Apps & Docs:>")
        print(space2)
        print("2.Calculator.py")
        print("3.GuessingNumbers.py")
        print("4.Exit")
        print(space1)
        op = int(input("Local:>"))
        if op == 4:
            break
        elif op == 1:
            print("Pythonix pY-DOS 5.0.3 Standard")
            pass
        elif op == 2:
            print("----------Calculator.py----------")
            print("Choose a way:")
            print("1=+ 2=- 3=* 4=/")
            ways = int(input("Way:"))
            num1 = int(input("The first number is:"))
            num2 = int(input("The second number is:"))
            if ways == 1:
                print(num1 + num2)
            elif ways == 2:
                print(num1 - num2)
            elif ways == 3:
                print(num1 * num2)
            else:
                print(num1 / num2)
        elif op == 3:
            print("-----GuessingNumbers.py-----")
            print("The number is from 1 to 100.")
            answer = randint(1,100)
            while 1:
                i = int(input("Guess:"))
                if i > answer:
                    print("It is big.")
                elif i < answer:
                    print("It is small.")
                else:
                    print("Great!")
                    sleep(0.5)
                    break
        else:
            print("Wrong letters.Type again.")
print("Cat-OS & pY DOS 5 Boot Manager :")
print('1.Start pY DOS Normally.')
print('2.Start Cat OS Normally.')
i=int(input('Boot:>'))
if i == 1:
    dos()
elif i == 2:
    catos()

