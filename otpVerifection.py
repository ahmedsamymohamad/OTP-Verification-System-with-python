import random
import smtplib

# Generate a 6-digit OTP
otp = random.randint(100000, 999999)

# Store the email details
sender_email = 'sender_email@example.com'
sender_password = 'sender_password'
receiver_email = input('Enter your email address: ')

# Send the OTP via email
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    message = f'The OTP for verification is {otp}.'
    smtp.sendmail(sender_email, receiver_email, message)

# Request the user to enter the OTP for verification
user_otp = input('Enter the OTP received via email: ')

# Verify the OTP
if int(user_otp) == otp:
    print('OTP verification successful.')
else:
    print('OTP verification failed.')