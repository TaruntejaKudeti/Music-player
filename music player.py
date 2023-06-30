import os
import pygame
import tkinter as tk
import random
from tkinter import filedialog
from PIL import ImageTk, Image
from pygame import mixer_music

# Initialize Pygame mixer
pygame.mixer.init()

# Create the GUI window
root = tk.Tk()
root.title("Music Player by Sravanth")
root.configure(bg="black")

# Set the window size
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# button size
button_width = 200
button_height = 200

# Create a frame to hold the listbox and buttons
frame = tk.Frame(root, bg="black", width=window_width)
frame.pack(side="top", fill="x")
track_label = tk.Label(frame, text="🎶 Music Player 🎶", font=("Comic Sans MS", 50, "bold"), bg="black", fg="white")
track_label.pack()

# Create the listbox
listbox = tk.Listbox(frame, bg="black", fg="white", width=50, height=10)
listbox.pack(side="bottom", padx=20, pady=20)

# Create the track label
track_label = tk.Label(root, text="", font=("Helvetica", 20), fg='white', bg="black")
track_label.pack()

# Load button images
play_img = Image.open("D:/music_player/images/play.png")
play_img = play_img.resize((button_width, button_height), Image.ANTIALIAS)
play_img = ImageTk.PhotoImage(play_img)

pause_img = Image.open("D:/music_player/images/stop.png")
pause_img = pause_img.resize((button_width, button_height), Image.ANTIALIAS)
pause_img = ImageTk.PhotoImage(pause_img)

next_img = Image.open("D:/music_player/images/next.png")
next_img = next_img.resize((button_width, button_height), Image.ANTIALIAS)
next_img = ImageTk.PhotoImage(next_img)

prev_img  = Image.open("D:/music_player/images/prev.png")
prev_img = prev_img .resize((button_width, button_height), Image.ANTIALIAS)
prev_img  = ImageTk.PhotoImage(prev_img )

add_img = Image.open("D:/music_player/images/add.png")
add_img = add_img.resize((button_width, button_height), Image.ANTIALIAS)
add_img = ImageTk.PhotoImage(add_img)

shuffle_img = Image.open("D:/music_player/images/shuffle.png")
shuffle_img = shuffle_img.resize((button_width, button_height), Image.ANTIALIAS)
shuffle_img = ImageTk.PhotoImage(shuffle_img)

# Create the play, pause, next, previous, and add buttons
play_button = tk.Button(root, image=play_img, command=lambda: play(), width=button_width, height=button_height, bg="black")
pause_button = tk.Button(root, image=pause_img, command=lambda: pause(), width=button_width, height=button_height, bg="black")
next_button = tk.Button(root, image=next_img, command=lambda: play_next(), width=button_width, height=button_height, bg="black")
prev_button = tk.Button(root, image=prev_img, command=lambda: play_prev(), width=button_width, height=button_height, bg="black")
add_button = tk.Button(root, image=add_img, command=lambda: add_music(), width=button_width, height=button_height, bg="black")
shuffle_button = tk.Button(root, image=shuffle_img, command=lambda: shuffle_music(), width=button_width, height=button_height, bg="black")

# Add the buttons to the window
shuffle_button.pack(side="left")
prev_button.pack(side="left")
play_button.pack(side="left")
pause_button.pack(side="left")
next_button.pack(side="left")
add_button.pack(side="left")

# Define helper functions for playing next and previous tracks
current_track = 0
music_files = []

def play():
    global current_track
    current_track = (current_track ) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()
    track_label.config(text=os.path.basename(music_files[current_track]))
        
def pause():
    global paused_position
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        paused_position = pygame.mixer.music.get_pos()
        
def play_next():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()
    track_label.config(text=os.path.basename(music_files[current_track]))

def play_prev():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()
    track_label.config(text=os.path.basename(music_files[current_track]))
    
def add_music():
    global music_files
    filetypes = (("MP3 files", "*.mp3"), ("WAV files", "*.wav"))
    new_files = filedialog.askopenfilenames(initialdir=".", title="Select Music Files", filetypes=filetypes)
    if len(new_files) > 0:
        music_files += list(new_files)
        # Update the listbox with the new files
        for file in new_files:
            listbox.insert(tk.END, os.path.basename(file))
        
def shuffle_music():
    global current_track, music_files
    random.shuffle(music_files)
    current_track = 0
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()
    track_label.config(text=os.path.basename(music_files[current_track]))

# Start playing the first track if any music files are loaded
if len(music_files) > 0:
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()
    track_label.config(text=os.path.basename(music_files[current_track]))
    # Update the listbox with the loaded files
    for file in music_files:
        listbox.insert(tk.END, os.path.basename(file))

# Run the GUI main loop
root.mainloop()