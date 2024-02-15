import tkinter as tk
from app import NFLStatsApp

def main():
    root = tk.Tk()
    app = NFLStatsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

    from tabs.game_tab import GameTab

class NFLStatsApp:
    def __init__(self, root):
        # Initialize the UI, including the tab control
        tab_control = ttk.Notebook(root)
        GameTab(tab_control)  # Add the game information tab
        # Add other tabs similarly
        tab_control.pack(expand=True, fill="both")
