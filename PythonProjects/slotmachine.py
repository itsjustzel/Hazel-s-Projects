import random
# Imports Python’s random module, which is used to randomly select slot symbols

# =========================
# Global constants
# =========================

MAX_LINES = 3
# Maximum number of lines a user is allowed to bet on

MAX_BET = 100
# Maximum bet amount allowed per line

MIN_BET = 1
# Minimum bet amount allowed per line

ROWS = 3
# Number of rows in the slot machine

COLS = 3
# Number of columns in the slot machine

# =========================
# Symbol configuration
# =========================

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
# Dictionary that defines how frequently each symbol appears
# Symbols with lower counts are rarer

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
# Dictionary that defines how much each symbol pays when matched

# =========================
# Checks winnings after a spin
# =========================

def check_winnings(columns, lines, bet, values):
    winnings = 0
    # Stores the total amount of money won

    winning_lines = []
    # Stores which lines resulted in a win

    for line in range(lines):
        # Loops through each line the user has bet on

        symbol = columns[0][line]
        # Takes the symbol from the first column for the current line

        for column in columns:
            # Loops through every column in the slot machine

            symbol_to_check = column[line]
            # Gets the symbol in the current column at the current line

            if symbol != symbol_to_check:
                # If any symbol does not match, the line is not a winning line
                break
        else:
            # This block runs only if the loop did NOT break
            winnings += values[symbol] * bet
            # Adds the winnings based on symbol value and bet amount

            winning_lines.append(line + 1)
            # Stores the winning line number (human-friendly numbering)

    return winnings, winning_lines
    # Returns total winnings and list of winning lines

# =========================
# Generates a slot machine spin
# =========================

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # List that will store symbols based on their frequency

    for symbols, symbol_count in symbols.items():
        # Loops through each symbol and its count

        for _ in range(symbol_count):
            # Repeats based on how frequent the symbol should be
            all_symbols.append(symbols)
            # Adds the symbol to the list

    columns = []
    # Will store all columns of the slot machine

    for _ in range(cols):
        # Generates each column

        column = []
        # Represents a single column

        current_symbols = all_symbols[:]
        # Copies the list so symbols can be removed safely

        for _ in range(rows):
            # Chooses symbols for each row in the column

            value = random.choice(current_symbols)
            # Randomly selects a symbol

            current_symbols.remove(value)
            # Removes chosen symbol to reduce repetition

            column.append(value)
            # Adds symbol to the column

        columns.append(column)
        # Adds completed column to the slot machine

    return columns
    # Returns the generated slot machine columns

# =========================
# Prints the slot machine
# =========================

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        # Loops through each row index

        for i, column in enumerate(columns):
            # Loops through each column with index

            if i != len(columns) - 1:
                # Checks if this is NOT the last column
                print(column[row], end=" | ")
                # Prints symbol followed by a separator
            else:
                print(column[row], end="")
                # Prints last symbol without separator

        print()
        # Moves to the next line after printing a row

# =========================
# Handles user deposit
# =========================

# GOOD COHESION - FUNCTIONAL COHESION
def deposit():
    while True:
        # Keeps asking until valid input is provided

        amount = input("What would you like to deposit? $")
        # Gets user input

        if amount.isdigit():
            # Checks if input contains only digits

            amount = int(amount)
            # Converts input to integer

            if amount > 0:
                # Ensures deposit is positive
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number!")

    return amount
    # Returns the validated deposit amount

# =========================
# Gets number of lines to bet on
# =========================

# BAD COUPLING - COMMON COUPLING
def get_numlines():
    while True:
        lines = input("How many lines do you want to bet on? (1-" + str(MAX_LINES) + ")")
        # Prompts user for number of lines

        if lines.isdigit():
            lines = int(lines)
            # Converts input to integer

            if 1 <= lines <= MAX_LINES:
                # Checks if within allowed range
                break
            else:
                print("Number of lines should be valid")
        else:
            print("Please enter a number!")

    return lines
    # Returns validated number of lines

# =========================
# Gets bet per line
# =========================

# BAD COUPLING - COMMON COUPLING
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        # Prompts user for bet amount

        if amount.isdigit():
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                # Ensures bet is within allowed limits
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number!")

    return amount
    # Returns validated bet amount

# =========================
# Runs one game spin
# =========================

#  GOOD COUPLING - DATA COUPLING
def spin(balance):
    lines = get_numlines()
    # Gets how many lines the user wants to bet on

    while True:
        bet = get_bet()
        # Gets bet per line

        total_bet = bet * lines
        # Calculates total bet amount

        if total_bet > balance:
            # Checks if user has enough balance
            print(f"You do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
    # Displays betting summary

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    # Generates a random slot machine spin

    print_slot_machine(slots)
    # Prints the slot machine to the console

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    # Checks if the spin resulted in any winnings

    print(f"You won ${winnings}.")
    # Displays total winnings

    print(f"You won on lines:", *winning_lines)
    # Displays which lines won

    return winnings - total_bet
    # Returns net profit or loss from the spin

# =========================
# Main program loop
# =========================

def main():
    balance = deposit()
    # Gets initial deposit from the user

    while True:
        print(f"Current balance is ${balance}")
        # Displays current balance

        answer = input("Press enter to play (q to quit).")
        # Asks user whether to continue

        if answer == "q":
            # Exits the loop if user chooses to quit
            break

        balance += spin(balance)
        # Updates balance after a spin

    print(f"You left with ${balance}")
    # Displays final balance when game ends

# Ensures the program runs only when this file is executed directly
if __name__ == "__main__":
    main()
