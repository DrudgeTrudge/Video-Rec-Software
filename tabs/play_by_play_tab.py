from tkinter import ttk, Frame, Button, Entry
from widgets.placeholder_entry import PlaceholderEntry

class PlayByPlayTab:
    def __init__(self, tab_control):
        self.tab = ttk.Frame(tab_control)
        tab_control.add(self.tab, text="Play-by-Play")
        self.setup_tab()

    def setup_tab(self):
        # Setup container for play entries
        self.play_container = Frame(self.tab)
        self.play_container.pack(fill='both', expand=True)
        
        # Add initial play entry
        self.add_play_entry()

        # Button to add more play entries
        self.add_more_button = Button(self.tab, text="Add Another Play", command=self.add_play_entry)
        self.add_more_button.pack(side='bottom', pady=10)

    def add_play_entry(self):
        # Frame for a single play entry
        play_frame = Frame(self.play_container)
        play_frame.pack(pady=5, padx=10, fill='x')
        
        # Play Description Entry
        play_description = PlaceholderEntry(play_frame, placeholder="Enter play description", width=50)
        play_description.pack(side="left", padx=5)
        
        # Time of Play Entry
        play_time = PlaceholderEntry(play_frame, placeholder="Time (e.g., Q1 12:34)", width=20)
        play_time.pack(side="left", padx=5)

        # Optionally, add more fields like player involved, result, etc.
from utils.utils import validate_time_format, display_messagebox

# Then, within your class or functions, you can use these utilities:
if not validate_time_format(time_str):
    display_messagebox("Invalid Time Format", "Please enter the time in 'Q1 12:34' format.", "warning")

