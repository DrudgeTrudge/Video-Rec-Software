from tkinter import ttk
from widgets.placeholder_entry import PlaceholderEntry

class GameTab:
    def __init__(self, tab_control):
        # Initialize a new tab for game information
        self.tab = ttk.Frame(tab_control)
        tab_control.add(self.tab, text="Game Info")
        self.setup_tab()

    def setup_tab(self):
        # Set up the UI components for the game information tab
        
        # Game ID
        ttk.Label(self.tab, text="Game ID:").pack(pady=(10, 0))
        self.game_id_entry = PlaceholderEntry(self.tab, placeholder="Enter Game ID", width=30)
        self.game_id_entry.pack(pady=(0, 10))
        
        # Weather
        ttk.Label(self.tab, text="Weather:").pack(pady=(10, 0))
        self.weather_entry = PlaceholderEntry(self.tab, placeholder="Enter Weather Condition", width=30)
        self.weather_entry.pack(pady=(0, 10))
        
        # Temperature
        ttk.Label(self.tab, text="Temperature:").pack(pady=(10, 0))
        self.temperature_entry = PlaceholderEntry(self.tab, placeholder="Enter Temperature (°F)", width=30)
        self.temperature_entry.pack(pady=(0, 10))
