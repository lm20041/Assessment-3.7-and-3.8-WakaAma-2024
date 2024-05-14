from tkinter import *
import re
import os

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

        # *** child-row1(Entry) ***
        # Add an entry boxs
        self.entry_boxes = []
        entry_name = ["fouder", "file", "points"]
        for i in range(3):
            self.entry_label = Label(self.parent_frame, text=entry_name[i], font=text_font_6, bg=background).grid(row=i, column=0, sticky=E)
            entry_box = Entry(self.parent_frame, font=text_font_6)
            entry_box.grid(row=i, column=1, pady=5)
            self.entry_boxes.append(entry_box)

        # Add a button to validate the text
        self.validate_button = Button(self.parent_frame, text="Validate", font=bold_font_12, fg=txt_fg, bg="#CCCCCC", command=self.validate_text)
        self.validate_button.grid(row=3, columnspan=2, pady=5)

        # Add a label to display validation result
        self.result_label = Label(self.parent_frame, text="", font=text_font_6, fg=txt_fg, bg=background)
        self.result_label.grid(row=4,columnspan=2, pady=5)

    def validate_text(self):
        # Clear the previous result
        self.result_label.config(text="", fg="black")
        #Var's
        all_valid = True
        folder  = ""
        search_term = ""
        points = ""

        for i, entry_box in enumerate(self.entry_boxes):
            entered_text = entry_box.get()
            # Check for numbers, symbols, and spaces
            if re.search(r'\d', entered_text) or re.search(r'\W', entered_text):
                self.result_label.config(text="Input contains invalid characters", fg="red")
                all_valid = False
                break
            else:
                if i == 0:
                    folder = entered_text
                elif i == 1:
                    search_term = entered_text
                elif i == 2:
                    points = entered_text

        if all_valid:
            self.result_label.config(text="All inputs are valid", fg="green")
            self.process_files(folder, search_term, points)
    def process_files(self, folder, search_term, points):
        # List all .lif files in the directory that match the file name
        lif_files = [f for f in os.listdir(folder) if f.endswith(".lif") and search_term in f]
    
        # Print the names of the matching .lif files
        for lif_file in lif_files:
            print(lif_file)

if __name__ == "__main__":
    root = Tk()
    root.configure(bg="#FFFFFF", borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
    root.title("Validation Example")
    app = Program(root)
    root.mainloop()