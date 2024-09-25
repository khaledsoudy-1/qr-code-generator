import qrcode


def get_qr_code():
    # Welcome message
    print("Welcome to the QR Code Generator! 🤩")
    print("Note: If you're entering a URL, please make sure it starts with 'http://' or 'https://'.\n")
    
    # Get Data from user
    data = input("Enter the text or URL: ").strip().lower()
    filename = input("Enter the file name: ").strip().lower()
    
    # Generate a QR code.
    qr = qrcode.make(data)
    
    # Save the QR code as an image file
    qr.save(f"{filename}.png")


if __name__ == '__main__':
    get_qr_code()
