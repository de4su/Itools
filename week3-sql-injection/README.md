# Week 3 SQL Injection Project

## Description
This project showcases a vulnerable web application that is susceptible to SQL Injection attacks. It provides both a vulnerable version and a secure version that utilizes best practices in code security to prevent these types of exploits.

### Vulnerable Version
The vulnerable version of the application allows attackers to manipulate SQL queries by injecting arbitrary SQL code via user input fields. This can lead to unauthorized access to data, data manipulation, or even database compromise.

### Secure Version
The secure version incorporates parameterized queries which prevent SQL Injection by ensuring that user input is treated as data, not executable code. Additionally, it employs password hashing techniques to securely store user credentials.

## Features
- **Vulnerable Application**: Demonstrates SQL Injection vulnerability.
- **Secure Application**: Implements secure coding practices to mitigate SQL Injection risks.
- **Parameterized Queries**: Uses prepared statements to safeguard against SQL Injection.
- **Password Hashing**: Securely hashes user passwords using modern hashing functions.

## Usage Instructions
### Starting the Servers
1. **Vulnerable Server**: Navigate to the `vulnerable` directory and run the server using the command:
   ```bash
   python app.py
   ```

2. **Secure Server**: Navigate to the `secure` directory and run the server using the command:
   ```bash
   python app.py
   ```

### Testing SQL Injection
To test the SQL Injection vulnerability on the vulnerable server:
- Use the following credentials:
  - **Username**: `admin' --`  
  - **Password**: any password (this will bypass the authentication process)

## Requirements
- Python 3.x
- Flask library (for running the web application)
- SQLite (for database management)