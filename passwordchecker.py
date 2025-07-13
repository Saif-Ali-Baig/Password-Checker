import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 12:
        score += 2
        feedback.append("Good: Password is 12+ characters.")
    elif len(password) >= 8:
        score += 1
        feedback.append("Moderate: Password is 8-11 characters.")
    else:
        feedback.append("Weak: Password is too short (<8 characters).")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("Good: Contains uppercase letters.")
    else:
        feedback.append("Weak: No uppercase letters.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("Good: Contains lowercase letters.")
    else:
        feedback.append("Weak: No lowercase letters.")
    
    # Check for digits
    if re.search(r'\d', password):
        score += 1
        feedback.append("Good: Contains numbers.")
    else:
        feedback.append("Weak: No numbers.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append("Good: Contains special characters.")
    else:
        feedback.append("Weak: No special characters.")
    
    # Check against common passwords
    common_passwords = ['password', '123456', 'qwerty', 'admin']
    if password.lower() in common_passwords:
        score = 0
        feedback.append("Critical: Password is too common!")
    
    # Determine strength
    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return strength, feedback

def main():
    password = input("Enter a password to check: ")
    strength, feedback = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")
    print("Feedback:")
    for comment in feedback:
        print(f"- {comment}")
if __name__ == "__main__":
    main()