import cv2

# Load encrypted image
img = cv2.imread("encryptedImage2.png")

if img is None:
    print("Error: Could not load encrypted image.")
    exit()

height, width, _ = img.shape
extracted_text = ""
index = 0
reading_password = True  # Track if we are still reading the password

# Extract password and message separately
for row in range(height):
    for col in range(width):
        for channel in range(3):
            char = chr(img[row, col, channel])

            if char == "#":  # First '#' marks the end of the password
                if reading_password:
                    extracted_password = extracted_text  # Store password
                    extracted_text = ""  # Reset to read the message
                    reading_password = False
                else:
                    break  # Second '#' marks end of the message
            else:
                extracted_text += char

        if not reading_password and char == "#":
            break
    if not reading_password and char == "#":
        break

# Final extracted message
decrypted_message = extracted_text.strip()

# Ask user for password
user_password = input("Enter passcode for decryption: ")

if user_password == extracted_password:
    print("Decrypted message:", decrypted_message)
else:
    print("YOU ARE NOT AUTHORIZED")
