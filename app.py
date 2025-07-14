import streamlit as st
import re

def check_password_strength(password):
    """Check the strength of a password based on various criteria."""
    if not password:
        return "Invalid", ["Critical: Password cannot be empty."]
    
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
    st.title("Password Strength Checker")
    st.write("Enter a password to evaluate its strength.")
    
    password = st.text_input("Password", type="password")
    
    if st.button("Check Strength"):
        if password:
            strength, feedback = check_password_strength(password)
            st.write(f"**Password Strength**: {strength}")
            st.write("**Feedback**:")
            for comment in feedback:
                st.write(f"- {comment}")
        else:
            st.error("Please enter a password.")

if __name__ == "__main__":
    main()