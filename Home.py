from tkinter import *
import sys
import os
from user1 import normalize

font10 = "-family {Viner Hand ITC} -size 40 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
font9 = "-family {Ink Free} -size 14 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"






def next_window():
    getQuery()
    top.quit()
    os.system('python3 Result_page.py')
    

query = ""

def getQuery():
    global query
    query = lyrics_text.get()
    print(query)
    normalize.TRF(query)
    Ans=normalize.cosine(query)
    file2 = open("out.txt", 'w')
    try:
        Ans = reversed(Ans)
        

        ctr=0;
        j = 0
        with open('outtmp.txt','w') as file1:
            file1.write('\n'.join('%s %s' % x for x in Ans))
            
        file1.close()

        strline = []
        file1 = open("outtmp.txt",'r')
        

        for line in file1:
            strline = line.split(' ')
            file2.write(str(strline[0]) + '\n')
            
        
    except:
        file2.write("No result found")
        
    file2.close()


    #label_name.configure(text = query)


top = Tk()
#top.geometry("1366x705+73+65")
top.attributes("-fullscreen", True)
top.title("Songle")
top.configure(background="#d9d9d9")
top.configure(highlightbackground="#d9d9d9")
top.configure(highlightcolor="black")



Frame1 = Frame(top)
Frame1.place(relx=0.29, rely=0.2, relheight=0.62, relwidth=0.41)
Frame1.configure(relief=RAISED)
Frame1.configure(borderwidth="2")
Frame1.configure(relief=RAISED)
Frame1.configure(background="#cecece")
Frame1.configure(highlightbackground="#efefef")
Frame1.configure(highlightcolor="black")

Heading = Label(Frame1)
Heading.place(relx=0.3, rely=0.23, relheight=.23, relwidth=.4)
Heading.configure(activebackground="#f9f9f9")
Heading.configure(activeforeground="black")
Heading.configure(background="#d9d9d9")
Heading.configure(disabledforeground="#a3a3a3")
Heading.configure(font=font10)
Heading.configure(foreground="#000000")
Heading.configure(highlightbackground="#d9d9d9")
Heading.configure(highlightcolor="black")
Heading.configure(relief=RIDGE)
Heading.configure(text='''Songle''')

name_text = Entry(Frame1)
name_text.place(relx=0.42, rely=0.48,height=30, relwidth=0.33)
name_text.configure(background="#ffffff")
name_text.configure(disabledforeground="#a3a3a3")
name_text.configure(font=font9)
name_text.configure(foreground="#000000")
name_text.configure(highlightbackground="#d9d9d9")
name_text.configure(highlightcolor="black")
name_text.configure(insertbackground="black")
name_text.configure(selectbackground="#c4c4c4")
name_text.configure(selectforeground="black")



composer_text = Entry(Frame1)
composer_text.place(relx=0.42, rely=0.57,height=30, relwidth=0.33)
composer_text.configure(background="white")
composer_text.configure(disabledforeground="#a3a3a3")
composer_text.configure(font="TkFixedFont")
composer_text.configure(foreground="#000000")
composer_text.configure(highlightbackground="#d9d9d9")
composer_text.configure(highlightcolor="black")
composer_text.configure(insertbackground="black")
composer_text.configure(selectbackground="#dbdbdb")
composer_text.configure(selectforeground="black")

lyrics_text = Entry(Frame1)
lyrics_text.place(relx=0.42, rely=0.67,height=30, relwidth=0.33)
lyrics_text.configure(background="white")
lyrics_text.configure(disabledforeground="#a3a3a3")
lyrics_text.configure(font="TkFixedFont")
lyrics_text.configure(foreground="#000000")
lyrics_text.configure(highlightbackground="#d9d9d9")
lyrics_text.configure(highlightcolor="black")
lyrics_text.configure(insertbackground="black")
lyrics_text.configure(selectbackground="#c4c4c4")
lyrics_text.configure(selectforeground="black")

label_name = Label(Frame1)
label_name.place(relx=0.25, rely=0.48, height=31, width=94)
label_name.configure(activebackground="#f9f9f9")
label_name.configure(activeforeground="black")
label_name.configure(background="#d9d9d9")
label_name.configure(disabledforeground="#a3a3a3")
label_name.configure(foreground="#000000")
label_name.configure(highlightbackground="#d9d9d9")
label_name.configure(highlightcolor="black")
label_name.configure(text='''Name''')

label_composer = Label(Frame1)
label_composer.place(relx=0.25, rely=0.57, height=31, width=94)
label_composer.configure(activebackground="#f9f9f9")
label_composer.configure(activeforeground="black")
label_composer.configure(background="#d9d9d9")
label_composer.configure(disabledforeground="#a3a3a3")
label_composer.configure(foreground="#000000")
label_composer.configure(highlightbackground="#d9d9d9")
label_composer.configure(highlightcolor="black")
label_composer.configure(text='''Composer''')

label_lyrics = Label(Frame1)
label_lyrics.place(relx=0.25, rely=0.67, height=31, width=94)
label_lyrics.configure(activebackground="#f9f9f9")
label_lyrics.configure(activeforeground="black")
label_lyrics.configure(background="#d9d9d9")
label_lyrics.configure(disabledforeground="#a3a3a3")
label_lyrics.configure(foreground="#000000")
label_lyrics.configure(highlightbackground="#d9d9d9")
label_lyrics.configure(highlightcolor="black")
label_lyrics.configure(text='''Lyrics''')

button_search = Button(Frame1, command = next_window)
button_search.place(relx=0.3, rely=0.8, height=24, width=67)
button_search.configure(activebackground="#d9d9d9")
button_search.configure(activeforeground="#000000")
button_search.configure(background="#d9d9d9")
button_search.configure(disabledforeground="#a3a3a3")
button_search.configure(foreground="#000000")
button_search.configure(highlightbackground="#d9d9d9")
button_search.configure(highlightcolor="black")
button_search.configure(pady="0")
button_search.configure(text='''Search''')

button_advanced_search = Button(Frame1)
button_advanced_search.place(relx=0.53, rely=0.8, height=24
                                  , width=97)
button_advanced_search.configure(activebackground="#d9d9d9")
button_advanced_search.configure(activeforeground="#000000")
button_advanced_search.configure(background="#d9d9d9")
button_advanced_search.configure(disabledforeground="#a3a3a3")
button_advanced_search.configure(foreground="#000000")
button_advanced_search.configure(highlightbackground="#d9d9d9")
button_advanced_search.configure(highlightcolor="black")
button_advanced_search.configure(pady="0")
button_advanced_search.configure(text='''Advanced Search''')

button_history = Button(Frame1)
button_history.place(relx=0.9, rely=0.02, height=24, width=49)
button_history.configure(activebackground="#d9d9d9")
button_history.configure(activeforeground="#000000")
button_history.configure(background="#d9d9d9")
button_history.configure(disabledforeground="#a3a3a3")
button_history.configure(foreground="#000000")
button_history.configure(highlightbackground="#d9d9d9")
button_history.configure(highlightcolor="black")
button_history.configure(pady="0")
button_history.configure(text='''History''')

Exit_button = Button(top, command = quit)
Exit_button.place(relx=.95, rely=0.02, height=24, width=49)
Exit_button.configure(text = '''Exit''')

#print(query)

top.mainloop()
