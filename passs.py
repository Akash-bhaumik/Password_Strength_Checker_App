import streamlit as st
import re

def calculate_password_strength(password):
    score = 0
    checks = []

    # Criteria
    length_criteria = len(password) >= 8
    digit_criteria = re.search(r"\d", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=;']", password) is not None

    # Each check with feedback
    if length_criteria:
        score += 1
        checks.append("✅ Length ≥ 8 characters")
    else:
        checks.append("❌ Length < 8 → Use at least 8 characters")

    if digit_criteria:
        score += 1
        checks.append("✅ Contains a number (0–9)")
    else:
        checks.append("❌ Missing number → Add digits")

    if uppercase_criteria:
        score += 1
        checks.append("✅ Contains uppercase letter")
    else:
        checks.append("❌ Missing uppercase → Add A–Z")

    if lowercase_criteria:
        score += 1
        checks.append("✅ Contains lowercase letter")
    else:
        checks.append("❌ Missing lowercase → Add a–z")

    if special_char_criteria:
        score += 1
        checks.append("✅ Contains special character")
    else:
        checks.append("❌ Missing special → Add !@#$% etc.")

    # Strength levels
    strength_levels = {
        0: ("Very Weak", "❌", "red"),
        1: ("Weak", "⚠️", "orange"),
        2: ("Fair", "🟡", "gold"),
        3: ("Moderate", "🔵", "blue"),
        4: ("Strong", "🟢", "green"),
        5: ("Very Strong", "💪", "darkgreen")
    }

    level, icon, color = strength_levels[score]

    # Show results
    st.markdown(f"### {icon} Password Strength: <span style='color:{color}'>{level}</span>", unsafe_allow_html=True)
    st.progress(score / 5)

    st.markdown("### 🔍 Detailed Analysis")
    for c in checks:
        st.write(c)

    # Extra pro tips for weak/moderate
    if score < 4:
        st.markdown("### 💡 Suggestions to Improve:")
        if len(password) < 12:
            st.write("➡️ Try to use **12+ characters** for extra security.")
        st.write("➡️ Mix words, numbers & symbols to make it unpredictable.")
        st.write("➡️ Avoid using names, birthdays, or common words.")

# Streamlit app
def main():
    st.set_page_config(page_title="Advanced Password Strength Tester", page_icon="🔐", layout="centered")
    st.title("🔐 Advanced Password Strength Tester")
    st.markdown("Check how strong your password is with a **detailed breakdown** & improvement tips.")

    password = st.text_input("Enter your password", type="password")

    if ' ' in password:
        st.error("🚫 Spaces are not allowed in the password.")
    elif password:
        calculate_password_strength(password)
    else:
        st.info("👆 Type a password above to see its strength.")

    st.markdown(
        """
        <hr>
        <div style="text-align: center;">
            Made with ❤️ by <a href="https://www.linkedin.com/in/akash-bhaumik-213802259" target="_blank">Akash Bhaumik</a>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
