I wanted to implement error handling to my code,  to ensure its smoothness and efficiency. This is done by using the try and except blocks. Which are used around the code. Which basically are built in functions inside python, made to handle errors efficiency. The code inside the try block is executed. It is caught by the except block at the end, which prevents the program from crashing. Instead of terminating, the error is set as a variable “e”, and is printed to display what went wrong to the user.

1. Error handling for invalid input during encoding:
- Located in the if choice == 1 code
try:
    message_number = int(input("Enter the message number to encrypt: "))
“””””””””””””””””””””””””””””””””””””””””””””””””””””””””””””””
except Exception as e:
    print("Error:", e)
This ensures that invalid inputs for the message, for example a character or string, does not crash the program. Instead, displays the error message and repeats the program

2. Error handling during decoding:
- Located in the if choice == 2
try:
    c1 = int(input("Enter ciphertext part 1 (c1): "))
    c2 = int(input("Enter ciphertext part 2 (c2): "))
“”””””””””””””””””””””””””””””””””””””””””””””””””””””””””””””
except Exception as e:
    print("Error:", e)
This ensures that invalid inputs for the ciphertext parts like non-integer inputs do not crash the program.

3. General handling around the entire main menu
- Surrounding the entire code with while loop:
while True:
“””””””””””””””””””””””””””””””””””””””””””””””””””””””
else:
    print("Invalid choice. Please try again.")
This block is executed if the user's input for choice does not match '1', '2', or '3'. 

