import pandas as pd

class ExcelExporter:
    def __init__(self, filepath="NFL_Stats.xlsx"):
        """
        Initializes the exporter with a path to save the Excel file.
        
        Parameters:
        - filepath: Path where the Excel file will be saved.
        """
        self.filepath = filepath
        self.writer = pd.ExcelWriter(self.filepath, engine='openpyxl')

    def add_data_to_sheet(self, data, sheet_name="Sheet1"):
        """
        Adds data to a specific sheet within the Excel workbook. If the sheet exists, it will be overwritten.
        
        Parameters:
        - data: A list of dictionaries where each dictionary represents a row in the sheet.
        - sheet_name: Name of the sheet where data will be added.
        """
        df = pd.DataFrame(data)
        df.to_excel(self.writer, sheet_name=sheet_name, index=False)

    def save(self):
        """
        Saves the workbook to the specified filepath.
        """
        self.writer.save()

    def close(self):
        """
        Closes the ExcelWriter object, releasing the Excel file.
        """
        self.writer.close()
# Assuming game_data and play_by_play_data are lists of dictionaries
game_data = [{'Game ID': '001', 'Weather': 'Sunny', 'Temperature': '75°F'}]
play_by_play_data = [{'Play Description': 'Touchdown', 'Time': 'Q1 12:34'}, {'Play Description': 'Interception', 'Time': 'Q1 10:21'}]

exporter = ExcelExporter(filepath="NFL_Stats.xlsx")
exporter.add_data_to_sheet(game_data, sheet_name="Game Info")
exporter.add_data_to_sheet(play_by_play_data, sheet_name="Play-by-Play")
exporter.save()
exporter.close()
