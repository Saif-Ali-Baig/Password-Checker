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

**Challenge:** Didn’t know how to use regex.  
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

**Challenge:** Scoring felt arbitrary.  
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
**Solution:** Used a simple list for now. If the password is common, I reset the score to prevent false positives.

**Challenge:** Feedback messages were inconsistent in tone.  
**Solution:** Standardized all responses to start with **"Good," "Moderate," "Weak,"** or **"Critical"** for consistency.

---

## Day 4: Streamlit Deployment and Final Polish

### What I Accomplished

- Converted the script into a **Streamlit web app** (`app.py`) for a user-friendly interface.
- Added error handling for empty passwords.
- Added a docstring to `check_password_strength` for better documentation.
- Deployed the app on **Streamlit Community Cloud** *(hypothetical deployment for this exercise)*.
- Tested with edge cases like empty strings and common passwords.

### Challenges and How I Resolved Them

**Challenge:** Never used Streamlit before; setup was confusing.  
**Solution:** Followed Streamlit’s official Getting Started guide and used `st.text_input()` and `st.write()` for simplicity.

**Challenge:** Empty passwords caused errors in the console version.  
**Solution:** Added a check at the beginning of `check_password_strength` to return `"Invalid"` for empty inputs.

---

## What I Learned

- **Python Basics:** Functions, conditionals, loops, and user input handling.
- **Regex:** How to use `re.search()` to check for uppercase, lowercase, digits, and special characters.
- **Code Organization:** Structured code into functions, used clear variable names, and added docstrings.
- **Streamlit:** Built a simple web app with text inputs, button interaction, and dynamic output.
- **Password Security:** Gained practical understanding of what makes a password strong.

---

## Technologies Used

- **Python 3**
- **re module** (regular expressions)
- **Streamlit** (for web app deployment)

---

## Future Vision

- Add a feature to **suggest stronger passwords** based on weak inputs.
- Expand the **common passwords list** using a larger database or API.
- Implement **password generation functionality** for users.
- Improve the UI with **better styling** and a **visual strength indicator** (e.g., progress bar).
- Explore **other deployment platforms** like **Flask** or **FastAPI** for comparison.
