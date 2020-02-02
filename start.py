from pynput.keyboard import Key, Listener
from PIL import Image, ImageTk
import threading
import tkinter as tk
import winsound


threads = {}

def Open():
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
    window = tk.Tk()
    window.title("Windows XP!!!!!!!!!!!!!!!!!!!!!")
    window.geometry("600x400")
    window.configure(background="grey")
    img = ImageTk.PhotoImage(Image.open("xp.jpg"), master=window)
    panel = tk.Label(window, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    window.attributes("-topmost", True)
    window.mainloop()




def on_press(key):
    try:
        KEY = key.char.lower()
        if KEY in["w", "i", "n", "d", "o", "w", "s", "x", "p"]:
            thread_id = len(threads) + 1
            threads[thread_id] = threading.Thread(target=Open)
            threads[thread_id].start()
    except:
        pass
    return True



with Listener(on_press=on_press) as listener:
    listener.join()
