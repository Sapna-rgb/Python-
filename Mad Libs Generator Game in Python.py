from tkinter import *

# Initialize the main window
Screen = Tk()
Screen.title("Fun Mad Libs Generator - PythonGeeks Edition")
Screen.geometry('500x500')
Screen.config(bg="#FCE4EC")  # Light pink background

# Title label with a larger, bold font
Label(Screen, text='Welcome to the Fun Mad Libs Generator!', font=("Comic Sans MS", 16, "bold"), fg="white", bg="#EC407A").pack(pady=20)

# Create attractive buttons for Story1 and Story2 with rounded corners and hover effects
def on_enter(e, button):
    button['background'] = '#D81B60'

def on_leave(e, button):
    button['background'] = '#E91E63'

# Button 1: Story 1 - A memorable day
Story1Button = Button(Screen, text='A Memorable Day', font=("Comic Sans MS", 13, "bold"), command=lambda: Story1(Screen), bg='#E91E63', fg="white", padx=10, pady=5, relief=GROOVE, bd=3)
Story1Button.place(x=180, y=150)
Story1Button.bind("<Enter>", lambda event, b=Story1Button: on_enter(event, b))
Story1Button.bind("<Leave>", lambda event, b=Story1Button: on_leave(event, b))

# Button 2: Story 2 - Ambitions
Story2Button = Button(Screen, text='Ambitions', font=("Comic Sans MS", 13, "bold"), command=lambda: Story2(Screen), bg='#E91E63', fg="white", padx=10, pady=5, relief=GROOVE, bd=3)
Story2Button.place(x=200, y=250)
Story2Button.bind("<Enter>", lambda event, b=Story2Button: on_enter(event, b))
Story2Button.bind("<Leave>", lambda event, b=Story2Button: on_leave(event, b))

# Function for "A memorable day"
def Story1(win):
    def final(tl: Toplevel, name, sports, City, playername, drinkname, snacks):
        text = f'''
        One day me and my friend {name} decided to play a {sports} game in {City}.
        We wanted to watch {playername}.
        We drank {drinkname} and also ate some {snacks}.
        We really enjoyed it! We are looking forward to going again and enjoying.
        '''
        tl.geometry('500x550')
        Label(tl, text='Story:', wraplength=tl.winfo_width()).place(x=160, y=310)
        Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0, y=330)

    NewScreen = Toplevel(win, bg='#FFEBEE')
    NewScreen.title("A Memorable Day - Mad Libs Story")
    NewScreen.geometry('500x500')
    Label(NewScreen, text='Memorable Day', font=("Comic Sans MS", 14, "bold"), fg='#880E4F').place(x=150, y=0)

    # Input labels and fields
    Label(NewScreen, text='Name:', font=("Comic Sans MS", 10), bg='#FFEBEE').place(x=0, y=35)
    Label(NewScreen, text='Enter a game:', font=("Comic Sans MS", 10), bg='#FFEBEE').place(x=0, y=70)
    Label(NewScreen, text='Enter a city:', font=("Comic Sans MS", 10), bg='#FFEBEE').place(x=0, y=110)
    Label(NewScreen, text='Enter the name of a player:', font=("Comic Sans MS", 10), bg='#FFEBEE').place(x=0, y=150)
    Label(NewScreen, text='Enter the name of a drink:', font=("Comic Sans MS", 10), bg='#FFEBEE').place(x=0, y=190)
    Label(NewScreen, text='Enter the name of a snack:', font=("Comic Sans MS", 10), bg='#FFEBEE').place(x=0, y=230)

    Name = Entry(NewScreen, width=17)
    Name.place(x=250, y=35)
    game = Entry(NewScreen, width=17)
    game.place(x=250, y=70)
    city = Entry(NewScreen, width=17)
    city.place(x=250, y=105)
    player = Entry(NewScreen, width=17)
    player.place(x=250, y=150)
    drink = Entry(NewScreen, width=17)
    drink.place(x=250, y=190)
    snack = Entry(NewScreen, width=17)
    snack.place(x=250, y=220)

    SubmitButton = Button(NewScreen, text="Submit", background="#EC407A", font=('Comic Sans MS', 12, "bold"), fg="white", command=lambda: final(NewScreen, Name.get(), game.get(), city.get(), player.get(), drink.get(), snack.get()))
    SubmitButton.place(x=150, y=270)

# Function for "Ambitions"
def Story2(win):
    def final(tl: Toplevel, profession, noun, feeling, emotion, verb):
        text = f'''
        I have always wanted to be a {profession}. One day, I found a {noun} that made me feel {feeling}.
        It was an unforgettable moment filled with {emotion}. After that, I decided to {verb} and chase my dreams.
        '''
        tl.geometry('500x550')
        Label(tl, text='Story:', wraplength=tl.winfo_width()).place(x=160, y=310)
        Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0, y=330)

    NewScreen = Toplevel(win, bg='#F8BBD0')
    NewScreen.title("Ambitions - Mad Libs Story")
    NewScreen.geometry('500x500')
    Label(NewScreen, text='Ambitions', font=("Comic Sans MS", 14, "bold"), fg='#880E4F').place(x=150, y=0)

    # Input labels and fields
    Label(NewScreen, text='Enter a profession:', font=("Comic Sans MS", 10), bg='#F8BBD0').place(x=0, y=35)
    Label(NewScreen, text='Enter a noun:', font=("Comic Sans MS", 10), bg='#F8BBD0').place(x=0, y=70)
    Label(NewScreen, text='Enter a feeling:', font=("Comic Sans MS", 10), bg='#F8BBD0').place(x=0, y=110)
    Label(NewScreen, text='Enter an emotion:', font=("Comic Sans MS", 10), bg='#F8BBD0').place(x=0, y=150)
    Label(NewScreen, text='Enter a verb:', font=("Comic Sans MS", 10), bg='#F8BBD0').place(x=0, y=190)

    Profession = Entry(NewScreen, width=17)
    Profession.place(x=250, y=35)
    Noun = Entry(NewScreen, width=17)
    Noun.place(x=250, y=70)
    Feeling = Entry(NewScreen, width=17)
    Feeling.place(x=250, y=105)
    Emotion = Entry(NewScreen, width=17)
    Emotion.place(x=250, y=150)
    Verb = Entry(NewScreen, width=17)
    Verb.place(x=250, y=190)

    SubmitButton = Button(NewScreen, text="Submit", background="#EC407A", font=('Comic Sans MS', 12, "bold"), fg="white", command=lambda: final(NewScreen, Profession.get(), Noun.get(), Feeling.get(), Emotion.get(), Verb.get()))
    SubmitButton.place(x=150, y=270)

Screen.mainloop()
