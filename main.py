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
    self.heading_label = Label(self.parent_frame, text="Welcome to Waka Ama", font=button_font_12, fg=txt_fg, bg=background)
    self.heading_label.grid(row=0, pady=5)
    # ***** row1(imag) *****
    image_path = "ColorCard-image/color_card-back_card.png"
    image_pit = PhotoImage(file=image_path)
    self.image_label = Label(self.parent_frame, image=image_pit)
    self.image_label.image = image_pit
    self.image_label.grid(row=1, padx=10, pady=10)
    self.create_widgets(num_cards, username)
    # ***** row2(text) *****
    pro_text = "This program is created for the wakana culbs to read and write files recorded throughout their races."
    self.text_label = Label(self.parent_frame, text=pro_text, font=button_font_12, fg=txt_fg, bg=background)
    self.text_label.grid(row=2, pady=5)
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