# Name: Damitrious Rivera
# Date: 10/02/2025
# Assignment: Module-4 - Sitka High/Low Menu
#
# Purpose: Extend the original sitka_highs.py program to add a simple menu
#          that lets the user view either daily HIGH temperatures or daily LOW
#          temperatures from the Sitka 2018 dataset, or EXIT. The program loops
#          until the user chooses to exit, and displays an exit message.
#
# Changes made (relative to original sitka_highs.py):
#   1) Loaded BOTH high (TMAX) and low (TMIN) temps from the CSV at startup.
#   2) Added a menu with options: 'highs', 'lows', and 'exit'.
#   3) Plotted highs in red (as before) and lows in BLUE (per assignment).
#   4) Loop continues to prompt until the user types 'exit' (case-insensitive).
#   5) Added an exit message and optional sys.exit() for clarity.
#
# Notes:
#   - CSV columns (Python Crash Course dataset):
#       DATE at index 2 (YYYY-MM-DD), TMAX at index 5, TMIN at index 6.
#   - Requires matplotlib. If not installed, run: pip install matplotlib
#
# Usage:
#   Run the script, then type one of: highs | lows | exit
#   Example:
#     > python sitka_high_low_DR.py
#     Enter choice [highs | lows | exit]: lows
#     (blue graph of lows appears)
#     Enter choice [highs | lows | exit]: exit
#     Exiting program. Goodbye!
#
import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt
FILENAME = 'sitka_weather_2018_simple.csv'

def load_data(filename):
    """Load dates, highs (TMAX), and lows (TMIN) from CSV."""
    dates, highs, lows = [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)  # skip header
        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                high = int(row[5])
                low = int(row[6])
            except (ValueError, IndexError):
                # Skip rows with missing or malformed data
                continue
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    return dates, highs, lows

def plot_series(dates, values, title, ylabel, color):
    """Plot a date-series with basic formatting."""
    fig, ax = plt.subplots()
    ax.plot(dates, values, c=color)
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel(ylabel, fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def main():
    dates, highs, lows = load_data(FILENAME)

    print("""\nSitka Weather Viewer (Module-4)
--------------------------------
Type one of the following options and press Enter:
  highs  - View daily HIGH temperatures (red)
  lows   - View daily LOW temperatures (blue)
  exit   - Exit the program
""")

    while True:
        choice = input("Enter choice [highs | lows | exit]: ").strip().lower()
        if choice == 'highs':
            plot_series(dates, highs, "Daily high temperatures - 2018", "Temperature (F)", color='red')
        elif choice == 'lows':
            # Requirement: lows should be plotted in BLUE
            plot_series(dates, lows, "Daily low temperatures - 2018", "Temperature (F)", color='blue')
        elif choice == 'exit':
            print("Exiting program. Goodbye!")
            # Using sys.exit for clarity; break would also suffice
            sys.exit(0)
        else:
            print("Unrecognized option. Please type: highs, lows, or exit.")

if __name__ == '__main__':
    main()
