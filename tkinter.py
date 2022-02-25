import tkinter 
import tkinter.messagebox 
 
def main(): 
 mainform = tkinter.Tk() 
 mainform.wm_title("Haha") 
 mainform.geometry("300x125") 
 
 def buttonclick(event): 
  tkinter.messagebox.showinfo("hihi", 
   "%s, Maaf belum beruntung " % (txt.get())) 
  
 lbl = tkinter.Label(mainform) 
 lbl['text'] = "Tulis Sesuatu" 
 lbl.pack() 
  
 txt = tkinter.Entry(mainform, bd=5, fg="black") 
 txt['width'] = 40 
 txt.pack() 
 
 btn = tkinter.Button(mainform) 
 btn.bind('<Button>', buttonclick) 
  
 btn['text'] = "oke" 
 btn['background'] = "blue" 
 btn.pack(padx= 30, pady= 20) 
 
 mainform.mainloop() 
 
if __name__ == "__main__": 
 main() 