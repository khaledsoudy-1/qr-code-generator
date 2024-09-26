
# 🖼️ QR Code Generator

## 📖 Description

Easily create QR codes with this Python-based generator! Whether you're encoding a message, a URL, or any other text, this tool will generate a custom QR code and save it as an image file.

## 🚀 How to Use

### For Quick Generation:
1. Run the basic QR code generator with:
   ```bash
   python qr_code.py
   ```
2. This will generate a QR code with the text `"صلي على النبي ♥♥"` and save it as `nice_note.png`.

### For Custom QR Code:
1. Run the customizable QR code generator:
   ```bash
   python generate_qr_code.py
   ```
2. Follow the prompts:
   - Enter the text or URL you want to encode.
   - Specify the file name for the saved image.

## 💻 Code Highlights

### Customizable QR Code Generator

In `generate_qr_code.py`, the user can input custom text and filename, and the QR code is generated with the following customization:

```python
qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=10,
    border=4
)
```

- `version=1`: Specifies the size of the QR code.
- `error_correction=ERROR_CORRECT_L`: Allows for a low level of error correction.
- `box_size=10`: Controls the size of each box in the QR code.
- `border=4`: Defines the border thickness.

## 📦 Requirements

To install the dependencies, run:
```bash
pip install -r requirements.txt
```

Dependencies include:
- `colorama==0.4.6`: For colored text in the terminal (optional for enhancements).
- `pillow==10.4.0`: For working with images.
- `pypng==0.20220715.0`: To support PNG generation.
- `qrcode==7.4.2`: Main library for generating QR codes.
- `typing_extensions==4.12.2`: For improved type hints (optional).

## 🛠️ Future Enhancements

- Add more customization options, such as different colors for the QR code and background.
- Implement a user-friendly GUI.
- Support for batch QR code generation from a list of data.

## 👨‍💻 Author

Khaled Soudy

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have any questions, please open an issue in the GitHub repository.

---

Enjoy generating your QR codes! 🎉
