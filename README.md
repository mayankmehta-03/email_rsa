
---

# 🔐 **RSA Email Encryption System**

A **secure web-based RSA encryption & decryption system** built with **Flask** and **Python**. This project empowers users to:
✅ **Encrypt messages using RSA**,
✅ **Send them securely via Gmail**, and
✅ **Decrypt** them from **any device** using their uploaded private key.

---

## 🚀 **Features**

* 🔑 **RSA Key Generation (2048-bit)**
  Generate strong RSA public-private key pairs for secure communication.

* ✉️ **Send Encrypted Messages via Gmail**
  Seamlessly email encrypted messages using Gmail’s SMTP.

* 🔐 **Password-Protected Private Key Storage**
  Keep private keys safe — optionally encrypt them with a password before storage.

* 🧩 **Base64-Encoded Output**
  Encode ciphertext in Base64 for easy sharing and transmission.

* 🌐 **Clean Flask Web Interface**
  Responsive and user-friendly Bootstrap-styled frontend.

* 💻 **Cross-Device Decryption Support**
  Access your encrypted messages and decrypt them securely from any device.

---

## 📂 **Project Structure**

```
rsa_email_project/
│
├── app.py                  # Flask app: routes for encryption, decryption, emailing
├── generate_keys.py         # RSA public/private key pair generation
├── key_utils.py            # Encrypt/decrypt private keys with password
│
├── templates/              # HTML templates (Bootstrap-styled)
│   ├── index.html
│   ├── encrypt.html
│   ├── decrypt.html
│   ├── upload_key.html
│   └── login.html          # (optional, if using authentication)
│
├── static/
│   └── style.css           # Custom styles
│
├── keys/                   # Stores public.pem & private.pem locally
│   ├── public.pem
│   └── private.pem
│
├── models.py               # SQLAlchemy User model (if using user accounts)
└── README.md               # Project documentation (you’re here!)
```

---

## 🛠 **Setup & Installation**

1️⃣ **Clone the repository**

```bash
git clone https://github.com/yourusername/rsa_email_project.git
cd rsa_email_project
```

2️⃣ **Create a virtual environment & install dependencies**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3️⃣ **Generate RSA keys**

```bash
python generate_keys.py
```

4️⃣ **Run the Flask app**

```bash
python app.py
```

---

## 🔧 **Usage**

✅ Visit the **web interface** → Encrypt your message → Send it via Gmail.
✅ Share your public key with others for secure communication.
✅ Upload your **private key** and decrypt messages from any device.

---

## 🛡️ **Security Notes**

* **Never share your private key.** Keep it secure and consider using a strong password for additional encryption.
* Use **Gmail App Passwords** (not your main Gmail password) for sending emails via SMTP.
* For production, consider adding **user authentication** and **SSL/TLS**.

---

## 🤝 **Contributing**

Want to improve this project?
✅ Submit issues
✅ Create pull requests
✅ Add new features or improve UI/UX!

---

## 📜 **License**

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---


