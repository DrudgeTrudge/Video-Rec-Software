class DataCollector:
    def __init__(self, app_reference):
        """
        Initializes the data collector with a reference to the main application.
        
        Parameters:
        - app_reference: A reference to the main application class (NFLStatsApp).
        """
        self.app = app_reference

    def collect_game_info(self):
        """
        Collects game information from the UI.
        
        Returns:
        A dictionary containing the game information.
        """
        game_info = {}
        for label, entry_widget in self.app.game_data.items():
            game_info[label] = entry_widget.get()
        return game_info

    def collect_player_stats(self):
        """
        Collects player statistics from the UI.
        
        Returns:
        A list of dictionaries, each representing a player and their stats.
        """
        player_stats = []
        for position, entries in self.app.player_data.items():
            for name_entry, stat_entry in entries:
                if name_entry.get() and stat_entry.get():  # Ensure both fields are filled
                    player_stats.append({
                        "Position": position,
                        "Name": name_entry.get(),
                        "Stat": stat_entry.get()
                    })
        return player_stats

    def collect_play_by_play_data(self):
        """
        Collects play-by-play data from the UI.
        
        Returns:
        A list of dictionaries, each representing a play's details.
        """
        play_by_play_data = []
        # Assuming play_by_play_data is a list of PlayEntry objects or similar structure
        for play_entry in self.app.play_by_play_data:
            play_data = {
                "Description": play_entry.description.get(),
                "Time": play_entry.time.get(),
                # Add more fields as necessary
            }
            play_by_play_data.append(play_data)
        return play_by_play_data
