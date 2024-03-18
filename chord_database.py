import time
import sys
import tkinter as tk
from tkinter import simpledialog

def submit(event=None):
    clear_text()
    root_pitch = float(entry_field.get())
    semitone_ratio = 2**(1/12)
    entry_text = f"Reference pitch: {root_pitch}\n"
    text_field.insert(tk.END, entry_text)

    note_list_down = ['Ab', 'G', 'Gb', 'F', 'E', 'Eb', 'D', 'Db', 'C', 'B', 'Bb', '<<<   A   >>>']
    note_list_up = ['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', '<<<   A   >>>']
    
    tone_down_range = 48  # Adjust the range as needed
    for i in range(tone_down_range):
        root_pitch /= semitone_ratio  # down
        note = note_list_down[i % len(note_list_down)]  # Get the note name
        entry_text = f"(DOWN) | Note: {note} | Frequency: {root_pitch:.2f} Hz\n"
        text_field.insert(tk.END, entry_text)


    root_pitch = float(entry_field.get())  # Reset root_pitch to the original value
    entry_text = f"\n"
    text_field.insert(tk.END, entry_text)

    for i in range(tone_down_range):
        root_pitch *= semitone_ratio  # up
        note = note_list_up[i % len(note_list_up)]  # Get the note name
        entry_text = f"(UP) | Note: {note} | Frequency: {root_pitch:.2f} Hz\n"
        text_field.insert(tk.END, entry_text)

    entry_text = f"\n"
    text_field.insert(tk.END, entry_text)
    entry_field.focus_set()

def clear_text(event=None):
    text_field.delete(1.0, tk.END)  # Clear all text in the text field



note_to_num_A= {'A': 0, 'A#': 1, "B": 2, "C": 3, "C#": 4, "D": 5, "D#": 6, "E": 7, "F": 8, "F#": 9, "G": 10, "G#": 11, 'A2': 12, 'A#2': 13, "B2": 14, "C2": 15, "C#2": 16}
note_to_num_Bb= {'A#': 0, 'B': 1, "C": 2, "C#": 3, "D": 4, "D#": 5, "E": 6, "F": 7, "F#": 8, "G": 9, "G#": 10, "A": 11, 'A#2': 12, 'B2': 13, "C2": 14, "C#2": 15, "D2": 16}
note_to_num_B = {'B': 0, 'C': 1, "C#": 2, "D": 3, "D#": 4, "E": 5, "F": 6, "F#": 7, "G": 8, "G#": 9, "A": 10, "A#": 11, 'B2': 12, 'C2': 13, "C#2": 14, "D2": 15, "D#2": 16}
note_to_num_C = {'C': 0, 'C#': 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11, 'C2': 12, 'C#2': 13, "D2": 14, "D#2": 15, "E2": 16}
note_to_num_Db = {'C#': 0, 'D': 1, "D#": 2, "E": 3, "F": 4, "F#": 5, "G": 6, "G#": 7, "A": 8, "A#": 9, "B": 10, "C": 11, 'C#2': 12, 'D2': 13, "D#2": 14, "E2": 15, "F2": 16}
note_to_num_D = {'D': 0, 'D#': 1, "E": 2, "F": 3, "F#": 4, "G": 5, "G#": 6, "A": 7, "A#": 8, "B": 9, "C": 10, "C#": 11, 'D2': 12, 'D#2': 13, "E2": 14, "F2": 15, "F#2": 16}
note_to_num_Eb = {'D#': 0, 'E': 1, "F": 2, "F#": 3, "G": 4, "G#": 5, "A": 6, "A#": 7, "B": 8, "C": 9, "C#": 10, "D": 11, 'D#2': 12, 'E2': 13, "F2": 14, "F#2": 15, "G2": 16}
note_to_num_E = {'E': 0, 'F': 1, "F#": 2, "G": 3, "G#": 4, "A": 5, "A#": 6, "B": 7, "C": 8, "C#": 9, "D": 10, "D#": 11, 'E2': 12, 'F2': 13, "F#2": 14, "G2": 15, "G#2": 16}
note_to_num_F = {'F': 0, 'F#': 1, "G": 2, "G#": 3, "A": 4, "A#": 5, "B": 6, "C": 7, "C#": 8, "D": 9, "D#": 10, "E": 11, 'F2': 12, 'F#2': 13, "G2": 14, "G#2": 15, "A2": 16}
note_to_num_Gb = {'F#': 0, 'G': 1, "G#": 2, "A": 3, "A#": 4, "B": 5, "C": 6, "C#": 7, "D": 8, "D#": 9, "E": 10, "F": 11, 'F#2': 12, 'G2': 13, "G#2": 14, "A2": 15, "A#2": 16}
note_to_num_G = {'G': 0, 'G#': 1, "A": 2, "A#": 3, "B": 4, "C": 5, "C#": 6, "D": 7, "D#": 8, "E": 9, "F": 10, "F#": 11, 'G2': 12, 'G#2': 13, "A2": 14, "A#2": 15, "B2": 16}
note_to_num_Ab = {'G#': 0, 'A': 1, "A#": 2, "B": 3, "C": 4, "C#": 5, "D": 6, "D#": 7, "E": 8, "F": 9, "F#": 10, "G": 11, 'G#2': 12, 'A2': 13, "A#2": 14, "B2": 15, "C2": 16}

def power_chord(root_note, note_to_num_key):
    note_to_num = note_to_num_key
    minor_root_note = root_note
    current_note = root_note
    steps = [0, 7, 5]
    text_field.insert("end", f"\n<<<{minor_root_note}>>> | 'Power' Chord\n")
    
    for step in steps:
        next_note_index = (note_to_num[current_note] + step) % 12
        next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
        current_note = next_note_candidates[0]
        text_field.insert(tk.END, f"{current_note}\n")

def minor_triad(root_note, note_to_num_key):
    note_to_num = note_to_num_key
    minor_root_note = root_note
    current_note = root_note
    steps = [0, 3, 4]
    text_field.insert("end", f"\n<<<{minor_root_note}>>> | Minor Triad\n")
    
    for step in steps:
        next_note_index = (note_to_num[current_note] + step) % 12
        next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
        current_note = next_note_candidates[0]
        text_field.insert(tk.END, f"{current_note}\n")


def major_triad(root_note, note_to_num_key):
    note_to_num = note_to_num_key
    minor_root_note = root_note
    current_note = root_note
    steps = [0, 4, 3]
    text_field.insert("end", f"\n<<<{minor_root_note}>>> | Major Triad\n")
    
    for step in steps:
        next_note_index = (note_to_num[current_note] + step) % 12
        next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
        current_note = next_note_candidates[0]
        text_field.insert(tk.END, f"{current_note}\n")

def suspended_fourth(root_note, note_to_num_key):
    note_to_num = note_to_num_key
    minor_root_note = root_note
    current_note = root_note
    steps = [0, 5, 2]
    text_field.insert("end", f"\n<<<{minor_root_note}>>> | Suspended Fourth\n")
    
    for step in steps:
        next_note_index = (note_to_num[current_note] + step) % 12
        next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
        current_note = next_note_candidates[0]
        text_field.insert(tk.END, f"{current_note}\n")

def simple_minor_seventh(root_note, note_to_num_key):
    note_to_num = note_to_num_key
    minor_root_note = root_note
    current_note = root_note
    steps = [0, 7, 3]
    text_field.insert("end", f"\n<<<{minor_root_note}>>> | Simple Minor Seventh\n")
    
    for step in steps:
        next_note_index = (note_to_num[current_note] + step) % 12
        next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
        current_note = next_note_candidates[0]
        text_field.insert(tk.END, f"{current_note}\n")

def minor_seventh(root_note, note_to_num_key):
    note_to_num = note_to_num_key
    minor_root_note = root_note
    current_note = root_note
    steps = [0, 3, 4, 3]
    text_field.insert("end", f"\n<<<{minor_root_note}>>> | Minor Seventh\n")
    
    for step in steps:
        next_note_index = (note_to_num[current_note] + step) % 12
        next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
        current_note = next_note_candidates[0]
        text_field.insert(tk.END, f"{current_note}\n")

def simple_major_seventh(root_note, note_to_num_key):
    note_to_num = note_to_num_key
    minor_root_note = root_note
    current_note = root_note
    steps = [0, 7, 4]
    text_field.insert("end", f"\n<<<{minor_root_note}>>> | Simple Minor Seventh\n")
    
    for step in steps:
        next_note_index = (note_to_num[current_note] + step) % 12
        next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
        current_note = next_note_candidates[0]
        text_field.insert(tk.END, f"{current_note}\n")

def major_seventh(root_note, note_to_num_key):
    note_to_num = note_to_num_key
    minor_root_note = root_note
    current_note = root_note
    steps = [0, 4, 3, 4]
    text_field.insert("end", f"\n<<<{minor_root_note}>>> | Major Seventh\n")
    
    for step in steps:
        next_note_index = (note_to_num[current_note] + step) % 12
        next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
        current_note = next_note_candidates[0]
        text_field.insert(tk.END, f"{current_note}\n")

def dominant_seventh(root_note, note_to_num_key):
    note_to_num = note_to_num_key
    minor_root_note = root_note
    current_note = root_note
    steps = [0, 4, 3, 3]
    text_field.insert("end", f"\n<<<{minor_root_note}>>> | Minor Seventh\n")
    
    for step in steps:
        next_note_index = (note_to_num[current_note] + step) % 12
        next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
        current_note = next_note_candidates[0]
        text_field.insert(tk.END, f"{current_note}\n")

def add_nine(root_note, note_to_num_key):
    note_to_num = note_to_num_key
    minor_root_note = root_note
    current_note = root_note
    steps = [0, 7, 7]
    text_field.insert("end", f"\n<<<{minor_root_note}>>> | Add Ninth\n")
    
    for step in steps:
        next_note_index = (note_to_num[current_note] + step) % 12
        next_note_candidates = [note for note, index in note_to_num.items() if index == next_note_index]
        current_note = next_note_candidates[0]
        text_field.insert(tk.END, f"{current_note}\n")


###########################################################################################################################################
def note_A():
    clear_text()
    note_to_num_key = note_to_num_A
    root_note = 'A'
    text_field.insert("end", f"A\n========================================\n")
    text_field.yview(tk.END)

    power_chord(root_note, note_to_num_key)
    minor_triad(root_note, note_to_num_key)
    major_triad(root_note, note_to_num_key)
    suspended_fourth(root_note, note_to_num_key)
    simple_minor_seventh(root_note, note_to_num_key)
    minor_seventh(root_note, note_to_num_key)
    simple_major_seventh(root_note, note_to_num_key)
    major_seventh(root_note, note_to_num_key)
    dominant_seventh(root_note, note_to_num_key)
    add_nine(root_note, note_to_num_key)

def note_Bb():
    clear_text()
    note_to_num_key = note_to_num_Bb
    root_note = 'A#'
    text_field.insert("end", f"A#/Bb\n========================================\n")
    text_field.yview(tk.END)

    power_chord(root_note, note_to_num_key)
    minor_triad(root_note, note_to_num_key)
    major_triad(root_note, note_to_num_key)
    suspended_fourth(root_note, note_to_num_key)
    simple_minor_seventh(root_note, note_to_num_key)
    minor_seventh(root_note, note_to_num_key)
    simple_major_seventh(root_note, note_to_num_key)
    major_seventh(root_note, note_to_num_key)
    dominant_seventh(root_note, note_to_num_key)
    add_nine(root_note, note_to_num_key)

def note_B():
    clear_text()
    note_to_num_key = note_to_num_B
    root_note = 'B'
    text_field.insert("end", f"B\n========================================\n")
    text_field.yview(tk.END)

    power_chord(root_note, note_to_num_key)
    minor_triad(root_note, note_to_num_key)
    major_triad(root_note, note_to_num_key)
    suspended_fourth(root_note, note_to_num_key)
    simple_minor_seventh(root_note, note_to_num_key)
    minor_seventh(root_note, note_to_num_key)
    simple_major_seventh(root_note, note_to_num_key)
    major_seventh(root_note, note_to_num_key)
    dominant_seventh(root_note, note_to_num_key)
    add_nine(root_note, note_to_num_key)

   
def note_C():
    clear_text()
    note_to_num_key = note_to_num_C
    root_note = 'C'
    text_field.insert("end", f"C\n========================================\n")
    text_field.yview(tk.END)

    power_chord(root_note, note_to_num_key)
    minor_triad(root_note, note_to_num_key)
    major_triad(root_note, note_to_num_key)
    suspended_fourth(root_note, note_to_num_key)
    simple_minor_seventh(root_note, note_to_num_key)
    minor_seventh(root_note, note_to_num_key)
    simple_major_seventh(root_note, note_to_num_key)
    major_seventh(root_note, note_to_num_key)
    dominant_seventh(root_note, note_to_num_key)
    add_nine(root_note, note_to_num_key)


def note_Cs():
    clear_text()
    note_to_num_key = note_to_num_Db
    root_note = 'C#'
    text_field.insert("end", f"C#/Db\n========================================\n")
    text_field.yview(tk.END)

    power_chord(root_note, note_to_num_key)
    minor_triad(root_note, note_to_num_key)
    major_triad(root_note, note_to_num_key)
    suspended_fourth(root_note, note_to_num_key)
    simple_minor_seventh(root_note, note_to_num_key)
    minor_seventh(root_note, note_to_num_key)
    simple_major_seventh(root_note, note_to_num_key)
    major_seventh(root_note, note_to_num_key)
    dominant_seventh(root_note, note_to_num_key)
    add_nine(root_note, note_to_num_key)
 
def note_D():
    clear_text()
    note_to_num_key = note_to_num_D
    root_note = 'D'
    text_field.insert("end", f"D\n========================================\n")
    text_field.yview(tk.END)

    power_chord(root_note, note_to_num_key)
    minor_triad(root_note, note_to_num_key)
    major_triad(root_note, note_to_num_key)
    suspended_fourth(root_note, note_to_num_key)
    simple_minor_seventh(root_note, note_to_num_key)
    minor_seventh(root_note, note_to_num_key)
    simple_major_seventh(root_note, note_to_num_key)
    major_seventh(root_note, note_to_num_key)
    dominant_seventh(root_note, note_to_num_key)
    add_nine(root_note, note_to_num_key)



def note_Eb():
    clear_text()
    note_to_num_key = note_to_num_Eb
    root_note = 'D#'
    text_field.insert("end", f"D#/Eb\n========================================\n")
    text_field.yview(tk.END)

    power_chord(root_note, note_to_num_key)
    minor_triad(root_note, note_to_num_key)
    major_triad(root_note, note_to_num_key)
    suspended_fourth(root_note, note_to_num_key)
    simple_minor_seventh(root_note, note_to_num_key)
    minor_seventh(root_note, note_to_num_key)
    simple_major_seventh(root_note, note_to_num_key)
    major_seventh(root_note, note_to_num_key)
    dominant_seventh(root_note, note_to_num_key)
    add_nine(root_note, note_to_num_key)



def note_E():
    clear_text()
    note_to_num_key = note_to_num_E
    root_note = 'E'
    text_field.insert("end", f"E\n========================================\n")
    text_field.yview(tk.END)

    power_chord(root_note, note_to_num_key)
    minor_triad(root_note, note_to_num_key)
    major_triad(root_note, note_to_num_key)
    suspended_fourth(root_note, note_to_num_key)
    simple_minor_seventh(root_note, note_to_num_key)
    minor_seventh(root_note, note_to_num_key)
    simple_major_seventh(root_note, note_to_num_key)
    major_seventh(root_note, note_to_num_key)
    dominant_seventh(root_note, note_to_num_key)
    add_nine(root_note, note_to_num_key)


def note_F():
    clear_text()
    note_to_num_key = note_to_num_F
    root_note = 'F'
    text_field.insert("end", f"F\n========================================\n")
    text_field.yview(tk.END)

    power_chord(root_note, note_to_num_key)
    minor_triad(root_note, note_to_num_key)
    major_triad(root_note, note_to_num_key)
    suspended_fourth(root_note, note_to_num_key)
    simple_minor_seventh(root_note, note_to_num_key)
    minor_seventh(root_note, note_to_num_key)
    simple_major_seventh(root_note, note_to_num_key)
    major_seventh(root_note, note_to_num_key)
    dominant_seventh(root_note, note_to_num_key)
    add_nine(root_note, note_to_num_key)


    
def note_Fs():
    clear_text()
    note_to_num_key = note_to_num_Gb
    root_note = 'F#'
    text_field.insert("end", f"F#/Gb\n========================================\n")
    text_field.yview(tk.END)

    power_chord(root_note, note_to_num_key)
    minor_triad(root_note, note_to_num_key)
    major_triad(root_note, note_to_num_key)
    suspended_fourth(root_note, note_to_num_key)
    simple_minor_seventh(root_note, note_to_num_key)
    minor_seventh(root_note, note_to_num_key)
    simple_major_seventh(root_note, note_to_num_key)
    major_seventh(root_note, note_to_num_key)
    dominant_seventh(root_note, note_to_num_key)
    add_nine(root_note, note_to_num_key)


def note_G():
    clear_text()
    note_to_num_key = note_to_num_G
    root_note = 'G'
    text_field.insert("end", f"G\n========================================\n")
    text_field.yview(tk.END)

    power_chord(root_note, note_to_num_key)
    minor_triad(root_note, note_to_num_key)
    major_triad(root_note, note_to_num_key)
    suspended_fourth(root_note, note_to_num_key)
    simple_minor_seventh(root_note, note_to_num_key)
    minor_seventh(root_note, note_to_num_key)
    simple_major_seventh(root_note, note_to_num_key)
    major_seventh(root_note, note_to_num_key)
    dominant_seventh(root_note, note_to_num_key)
    add_nine(root_note, note_to_num_key)



def note_Gs():
    clear_text()
    note_to_num_key = note_to_num_Ab
    root_note = 'G#'
    text_field.insert("end", f"G#/Ab\n========================================\n")
    text_field.yview(tk.END)

    power_chord(root_note, note_to_num_key)
    minor_triad(root_note, note_to_num_key)
    major_triad(root_note, note_to_num_key)
    suspended_fourth(root_note, note_to_num_key)
    simple_minor_seventh(root_note, note_to_num_key)
    minor_seventh(root_note, note_to_num_key)
    simple_major_seventh(root_note, note_to_num_key)
    major_seventh(root_note, note_to_num_key)
    dominant_seventh(root_note, note_to_num_key)
    add_nine(root_note, note_to_num_key)


def update_buttons():
    if var.get() == 1:
        button_A.config(text="A")
        button_Bb.config(text="A#")
        button_B.config(text="B")
        button_C.config(text="C")
        button_Cs.config(text="C#")
        button_D.config(text="D")
        button_Eb.config(text="D#")
        button_E.config(text="E")
        button_F.config(text="F")
        button_Fs.config(text="F#")
        button_G.config(text="G")
        button_Gs.config(text="G#")
    elif var.get() == 2:
        button_A.config(text="A")
        button_Bb.config(text="Bb")
        button_B.config(text="B")
        button_C.config(text="C")
        button_Cs.config(text="Db")
        button_D.config(text="D")
        button_Eb.config(text="Eb")
        button_E.config(text="E")
        button_F.config(text="F")
        button_Fs.config(text="Gb")
        button_G.config(text="G")
        button_Gs.config(text="Ab")


root = tk.Tk()
root.title("LSC Chord Database")
root.geometry("880x660")
root.configure(bg="#111111")

#root note frame
root_note_frame = tk.Frame(root)
root_note_frame.grid(row=0, column=0, padx=8, pady=16, sticky="n")
root_note_frame.configure(bg="#111111", relief="sunken")
root_note_frame.columnconfigure(0, weight=1)
root_note_frame.columnconfigure(1, weight=1)

#note buttons
root_note_label = tk.Label(root_note_frame, text="Root\nNote", bg="#080b19", fg="white")
root_note_label.grid(row=2, column=2, columnspan=2, padx=4, pady=4, sticky="nsew")
button_A = tk.Button(root_note_frame, text="A", command = note_A, bg="#080b19", fg="white")
button_A.grid(row=0, column=3, padx=4, pady=4, sticky="nsew")
button_Bb = tk.Button(root_note_frame, text="A#", command = note_Bb, bg="#080b19", fg="white")
button_Bb.grid(row=1, column=4, padx=4, pady=0, sticky="ne")
button_B = tk.Button(root_note_frame, text="B", command = note_B, bg="#080b19", fg="white")
button_B.grid(row=2, column=5, padx=4, pady=0, sticky="nsew")
button_C = tk.Button(root_note_frame, text="C", command = note_C, bg="#080b19", fg="white")
button_C.grid(row=3, column=5, padx=4, pady=0, sticky="se")
button_Cs = tk.Button(root_note_frame, text="C#", command = note_Cs, bg="#080b19", fg="white")
button_Cs.grid(row=4, column=4, padx=4, pady=0, sticky="nsew")
button_D = tk.Button(root_note_frame, text="D", command = note_D, bg="#080b19", fg="white")
button_D.grid(row=5, column=3, padx=4, pady=4, sticky="nsew")
button_Eb = tk.Button(root_note_frame, text="D#", command = note_Eb, bg="#080b19", fg="white")
button_Eb.grid(row=5, column=2, padx=4, pady=4, sticky="nsew")
button_E = tk.Button(root_note_frame, text="E", command = note_E, bg="#080b19", fg="white")
button_E.grid(row=4, column=1, padx=4, pady=0, sticky="sw")
button_F = tk.Button(root_note_frame, text="F", command = note_F, bg="#080b19", fg="white")
button_F.grid(row=3, column=0, padx=4, pady=0, sticky="nsew")
button_Fs = tk.Button(root_note_frame, text="F#", command = note_Fs, bg="#080b19", fg="white")
button_Fs.grid(row=2, column=0, padx=4, pady=0, sticky="nsew")
button_G = tk.Button(root_note_frame, text="G", command = note_G, bg="#080b19", fg="white")
button_G.grid(row=1, column=1, padx=4, pady=0, sticky="nw")
button_Gs = tk.Button(root_note_frame, text="G#", command = note_Gs, bg="#080b19", fg="white")
button_Gs.grid(row=0, column=2, padx=4, pady=4, sticky="nsew")


#radio buttons
radio_button_frame = tk.Frame(root, bg="#111111", relief="sunken")
radio_button_frame.grid(row=1, column=0, padx=8, pady=16, sticky="n")
var = tk.IntVar(value=1)
radio_button1 = tk.Radiobutton(radio_button_frame, text="Root Up", bg="cyan", fg="black", relief="raised", variable=var, value=1, command=update_buttons)
radio_button2 = tk.Radiobutton(radio_button_frame, text="Root Down", bg="magenta", fg="black", relief="raised", variable=var, value=2, command=update_buttons)
radio_button1.grid(row=6, column=0, padx=4, pady=4, sticky="nsew")
radio_button2.grid(row=6, column=1, padx=4, pady=4, sticky="nsew")


#entry frame
entry_frame = tk.Frame(root, bg="#222222", relief="sunken")
entry_frame.grid(row=0, column=0, columnspan=1, padx=8, pady=16, sticky="s")
entry_frame.columnconfigure(0, weight=1)
entry_frame.columnconfigure(1, weight=1)
entry_frame.columnconfigure(2, weight=1)

entry_label = tk.Label(entry_frame, text="Enter pitch as # (float accepted):", bg="#131938", fg="white", relief="sunken")
entry_label.grid(row=6, column=0, padx=4, pady=4, sticky="w")
button_submit = tk.Button(entry_frame, text="Enter", command = submit, bg="#080b19", fg="white")
button_submit.grid(row=7, column=1, padx=4, pady=4, sticky="e")
entry_field = tk.Entry(entry_frame, width=30)
entry_field.insert(0, "440.0")  # Set initial text
entry_field.grid(row=7, column=0, padx=4, pady=4, sticky="w")

button_clear = tk.Button(entry_frame, text="Clear (Esc)", command = clear_text, bg="#080b19", fg="white")
button_clear.grid(row=7, column=2, padx=4, pady=4, sticky="e")

#text frame
text_frame = tk.Frame(root, bg="magenta")
text_frame.grid(row=0, column=1, padx=4, pady=4, sticky="nw")
text_field = tk.Text(text_frame, width=60, height=35)
text_field.grid(row=0, column=0, padx=4, pady=4, sticky="nw")
text_field.configure(bg="#000000", fg="#00ffed", highlightbackground="#00ffed", highlightcolor="#00ffed", highlightthickness=2)
scrollbar = tk.Scrollbar(text_frame, command=text_field.yview, troughcolor="#00ff00", relief="raised")
scrollbar.grid(row=0, column=1, padx=0, pady=0, sticky="ns")
text_field.config(yscrollcommand=scrollbar.set)
text_frame.columnconfigure(0, weight=1)
text_frame.columnconfigure(1, weight=1)


root.bind("<Return>", submit)
root.bind("<Escape>", clear_text)


root.mainloop()
