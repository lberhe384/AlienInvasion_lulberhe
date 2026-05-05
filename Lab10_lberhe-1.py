"""
Program Name: Deal Cards
Author: Lewam Berhe
Purpose: Lab 10 Word Count
Starter Code: None
Date: March 31, 2026
"""
from pathlib import Path
import string

class WordAnalyzer:
    def __init__(self, filepath):
        self._filepath = Path(filepath)
        self._frequencies = {}
    def process_file(self):
        """Reads the file and counts word frequencies."""
        try:
            if not self._filepath.exists():
                print(f"Error: {self._filepath} does not exist!")
                return False

            with self._filepath.open("r", encoding="utf-8") as file:
                translator = str.maketrans('', '', string.punctuation)
                
                for line in file:
                    line = line.translate(translator).lower()
                    words = line.split()
                    
                    for word in words:
                        if word in self._frequencies:
                            self._frequencies[word] += 1
                        else:
                            self._frequencies[word] = 1
            return True
        except FileNotFoundError:
            print("File not found.")
            return False
    def print_report(self):
        """Prints words in alphabetical order with counts."""
        for word in sorted(self._frequencies):
            print(f"{word:<10} :: {self._frequencies[word]}")
def main():
    files = {
        "1": Path("princess_mars.txt"),
        "2": Path("tarzan.txt"),
        "3": Path("treasure_island.txt"),
        "4": Path("monte_cristo.txt")
    }
    names = {
        "1": "Princess Mars",
        "2": "Tarzan",
        "3": "Treasure Island",
        "4": "Monte Cristo"
    }
    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        for key in files:
            print(f"{key}. {names[key]}")
        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        elif choice in files:
            print(f"\nProcessing '{files[choice].name}'...\n")
            analyzer = WordAnalyzer(files[choice])
            if analyzer.process_file():
                analyzer.print_report()
            input("\nPress Enter to return to the menu...")
        else:
            print("\nInvalid choice. Please select from 1-5.")
            input("Press Enter to continue...")
