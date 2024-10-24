import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Scientific Calculator")
        self.master.geometry("400x600")

        self.expression = ""
        self.input_var = tk.StringVar()
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the expression
        entry = tk.Entry(self.master, textvariable=self.input_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3),
            ('sqrt', 6, 0), ('^', 6, 1), ('(', 6, 2), (')', 6, 3),
            ('C', 7, 0), ('!', 7, 1), ('History', 7, 2)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, padx=20, pady=20, font=("Arial", 18),
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col)

    def on_button_click(self, char):
        if char == '=':
            try:
                # Evaluate the expression
                result = eval(self.expression.replace('^', '**'))  # Handle exponentiation
                self.input_var.set(result)
                self.history.append(f"{self.expression} = {result}")
                self.expression = str(result)
            except Exception:
                self.input_var.set("Error")
                self.expression = ""
        elif char == 'C':
            self.expression = ""
            self.input_var.set("")
        elif char == '!':
            try:
                num = int(self.input_var.get())
                result = math.factorial(num)
                self.input_var.set(result)
                self.history.append(f"{num}! = {result}")
                self.expression = str(result)
            except Exception:
                self.input_var.set("Error")
                self.expression = ""
        elif char == 'sqrt':
            try:
                num = float(self.input_var.get())
                result = math.sqrt(num)
                self.input_var.set(result)
                self.history.append(f"sqrt({num}) = {result}")
                self.expression = str(result)
            except Exception:
                self.input_var.set("Error")
                self.expression = ""
        elif char == 'History':
            self.show_history()
        else:
            self.expression += str(char)
            self.input_var.set(self.expression)

    def show_history(self):
        history_window = tk.Toplevel(self.master)
        history_window.title("Calculation History")
        history_window.geometry("300x400")

        history_label = tk.Label(history_window, text="History", font=("Arial", 20))
        history_label.pack(pady=10)

        history_text = tk.Text(history_window, height=15, width=35, font=("Arial", 12))
        history_text.pack(pady=10)

        for entry in self.history:
            history_text.insert(tk.END, entry + "\n")

        history_text.config(state=tk.DISABLED)

# Main function to run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
    
