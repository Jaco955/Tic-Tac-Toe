from tkinter import*
from tkinter import messagebox



def ButtonClick(button, texto):
    
    global x_o, flag, active, turno
    button["bg"] = "#2ec4b6"
    

    print(turno)
    if button["text"] == "" and x_o ==True:
        button["text"] = "X"
        x_o = False
        if(checkforwin()):
            reset()
        flag = flag+1
        texto["text"] = "Turn O"
    elif button["text"] == "" and x_o ==False:
        button["text"] = "O"
        x_o = True
        if(checkforwin()):
            reset()
        flag = flag+1
        texto["text"] = "Turn X"
    else:
        messagebox.showinfo("Tic Tac Toe", "Player inside alr gng")
            

def EasterEgg(btn):
    
    if messagebox.askquestion("A question", "are you human?") == "yes": 
        messagebox.showinfo ("yipee", "you a sigma sir")

        if messagebox.askquestion("Another question", "do you think papayas are great?") =="yes":
            if messagebox.askquestion("tell me", "do you prefer fried papayas(yes) or normal papayas(no)") == "yes":
                messagebox.showinfo("okok", "not that healthy but okiee")
            else:
                messagebox.showinfo("yippiee", "you healthy af my dude, go buy colombian papayas")

        else: 
            messagebox.showinfo ("WHYYY", "now go eat papaya as a punishment :(")
        
    else:
        messagebox.showinfo ("alr", "so a bot huh")
    

  
        


"""
1 2 3
4 5 6
7 8 9
1 5 9
3 5 7
1 4 7
2 5 8
3 6 9
"""


def checkforwin():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9, active
    if button1["text"] == "X" and button2["text"] =="X" and button3["text"] =="X" or button4["text"] =="X" and button5["text"] =="X" and button6["text"] =="X" or button7["text"] =="X" and button8["text"] =="X" and button9["text"] =="X" or button1["text"] =="X" and button5["text"] =="X" and button9["text"] =="X" or button3 ["text"] =="X"  and button5["text"] =="X" and button7["text"] =="X" or button1["text"] =="X" and button4["text"] =="X" and button7["text"] =="X" or button2["text"] =="X" and button5["text"] =="X" and button8["text"] =="X" or button3["text"] =="X" and button6["text"] =="X" and button9["text"] =="X":
        active = False
        return messagebox.askyesno ("Tic Tac Toe", "Player X wins, Player O learn how to play. Play again?")
    elif button1["text"] == "O" and button2["text"] =="O" and button3["text"] =="O" or button4["text"] =="O" and button5["text"] =="O" and button6["text"] =="O" or button7["text"] =="O" and button8["text"] =="O" and button9["text"] =="O" or button1["text"] =="O" and button5["text"] =="O" and button9["text"] =="O" or button3 ["text"] =="O"  and button5["text"] =="O" and button7["text"] =="O" or button1["text"] =="O" and button4["text"] =="O" and button7["text"] =="O" or button2["text"] =="O" and button5["text"] =="O" and button8["text"] =="O" or button3["text"] =="O" and button6["text"] =="O" and button9["text"] =="O":
        
        active = False

        return messagebox.askyesno ("Tic Tac Toe", "Player O wins, Womp Womp Player X. Play again?")
    elif flag == 8:
        active = False
        return messagebox.askyesno ("Game tied", "Try again dudes. Play again?")
        

main = Tk()
main.title("Tic tac toe")

def reset():
    global x_o, flag, active, turno
    global button1, button2, button3, button4, button5, button6, button7, button8, button9

    x_o = True
    flag = 0
    active = True

    botones = [button1, button2, button3,button4, button5, button6,button7, button8, button9]

    for boton in botones:
        boton["text"] = ""
        boton["bg"] = "#e0ffa7"
    
active = True    
x_o = True
flag = 0
turno  = "Player X"
import tkinter as tk

texto = tk.Label(main, text="Tic Tac Toe",font=("arial", 30), bg="#a7f9ff", width=10)
texto.grid(row=0, column=0, columnspan=3)

textoturno = tk.Label(main, text="Player X Starts",font=("arial", 25), bg="#e0ffa7", width=10)
textoturno.grid(row=1, column=0, columnspan=3)

button1 = Button(main,text="", font=("arial", 60,"bold"), bg="#e0ffa7", fg="white", width=3, command=lambda: ButtonClick(button1, textoturno))
button1.grid(row=2, column=0)

button2 = Button(main,text="", font=("arial", 60,"bold"), bg="#e0ffa7", fg="white", width=3, command=lambda: ButtonClick(button2, textoturno))
button2.grid(row=2, column=1)

button3 = Button(main,text="", font=("arial", 60,"bold"), bg="#e0ffa7", fg="white", width=3, command=lambda: ButtonClick(button3, textoturno))
button3.grid(row=2, column=2)

button4 = Button(main,text="", font=("arial", 60,"bold"), bg="#e0ffa7", fg="white", width=3, command=lambda: ButtonClick(button4, textoturno))
button4.grid(row=3, column=0)

button5 = Button(main,text="", font=("arial", 60,"bold"), bg="#e0ffa7", fg="white", width=3, command=lambda: ButtonClick(button5, textoturno))
button5.grid(row=3, column=1)

button6 = Button(main,text="", font=("arial", 60,"bold"), bg="#e0ffa7", fg="white", width=3, command=lambda: ButtonClick(button6, textoturno))
button6.grid(row=3, column=2)

button7 = Button(main,text="", font=("arial", 60,"bold"), bg="#e0ffa7", fg="white", width=3, command=lambda: ButtonClick(button7, textoturno))
button7.grid(row=4, column=0)

button8 = Button(main,text="", font=("arial", 60,"bold"), bg="#e0ffa7", fg="white", width=3, command=lambda: ButtonClick(button8, textoturno))
button8.grid(row=4, column=1)

button9 = Button(main,text="", font=("arial", 60,"bold"), bg="#e0ffa7", fg="white", width=3, command=lambda: ButtonClick(button9, textoturno))
button9.grid(row=4, column=2)

buttonrestart = Button(main,text="Restart", font=("arial", 24,"bold"), bg="#e0ffa7", fg="black", width=8, command=lambda: reset())
buttonrestart.grid(row=5, column=0)

buttoneasteregg = Button(main, text="Easter egg", font=("arial", 24, "bold"), bg="#e0ffa7", fg="black", width=8, command=lambda: EasterEgg(buttoneasteregg))
buttoneasteregg.grid(row=5, column=2)

main.mainloop()