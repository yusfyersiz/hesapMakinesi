import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("labaelcebes")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_266=tk.Button(root)
        GButton_266["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_266["font"] = ft
        GButton_266["fg"] = "#000000"
        GButton_266["justify"] = "center"
        GButton_266["text"] = "+"
        GButton_266.place(x=330,y=240,width=30,height=25)
        GButton_266["command"] = self.GButton_266_command

        GButton_805=tk.Button(root)
        GButton_805["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_805["font"] = ft
        GButton_805["fg"] = "#000000"
        GButton_805["justify"] = "center"
        GButton_805["text"] = "-"
        GButton_805.place(x=110,y=240,width=30,height=25)
        GButton_805["command"] = self.GButton_805_command

        GButton_245=tk.Button(root)
        GButton_245["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_245["font"] = ft
        GButton_245["fg"] = "#000000"
        GButton_245["justify"] = "center"
        GButton_245["text"] = "x"
        GButton_245.place(x=180,y=240,width=30,height=25)
        GButton_245["command"] = self.GButton_245_command

        GButton_616=tk.Button(root)
        GButton_616["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_616["font"] = ft
        GButton_616["fg"] = "#000000"
        GButton_616["justify"] = "center"
        GButton_616["text"] = "/"
        GButton_616.place(x=250,y=240,width=30,height=25)
        GButton_616["command"] = self.GButton_616_command

        GLineEdit_336=tk.Entry(root)
        GLineEdit_336["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_336["font"] = ft
        GLineEdit_336["fg"] = "#333333"
        GLineEdit_336["justify"] = "center"
        GLineEdit_336["text"] = "Entry"
        GLineEdit_336.place(x=150,y=130,width=70,height=25)

        GLineEdit_348=tk.Entry(root)
        GLineEdit_348["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_348["font"] = ft
        GLineEdit_348["fg"] = "#333333"
        GLineEdit_348["justify"] = "center"
        GLineEdit_348["text"] = "Entry"
        GLineEdit_348.place(x=240,y=130,width=70,height=25)

        GLineEdit_446=tk.Entry(root)
        GLineEdit_446["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_446["font"] = ft
        GLineEdit_446["fg"] = "#333333"
        GLineEdit_446["justify"] = "center"
        GLineEdit_446["text"] = "Entry"
        GLineEdit_446.place(x=340,y=130,width=70,height=25)

        GLabel_972=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_972["font"] = ft
        GLabel_972["fg"] = "#333333"
        GLabel_972["justify"] = "center"
        GLabel_972["text"] = "rakam1"
        GLabel_972.place(x=130,y=90,width=70,height=25)

        GLabel_948=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_948["font"] = ft
        GLabel_948["fg"] = "#333333"
        GLabel_948["justify"] = "center"
        GLabel_948["text"] = "rakam2"
        GLabel_948.place(x=240,y=90,width=70,height=25)

        GLabel_948=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_948["font"] = ft
        GLabel_948["fg"] = "#333333"
        GLabel_948["justify"] = "center"
        GLabel_948["text"] = "rakam2"
        GLabel_948.place(x=240,y=90,width=70,height=25)

        GLabel_163=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_163["font"] = ft
        GLabel_163["fg"] = "#333333"
        GLabel_163["justify"] = "center"
        GLabel_163["text"] = "rakam3"
        GLabel_163.place(x=340,y=100,width=70,height=25)

    def GButton_266_command(self):
        print("buton 4 e basildi")


    def GButton_805_command(self):
        print("buton 1 e basildi")


    def GButton_245_command(self):
        print("buton 2 ye basildi")


    def GButton_616_command(self):
        print("buton 3 e basildi")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    textboxyazilanlar1 = tk.StringVar()
    textboxyazilanlar2 = tk.StringVar()
    textboxyazilanlar3 = tk.StringVar()
   


    root.mainloop()
