
# CodeAlpha Secure Coding Review

## 1. Aim
To identify security vulnerabilities in a Python login application
and improve the code using secure coding practices.

## 2. Technologies Used
- Python
- Visual Studio Code
- Bandit Security Analyzer

## 3. Project Description
This project demonstrates a simple login system.
The original code used a hardcoded password.
The improved version uses password hashing and limits
failed login attempts during a program session.

## 4. Security Vulnerabilities Identified
1. Hardcoded credentials
2. Weak password requirements
3. No limit on repeated login attempts
4. Unsafe password storage in the original design

## 5. Security Improvements
1. Passwords are hashed using PBKDF2-HMAC-SHA256.
2. A random salt is generated for each account.
3. Passwords must contain at least eight characters.
4. Login attempts are limited during a single run.
5. Bandit is used to scan the Python source code.

## 6. Testing
- Account creation
- Successful login
- Incorrect password
- Maximum login attempts
- Bandit security scan

## 7. Conclusion
The project demonstrates how manual code review and
automated security analysis can help identify and reduce
common security weaknesses in a Python login application.
