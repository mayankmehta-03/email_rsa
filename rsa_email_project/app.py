from flask import Flask, render_template, request, redirect, flash
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  

# Home page
@app.route('/')
def home():
    return render_template('home.html')

@app.route("/contribution")
def contribution():
    return render_template("contribution.html")

# Encrypt + Send Email
@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        message = request.form['message']
        email = request.form['email']

        # Load public key
        with open("keys/public.pem", "rb") as f:
            pub_key = RSA.import_key(f.read())

        cipher = PKCS1_OAEP.new(pub_key)
        encrypted = cipher.encrypt(message.encode())
        encrypted_b64 = base64.b64encode(encrypted).decode()

        # Email it
        sender = "yoichiisagi696942@gmail.com"
        password = ""

        msg = EmailMessage()
        msg.set_content(encrypted_b64)
        msg['Subject'] = 'Encrypted Message'
        msg['From'] = sender
        msg['To'] = email

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(sender, password)
                smtp.send_message(msg)
            flash('Encrypted email sent successfully!', 'success')
        except Exception as e:
            flash(f'Failed to send email: {e}', 'danger')

        return redirect('/encrypt')

    return render_template('encrypt.html')

# Decrypt Page
@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        encrypted_b64 = request.form['encrypted']
        try:
            encrypted = base64.b64decode(encrypted_b64)

            with open("keys/private.pem", "rb") as f:
                priv_key = RSA.import_key(f.read())

            cipher = PKCS1_OAEP.new(priv_key)
            decrypted = cipher.decrypt(encrypted).decode()

            return render_template('decrypt.html', decrypted=decrypted)

        except Exception as e:
            flash(f'Decryption failed: {e}', 'danger')
            return redirect('/decrypt')

    return render_template('decrypt.html')

if __name__ == '__main__':
    app.run(debug=True)
