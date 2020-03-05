#My glossary Project

#importing tkinter library from Python
from tkinter import *

#key down functions

def click():
    entered_text= textentry.get() #this will collect the text from the entry box
    #output.delete(0.0,END) #this will completely clear the box



    
    #this will test if there are any ambiguos words within the sentence and the dictionary!

    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "Sorry there is no word like that, please try again!"
    output.insert(END, definition)


##main

window = Tk()
window.title("Xhosa Word Scense Disambiguation Application")
window.configure(background = "black")

###My photo
photo1 = PhotoImage(file="Capture.gif")
Label (window, image=photo1, bg="black") .grid(row=0 , column=0, sticky=E)

#Create label

Label (window, text="Please Input Sentence: ", bg="black",fg="white",font="none 14 bold"). grid(row=1,column=0,sticky=W)

#create a text entry box

textentry = Entry(window, width=100,bg="white")
textentry.grid(row=2, column=0,sticky=W)

#add submit button

Button(window, text="SUBMIT", width= 30, command=click).grid(row = 2,column=0,sticky=E)

#create another label


Label (window, text="\n Output Results: ", bg="black",fg="white",font="none 14 bold"). grid(row=3,column=0,sticky=W)


#create a text box

output = Text(window, width=108,height=8,wrap=WORD, background="white")
output.grid(row=4, column=0,columnspan=2,sticky=W)

#the dictionary

my_compdictionary = {
    
    'Idolo': 'yindlela enjikayo'  '\nIdolo lilungu lomzimba',
   
    }



#clear button

def clear():
     entered_text= textentry.get()
     output.delete(0.0,END)

     output.delete(0.0,END)
    
    

Button(window, text="Clear Text",command=clear, width= 30).grid(row = 7,column=0,sticky=W)




#exit function

def close_window():
    window.destroy()
    exit()

#exit button

Label (window, text=" ", bg="black",fg="white",font="none 14 bold"). grid(row=6,column=0,sticky=W)

Button(window, text="Exit", width= 30, command=close_window).grid(row = 7,column=0,sticky=E)





###run the main loop
window.mainloop()
