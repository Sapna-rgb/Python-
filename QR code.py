import qrcode

# Data to be encoded in the QR code
data = "https://www.siesascs.edu.in/"  # Replace with your desired URL or text

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4,  # Thickness of the border (minimum is 4)
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)  # Fit the QR code to the data

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("sies_college_sion_west_qrcode.png")

# Optionally, display the QR code
img.show()
