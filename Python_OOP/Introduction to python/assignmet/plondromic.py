import pyautogui

# Function to draw a pyramid


def draw_pyramid(height):
    # Calculate the width of the base of the pyramid
    base_width = 2 * height - 1

    for i in range(1, height + 1):
        # Calculate the number of '#' characters to print on this row
        num_chars = 2 * i - 1

        # Calculate the number of spaces before the '#' characters
        num_spaces = (base_width - num_chars) // 2

        # Create the string to print on this row
        row_str = ' ' * num_spaces + '#' * num_chars + '\n'

        # Print the row using PyAutoGUI
        pyautogui.typewrite(row_str)


# Ask the user for the height of the pyramid
try:
    height = int(input("Enter the height of the pyramid: "))
except ValueError:
    print("Please enter a valid number.")
else:
    # Call the draw_pyramid function
    draw_pyramid(height)
