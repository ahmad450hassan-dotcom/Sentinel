
import tkinter as tk
from characters import fighters
import os

root = tk.Tk()
root.title("Malakand Rumble - 25 Fighters")
root.geometry("1000x700")

# Background Image Load Karo
bg_path = "assets/WhatsApp Image 2026-10-06 at 5.52.39 AM.jpg"
# Check if file exists
if not os.path.exists(bg_path):
    # Try short name if spaces issue
    for f in os.listdir("assets"):
        if f.lower().endswith(('.jpg','.png','.jpeg')):
            bg_path = os.path.join("assets", f)
            break

try:
    from PIL import Image, ImageTk
    bg_image = Image.open(bg_path)
    bg_image = bg_image.resize((1000, 700))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_photo_ref = bg_photo # Keep reference
except:
    # Agar PIL nahi hai to dark background
    root.configure(bg="#141428")
    bg_label = tk.Frame(root, bg="#141428")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title on top of background
title = tk.Label(root, text="MALAKAND RUMBLE - 25 FIGHTERS BASE", 
                 font=("Arial", 20, "bold"), bg="black", fg="#FFD700")
title.pack(pady=15)

# Fighters Frame (transparent black)
frame = tk.Frame(root, bg="black")
frame.pack(padx=20, pady=10)

row = 0
col = 0
for key, f in fighters.items():
    color = "#00FF00" if f['name'] == "MALIK" else "white"
    text = f"{f['name']} | {f['country']} | P:{f['power']}"
    label = tk.Label(frame, text=text, font=("Arial", 11, "bold"), 
                     bg="black", fg=color, width=28, anchor="w")
    label.grid(row=row, column=col, padx=10, pady=6, sticky="w")
    row += 1
    if row >= 9:
        row = 0
        col += 1

hero_box = tk.Label(root, text="SELECTED HERO: MALIK - PAKISTAN - LV 20 - READY TO RUMBLE!", 
                    font=("Arial", 13, "bold"), bg="#FFD700", fg="black", pady=8)
hero_box.pack(side="bottom", fill="x", padx=0, pady=0)

root.mainloop()