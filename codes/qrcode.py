import os
import qrcode
# Generate QR code
img = qrcode.make("your image or file link here")
# Save as file
img.save("qrcode.png", "PNG")
# Open file
os.system("open qrcode.png")
