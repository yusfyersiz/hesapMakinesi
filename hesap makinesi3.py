import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        # Pencere başlığı ve boyutu ayarı
        root.title("Hesap Makinesi")
        width = 300
        height = 400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Yazı tipi
        btn_font = tkFont.Font(family='Arial', size=14, weight="bold")

        # Ekran (Sonuç gösterimi için giriş alanı)
        self.display = tk.Entry(root, font=("Arial", 18), justify="right", bd=10, insertwidth=2)
        self.display.place(x=10, y=10, width=280, height=50)

        # Sayılar ve işlemler için düğmeler
        buttons = [
            ('7', 10, 70), ('8', 80, 70), ('9', 150, 70), ('/', 220, 70),
            ('4', 10, 130), ('5', 80, 130), ('6', 150, 130), ('x', 220, 130),
            ('1', 10, 190), ('2', 80, 190), ('3', 150, 190), ('-', 220, 190),
            ('C', 10, 250), ('0', 80, 250), ('=', 150, 250), ('+', 220, 250)
        ]

        for (text, x, y) in buttons:
            if text == '=':
                btn = tk.Button(root, text=text, font=btn_font, bg="#5cb85c", command=self.calculate)
            elif text == 'C':
                btn = tk.Button(root, text=text, font=btn_font, bg="#d9534f", command=self.clear_display)
            else:
                btn = tk.Button(root, text=text, font=btn_font, bg="#f7f7f7", command=lambda t=text: self.on_button_click(t))
            btn.place(x=x, y=y, width=60, height=50)

    def on_button_click(self, char):
        current_text = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current_text + char)

    def clear_display(self):
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            expression = self.display.get().replace('x', '*').replace('/', '/')
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Hata")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
