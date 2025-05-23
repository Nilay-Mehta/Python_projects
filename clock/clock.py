import tkinter as tk
from datetime import datetime

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.configure(bg="black")
        self.root.geometry("1000x400")
        self.root.minsize(500, 200)

        self.is_24_hour = True
        self.fullscreen = False

        # Bind keys
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.exit_fullscreen)

        # Fonts - simulate 7-segment display
        try:
            self.font_main = ("DS-Digital", 160, "bold")
            self.font_sec = ("DS-Digital", 50, "bold")
            self.font_ampm = ("DS-Digital", 40, "bold")
            self.button_font = ("DS-Digital", 20, "bold")
        except:
            self.font_main = ("Courier", 160, "bold")
            self.font_sec = ("Courier", 50, "bold")
            self.font_ampm = ("Courier", 40, "bold")
            self.button_font = ("Courier", 20, "bold")

        # Main time frame
        self.time_frame = tk.Frame(self.root, bg="black")
        self.time_frame.pack(expand=True)

        # Hour and Minute label
        self.time_label = tk.Label(
            self.time_frame, font=self.font_main, fg="white", bg="black"
        )
        self.time_label.pack(side="left")

        # AM/PM and Seconds o top of each othr
        self.right_frame = tk.Frame(self.time_frame, bg="black")
        self.right_frame.pack(side="left", anchor="n", pady=40)

        self.ampm_label = tk.Label(
            self.right_frame, font=self.font_ampm, fg="white", bg="black"
        )
        self.ampm_label.pack(side="top", anchor="w", pady=(0, 5))

        self.sec_label = tk.Label(
            self.right_frame, font=self.font_sec, fg="white", bg="black"
        )
        self.sec_label.pack(side="top", anchor="w")

        # Format toggle button
        self.toggle_button = tk.Button(
            self.root,
            text="12 Hour" if self.is_24_hour else "24 Hour",
            command=self.toggle_format,
            font=self.button_font,
            bg="#222", fg="white",
            activebackground="#444",
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
        )
        self.toggle_button.pack(pady=20)

        self.toggle_button.bind("<Enter>", lambda e: self.toggle_button.config(bg="#333"))
        self.toggle_button.bind("<Leave>", lambda e: self.toggle_button.config(bg="#222"))

        self.update_time()

    def toggle_format(self):
        self.is_24_hour = not self.is_24_hour
        self.toggle_button.config(text="12 Hour" if self.is_24_hour else "24 Hour")

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)

    def exit_fullscreen(self, event=None):
        self.fullscreen = False
        self.root.attributes("-fullscreen", False)

    def update_time(self):
        now = datetime.now()

        if self.is_24_hour:
            hour_min = now.strftime("%H:%M")
            am_pm = ""
        else:
            hour_min = now.strftime("%I:%M")
            am_pm = now.strftime("%p")

        seconds = now.strftime("%S")

        self.time_label.config(text=hour_min)
        self.ampm_label.config(text=am_pm)
        self.sec_label.config(text=seconds)

        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalClock(root)
    root.mainloop()
