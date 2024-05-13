from tkinter import *
from tkinter import PhotoImage
from functools import partial

class program:
  def __init__(self, master):
    #Var's
    background = "white"
    bold_font_12 = ("Arial", 12, "bold")
    text_font_6 = ("Arial", 10)
    txt_fg = "black"
    self.master = master #self.Var
    # ***** Create frame *****
    # Create the parent frame
    self.parent_frame = Frame(self.master, bg="lightgrey", borderwidth=2, relief="ridge")
    self.parent_frame.grid(padx=60, pady=10)
    # ***** row0(text) *****
    self.heading_label = Label(self.parent_frame, text="Welcome to Waka Ama", font=bold_font_12, fg=txt_fg)
    self.heading_label.grid(row=0, pady=5)
    # ***** row1(imag) *****
    image_path = "PhotoImage/culture_of_waka_ama-main-image.png"
    image = PhotoImage(file=image_path)
    image = image.subsample(5, 5)
    self.image_label = Label(self.parent_frame, image=image)
    self.image_label.image = image
    self.image_label.grid(row=1, padx=10, pady=10)
    # ***** row2(text) *****
    pro_text = "This program is created for the wakana culbs to read and write files recorded throughout their races."
    self.text_label = Label(self.parent_frame, text=pro_text, wrap=250, font=text_font_6, fg=txt_fg)
    self.text_label.grid(row=2, pady=5)
    # ***** row3(button) *****
    self.to_converter_button = Button(self.parent_frame, text="Start Program", font=bold_font_12, fg=txt_fg, command=self.to_converter)
    self.to_converter_button.grid(row=3, pady=5)
  def to_converter(self):
    Convertor(self)

class Convertor:
  def __init__(self, partner):
    # ***** Var's *****
    background = "white"
    bold_font_12 = ("Arial", 12, "bold")
    text_font_6 = ("Arial", 10)
    txt_fg = "black"
    # ***** Create frame *****
    #set up dialogue box
    self.Convertor_box = Toplevel()
    # disable help button
    partner.to_converter_button.config(state=DISABLED)
    # If users press cross at top, closes help and 'releases' help button
    self.Convertor_box.protocol('WM_DELETE_WINDOW', partial(self.close_Convertor, partner))
    # Create the parent frame
    self.Convertor_frame = Frame(self.Convertor_box, width=300, height=200, bg=background)
    print("you pressed help") # <debug>
    self.Convertor_frame.grid()
    # ***** row0(text) *****
    self.heading_label = Label(self.Convertor_frame, text="Convertor", font=bold_font_12)
    self.heading_label.grid(row=0)
    # ***** row1() *****
    # ***** row2() *****
  def close_Convertor(self, partner):
    #put help button back to normal...
    partner.to_converter_button.config(state=NORMAL)
    self.Convertor_box.destroy()

if __name__ == "__main__":
  root = Tk()
  #root.geometry("300x200")
  root.configure(bg="#FFFFFF", borderwidth=5, highlightbackground="#CCCCCC", highlightthickness=10, highlightcolor="#CCCCCC")
  root.title("window")
  app = program(root)
  root.mainloop()