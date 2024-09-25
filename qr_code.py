import qrcode

# Generate a simple QR code for a text.
qr = qrcode.make("صلي على النبي ♥♥")

# Save the QR code as an image file
qr.save("nice_note.png")

