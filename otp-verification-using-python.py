


import pyotp
import base64
import os

def generate_secret_key():
    return base64.b32encode(os.urandom(10)).decode('utf-8')

def generate_otp(secret_key):
    totp = pyotp.TOTP(secret_key)
    return totp.now()

def verify_otp(secret_key, user_input_otp):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(user_input_otp)

if __name__ == "__main__":
    # Step 1: Generate a new secret key (replace this with a method to associate it with a user in a real application)
    secret_key = generate_secret_key()
    print("Generated Secret Key:", secret_key)

    # Step 2: Generate OTP
    otp = generate_otp(secret_key)
    print("Generated OTP:", otp)

    # Step 3: Simulate user input for OTP verification
    user_input_otp = input("Enter OTP received on your device: ")

    # Step 4: Verify OTP
    if verify_otp(secret_key, user_input_otp):
        print("OTP verification successful. User is authenticated.")
    else:
        print("OTP verification failed. User is not authenticated.")






