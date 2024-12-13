import tkinter as tk
from tkinter import messagebox, filedialog
import sounddevice as sd
import wavio
import threading
import time

# Global variables
is_recording = False
recorded_frames = []
sample_rate = 44100  # Sample rate for recording
start_time = 0

def start_recording():
    global is_recording, recorded_frames, start_time
    is_recording = True
    recorded_frames = []
    start_time = time.time()
    record_button.config(state="disabled")
    stop_button.config(state="normal")
    update_timer()  # Start updating the timer
    threading.Thread(target=record_audio).start()

def stop_recording():
    global is_recording
    is_recording = False
    record_button.config(state="normal")
    stop_button.config(state="disabled")

def record_audio():
    global is_recording, recorded_frames
    while is_recording:
        audio_data = sd.rec(int(sample_rate * 0.5), samplerate=sample_rate, channels=2, dtype="int16")
        sd.wait()
        recorded_frames.append(audio_data)

def save_recording():
    global recorded_frames
    if not recorded_frames:
        messagebox.showwarning("Warning", "No recording to save!")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
    if file_path:
        all_frames = recorded_frames
        wavio.write(file_path, all_frames, sample_rate, sampwidth=2)
        messagebox.showinfo("Success", f"Recording saved to {file_path}")

def update_timer():
    if is_recording:
        elapsed_time = int(time.time() - start_time)
        minutes, seconds = divmod(elapsed_time, 60)
        timer_label.config(text=f"Recording Time: {minutes:02}:{seconds:02}")
        timer_label.after(1000, update_timer)

# GUI Setup
root = tk.Tk()
root.title("Simple Voice Recorder")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="🎤 Voice Recorder App", font=("Helvetica", 20, "bold"), fg="#333", bg="#f0f0f0")
title_label.pack(pady=10)

desc_label = tk.Label(
    root,
    text="Simple Easily record, stop, and save your audio files!",
    font=("Helvetica", 12),
    fg="#666",
    bg="#f0f0f0"
)
desc_label.pack(pady=5)

# Timer label
timer_label = tk.Label(root, text="Recording Time: 00:00", font=("Helvetica", 14), fg="#ff4500", bg="#f0f0f0")
timer_label.pack(pady=10)

# Button Frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

# Record Button
record_button = tk.Button(
    button_frame,
    text="Start Recording 🎙️",
    command=start_recording,
    font=("Helvetica", 14),
    bg="#28a745",
    fg="white",
    width=20,
    padx=10
)
record_button.grid(row=0, column=0, padx=10, pady=10)

# Stop Button
stop_button = tk.Button(
    button_frame,
    text="Stop Recording ⏹️",
    command=stop_recording,
    font=("Helvetica", 14),
    bg="#dc3545",
    fg="white",
    width=20,
    padx=10,
    state="disabled"
)
stop_button.grid(row=0, column=1, padx=10, pady=10)

# Save Button
save_button = tk.Button(
    root,
    text="Save Recording 💾",
    command=save_recording,
    font=("Helvetica", 14),
    bg="#007bff",
    fg="white",
    width=30
)
save_button.pack(pady=20)

footer = tk.Label(root, text="Developed by Hassan Ahmed", bg="#f0f0f0", fg="#999", font=("Helvetica", 10))
footer.pack(side="bottom", pady=10)

root.mainloop()
