import cv2
import os

# Load image
img = cv2.imread("image2.jpg")

if img is None:
    print("Error: Could not load image.")
    exit()

# Get user input
password = input("Enter a passcode: ")
msg = input("Enter secret message : ")

# Convert message to exactly 100 words
words = msg.split()
if len(words) > 100:
    words = words[:100]  # Trim if too long
elif len(words) < 100:
    words += [" "] * (100 - len(words))  # Pad if too short

msg = password + "#" + " ".join(words) + "#"  # Store password first and add termination marker

# Convert message to ASCII values
msg_ascii = [ord(char) for char in msg]

# Encode message into image
height, width, _ = img.shape
index = 0
max_length = len(msg_ascii)

for row in range(height):
    for col in range(width):
        for channel in range(3):  # Iterate through R, G, B
            if index < max_length:
                img[row, col, channel] = msg_ascii[index]
                index += 1
            else:
                break
    if index >= max_length:
        break

# Save encrypted image without compression loss
cv2.imwrite("encryptedImage2.png", img)  # Use PNG to avoid data loss
os.system("start encryptedImage2.png")  # Open image (Windows)

print("Message encrypted successfully!")
