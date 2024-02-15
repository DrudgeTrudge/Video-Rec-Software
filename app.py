import tkinter as tk
from tkinter import ttk
from tabs.game_tab import GameTab
from tabs.play_by_play_tab import PlayByPlayTab
# Import other tabs as needed

class NFLStatsApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.title("NFL Stats Program")
        self.root.geometry("1000x700")

        tab_control = ttk.Notebook(self.root)
        GameTab(tab_control)
        PlayByPlayTab(tab_control)
        # Initialize other tabs as needed

        tab_control.pack(expand=True, fill="both")

data_collector = DataCollector(app_reference=self)
game_info = data_collector.collect_game_info()
player_stats = data_collector.collect_player_stats()
play_by_play_data = data_collector.collect_play_by_play_data()
