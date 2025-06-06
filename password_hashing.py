import bcrypt

# Step 1: Get a plain password
password = b"my_secure_password"  # b"" means it's a byte string

# Step 2: Hash the password
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)
print("Hashed Password:", hashed_password)

# Step 3: Verify the password
entered_password = b"my_secure_password"
if bcrypt.checkpw(entered_password, hashed_password):
    print("Password is correct!")
else:
    print("Incorrect password.")
