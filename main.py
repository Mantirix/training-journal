
"""Main program"""

import diary


def main():
    
    filename = "training.txt"

    while True:
        print("\n-------------------------------")
        print("   TRAINING & WRESTLING JOURNAL")
        print("....................................")
        print("Current diary:", filename)
        print()
        print("1. Create a new diary entry")
        print("2. View all diary entries")
        print("3. Search entries by date")
        print("4. Choose or change diary file")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            print("\n--- NEW TRAINING REGIME ENTRY ---")
            date = input("Enter date (YYYY-MM-DD): ")
            notes = input("Enter training notes: ")

            if date and notes:
                diary.save_entry(filename, date, notes)
                print("Entry saved successfully!")
            else:
                print("Date and notes cannot be empty...")

        elif choice == "2":
            print("\n--- ALL TRAINING ENTRIES ---")
            entries = diary.load_entries(filename)

            if entries:
                for entry in entries:
                    print(entry.strip())
                print("Total entries:", len(entries))
            else:
                print("No entries found.")

        elif choice == "3":
            print("\n--- SEARCH BY DATE ---")
            date = input("Enter date (YYYY-MM-DD): ")
            matches = diary.search_entries(filename, date)

            if matches:
                for entry in matches:
                    print(entry.strip())
                print("Total matching entries:", len(matches))
            else:
                print("No entries found for this date.")

        elif choice == "4":
            print("\n--- CHOOSE DIARY FILE ---")
            new_filename = input("Enter diary filename: ")

            if new_filename.endswith(".txt"):
                filename = new_filename
                print("Diary selected:", filename)
            else:
                print("Please enter a .txt filename.")

        elif choice == "5":
            print("\nThank you for using the journal!")
            print("Keep training hard!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
