def format_temperature(temp):
    """
    Formats the temperature to include the Fahrenheit symbol and ensures it's a valid temperature.
    
    Parameters:
    - temp: The temperature value as a string or integer.
    
    Returns:
    - A formatted string with the temperature followed by °F or an error message if the input is invalid.
    """
    try:
        temp = int(temp)  # Convert to integer to check validity
        return f"{temp}°F"
    except ValueError:
        return "Invalid temperature"

def validate_time_format(time_str):
    """
    Validates that a time string is in the correct format (e.g., "Q1 12:34").
    
    Parameters:
    - time_str: The time string to validate.
    
    Returns:
    - True if the format is correct; False otherwise.
    """
    import re
    pattern = re.compile(r"^Q[1-4] \d{1,2}:\d{2}$")
    return bool(pattern.match(time_str))

def convert_to_24h_format(time_str):
    """
    Converts a time string from 12-hour format (e.g., "1:00 PM") to 24-hour format (e.g., "13:00").
    
    Parameters:
    - time_str: The time string in 12-hour format.
    
    Returns:
    - The time string in 24-hour format.
    """
    from datetime import datetime
    return datetime.strptime(time_str, "%I:%M %p").strftime("%H:%M")

def display_messagebox(title, message, kind="info"):
    """
    Displays a messagebox with a given title and message.
    
    Parameters:
    - title: The title of the messagebox.
    - message: The message to display.
    - kind: The type of messagebox ("info", "warning", "error").
    """
    from tkinter import messagebox
    if kind == "info":
        messagebox.showinfo(title, message)
    elif kind == "warning":
        messagebox.showwarning(title, message)
    elif kind == "error":
        messagebox.showerror(title, message)
    else:
        messagebox.showinfo(title, message)  # Default to info if kind is not recognized
