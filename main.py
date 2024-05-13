from tkinter import *

class program:
  def __init__(self, master):
    #Var's
    background = "white"
    button_font_12 = ("Arial", 12, "bold")
    txt_fg = "black"
    self.master = master #self.Var
    # ***** Create frame *****
    # Create the parent frame
    self.parent_frame = Frame(self.master, bg="lightgrey", borderwidth=2, relief="ridge")
    self.parent_frame.grid(padx=20, pady=20)
    # ***** row0(text) *****
    self.heading_label = Label(self.parent_frame, text="Window-Test1", font=button_font_12, fg=txt_fg, bg=background)
    self.heading_label.grid(row=0, pady=5)
    # ***** row1(imag) *****

    # ***** row2(text) *****
    self.heading_label = Label(self.parent_frame, text="Window-Test1", font=button_font_12, fg=txt_fg, bg=background)
    self.heading_label.grid(row=0, pady=5)
    # ***** row3(button) *****
    self.button = Button(self.parent_frame, text="Start Program", font=button_font_12, fg=txt_fg, command=self.to_converter)
    self.button.grid(row=3, pady=5)
  def to_converter(self):
    print("test")

if __name__ == "__main__":
  root = Tk()
  #root.geometry("300x200")
  root.configure(bg="#FFFFFF", borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
  root.title("window")
  app = program(root)
  root.mainloop()