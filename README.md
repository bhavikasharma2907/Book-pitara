# Book-pitara
# Book Pitara

A simple Python command-line application that introduces users to a curated book library. Users can select from four recommended books, read short descriptions, and choose whether to continue browsing or exit.

---

## Features

- Interactive menu for book selection
- Four books to choose from:
  - The Diary of a Young Girl
  - Atomic Habits
  - Attention
  - Psychology of Humans
- Book descriptions displayed after selection
- Option to continue browsing books or exit
- User-friendly input validation and error messages

---

## How to Use

1. Save the code below in a file named `book_pitara.py`.
2. Run the script:

    ```
    python book_pitara.py
    ```

3. Follow the prompts to select books and navigate the menu.

---

## Example Output

Welcome to my Book Pitara
Press 1 for Book 1: The Diary of a Young Girl
Press 2 for Book 2: Atomic Habits
Press 3 for Book 3: Attention
Press 4 for Book 4: Psychology of Humans
Enter book number to continue: 1
Book 1: The Diary of a Young Girl, commonly referred to as The Diary of Anne Frank, ...
Press 1 for exit
Press 2 to continue
Enter your choice (1 = Exit, 2 = Continue): 2
Returning to books menu.

text

---

## Source Code

def run():
while True:
print("\nPress 1 for exit")
print("Press 2 to continue")
try:
choice = int(input("Enter your choice (1 = Exit, 2 = Continue): "))
if choice == 1:
print("Thank you for visiting Book Pitara. Goodbye!")
return False # Signal to exit
elif choice == 2:
print("Returning to books menu.\n")
return True # Signal to continue
else:
print("Invalid choice. Please enter 1 or 2.")
except ValueError:
print("Invalid input. Please enter a number.")

def book():
while True:
print("\nWelcome to my Book Pitara")
print("Press 1 for Book 1: The Diary of a Young Girl")
print("Press 2 for Book 2: Atomic Habits")
print("Press 3 for Book 3: Attention")
print("Press 4 for Book 4: Psychology of Humans")
try:
b = int(input("Enter book number to continue: "))
if b == 1:
print("Book 1: The Diary of a Young Girl, commonly referred to as The Diary of Anne Frank, is a collection of writings from Anne Frank's diary while she was in hiding during the Nazi occupation of the Netherlands in World War II.")
elif b == 2:
print("Book 2: Atomic Habits is a self-help book by James Clear that explores strategies for building good habits, breaking bad ones, and mastering the tiny behaviors that lead to remarkable results.")
elif b == 3:
print("Book 3: Attention discusses the concentration of awareness on some phenomena to the exclusion of others, involving selective focus and cognitive processing.")
elif b == 4:
print("Book 4: Psychology of Humans is the scientific study of behavior and mind, including conscious and unconscious phenomena, as well as thoughts and feelings.")
else:
print("Book not found. Please try again.\n")
continue
if not run():
break # Exit loop if user chooses to exit
except ValueError:
print("Invalid input. Please enter a number.")

def main():
book()

if name == "main":
main()
