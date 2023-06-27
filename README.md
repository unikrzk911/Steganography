# What is steganography?

Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video.

What is the advantage of steganography over cryptography?

The advantage of steganography over cryptography alone is that the intended secret message does not attract attention to itself as an object of scrutiny. Plainly visible encrypted messages, no matter how unbreakable they are, arouse interest and may in themselves be incriminating in countries in which encryption is illegal.

In other words, steganography is more discreet than cryptography when we want to send a secret information. On the other hand, the hidden message is easier to extract.

## Installation Instructions

0. Make sure that you have `Python 3`, `python-3-devel`, `gcc`, `virtualenv`, and `pip` installed.

1. Clone this repository

2. Create a python 3 virtualenv inside the repository, activate the environment and Install the project dependencies. (Second option)

   ```powershell copy
       python -m venv venv
   ```

   ```powershell copy
      ./venv/Scripts/Activate.ps1
   ```

   ```powershell copy
    py -m pip install -r requirements.txt
   ```

3. Run the project

   ```powershell copy
    py main.py
   ```

You have now successfully set up the project on your environment.
