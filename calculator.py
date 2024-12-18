import customtkinter

root = customtkinter.CTk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)  # Fixed window size
root.configure(bg="#F4F4F4")  # Subtle grey background

# Display widget for showing numbers and results
display = customtkinter.CTkEntry(root, font=('Roboto', 20), justify='right', width=280)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to handle button clicks
def on_button_click(value):
    current_text = display.get()
    display.delete(0, "end")
    display.insert("end", current_text + value)

# Function to clear the display
def clear_display():
    display.delete(0, "end")

# Function to delete the last character
def delete_last_character():
    current_text = display.get()
    display.delete(0, "end")
    display.insert("end", current_text[:-1])

# Function to evaluate the expression
def calculate_result():
    try:
        result = eval(display.get())
        display.delete(0, "end")
        display.insert("end", str(result))
    except Exception:
        display.delete(0, "end")
        display.insert("end", "Error")

def create_button(text, row, col, command, color="#E0E0E0", colspan=1):
    button = customtkinter.CTkButton(
        root, 
        text=text, 
        font=('Roboto', 20), 
        text_color='black',
        fg_color=color, 
        hover_color="#D5D5D5",
        corner_radius=8, 
        width=60 * colspan, 
        height=60, 
        command=command
    )
    button.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)

# Define button layout with their properties
button_definitions = [
    ('7', 1, 0, lambda: on_button_click('7'), '#E0E0E0', 1), 
    ('8', 1, 1, lambda: on_button_click('8'), '#E0E0E0', 1), 
    ('9', 1, 2, lambda: on_button_click('9'), '#E0E0E0', 1), 
    ('DEL', 1, 3, delete_last_character, '#FF9F9F', 1),
    ('4', 2, 0, lambda: on_button_click('4'), '#E0E0E0', 1), 
    ('5', 2, 1, lambda: on_button_click('5'), '#E0E0E0', 1), 
    ('6', 2, 2, lambda: on_button_click('6'), '#E0E0E0', 1), 
    ('-', 2, 3, lambda: on_button_click('-'), '#E0E0E0', 1),
    ('1', 3, 0, lambda: on_button_click('1'), '#E0E0E0', 1), 
    ('2', 3, 1, lambda: on_button_click('2'), '#E0E0E0', 1), 
    ('3', 3, 2, lambda: on_button_click('3'), '#E0E0E0', 1), 
    ('+', 3, 3, lambda: on_button_click('+'), '#E0E0E0', 1),
    ('0', 4, 0, lambda: on_button_click('0'), '#E0E0E0', 1), 
    ('.', 4, 1, lambda: on_button_click('.'), '#E0E0E0', 1), 
    ('/', 4, 2, lambda: on_button_click('/'), '#E0E0E0', 1), 
    ('*', 4, 3, lambda: on_button_click('*'), '#E0E0E0', 1),
    ('AC', 5, 0, clear_display, '#FF9F9F', 1), 
    ('=', 5, 1, calculate_result, '#B6E3B6', 3),
]
# Dynamically create buttons using the layout
for button in button_definitions:
    text, row, col, command, color, colspan = button  # Unpack the button properties
    create_button(text, row, col, command, color=color, colspan=colspan)

# Start the main application loop
root.mainloop()
