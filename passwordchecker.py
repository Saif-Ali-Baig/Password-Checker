import re

def check_password_strength(password):
    feedback = []
    score = 0
    # Check length
    if len(password) >= 8:
        score += 1
        feedback.append("Good: Password is long enough")
    else:
        feedback.append("Weak: Password too short")
    # Check uppercase
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("Good: Has uppercase letters")
    else:
        feedback.append("Weak: No uppercase letters")
    # Check lowercase
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("Good: Has lowercase letters")
    else:
        feedback.append("Weak: No lowercase letters")
    # Check digits
    if re.search(r'[0-9]', password):
        score += 1
        feedback.append("Good: Has numbers")
    else:
        feedback.append("Weak: No numbers")
    # Check special chars
    if re.search(r'[!@#$%^&*]', password):
        score += 1
        feedback.append("Good: Has special characters")
    else:
        feedback.append("Weak: No special characters")
    
    if score >= 4:
        strength = "Strong"
    elif score >= 2:
        strength = "Moderate"
    else:
        strength = "Weak"
    return strength, feedback

def main():
    password = input("Enter password: ")
    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {strength}")
    print("Feedback:")
    for comment in feedback:
        print(f"- {comment}")

main()