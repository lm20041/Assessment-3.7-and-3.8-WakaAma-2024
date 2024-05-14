from tkinter import *
import re

class Program:
    def __init__(self, master):
        # Var's
        background = "white"
        bold_font_12 = ("Arial", 12, "bold")
        text_font_6 = ("Arial", 10)
        txt_fg = "black"
        self.master = master  # self.Var

        # Create the parent frame
        self.parent_frame = Frame(self.master, bg="lightgrey", borderwidth=2, relief="ridge")
        self.parent_frame.grid(padx=60, pady=10)

        # Add an entry box
        self.entry_box = Entry(self.parent_frame, font=text_font_6)
        self.entry_box.grid(row=0, column=0, pady=5, columnspan=2)

        # Add a button to validate the text
        self.validate_button = Button(self.parent_frame, text="Validate", font=bold_font_12, fg=txt_fg, bg="#CCCCCC", command=self.validate_text)
        self.validate_button.grid(row=1, column=0, pady=5)

        # Add a label to display validation result
        self.result_label = Label(self.parent_frame, text="", font=text_font_6, fg=txt_fg, bg=background)
        self.result_label.grid(row=2, column=0, pady=5, columnspan=2)

    def validate_text(self):
        # Retrieve the text from the entry box
        entered_text = self.entry_box.get()

        # Check for numbers, symbols, and spaces
        if re.search(r'\d', entered_text) or re.search(r'\W', entered_text):
            self.result_label.config(text="Input contains invalid characters", fg="red")
        elif entered_text.lower() == "mouse":  # Check if the entered text is "mouse"
            self.result_label.config(text="Valid input", fg="green")
        else:
            self.result_label.config(text="Invalid input", fg="red")

if __name__ == "__main__":
    root = Tk()
    root.configure(bg="#FFFFFF", borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
    root.title("Validation Example")
    app = Program(root)
    root.mainloop()