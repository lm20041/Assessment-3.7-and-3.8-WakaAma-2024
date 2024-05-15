from tkinter import *
import re
import os

class Program:
    def __init__(self, master):
        self.master = master
        self.master.title("Validation Example")
        self.master.configure(bg="#FFFFFF", borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")

        self.setup_gui()

    def setup_gui(self):
        background = "white"
        bold_font_12 = ("Arial", 12, "bold")
        text_font_6 = ("Arial", 10)
        txt_fg = "black"

        # Create the parent frame
        self.parent_frame = Frame(self.master, bg="lightgrey", borderwidth=2, relief="ridge")
        self.parent_frame.grid(padx=60, pady=10)

        # Entry labels and boxes
        entry_labels = ["Folder", "File", "Points"]
        self.entry_boxes = []

        for i, label in enumerate(entry_labels):
            Label(self.parent_frame, text=label, font=text_font_6, bg=background).grid(row=i, column=0, sticky=E)
            entry_box = Entry(self.parent_frame, font=text_font_6)
            entry_box.grid(row=i, column=1, pady=5)
            self.entry_boxes.append(entry_box)

        # Validate button
        self.validate_button = Button(self.parent_frame, text="Validate", font=bold_font_12, fg=txt_fg, bg="#CCCCCC", command=self.validate_text)
        self.validate_button.grid(row=3, columnspan=2, pady=5)

        # Result label
        self.result_label = Label(self.parent_frame, text="", font=text_font_6, fg=txt_fg, bg=background)
        self.result_label.grid(row=4, columnspan=2, pady=5)

    def validate_text(self):
        self.result_label.config(text="", fg="black")

        folder = self.entry_boxes[0].get()
        search_term = self.entry_boxes[1].get()
        points = self.entry_boxes[2].get()

        if not folder or not search_term or not points:
            self.result_label.config(text="All fields are required", fg="red")
            return

        if re.search(r'\d', search_term) or re.search(r'\W', search_term):
            self.result_label.config(text="File search term contains invalid characters", fg="red")
            return

        self.process_files(folder, search_term, points)

    def process_files(self, folder, search_term, points):
        try:
            lif_files = [f for f in os.listdir(folder) if f.endswith(".lif") and search_term in f]
            if lif_files:
                self.result_label.config(text="Found files:\n" + "\n".join(lif_files), fg="green")
            else:
                self.result_label.config(text="No matching files found", fg="red")
        except FileNotFoundError:
            self.result_label.config(text="Folder not found", fg="red")
        except Exception as e:
            self.result_label.config(text=f"An error occurred: {e}", fg="red")

if __name__ == "__main__":
    root = Tk()
    app = Program(root)
    root.mainloop()