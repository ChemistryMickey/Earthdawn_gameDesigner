#!/bin/python3

import tkinter as tk #general GUI object
import random
from tkinter import messagebox as mb #message box for errors and warnings
from tkFileDialog import askopenfilename

from math import * #for calculatorTest


#-------------------------------
#    x = StringVar()    # Holds a string; default value ""
#    x = IntVar()       # Holds an integer; default value 0
#    x = DoubleVar()    # Holds a float; default value 0.0
#    x = BooleanVar()   # Holds a boolean, returns 0 for False and 1 for True
#-------------------------------


root = tk.Tk(); #make top level TK window

#--Basic Label
def basicLabelTest():
    w = tk.Label(root, text = "Hello Tkinter!"); #label object
    w.pack(); #add the object to the window


#--Message
def messageTest():
    messageTest = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)";
    msg = tk.Message(root, text = messageTest);

    #bg = background, font = font style, aspect = aspect ratio of message
    msg.config(bg = 'lightgreen', font = ('times', 24, 'italic' ), aspect = 300);
    msg.pack(); #add to window

#--Button
def buttonTest():
    def write_slogan():
        print("Tkinter is easy to use!");
        
    frame = tk.Frame(root); #create canvas for button
    frame.pack();

    button = tk.Button( frame, 
                        text = "QUIT",  #text color
                        fg = "red",     #foreground color
                        command = quit);#command to run
    button.pack( side = tk.LEFT ); #add the button to the frame on the left side

    slogan = tk.Button( frame,
                        text = "Hello!",
                        command = write_slogan); #no arguments passed to function
    slogan.pack( side = tk.LEFT );  #stacks button (priority given to first packed button)

#--Incrementing counter button
def incrementCounterButton():
    counter = 0;
    def counter_label( label ):
        counter = 0;
        
        def count():
            global counter;
            counter += 1;
            label.config( text = str(counter) ); #change label text
            label.after(1000, count)
        count();
        
    root.title("Counting seconds");

    label = tk.Label(root, fg = 'dark green');
    label.pack();

    counter_label(label);

    increButton = tk.Button(root, 
                            text = 'Stop', 
                            width=25, 
                            command = root.destroy); #destroy appears indistinguishable from "quit" but it might be window specific
    increButton.pack();

#--Radio Button
def radioButtonTest():
    v = tk.IntVar() #integer variable which can change in tkinter application
    tk.Label(root,
             text = """Choose a programming language:""",
             justify = tk.LEFT,
             padx = 20).pack(); #create a label and immediately pack it
    tk.Radiobutton(root, 
                    text = 'Python',
                    padx = 20,
                    variable=v,
                    value = 1).pack( anchor = tk.W ); #anchor it to the active window(?)
    tk.Radiobutton( root,
                    text = 'Perl',
                    padx = 20,
                    variable = v,
                    value = 2).pack( anchor = tk.W );
                    
#--Enumerated Radio Buttons
def enumeratedRadioButtons():
    v = tk.IntVar();
    v.set(1); #initialize choice
    
    languages = [   ("Python", 1),
                    ("Perl", 2),
                    ("Java", 3),
                    ("C++", 4),
                    ("C", 5)
    ];
    
    def ShowChoice():
        print(v.get()); #getter for tk variable
    
    tk.Label(   root,
                text = """Choose your favourite programming language:""",
                justify = tk.LEFT,
                padx = 20
            ).pack();
    for val, language in enumerate( languages ):
        tk.Radiobutton( root,
                        text = language,
                        indicatoron = 0, #turn white button of radio buttons off
                        width = 20,
                        padx = 20,
                        variable = v,
                        command = ShowChoice,
                        value = val
                    ).pack(anchor = tk.W);

def checkboxTest():
    var1 = tk.IntVar();
    tk.Checkbutton( root,
                    text = "Male",
                    variable = var1
                ).grid( row = 0, sticky = tk.W );
    var2 = tk.IntVar();
    tk.Checkbutton( root,
                    text = "Female",
                    variable = var2
                ).grid( row = 1, sticky = tk.W );
                
def entryWidgetTest():
    
    def show_entry_fields():
        print( "First Name: {0}\nLast Name: {1}".format( e1.get(), e2.get() ) );

    tk.Label(   root,
                text = "First Name"
            ).grid(row = 0);
    tk.Label(   root,
                text = "Last Name"
            ).grid(row = 1);
    e1 = tk.Entry(root); #create entry object (not immediately using .grid so we don't just store the return type of grid)
    e1.grid( row = 0, column = 1 );
    e1.insert( 10, "Miller" ); #give it a default value
    
    e2 = tk.Entry(root);
    e2.grid( row = 1, column = 1 );
    e2.insert( 10, 'Doe' );
    
    tk.Button(  root,
                text = 'Quit',
                command = root.quit
            ).grid( row = 3,
                    column = 0,
                    sticky = tk.W,
                    pady = 4
                );
    tk.Button(  root,   
                text = 'Show',
                command = show_entry_fields
            ).grid( row = 3,
                    column = 1,
                    sticky = tk.W,
                    pady = 4
                );
    

def calculatorTest():
    
    def evaluate( event ):
        res.configure( text = "Result: " + str(eval( entry.get() )) );
    
    tk.Label(   root,
                text = "Your Expression: "
            ).pack()
    entry = tk.Entry(root);
    entry.bind("<Return>", evaluate);
    entry.pack();
    
    res = tk.Label(root);
    res.pack();
    
def canvasTest():
    canvas_width = 80;
    canvas_height = 40;
    w = tk.Canvas(  root,
                    width = canvas_width,
                    height = canvas_height
                );
    w.pack();
    
    y = int( canvas_height / 2);
    w.create_line( 0, y, canvas_width, y, fill = "#476042" );
    
def paintingCanvasTest():
    canvas_width = 500;
    canvas_height = 150;
    
    def paint( event ):
        python_green = "#476042";
        x1, y1 = (event.x - 1), (event.y - 1);
        x2, y2 = (event.x + 1), (event.y + 1); #get pixel width
        w.create_oval( x1, y1, x2, y2, fill = python_green );
        
    root.title( "Painting with Ovals" );
    w = tk.Canvas(  root,
                    width = canvas_width,
                    height = canvas_height
                );
    w.pack( expand = tk.YES, fill = tk.BOTH );
    w.bind( "<B1-Motion>", paint );
    
    message = tk.Label( root,
                        text = "Press and Drag the mouse to draw"
                    );
    message.pack( side = tk.BOTTOM );


def sliderTest():
    
    def show_values():
        print( w1.get(), w2.get() );
        
        
    w1 = tk.Scale(   root,
                    from_=0, #not sure why the underscore is needed...
                    to = 42,
                    length = 200,
                    tickinterval = 8
                );
    w1.pack();
    w2 = tk.Scale(   root,
                    from_ = 0,
                    to = 200,
                    tickinterval = 10,
                    length = 600,
                    orient = tk.HORIZONTAL
                );
    w2.pack();
    
    tk.Button(  root,
                text = "Show Values",
                command = show_values
            ).pack();

def textTest():

    S = tk.Scrollbar( root ); #create a sidebar for scrolling through text
    S.pack( side = tk.RIGHT, fill = tk.Y );
    T = tk.Text(    root,
                    height = 2,
                    width = 30
                );
    T.pack(expand = tk.YES, side = tk.LEFT, fill = tk.BOTH);
    S.config( command = T.yview );
    T.config( yscrollcommand = S.set );

    T.insert( tk.END, "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed doeiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enimad minim veniam, quis nostrud exercitation ullamco laboris nisi utaliquip ex ea commodo consequat. Duis aute irure dolor inreprehenderit in voluptate velit esse cillum dolore eu fugiat nullapariatur. Excepteur sint occaecat cupidatat non proident, sunt inculpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed doeiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enimad minim veniam, quis nostrud exercitation ullamco laboris nisi utaliquip ex ea commodo consequat. Duis aute irure dolor inreprehenderit in voluptate velit esse cillum dolore eu fugiat nullapariatur. Excepteur sint occaecat cupidatat non proident, sunt inculpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed doeiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enimad minim veniam, quis nostrud exercitation ullamco laboris nisi utaliquip ex ea commodo consequat. Duis aute irure dolor inreprehenderit in voluptate velit esse cillum dolore eu fugiat nullapariatur. Excepteur sint occaecat cupidatat non proident, sunt inculpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed doeiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enimad minim veniam, quis nostrud exercitation ull");
    
def messageBoxTest():
    def answer():
        mb.showerror( "Answer", "Sorry, no answer available" );
        
    def callback():
        if mb.askyesno('Verify', 'Really Quit?'):
            mb.showwarning('Yes', 'Not yet implemented');
        else:
            mb.showinfo('No', 'Quit has been cancelled' );
            
    tk.Button(  text = 'Quit',
                command = callback
            ).pack(fill = tk.X);
    tk.Button(  text = 'Answer',
                command = answer
            ).pack(fill = tk.X);

def labelPaddingTest():
    w = tk.Label(root, text="Red Sun", bg="red", fg="white")
    w.pack(fill=tk.X, padx=10)
    w = tk.Label(root, text="Green Grass", bg="green", fg="black")
    w.pack(fill=tk.X, padx=10)
    w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
    w.pack(fill=tk.X, padx=10)
    
def labelArrangingTest():
    # width x height + x_offset + y_offset:
    root.geometry("170x200+30+30") 
         
    languages = ['Python','Perl','C++','Java','Tcl/Tk']
    labels = range(5)
    for i in range(5):
       ct = [random.randrange(256) for x in range(3)]
       brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
       ct_hex = "%02x%02x%02x" % tuple(ct)
       bg_colour = '#' + "".join(ct_hex)
       l = tk.Label(root, 
                    text=languages[i], 
                    fg='White' if brightness < 120 else 'Black', 
                    bg=bg_colour)
       l.place(x = 20, y = 30 + i*30, width=120, height=25)
       
def arrangeWithGrid():
    colours = ['red','green','orange','white','yellow','blue']

    r = 0
    for c in colours:
        tk.Label(text=c, relief=tk.RIDGE, width=15).grid(row=r,column=0)
        tk.Entry(bg=c, relief=tk.SUNKEN, width=10).grid(row=r,column=1)
        r = r + 1

def menuTest():
    def NewFile():
        print( "New File!" );
    
    def OpenFile():
        name = askopenfilename();
        print( name );
    
    def About():
        print( "This is a simple example of a menu" );
        
    menu = tk.Menu( root );
    root.config( menu = menu );
    filemenu = tk.Menu( menu );
    menu.add_cascade( label = "File", menu = filemenu );
    
    filemenu.add_command( label = "New", command = NewFile );
    filemenu.add_command( label = "Open...", command = OpenFile );
    filemenu.add_separator();
    filemenu.add_command( label = "Exit", command = root.quit );
    
    helpmenu = tk.Menu( menu );
    menu.add_cascade( label = "Help", menu = helpmenu );
    helpmenu.add_command( label = "About...", command = About );


#-------MAIN LOOP--------#
menuTest();
root.mainloop(); #start the window "root"
