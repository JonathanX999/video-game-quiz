from tkinter import *
import random



class QuizBegin:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color = "OldLace"# to set it as background color for all the label widgets
        acolor="Dim Grey"
        #frame set up
        self.quiz_frame = Frame(parent, bg = acolor, padx=100, pady=100)
        #padx, pady How many pixels to pad widget, horizontally (x) and vertically (y), outside widget's borders.
        self.quiz_frame.grid()#This geometry manager organizes widgets in a table-like structure in the parent widget.
               
        #widgets goes below
        self.heading_label=Label(self.quiz_frame, text="Gaming Quiz", font=("Tw Cen MT","18","bold"),bg="Dim Grey", foreground= "white smoke")
        self.heading_label.grid(row=0, padx=20) 
        self.var1=IntVar() #holds value of radio buttons
        
        #label for username
        self.user_label=Label(self.quiz_frame, text="Please enter your name: ", font=("Tw Cen MT","16"),bg="Dim Grey", foreground= "white smoke")
        self.user_label.grid(row=1, padx=20, pady=20) 
        
        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)
        
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Next", font=("Helvetica", "13", "bold"), bg="lime", command=self.name_collection)
        self.continue_button.grid(row=3,  padx=20, pady=20)
        
        def name_collection(self):
    name=self.entry_box.get()
    names.append(name) #add name to names list declared at the beginning
    self.quiz_frame.destroy() #destroy the starter
    Quiz(root)
    
    
    if __name__ == "__main__":
    root = Tk()
    root.title("Gaming Quiz") 

    quiz_instance = QuizBegin(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear
