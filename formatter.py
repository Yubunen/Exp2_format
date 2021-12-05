from os import close
from tkinter import *
from tkinter import ttk

def Add_b():
    Direction = ''
    Boat_s = 0
    Boat_e = 0
    Boat_h = 0
    Boat_o = 0
    S_m_i = int(S_m.get())
    S_s_i = int(S_s.get())
    E_m_i = int(E_m.get())
    E_s_i = int(E_s.get())
    H_s_i = int(Hum_s_n.get())
    H_e_i = int(Hum_e_n.get())
    O_s_i = int(Oni_s_n.get())
    O_e_i = int(Oni_e_n.get())
    command_s = ' #' + command.get()

    if(H_s_i < H_e_i or O_s_i < O_e_i):
        Direction = 'RL'
        Boat_h = H_e_i - H_s_i
        Boat_o = O_e_i - O_s_i
        Boat_s = 0
        Boat_e = 1
    elif(H_s_i > H_e_i or O_s_i > O_e_i):
        Direction = 'LR'
        Boat_h = H_s_i - H_e_i
        Boat_o = O_s_i - O_e_i
        Boat_s = 1
        Boat_e = 0
    else:
        Direction = ''
    
    output = f'{S_m_i}:{S_s_i} {E_m_i}:{E_s_i} {Direction}({Boat_h},{Boat_o}) ({H_s_i},{O_s_i},{Boat_s}) ({H_e_i},{O_e_i},{Boat_e})'

    if command.get() == 'Reset':
        output = f'{S_m_i}:{S_s_i} {E_m_i}:{E_s_i}' + command_s
        Hum_s_n.set(0)
        Hum_e_n.set(0)
        Oni_s_n.set(0)
        Oni_e_n.set(0)
    elif command.get() == 'Start':
        output = f'{S_m_i}:{S_s_i}' + command_s
        E_m.set(S_m.get())
        E_s.set(S_s.get())
        Hum_s_n.set(0)
        Hum_e_n.set(0)
        Oni_s_n.set(0)
        Oni_e_n.set(0)
    elif (H_e_i == 3 and O_e_i == 3 and Boat_e == 1):
        output += ' #End'
    elif command.get() != '':
        output += command_s
    elif Direction == '':
        print('Error')
        return
    
    
    command.set('')
    Hum_s_n.set(Hum_e_n.get())
    Oni_s_n.set(Oni_e_n.get())

    print('add>> ' + output)
    added_stv.set(output)

    if file_stv.get() != '':
        FILE_PATH = file_stv.get()
        f = open(FILE_PATH, 'a')
        f.write(output + '\n')
        f.close()




root = Tk()
root.title('FormatExp')

# Frame
frame1 = ttk.Frame(root, padding=(10))
# Style - Theme

Start_label = ttk.Label(frame1, text="Start condition")
End_Label = ttk.Label(frame1, text='End Condition')

Start_time_frame = ttk.Labelframe(
    frame1,
    text="Time",
    padding=(10),
)

S_m = StringVar()
S_m.set('0')
Start_time_m_sp = ttk.Spinbox(
    Start_time_frame,
    textvariable=S_m,
    width=5,
    from_=0,
    to=60,
    increment=1,
)

Start_time_label = ttk.Label(
    Start_time_frame,
    text=':'
)

S_s = StringVar()
S_s.set('0')
Start_time_s_sp = ttk.Spinbox(
    Start_time_frame,
    textvariable=S_s,
    width=5,
    from_=0,
    to=59,
    increment=1,
)

End_time_frame = ttk.Labelframe(
    frame1,
    text="Time",
    padding=(10),
)

E_m = StringVar()
E_m.set('0')
End_time_m_sp = ttk.Spinbox(
    End_time_frame,
    textvariable=E_m,
    width=5,
    from_=0,
    to=60,
    increment=1,
)

End_time_label = ttk.Label(
    End_time_frame,
    text=':'
)

E_s = StringVar()
E_s.set('0')
End_time_s_sp = ttk.Spinbox(
    End_time_frame,
    textvariable=E_s,
    width=5,
    from_=0,
    to=59,
    increment=1,
)

# Label Frame
Oni_start_frame = ttk.Labelframe(
    frame1,
    text='Oni',
    padding=10,
    style='My.TLabelframe')

# Radiobutton 1
Oni_s_n = StringVar()
Oni_s_n.set(0)
Oni_s_rb0 = ttk.Radiobutton(
    Oni_start_frame,
    text='0',
    value=0,
    variable=Oni_s_n)

# Radiobutton 2
Oni_s_rb1 = ttk.Radiobutton(
    Oni_start_frame,
    text='1',
    value=1,
    variable=Oni_s_n)

Oni_s_rb2 = ttk.Radiobutton(
    Oni_start_frame,
    text='2',
    value=2,
    variable=Oni_s_n)

Oni_s_rb3 = ttk.Radiobutton(
    Oni_start_frame,
    text='3',
    value=3,
    variable=Oni_s_n)


# Label Frame
Oni_end_frame = ttk.Labelframe(
    frame1,
    text='Oni',
    padding=(10),
    style='My.TLabelframe')

# Radiobutton 1
Oni_e_n = StringVar()
Oni_e_n.set(0)
Oni_e_rb0 = ttk.Radiobutton(
    Oni_end_frame,
    text='0',
    value=0,
    variable=Oni_e_n)

# Radiobutton 2
Oni_e_rb1 = ttk.Radiobutton(
    Oni_end_frame,
    text='1',
    value=1,
    variable=Oni_e_n)

Oni_e_rb2 = ttk.Radiobutton(
    Oni_end_frame,
    text='2',
    value=2,
    variable=Oni_e_n)

Oni_e_rb3 = ttk.Radiobutton(
    Oni_end_frame,
    text='3',
    value=3,
    variable=Oni_e_n)

    
Hum_start_frame = ttk.Labelframe(
    frame1,
    text='Human',
    padding=(10),
    style='My.TLabelframe')

# Radiobutton 1
Hum_s_n = StringVar()
Hum_s_n.set(0)
Hum_s_rb0 = ttk.Radiobutton(
    Hum_start_frame,
    text='0',
    value=0,
    variable=Hum_s_n)

# Radiobutton 2
Hum_s_rb1 = ttk.Radiobutton(
    Hum_start_frame,
    text='1',
    value=1,
    variable=Hum_s_n)

Hum_s_rb2 = ttk.Radiobutton(
    Hum_start_frame,
    text='2',
    value=2,
    variable=Hum_s_n)

Hum_s_rb3 = ttk.Radiobutton(
    Hum_start_frame,
    text='3',
    value=3,
    variable=Hum_s_n)


# Label Frame
Hum_end_frame = ttk.Labelframe(
    frame1,
    text='Human',
    padding=(10),
    style='My.TLabelframe')

# Radiobutton 1
Hum_e_n = StringVar()
Hum_e_n.set(0)
Hum_e_rb0 = ttk.Radiobutton(
    Hum_end_frame,
    text='0',
    value=0,
    variable=Hum_e_n)

# Radiobutton 2
Hum_e_rb1 = ttk.Radiobutton(
    Hum_end_frame,
    text='1',
    value=1,
    variable=Hum_e_n)

Hum_e_rb2 = ttk.Radiobutton(
    Hum_end_frame,
    text='2',
    value=2,
    variable=Hum_e_n)

Hum_e_rb3 = ttk.Radiobutton(
    Hum_end_frame,
    text='3',
    value=3,
    variable=Hum_e_n)

#Text
command = StringVar()
command.set('')
command_box = ttk.Entry(
    frame1,
    textvariable=command,
    width=23
)

# Button
add_button = ttk.Button(
    frame1,
    text='Add',
    padding=(20, 5),
    command=lambda:[Add_b()]
)

add_reset_button = ttk.Button(
    frame1,
    text='Add Reset',
    padding=(20, 5),
    command=lambda:[command.set('Reset'), Add_b()]
)

add_start_button = ttk.Button(
    frame1,
    text='Add Start',
    padding=(20, 5),
    command=lambda:[command.set('Start'), Add_b()]
)

add_com_button = ttk.Button(
    frame1,
    text='Add with Comment',
    padding=(20, 5),
    command=lambda:[Add_b()]
)

added_frame = ttk.Frame(
    frame1,
    padding=4
)

added_lb = ttk.Label(
    added_frame,
    text='Add >> '
)

added_stv = StringVar()
added_box = ttk.Entry(
    added_frame,
    state='readonly',
    textvariable=added_stv,
    width=40
)

file_frame = ttk.Frame(
    frame1,
    padding=4
)

file_lb = ttk.Label(
    file_frame,
    text='File Path'
)

file_stv = StringVar()
file_box = ttk.Entry(
    file_frame,
    textvariable=file_stv,
    width=40
)

# Layout
frame1.grid(row = 0)
Start_label.grid(row=0, column=0)
End_Label.grid(row=0, column=1)

Start_time_frame.grid(row=1, column=0)
Start_time_m_sp.grid(row=0, column=0)
Start_time_label.grid(row=0, column=1)
Start_time_s_sp.grid(row=0, column=2)
End_time_frame.grid(row=1, column=1)
End_time_m_sp.grid(row=0, column=0)
End_time_label.grid(row=0, column=1)
End_time_s_sp.grid(row=0, column=2)

Hum_start_frame.grid(row=2, column=0)
Hum_s_rb0.grid(row=0, column=0) # LabelFrame
Hum_s_rb1.grid(row=0, column=1) 
Hum_s_rb2.grid(row=0, column=2) 
Hum_s_rb3.grid(row=0, column=3) 

Hum_end_frame.grid(row=2, column=1)
Hum_e_rb0.grid(row=0, column=0) # LabelFrame
Hum_e_rb1.grid(row=0, column=1) 
Hum_e_rb2.grid(row=0, column=2) 
Hum_e_rb3.grid(row=0, column=3) 

Oni_start_frame.grid(row=3, column=0)
Oni_s_rb0.grid(row=0, column=0) # LabelFrame
Oni_s_rb1.grid(row=0, column=1) 
Oni_s_rb2.grid(row=0, column=2) 
Oni_s_rb3.grid(row=0, column=3) 

Oni_end_frame.grid(row=3, column=1)
Oni_e_rb0.grid(row=0, column=0) # LabelFrame
Oni_e_rb1.grid(row=0, column=1) 
Oni_e_rb2.grid(row=0, column=2) 
Oni_e_rb3.grid(row=0, column=3) 

add_button.grid(row=1, column=2, padx=4)
add_reset_button.grid(row=2, column=2, padx=4)
add_start_button.grid(row=3, column=2, padx=4)
add_com_button.grid(row=2, column=3, padx=10)

command_box.grid(row=1, column=3)

added_frame.grid(row=4, column=0, columnspan=2)
added_lb.grid(row=0,column=0)
added_box.grid(row=0, column=1, columnspan=2)

file_frame.grid(row=5, column=0, columnspan=2)
file_lb.grid(row=0, column=0)
file_box.grid(row=0, column=1, columnspan=2)


# Start App
root.mainloop()