import qrcode

# Data to encode (you can also prompt the user for input)
data = input("enter the url:")

# Generate the QR code
qr_image = qrcode.make(data)

# Save the QR code as an image file
qr_image.save("Github_qrcode.png")
print("QR code successfully generated and saved as 'Github_qrcode.png'.")
