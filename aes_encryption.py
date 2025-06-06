from cryptography.fernet import Fernet

# Step 1: Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Step 2: Original message
original_message = "Hello Cybersecurity!"
print("Original:", original_message)

# Step 3: Encrypt the message
encrypted_message = cipher.encrypt(original_message.encode())
print("Encrypted:", encrypted_message)

# Step 4: Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message).decode()
print("Decrypted:", decrypted_message)
