import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
import webbrowser
import os
import subprocess
import pyttsx3
import speech_recognition as sr
import qrcode
import cv2
import time

# Function to handle application exit
def on_exit():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        root.destroy()

# Function to open Notepad
def open_notepad():
    subprocess.Popen(["notepad.exe"])

# Function to open Calculator
def open_calculator():
    subprocess.Popen(["calc.exe"])

# Function to open YouTube
def open_youtube():
    song_name = simpledialog.askstring("Open YouTube", "Enter the name of your favorite song:")
    if song_name:
        search_query = song_name.replace("", "+")
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

# Function to assist deaf people
def deaf_people_help():
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    cap = cv2.VideoCapture(0)
    model = HandDetector()
    while True:
        status, photo = cap.read()
        cv2.imshow("pic1", photo)
        if cv2.waitKey(10) == 13:
            break

        hand = model.findHands(photo, draw=False)
        if hand:
            handPhoto = hand[0]
            fingerlist = model.fingersUp(handPhoto)
            if fingerlist == [0, 1, 1, 1, 1]:
                engine.say("namaste")
                engine.runAndWait()
                print("namaste")
                time.sleep(2)
            elif fingerlist == [1, 0, 0, 0, 0]:
                engine.say("Good job")
                engine.runAndWait()
                print("Good job")
                time.sleep(2)
            elif fingerlist == [0, 1, 1, 0, 0]:
                engine.say("Pleasure meeting with you")
                engine.runAndWait()
                print("Pleasure meeting with you")
                time.sleep(2)
            elif fingerlist == [0, 1, 1, 0, 0]:
                engine.say("Perfect")
                engine.runAndWait()
                print("Perfect")
                time.sleep(2)
            elif fingerlist == [1, 1, 0, 0, 1]:
                engine.say("I love Vimal Sir")
                engine.runAndWait()
                print("I love Vimal Sir")
                time.sleep(2)
            elif fingerlist == [0, 0, 0, 0, 0]:
                engine.say("Sorry")
                engine.runAndWait()
                print("Sorry")
                time.sleep(2)
            elif fingerlist == [0, 1, 0, 0, 0]:
                engine.say("Help")
                engine.runAndWait()
                print("Help")
                time.sleep(2)
            else:
                print("dont support")
                time.sleep(2)

    cv2.destroyAllWindows()
    cap.release()

# Function to capture video
def capture_video():
    if messagebox.askyesno("Exit", "Want to Capture?"):
        cap = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter("captured_video.avi", fourcc, 20.0, (640, 480))

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)

            cv2.imshow("Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if cv2.waitKey(5) == 13:
                break

        out.release()
        cv2.destroyAllWindows()
        cap.release()
        messagebox.showinfo("Video Captured", "Video captured and saved as 'captured_video.avi'")

# Function to get weather information (API-related code removed)
def get_weather():
    pass

# Function for voice assistant (speech recognition) - requires a microphone
def voice_assistant():
    engine = pyttsx3.init()
    engine.say("How can I assist you?")
    engine.runAndWait()

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio)
        messagebox.showinfo("Voice Assistant", f"You said: {recognized_text}")
    except sr.UnknownValueError:
        messagebox.showerror("Error", "Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        messagebox.showerror("Error", "Sorry, the speech recognition service is currently unavailable.")

# Function to generate a QR code
def generate_qr_code():
    data = simpledialog.askstring("QR Code Generator", "Enter the text or URL to encode:")
    if data:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qr_code.png")
        img.show()

# Function for your additional feature (API-related code removed)
def langchain():
    pass

# Create the main GUI window
root = tk.Tk()

root.geometry("800x600")
root.configure(bg="#ff99c8")

# Create a title label
title_label = tk.Label(root, text="Menu", font=("Arial", 30, "bold"), bg="seagreen")
title_label.pack(pady=20)

# Create frames for organization
top_frame = tk.Frame(root, bg="seagreen")
top_frame.pack(side=tk.TOP, pady=10)

middle_frame = tk.Frame(root, bg="seagreen")
middle_frame.pack(side=tk.TOP, pady=10)

bottom_frame = tk.Frame(root, bg="seagreen")
bottom_frame.pack(side=tk.TOP, pady=10)

# Create buttons for each feature and place them in the respective frames
top_buttons = [
    ("Open Notepad", open_notepad),
    ("Open Calculator", open_calculator),
    ("Open YouTube", open_youtube)
]

for text, command in top_buttons:
    button = tk.Button(top_frame, text=text, command=command, width=20)
    button.pack(side=tk.LEFT, padx=10)

middle_buttons = [
    ("Deaf People Help", deaf_people_help),
    ("Capture Video", capture_video),
    ("Get Weather Update", get_weather)
]

for text, command in middle_buttons:
    button = tk.Button(middle_frame, text=text, command=command, width=20)
    button.pack(side=tk.LEFT, padx=10)

bottom_buttons = [
    ("Voice Assistant", voice_assistant),
    ("Generate QR Code", generate_qr_code),
    ("Your Additional Feature", langchain)
]

for text, command in bottom_buttons:
    button = tk.Button(bottom_frame, text=text, command=command, width=20)
    button.pack(side=tk.LEFT, padx=10)

# Create an Exit button at the bottom
exit_button = tk.Button(root, text="Exit", command=on_exit, width=20)
exit_button.pack(pady=20)

# Start the GUI main loop
root.mainloop()
