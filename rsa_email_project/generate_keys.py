from Crypto.PublicKey import RSA

# Generate RSA keys
key = RSA.generate(2048)

# Export private key in PEM format
private_key = key.export_key()
with open("keys/private.pem", "wb") as priv_file:
    priv_file.write(private_key)

# Export public key in PEM format
public_key = key.publickey().export_key()
with open("keys/public.pem", "wb") as pub_file:
    pub_file.write(public_key)

print("Keys generated and saved.")
