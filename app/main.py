import tkinter as tk
from tkinter import filedialog
import os

class Croissant: 
    def __init__(self, root): 
        self.root=root 
        self.root.title ("I love you couter") 
        self.root.geometry ("800x600")

        self.count
        self.timer 
        self.heart_color ="#FFD1DC" 
        self.dark_color = "#F8B2C1"
        self.is_dark = False
        self.bg_photo = None

        self.canvas = tk.Canvas(root, highlightthickness=0, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.counter_label = tk.Label(self.canvas, text="0", font=("Arial", 48, "bold"), bg="white", fg="#F8B2C1")
        self.counter_window = self.canvas.create_window(0,0, window = self.counter_label)

        self.heart_canvas = tk.Canvas(self.canvas, width= 200, height= 200, bg = "white", highlightthickness=0)
        self.heart_window = self.canvas.create_window(0,0, window=self.heart_canvas)

        self.heart = self.heart_canvas.create_oval(50, 80, 150, 180, fill = self.heart_color, outline="")
        self.heart_text=""
        self.heart_canvas.create_text(100, 130, text="", font=("Arial", 16, "bold"), fill="white")

        menubar = tk.Menu(root)
        root.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Set Background", command=self.set_background)
        file_menu.add_command(label="Set Background Color", command=self.set_bg_color)
        file_menu.add_command(label="Fullscreen = <F11>", command=self.toggle_fullscreen)
        
        self.heart_canvas.bind("<Button-1>", self.on_heart_click)
        self.root.bind("<F11>", lambda e: self.toggle_fullscreen())
        self.root.bind("<Configure>", self.on_resize)
        self.on_resize()

        def set_background(self):
            path = filedialog.askopenfilename(filetypes=[("PNG Files","*.png")])
            if path:
                try: 
                    self.bg_photo=tk.PhotoImage(file=path)
                    self.canvas.delete("bg")
                    self.canvas.create_image(0,0,image=self.bg_photo, anchore=tk.NW, tags="bg")
                    self.canvas.tag_lower("bg")
                except:
                    print("Error Loading This Pudding")
            
        def set_bg_color(self):
            from tkinter import colorchooser
            color = colorchooser.askcolor(title="Choose Wisely")
            if color[1]: 
                self.canvas.config(bg=color[1])

        def on_resize(self, event=none): 
            w=self.canvas.winfo_width()
            h=self.canvas.winfo_height()
            if w>1 and h>1: 
                self.canvas.cords(self.counter_window,w//2, h//4)
                self.canvas.cords(self.heart_window,w//2, h//2)
                

                

        
            
                





         
