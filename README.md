# Password Strength Checker Project

## Why I Started This

I wanted to learn Python and regex because I saw a lot of talk on X about password security. I thought building a password strength checker would be a cool way to practice coding and understand what makes passwords secure. Plus, it’s something practical I can use myself!

---

## Day 1: Initial Setup 

### What I Accomplished

- Wrote a basic Python script to check password length and uppercase letters.
- Used regex for the first time to check for uppercase letters.
- Got user input and printed some feedback.

### Challenges and How I Resolved Them

**Challenge:** Didn’t know how to use regex. Kept getting errors with the pattern.  
**Solution:** Looked up regex basics on the web and found `re.search("[A-Z]", password)` works for uppercase checks. Trial and error helped.

**Challenge:** Code felt messy, and I wasn’t sure how to structure it better.  
**Solution:** Decided to keep going and clean it up later as I learn more.

---

## Day 2: Expanding Checks and Cleanup 

### What I Accomplished

- Added checks for lowercase letters, digits, and special characters using regex.
- Improved variable names (e.g., `check_pass` to `check_password_strength`).
- Added a scoring system to classify passwords as **"Strong," "Moderate,"** or **"Weak."**
- Structured the feedback to be more readable with a loop.

### Challenges and How I Resolved Them

**Challenge:** Wasn’t sure which special characters to include in the regex.  
**Solution:** Searched online and chose a common set `[!@#$%^&*]` for simplicity. Will expand later if needed.

**Challenge:** Scoring felt arbitrary, and I wasn’t sure how to balance it.  
**Solution:** Set a simple threshold:  
- **Strong**: score ≥ 4  
- **Moderate**: score = 2–3  
- **Weak**: score < 2  
Will refine after testing.

---

## Day 3: Refining Logic and Common Passwords 

### What I Accomplished

- Added a check for common passwords (e.g., `"password"`, `"qwerty"`).
- Made length scoring more granular:
  - +2 points for 12+ characters
  - +1 point for 8–11 characters
- Expanded special characters regex to include more symbols.
- Added `if __name__ == "__main__":` for better code organization.
- Improved feedback messages for clarity.

### Challenges and How I Resolved Them

**Challenge:** Wasn’t sure how to handle common passwords effectively.  
**Solution:** Used a simple list for now. If the password is common, I reset the score in case it’s too easy to guess.

**Challenge:** Feedback messages were inconsistent in tone.  
**Solution:** Standardized them to start with **"Good," "Moderate," "Weak,"** or **"Critical"** for clarity.

---

## Next Steps

- Plan to deploy this as a web app using **Streamlit** for a better user interface.
- Test with edge cases (e.g., empty passwords, very long passwords).
- Maybe add a feature to suggest improvements for weak passwords.