import qrcode
from qrcode.constants import ERROR_CORRECT_L


def get_qr_code():
    # Welcome message
    print("Welcome to the QR Code Generator! 🤩")
    print("Note: If you're entering a URL, please make sure it starts with 'http://' or 'https://'.\n")
    
    # Get Data from user
    data = input("Enter the text or URL: ").strip().lower()
    filename = input("Enter the file name: ").strip().lower()
    
    # Create a QR code object for customization
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    
    # Add data to the QR code
    qr.add_data(data)
    
    # Make the QR code fit the data
    qr.make(fit=True)
    
    # Create an image with custom colors
    img = qr.make_image(fill="black", back_color="white")
    
    # Save the image
    img.save(f"{filename}.png")


if __name__ == '__main__':
    get_qr_code()
