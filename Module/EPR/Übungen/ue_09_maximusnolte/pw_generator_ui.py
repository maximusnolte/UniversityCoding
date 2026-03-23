__author__ = "MatrNr, Nachname"

"""
Tkinter GUI for password generation.
"""

import tkinter as tk
from tkinter import messagebox

from pw_generator import generate_password


class PasswordGUI:
    """GUI for the password generator."""

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Password Generator")

        self.length_var = tk.IntVar(value=12)
        self.lower_var = tk.BooleanVar(value=True)
        self.upper_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=False)

        self._build_gui()

    def _build_gui(self) -> None:
        tk.Label(self.root, text="Password length:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.length_var).grid(row=0, column=1)

        tk.Checkbutton(self.root, text="Lowercase",
                       variable=self.lower_var).grid(row=1, column=0, sticky="w")
        tk.Checkbutton(self.root, text="Uppercase",
                       variable=self.upper_var).grid(row=2, column=0, sticky="w")
        tk.Checkbutton(self.root, text="Digits",
                       variable=self.digits_var).grid(row=3, column=0, sticky="w")
        tk.Checkbutton(self.root, text="Symbols",
                       variable=self.symbols_var).grid(row=4, column=0, sticky="w")

        tk.Button(self.root, text="Generate",
                  command=self._generate).grid(row=5, column=0, columnspan=2)

        self.result_entry = tk.Entry(self.root, width=40)
        self.result_entry.grid(row=6, column=0, columnspan=2)

    def _generate(self) -> None:
        try:
            password = generate_password(
                self.length_var.get(),
                self.lower_var.get(),
                self.upper_var.get(),
                self.digits_var.get(),
                self.symbols_var.get()
            )
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, password)
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    PasswordGUI().run()
