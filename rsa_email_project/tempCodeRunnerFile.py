import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Function to encrypt a message using RSA
def encrypt_message(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message using RSA
def decrypt_message(encrypted_message, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

# Load public and private keys from files
def load_keys():
    with open("keys/public.pem", "rb") as pub_file:
        public_key = RSA.import_key(pub_file.read())
    
    with open("keys/private.pem", "rb") as priv_file:
        private_key = RSA.import_key(priv_file.read())
    
    return public_key, private_key

# Route to Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle encryption
@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        message = request.form['message']
        public_key, _ = load_keys()
        encrypted_message = encrypt_message(message, public_key)
        
        # Send encrypted email
        sender_email = "your-email@gmail.com"  # Your email
        receiver_email = request.form['receiver_email']
        subject = "Encrypted Email"
        
        # Set up the email body
        body = f"Encrypted Message: {encrypted_message.decode('latin1')}"
        
        # Send email (you must have your app password in .env or environment variable)
        send_email(sender_email, receiver_email, subject, body)
        
        flash('Email sent successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('encrypt.html')

# Route to handle decryption
@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        encrypted_message = request.form['encrypted_message'].encode('latin1')
        _, private_key = load_keys()
        decrypted_message = decrypt_message(encrypted_message, private_key)
        return render_template('decrypt.html', decrypted_message=decrypted_message)
    return render_template('decrypt.html')

# Function to send an email
def send_email(sender_email, receiver_email, subject, body):
    # Retrieve app password from environment variables
    password = os.getenv('EMAIL_PASSWORD')  # Get app password from .env
    
    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Connect to Gmail's SMTP server and send the email
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()  # Secure the connection
        smtp.login(sender_email, password)  # Login with the email and app password
        smtp.sendmail(sender_email, receiver_email, msg.as_string())  # Send email
        smtp.quit()
    except Exception as e:
        flash(f"Failed to send email: {e}", 'danger')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
