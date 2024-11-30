import tkinter as tk

class SimpleCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        self.expression = ""
        
        self.equation = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Entry field for displaying the expression
        entry = tk.Entry(self.master, textvariable=self.equation, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 18),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        if button == 'C':
            self.expression = ""
        elif button == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += button
        
        self.equation.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()