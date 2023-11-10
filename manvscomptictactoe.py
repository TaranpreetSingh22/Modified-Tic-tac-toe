from tkinter import *
from tkinter import messagebox
from random import *

def main():
    win=Tk()

    w=400
    h=500

    ww=win.winfo_screenwidth()
    wh=win.winfo_screenheight()

    x=(ww/2)-(w/2)
    y=(wh/2)-(h/2)

    win.geometry('%dx%d+%d+%d'%(w,h,x,y))
    win.resizable(0,0)

    global first,col,textcol,randnolist,num,finallist
    first='X'
    col='red'
    textcol='black'
    randnolist=[]
    finallist=[]

    def write1():
        global first,col
        t1.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t1.cget('text')=='X':
            first='O'
            col='blue'  
        else:
            first='X'
            col='red'
    
        if (t1.cget('text')=='X' and t2.cget('text')=='X' and t3.cget('text')=='X') or (t1.cget('text')=='X' and t4.cget('text')=='X' and t7.cget('text')=='X') or (t1.cget('text')=='X' and t5.cget('text')=='X' and t9.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t1.cget('text')=='O' and t2.cget('text')=='O' and t3.cget('text')=='O') or (t1.cget('text')=='O' and t4.cget('text')=='O' and t7.cget('text')=='O') or (t1.cget('text')=='O' and t5.cget('text')=='O' and t9.cget('text')=='O') :
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t1.cget('text')=='X' and t2.cget('text')=='O' and t3.cget('text')=='O') or (t1.cget('text')=='X' and t2.cget('text')=='X' and t3.cget('text')=='O') or (t1.cget('text')=='O' and t2.cget('text')=='X' and t3.cget('text')=='O') or (t1.cget('text')=='O' and t2.cget('text')=='O' and t3.cget('text')=='X') or (t1.cget('text')=='O' and t2.cget('text')=='X' and t3.cget('text')=='X') or (t1.cget('text')=='X' and t2.cget('text')=='O' and t3.cget('text')=='X') or 
            (t1.cget('text')=='X' and t4.cget('text')=='O' and t7.cget('text')=='O') or (t1.cget('text')=='X' and t4.cget('text')=='X' and t7.cget('text')=='O') or (t1.cget('text')=='O' and t4.cget('text')=='X' and t7.cget('text')=='O') or (t1.cget('text')=='O' and t4.cget('text')=='O' and t7.cget('text')=='X') or (t1.cget('text')=='O' and t4.cget('text')=='X' and t7.cget('text')=='X') or (t1.cget('text')=='X' and t4.cget('text')=='O' and t7.cget('text')=='X') or 
            (t1.cget('text')=='X' and t5.cget('text')=='O' and t9.cget('text')=='O') or (t1.cget('text')=='X' and t5.cget('text')=='X' and t9.cget('text')=='O') or (t1.cget('text')=='O' and t5.cget('text')=='X' and t9.cget('text')=='O') or (t1.cget('text')=='O' and t5.cget('text')=='O' and t9.cget('text')=='X') or (t1.cget('text')=='O' and t5.cget('text')=='X' and t9.cget('text')=='X') or (t1.cget('text')=='X' and t5.cget('text')=='O' and t9.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()

        choices=[2,3,4,5,7,9]
        #num=choice(choices)
        #randnolist.append(num)
                  
        if first=='O':
            #for i in choices:
             #   if i in randnolist:
              #      choices.remove(i)
            for j in range(len(choices)):
                randno=choice(choices)
                if randno==2 and t2.cget('text')!='X' and t2.cget('text')!='O':
                    write2()
                    break
                elif randno==3 and t3.cget('text')!='X' and t3.cget('text')!='O':
                    write3()
                    break
                elif randno==4 and t4.cget('text')!='X' and t4.cget('text')!='O':
                    write4()
                    break
                elif randno==5 and t5.cget('text')!='X' and t5.cget('text')!='O':
                    write5()
                    break
                elif randno==6 and t6.cget('text')!='X' and t6.cget('text')!='O':
                    write6()
                    break
                elif randno==7 and t7.cget('text')!='X' and t7.cget('text')!='O':
                    write7()
                    break
                elif randno==8 and t8.cget('text')!='X' and t8.cget('text')!='O':
                    write8()
                    break
                elif randno==9 and t9.cget('text')!='X' and t9.cget('text')!='O':
                    write9()
                    break
                else:
                    continue


    def write2():
        global first,col
        t2.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t2.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t1.cget('text')=='X' and t2.cget('text')=='X' and t3.cget('text')=='X') or (t2.cget('text')=='X' and t5.cget('text')=='X' and t8.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t1.cget('text')=='O' and t2.cget('text')=='O' and t3.cget('text')=='O') or (t2.cget('text')=='O' and t5.cget('text')=='O' and t8.cget('text')=='O'):
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t1.cget('text')=='X' and t2.cget('text')=='O' and t3.cget('text')=='O') or (t1.cget('text')=='X' and t2.cget('text')=='X' and t3.cget('text')=='O') or (t1.cget('text')=='O' and t2.cget('text')=='X' and t3.cget('text')=='O') or (t1.cget('text')=='O' and t2.cget('text')=='O' and t3.cget('text')=='X') or (t1.cget('text')=='O' and t2.cget('text')=='X' and t3.cget('text')=='X') or (t1.cget('text')=='X' and t2.cget('text')=='O' and t3.cget('text')=='X') or 
            (t2.cget('text')=='X' and t5.cget('text')=='O' and t8.cget('text')=='O') or (t2.cget('text')=='X' and t5.cget('text')=='X' and t8.cget('text')=='O') or (t2.cget('text')=='O' and t5.cget('text')=='X' and t8.cget('text')=='O') or (t2.cget('text')=='O' and t5.cget('text')=='O' and t8.cget('text')=='X') or (t2.cget('text')=='O' and t5.cget('text')=='X' and t8.cget('text')=='X') or (t2.cget('text')=='X' and t5.cget('text')=='O' and t8.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):       
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()

        choices=[1,3,5,8]
       # num=choice(choices)
        #randnolist.append(num)
                
        if first=='O':
           #for i in choices:
            #    if i in randnolist:
             #       choices.remove(i)
            for j in range(len(choices)):
                randno=choice(choices)
                if randno==1 and t1.cget('text')!='X' and t1.cget('text')!='O':
                    write1()
                    break
                elif randno==3 and t3.cget('text')!='X' and t3.cget('text')!='O':
                    write3()
                    break
                elif randno==4 and t4.cget('text')!='X' and t4.cget('text')!='O':
                    write4()
                    break
                elif randno==5 and t5.cget('text')!='X' and t5.cget('text')!='O':
                    write5()
                    break
                elif randno==6 and t6.cget('text')!='X' and t6.cget('text')!='O':
                    write6()
                    break
                elif randno==7 and t7.cget('text')!='X' and t7.cget('text')!='O':
                    write7()
                    break
                elif randno==8 and t8.cget('text')!='X' and t8.cget('text')!='O':
                    write8()
                    break
                elif randno==9 and t9.cget('text')!='X' and t9.cget('text')!='O':
                    write9()
                    break
                else:
                    continue
        


    def write3():
        global first,col
        t3.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t3.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t1.cget('text')=='X' and t2.cget('text')=='X' and t3.cget('text')=='X') or (t7.cget('text')=='X' and t5.cget('text')=='X' and t3.cget('text')=='X') or (t3.cget('text')=='X' and t6.cget('text')=='X' and t9.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t1.cget('text')=='O' and t2.cget('text')=='O' and t3.cget('text')=='O') or (t7.cget('text')=='O' and t5.cget('text')=='O' and t3.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='O' and t9.cget('text')=='O') :
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t1.cget('text')=='X' and t2.cget('text')=='O' and t3.cget('text')=='O') or (t1.cget('text')=='X' and t2.cget('text')=='X' and t3.cget('text')=='O') or (t1.cget('text')=='O' and t2.cget('text')=='X' and t3.cget('text')=='O') or (t1.cget('text')=='O' and t2.cget('text')=='O' and t3.cget('text')=='X') or (t1.cget('text')=='O' and t2.cget('text')=='X' and t3.cget('text')=='X') or (t1.cget('text')=='X' and t2.cget('text')=='O' and t3.cget('text')=='X') or 
            (t3.cget('text')=='X' and t6.cget('text')=='O' and t9.cget('text')=='O') or (t3.cget('text')=='X' and t6.cget('text')=='X' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='X' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='O' and t9.cget('text')=='X') or (t3.cget('text')=='O' and t6.cget('text')=='X' and t9.cget('text')=='X') or (t3.cget('text')=='X' and t6.cget('text')=='O' and t9.cget('text')=='X') or 
            (t3.cget('text')=='X' and t5.cget('text')=='O' and t7.cget('text')=='O') or (t3.cget('text')=='X' and t5.cget('text')=='X' and t7.cget('text')=='O') or (t3.cget('text')=='O' and t5.cget('text')=='X' and t7.cget('text')=='O') or (t3.cget('text')=='O' and t5.cget('text')=='O' and t7.cget('text')=='X') or (t3.cget('text')=='O' and t5.cget('text')=='X' and t7.cget('text')=='X') or (t3.cget('text')=='X' and t5.cget('text')=='O' and t7.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()

        choices=[1,2,5,6,7,9]
       # num=choice(choices)
        #randnolist.append(num)
                
        if first=='O':
         #   for i in choices:
          #      if i in randnolist:
           #         choices.remove(i)
            for j in range(len(choices)):
                randno=choice(choices)
                if randno==1 and t1.cget('text')!='X' and t1.cget('text')!='O':
                    write1()
                    break
                elif randno==2 and t2.cget('text')!='X' and t2.cget('text')!='O':
                    write2()
                    break
                elif randno==4 and t4.cget('text')!='X' and t4.cget('text')!='O':
                    write4()
                    break
                elif randno==5 and t5.cget('text')!='X' and t5.cget('text')!='O':
                    write5()
                    break
                elif randno==6 and t6.cget('text')!='X' and t6.cget('text')!='O':
                    write6()
                    break
                elif randno==7 and t7.cget('text')!='X' and t7.cget('text')!='O':
                    write7()
                    break
                elif randno==8 and t8.cget('text')!='X' and t8.cget('text')!='O':
                    write8()
                    break
                elif randno==9 and t9.cget('text')!='X' and t9.cget('text')!='O':
                    write9()
                    break
                else:
                    continue

        
    def write4():
        global first,col
        t4.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t4.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t1.cget('text')=='X' and t4.cget('text')=='X' and t7.cget('text')=='X') or (t4.cget('text')=='X' and t5.cget('text')=='X' and t6.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t1.cget('text')=='O' and t4.cget('text')=='O' and t7.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='O' and t6.cget('text')=='O'):
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t1.cget('text')=='X' and t4.cget('text')=='O' and t7.cget('text')=='O') or (t1.cget('text')=='X' and t4.cget('text')=='X' and t7.cget('text')=='O') or (t1.cget('text')=='O' and t4.cget('text')=='X' and t7.cget('text')=='O') or (t1.cget('text')=='O' and t4.cget('text')=='O' and t7.cget('text')=='X') or (t1.cget('text')=='O' and t4.cget('text')=='X' and t7.cget('text')=='X') or (t1.cget('text')=='X' and t4.cget('text')=='O' and t7.cget('text')=='X') or 
            (t4.cget('text')=='X' and t5.cget('text')=='O' and t6.cget('text')=='O') or (t4.cget('text')=='X' and t5.cget('text')=='X' and t6.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='X' and t6.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='O' and t6.cget('text')=='X') or (t4.cget('text')=='O' and t5.cget('text')=='X' and t6.cget('text')=='X') or (t4.cget('text')=='X' and t5.cget('text')=='O' and t6.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()

        choices=[1,5,6,7]
       # num=choice(choices)
        #randnolist.append(num)
                
        if first=='O':
         #   for i in choices:
          #      if i in randnolist:
           #         choices.remove(i)
            for j in range(len(choices)):
                randno=choice(choices)
                if randno==1 and t1.cget('text')!='X' and t1.cget('text')!='O':
                    write1()
                    break
                elif randno==2 and t2.cget('text')!='X' and t2.cget('text')!='O':
                    write2()
                    break
                elif randno==3 and t3.cget('text')!='X' and t3.cget('text')!='O':
                    write3()
                    break
                elif randno==5 and t5.cget('text')!='X' and t5.cget('text')!='O':
                    write5()
                    break
                elif randno==6 and t6.cget('text')!='X' and t6.cget('text')!='O':
                    write6()
                    break
                elif randno==7 and t7.cget('text')!='X' and t7.cget('text')!='O':
                    write7()
                    break
                elif randno==8 and t8.cget('text')!='X' and t8.cget('text')!='O':
                    write8()
                    break
                elif randno==9 and t9.cget('text')!='X' and t9.cget('text')!='O':
                    write9()
                    break
                else:
                    continue

       
    def write5():
        global first,col
        t5.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t5.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t2.cget('text')=='X' and t5.cget('text')=='X' and t8.cget('text')=='X') or (t1.cget('text')=='X' and t5.cget('text')=='X' and t9.cget('text')=='X') or (t3.cget('text')=='X' and t5.cget('text')=='X' and t7.cget('text')=='X') or (t4.cget('text')=='X' and t5.cget('text')=='X' and t6.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif ((t2.cget('text')=='O' and t5.cget('text')=='O' and t8.cget('text')=='O') or (t1.cget('text')=='O' and t5.cget('text')=='O' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t5.cget('text')=='O' and t7.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='O') and t6.cget('text')=='O'):
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t4.cget('text')=='X' and t5.cget('text')=='O' and t6.cget('text')=='O') or (t4.cget('text')=='X' and t5.cget('text')=='X' and t6.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='X' and t6.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='O' and t6.cget('text')=='X') or (t4.cget('text')=='O' and t5.cget('text')=='X' and t6.cget('text')=='X') or (t4.cget('text')=='X' and t5.cget('text')=='O' and t6.cget('text')=='X') or 
            (t2.cget('text')=='X' and t5.cget('text')=='O' and t8.cget('text')=='O') or (t2.cget('text')=='X' and t5.cget('text')=='X' and t8.cget('text')=='O') or (t2.cget('text')=='O' and t5.cget('text')=='X' and t8.cget('text')=='O') or (t2.cget('text')=='O' and t5.cget('text')=='O' and t8.cget('text')=='X') or (t2.cget('text')=='O' and t5.cget('text')=='X' and t8.cget('text')=='X') or (t2.cget('text')=='X' and t5.cget('text')=='O' and t8.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()

        choices=[1,2,3,4,6,7,8,9]
       # num=choice(choices)
        #randnolist.append(num)
                
        if first=='O':
         #   for i in choices:
          #      if i in randnolist:
           #         choices.remove(i)
            for j in range(len(choices)):
                randno=choice(choices)
                if randno==1 and t1.cget('text')!='X' and t1.cget('text')!='O':
                    write1()
                    break
                elif randno==2 and t2.cget('text')!='X' and t2.cget('text')!='O':
                    write2()
                    break
                elif randno==4 and t4.cget('text')!='X' and t4.cget('text')!='O':
                    write4()
                    break
                elif randno==3 and t3.cget('text')!='X' and t3.cget('text')!='O':
                    write3()
                    break
                elif randno==6 and t6.cget('text')!='X' and t6.cget('text')!='O':
                    write6()
                    break
                elif randno==7 and t7.cget('text')!='X' and t7.cget('text')!='O':
                    write7()
                    break
                elif randno==8 and t8.cget('text')!='X' and t8.cget('text')!='O':
                    write8()
                    break
                elif randno==9 and t9.cget('text')!='X' and t9.cget('text')!='O':
                    write9()
                    break
                else:
                    continue
        


    def write6():
        global first,col
        t6.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t6.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t3.cget('text')=='X' and t6.cget('text')=='X' and t9.cget('text')=='X') or (t4.cget('text')=='X' and t5.cget('text')=='X' and t6.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t3.cget('text')=='O' and t6.cget('text')=='O' and t9.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='O' and t6.cget('text')=='O'):
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t4.cget('text')=='X' and t5.cget('text')=='O' and t6.cget('text')=='O') or (t4.cget('text')=='X' and t5.cget('text')=='X' and t6.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='X' and t6.cget('text')=='O') or (t4.cget('text')=='O' and t5.cget('text')=='O' and t6.cget('text')=='X') or (t4.cget('text')=='O' and t5.cget('text')=='X' and t6.cget('text')=='X') or (t4.cget('text')=='X' and t5.cget('text')=='O' and t6.cget('text')=='X') or 
            (t3.cget('text')=='X' and t6.cget('text')=='O' and t9.cget('text')=='O') or (t3.cget('text')=='X' and t6.cget('text')=='X' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='X' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='O' and t9.cget('text')=='X') or (t3.cget('text')=='O' and t6.cget('text')=='X' and t9.cget('text')=='X') or (t2.cget('text')=='X' and t5.cget('text')=='O' and t8.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()

        choices=[3,4,5,9]
        #num=choice(choices)
        #randnolist.append(num)
                
        if first=='O':
         #   for i in choices:
          #      if i in randnolist:
           #         choices.remove(i)
            for j in range(len(choices)):
                randno=choice(choices)
                if randno==1 and t1.cget('text')!='X' and t1.cget('text')!='O':
                    write1()
                    break
                elif randno==2 and t2.cget('text')!='X' and t2.cget('text')!='O':
                    write2()
                    break
                elif randno==4 and t4.cget('text')!='X' and t4.cget('text')!='O':
                    write4()
                    break
                elif randno==5 and t5.cget('text')!='X' and t5.cget('text')!='O':
                    write5()
                    break
                elif randno==3 and t3.cget('text')!='X' and t3.cget('text')!='O':
                    write3()
                    break
                elif randno==7 and t7.cget('text')!='X' and t7.cget('text')!='O':
                    write7()
                    break
                elif randno==8 and t8.cget('text')!='X' and t8.cget('text')!='O':
                    write8()
                    break
                elif randno==9 and t9.cget('text')!='X' and t9.cget('text')!='O':
                    write9()
                    break
                else:
                    continue
       

    def write7():
        global first,col
        t7.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t7.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t1.cget('text')=='X' and t4.cget('text')=='X' and t7.cget('text')=='X') or (t7.cget('text')=='X' and t8.cget('text')=='X' and t9.cget('text')=='X') or (t7.cget('text')=='X' and t5.cget('text')=='X' and t3.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t1.cget('text')=='O' and t4.cget('text')=='O' and t7.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='O' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t5.cget('text')=='O' and t3.cget('text')=='O'):
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t1.cget('text')=='X' and t4.cget('text')=='O' and t7.cget('text')=='O') or (t1.cget('text')=='X' and t4.cget('text')=='X' and t7.cget('text')=='O') or (t1.cget('text')=='O' and t4.cget('text')=='X' and t7.cget('text')=='O') or (t1.cget('text')=='O' and t4.cget('text')=='O' and t7.cget('text')=='X') or (t1.cget('text')=='O' and t4.cget('text')=='X' and t7.cget('text')=='X') or (t1.cget('text')=='X' and t4.cget('text')=='O' and t7.cget('text')=='X') or 
            (t7.cget('text')=='X' and t5.cget('text')=='O' and t3.cget('text')=='O') or (t7.cget('text')=='X' and t5.cget('text')=='X' and t3.cget('text')=='O') or (t7.cget('text')=='O' and t5.cget('text')=='X' and t3.cget('text')=='O') or (t7.cget('text')=='O' and t5.cget('text')=='O' and t3.cget('text')=='X') or (t7.cget('text')=='O' and t5.cget('text')=='X' and t3.cget('text')=='X') or (t7.cget('text')=='X' and t5.cget('text')=='O' and t3.cget('text')=='X') or 
            (t7.cget('text')=='X' and t8.cget('text')=='O' and t9.cget('text')=='O') or (t7.cget('text')=='X' and t8.cget('text')=='X' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='X' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='O' and t9.cget('text')=='X') or (t7.cget('text')=='O' and t8.cget('text')=='X' and t9.cget('text')=='X') or (t7.cget('text')=='X' and t8.cget('text')=='O' and t9.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()

        choices=[1,3,4,5,8,9]
       # num=choice(choices)
        #randnolist.append(num)
                
        if first=='O':
         #   for i in choices:
          #      if i in randnolist:
           #         choices.remove(i)
            for j in range(len(choices)):
                randno=choice(choices)
                if randno==1 and t1.cget('text')!='X' and t1.cget('text')!='O':
                    write1()
                    break
                elif randno==2 and t2.cget('text')!='X' and t2.cget('text')!='O':
                    write2()
                    break
                elif randno==4 and t4.cget('text')!='X' and t4.cget('text')!='O':
                    write4()
                    break
                elif randno==5 and t5.cget('text')!='X' and t5.cget('text')!='O':
                    write5()
                    break
                elif randno==6 and t6.cget('text')!='X' and t6.cget('text')!='O':
                    write6()
                    break
                elif randno==3 and t3.cget('text')!='X' and t3.cget('text')!='O':
                    write3()
                    break
                elif randno==8 and t8.cget('text')!='X' and t8.cget('text')!='O':
                    write8()
                    break
                elif randno==9 and t9.cget('text')!='X' and t9.cget('text')!='O':
                    write9()
                    break
                else:
                    continue
      

    def write8():
        global first,col
        t8.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t8.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t2.cget('text')=='X' and t5.cget('text')=='X' and t8.cget('text')=='X') or (t7.cget('text')=='X' and t8.cget('text')=='X' and t9.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t2.cget('text')=='O' and t5.cget('text')=='O' and t8.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='O' and t9.cget('text')=='O'):
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t2.cget('text')=='X' and t5.cget('text')=='O' and t8.cget('text')=='O') or (t2.cget('text')=='X' and t5.cget('text')=='X' and t8.cget('text')=='O') or (t2.cget('text')=='O' and t5.cget('text')=='X' and t8.cget('text')=='O') or (t2.cget('text')=='O' and t5.cget('text')=='O' and t8.cget('text')=='X') or (t2.cget('text')=='O' and t5.cget('text')=='X' and t8.cget('text')=='X') or (t2.cget('text')=='X' and t5.cget('text')=='O' and t8.cget('text')=='X') or 
            (t7.cget('text')=='X' and t8.cget('text')=='O' and t9.cget('text')=='O') or (t7.cget('text')=='X' and t8.cget('text')=='X' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='X' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='O' and t9.cget('text')=='X') or (t7.cget('text')=='O' and t8.cget('text')=='X' and t9.cget('text')=='X') or (t7.cget('text')=='X' and t8.cget('text')=='O' and t9.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()

        choices=[2,5,7,9]
       # num=choice(choices)
        #randnolist.append(num)
                
        if first=='O':
         #   for i in choices:
          #      if i in randnolist:
           #         choices.remove(i)
            for j in range(len(choices)):
                randno=choice(choices)
                if randno==1 and t1.cget('text')!='X' and t1.cget('text')!='O':
                    write1()
                    break
                elif randno==2 and t2.cget('text')!='X' and t2.cget('text')!='O':
                    write2()
                    break
                elif randno==4 and t4.cget('text')!='X' and t4.cget('text')!='O':
                    write4()
                    break
                elif randno==5 and t5.cget('text')!='X' and t5.cget('text')!='O':
                    write5()
                    break
                elif randno==6 and t6.cget('text')!='X' and t6.cget('text')!='O':
                    write6()
                    break
                elif randno==7 and t7.cget('text')!='X' and t7.cget('text')!='O':
                    write7()
                    break
                elif randno==3 and t3.cget('text')!='X' and t3.cget('text')!='O':
                    write3()
                    break
                elif randno==9 and t9.cget('text')!='X' and t9.cget('text')!='O':
                    write9()
                    break
                else:
                    continue

     
    def write9():
        global first,col
        t9.configure(text=first,state=DISABLED,disabledforeground=textcol,bg=col)
        if t9.cget('text')=='X':
            first='O'
            col='blue'
        else:
            first='X'
            col='red'

        if (t1.cget('text')=='X' and t5.cget('text')=='X' and t9.cget('text')=='X') or (t3.cget('text')=='X' and t6.cget('text')=='X' and t9.cget('text')=='X') or (t7.cget('text')=='X' and t8.cget('text')=='X' and t9.cget('text')=='X'):
            ans=messagebox.askyesno('Winner',"X Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (t1.cget('text')=='O' and t5.cget('text')=='O' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='O' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='O' and t9.cget('text')=='O') :
            ans=messagebox.askyesno('Winner',"O Won \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()
        elif (((t1.cget('text')=='X' and t5.cget('text')=='O' and t9.cget('text')=='O') or (t1.cget('text')=='X' and t5.cget('text')=='X' and t9.cget('text')=='O') or (t1.cget('text')=='O' and t5.cget('text')=='X' and t9.cget('text')=='O') or (t1.cget('text')=='O' and t5.cget('text')=='O' and t9.cget('text')=='X') or (t1.cget('text')=='O' and t5.cget('text')=='X' and t9.cget('text')=='X') or (t1.cget('text')=='X' and t5.cget('text')=='O' and t9.cget('text')=='X') or 
            (t3.cget('text')=='X' and t6.cget('text')=='O' and t9.cget('text')=='O') or (t3.cget('text')=='X' and t6.cget('text')=='X' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='X' and t9.cget('text')=='O') or (t3.cget('text')=='O' and t6.cget('text')=='O' and t9.cget('text')=='X') or (t3.cget('text')=='O' and t6.cget('text')=='X' and t9.cget('text')=='X') or (t3.cget('text')=='X' and t6.cget('text')=='O' and t9.cget('text')=='X') or 
            (t7.cget('text')=='X' and t8.cget('text')=='O' and t9.cget('text')=='O') or (t7.cget('text')=='X' and t8.cget('text')=='X' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='X' and t9.cget('text')=='O') or (t7.cget('text')=='O' and t8.cget('text')=='O' and t9.cget('text')=='X') or (t7.cget('text')=='O' and t8.cget('text')=='X' and t9.cget('text')=='X') or (t7.cget('text')=='X' and t8.cget('text')=='O' and t9.cget('text')=='X')) and
            ((t1.cget('text')=='X' or t1.cget('text')=='O') and (t2.cget('text')=='X' or t2.cget('text')=='O') and (t3.cget('text')=='X' or t3.cget('text')=='O') and (t4.cget('text')=='X' or t4.cget('text')=='O') and (t5.cget('text')=='X' or t5.cget('text')=='O') and (t6.cget('text')=='X' or t6.cget('text')=='O') and (t7.cget('text')=='X' or t7.cget('text')=='O') and (t8.cget('text')=='X' or t8.cget('text')=='O') and (t9.cget('text')=='X' or t9.cget('text')=='O'))):
            ans=messagebox.askyesno('Winner',"It's A Tie \n Do u Want to Play Again?")
            if ans==True:
                win.destroy()
                main()
            else:
                win.destroy()

        choices=[1,3,5,6,7,8]
       # num=choice(choices)
        #randnolist.append(num)
                
        if first=='O':
         #   for i in choices:
          #      if i in randnolist:
           #         choices.remove(i)
            for j in range(len(choices)):
                randno=choice(choices)
                if randno==1 and t1.cget('text')!='X' and t1.cget('text')!='O':
                    write1()
                    break
                elif randno==2 and t2.cget('text')!='X' and t2.cget('text')!='O':
                    write2()
                    break
                elif randno==4 and t4.cget('text')!='X' and t4.cget('text')!='O':
                    write4()
                    break
                elif randno==5 and t5.cget('text')!='X' and t5.cget('text')!='O':
                    write5()
                    break
                elif randno==6 and t6.cget('text')!='X' and t6.cget('text')!='O':
                    write6()
                    break
                elif randno==7 and t7.cget('text')!='X' and t7.cget('text')!='O':
                    write7()
                    break
                elif randno==8 and t8.cget('text')!='X' and t8.cget('text')!='O':
                    write8()
                    break
                elif randno==3 and t3.cget('text')!='X' and t3.cget('text')!='O':
                    write3()
                    break
                else:
                    continue
       

    t1=Button(win,width=15,height=10,command=write1)
    t1.grid(column=2,row=3,padx=(30,0))
    t2=Button(win,width=15,height=10,command=write2)
    t2.grid(column=3,row=3)
    t3=Button(win,width=15,height=10,command=write3)
    t3.grid(column=4,row=3)
    t4=Button(win,width=15,height=10,command=write4)
    t4.grid(column=2,row=4,padx=(30,0))
    t5=Button(win,width=15,height=10,command=write5)
    t5.grid(column=3,row=4)
    t6=Button(win,width=15,height=10,command=write6)
    t6.grid(column=4,row=4)
    t7=Button(win,width=15,height=10,command=write7)
    t7.grid(column=2,row=5,padx=(30,0))
    t8=Button(win,width=15,height=10,command=write8)
    t8.grid(column=3,row=5)
    t9=Button(win,width=15,height=10,command=write9)
    t9.grid(column=4,row=5)

    #photo=PhotoImage(file="rightline02.png")

    win.mainloop()

if __name__=="__main__":
    main()
