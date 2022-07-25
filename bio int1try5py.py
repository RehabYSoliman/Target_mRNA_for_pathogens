import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkinter import filedialog as fd

# Root window
root = tk.Tk()
root.title('Learn RNA Design')
root.geometry('520x520')
# Text editor
text = tk.Text(root, height=12)
text.grid(column=0, row=0, sticky='nsew')


def open_text_file():
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = fd.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    text.insert('1.0', f.readlines())


# open file button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=open_text_file
)

open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)

def complement_base(base, material='DNA'):
    """Returns the Watson-Crick complement of a base."""
    
    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'
    
def reverse_complement(seq, material='DNA'):
    """Compute reverse complement of a sequence."""
    
    # Initialize reverse complement
    rev_seq = ''
    
    # Loop through and populate list with reverse complement
    for base in reversed(seq):
        rev_seq += complement_base(base, material=material)
        
    return rev_seq

# DNA entry
DNA = tk.StringVar()
DNA_entry = ttk.Entry(text , textvariable=DNA)
DNA_entry.grid(column=2, row=3)
DNA_entry.focus()

# convert button


def convert_button_clicked():
    """  Handle convert button click event 
    """
    try:
        D = str(DNA.get())
        c = reverse_complement(D)
        result = c 
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)


convert_button = ttk.Button(text , text='Convert')
convert_button.grid(column=3, row=4, sticky='W')
convert_button.configure(command=convert_button_clicked)

# result label
result_label = ttk.Label(text)
result_label.grid(row=5, column=4)

# add padding to the text and show it
text.grid(padx=10, pady=10)


# start the app

def open_text_file():
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = fd.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    text.insert('1.0', f.readlines())


# open file button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=open_text_file
)


# display an image label
photo = tk.PhotoImage(file='C:\\Users\\Admin\\Downloads\\Your_image.png')
image_label = ttk.Label(
    root,
    image=photo
)
image_label.grid()


root.mainloop()
