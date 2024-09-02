🔐 Python User Authentication System with Salted Password Hashing

This project implements a simple user authentication system in Python that securely stores and verifies user credentials using salted password hashing. It is a basic yet effective way to manage user authentication in a Python application, demonstrating fundamental concepts of cryptography, file I/O, and user input handling.

🛠 Features
Salted Password Hashing: Each user password is combined with a unique random salt before being hashed using the SHA-256 algorithm. This technique greatly enhances security by making it difficult for attackers to crack passwords using precomputed hash tables (rainbow tables).

User Registration: New users can register by providing a username and password. The system automatically generates a salt, combines it with the password, hashes the result, and stores the hashed password and salt in a file.

User Authentication: Existing users can log in by providing their username and password. The system retrieves the stored salt and hashed password, rehashes the entered password with the salt, and compares it to the stored hash to authenticate the user.

Secure Data Storage: The password is salted and then hashed to keep the credentials secure.


📂 File Structure
login and create.py: Handles user interactions, including login and account creation.
hashing.py: Contains utility functions for generating salts, hashing passwords, and processing user data.
