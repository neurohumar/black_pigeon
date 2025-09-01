# About __*Black Pigeon*__

__*Black Pigeon*__ is a simple python script , responsible for hiding various types of data into __PNG__ or __JPEG__ image file to ensure security and privacy.
It typically compresses files to be hidden , with popular LZMA algorithm to reduce size . Besides it uses cryptographic algorithm to encrypt data during hiding process

# Supported Files
1. PNG (.png)
2. JPEG (.jpeg)
3. ZIP (.zip)

# Features 
- Compression
- Decompression
- Encryption
- Decryption
- Steganographic obscuration
- File Injection
- File extration

# Installation

## Step 1 :
```sh
git clone https://github.com/neurohumar/black_pigeon.git
```

## Step 2 :
```sh
cd black_pigeon
```

## Step 3 :
For Windows :
```sh
pip install -r requirements.txt
```

For Linux/MacOS
```sh
pip3 install -r requirements.txt
```
## Step 4 (Optional):
For Linux :
```sh
chmod +x main.py
```

# Usage
1. Aggregate all files to be obscured in a clean and separate directory.
2. Select a __*cover image*__ file```(.png or .jpeg)``` and copy the path of that image. This image is the carrier of all hidden file(s)
3. Copy the path of the directory.
4. run ```main.py ``` and select a option mentioned on the menu in the console as your need.
5. To obscure the directory, select option 1 . Then enter necessary information required by the script and don't forget to set a password for better security .
7. For extracting contents from a image where you have obscured info through __Black Pigeon__ , Select correct option from the menu and enter the password key that you set earlier during the encryption process.
8. provide a output path to save extracted information.

__*All types of path mentioned earlier have to be absolute, not relative*__
