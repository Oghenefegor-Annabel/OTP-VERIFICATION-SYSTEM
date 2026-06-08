import random

# Function to generate OTP
def generate_otp():
    return random.randint(100000, 999999)

def main():
    print("==== OTP Verification System ====")

    otp = generate_otp()

    print("Generated OTP:", otp) #Hidden in real apps

    attempts = 3

    while attempts > 0:
        try:
            user_otp = int(input("Enter OTP: "))
            if user_otp == otp:
                print("Access Granted")
                return
            else:
                print("Incorrect OTP")
                attempts -= 1
                print("Attempts left:", attempts)
        except ValueError:
            print("Please Enter Numbers Only")
            attempts -=1 #this will bring it to an end when adding alphabets

    print("OTP Expired")

if __name__ == "__main__":
    main()