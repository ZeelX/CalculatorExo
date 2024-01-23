import tkinter as tk
from tkinter import ttk


def perf_ope():
    """ Performs the calculated selection in the checkbox

    :returns
    float -- The result of the calculation

    string -- Error result
    """
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        selected_operation = operation_var.get()

        match selected_operation:
            case "+":
                result.set(num1 + num2)

            case "-":
                result.set(num1 - num2)

            case "*":
                result.set(num1 * num2)

            case "**":
                result.set(num1 ** num2)

            case "/":
                result.set(num1 / num2)

            case "//":
                result.set(num1 // num2)

            case "%":
                result.set(num1 % num2)

    except ValueError:
        result.set("Input issues")
    except ZeroDivisionError:
        result.set("I can't divide by 0")


window = tk.Tk()
window.title("Calculator")

result = tk.StringVar()

# Entry One
entry1 = tk.Entry(window, width=15)
entry1.grid(row=0, column=0, padx=10, pady=10)

# Entry Two
entry2 = tk.Entry(window, width=15)
entry2.grid(row=0, column=1, padx=10, pady=10)

# List of operations
operations = ["+", "-", "*", "/", "**", "//", "%"]
operation_var = tk.StringVar()
operation_dropdown = ttk.Combobox(window, textvariable=operation_var, values=operations)
operation_dropdown.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
operation_dropdown.set("+")

# Bouton pour effectuer l'opération
calculate_button = tk.Button(window, text="calculate", command=perf_ope)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, textvariable=result)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
