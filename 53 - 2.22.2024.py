''' Problem Statement: Develop a timer function that counts down from a given time to zero,
displaying the time remaining in minutes and seconds. This timer should be able to start,
pause, resume, and reset, providing precise control over its operation.

Example:

Start with a countdown from 5 minutes.

Display updates every second in the format: mm:ss.

Include functionalities to pause, resume, and reset the countdown.

Guidelines:

Choose any programming language to implement your timer.

Focus on creating a user-friendly and accurate timer mechanism.

Bonus Challenge: Extend your timer with additional features, such as setting
custom countdown durations or adding alarm sounds for when the timer reaches zero. '''

# using tkinter here as it's the only GUI I've worked with

import tkinter as tk
import threading
import time

# create class for the timer
class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer") # title of GUI window
        self.root.geometry("300x200") # size of GUI window
        
        self.minutes_var = tk.StringVar()
        self.minutes_var.set("5")  # set 5 mins as default countdown time (as given in example)
        
        self.timer_label = tk.Label(root, text="", font=("Helvetica", 20)) # text properties
        self.timer_label.pack(pady=20)
        
        time_frame = tk.Frame(root)
        time_frame.pack()
        
        tk.Label(time_frame, text="Countdown Time (min):").pack(side=tk.LEFT, padx=10)
        time_entry = tk.Entry(time_frame, textvariable=self.minutes_var, width=5)
        time_entry.pack(side=tk.LEFT, padx=5)
        
        separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
        separator.pack(fill=tk.X, padx=5, pady=5)
        
        control_frame = tk.Frame(root)
        control_frame.pack()
        
        self.start_button = tk.Button(control_frame, text="Start", command=self.start_timer) # start button
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.pause_button = tk.Button(control_frame, text="Pause", command=self.pause_timer) # pause button
        self.pause_button.pack(side=tk.LEFT, padx=10)
        
        self.resume_button = tk.Button(control_frame, text="Resume", command=self.resume_timer) # resume button
        self.resume_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(control_frame, text="Reset", command=self.reset_timer) # reset button
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        self.remaining_seconds = int(self.minutes_var.get()) * 60
        self.is_running = False
        self.pause_event = threading.Event()
        self.pause_event.set()
    
    # start button function
    def start_timer(self):
        if not self.is_running:
            self.remaining_seconds = int(self.minutes_var.get()) * 60
            self.is_running = True
            self.pause_event.set()
            threading.Thread(target=self._countdown).start()
    
    # pause button function
    def pause_timer(self):
        if self.is_running:
            self.is_running = False
            self.pause_event.clear()
    
    # resume button function
    def resume_timer(self):
        if not self.is_running:
            self.is_running = True
            self.pause_event.set()
    
    # reset button function
    def reset_timer(self):
        self.is_running = False
        self.remaining_seconds = int(self.minutes_var.get()) * 60
        self.pause_event.set()
        self.timer_label.config(text="")
    
    # countdown timer function
    def _countdown(self):
        while self.remaining_seconds > 0:
            if self.pause_event.is_set():
                minutes, seconds = divmod(self.remaining_seconds, 60)
                time_str = f"{minutes:02d}:{seconds:02d}" # proper format as given in example
                self.timer_label.config(text=time_str)
                time.sleep(1) # change visual every 1 second
                self.remaining_seconds -= 1 # decrement 1 second
            else:
                time.sleep(0.1)
        self.timer_label.config(text="Time's up!")
        self.is_running = False

# main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()