import streamlit as st
import re

st.set_page_config(page_title="Passwords Strenght Checker", page_icon="🔒")
st.title("🔏Passwords Strenght Checker")
st.markdown(""""
            "## Welcome tpo the ultimate passwords strenght checker! 👋
             use this simple tool to check strength of your password and get suggestions on how to  make it suggestion.
             we will give you helpful tips to crrate a ** Strong Passwords** 🔒""")

password = st.text_input("Enter your password", type="password")

feedback=[]

score = 0
if password:
    if len(password) >= 8:
        score +=1
    else :
        feedback.append(" ❌Password should be atleast 8 character long.")
if re.search(r'[A-Z]', password) and  re.search(r'[a-z]', password):
 score += 1

else:
   feedback.append("❌Password should contain both upper and lowe case characters.")
if re.search(r'\d', password):
    score += 1
else:feedback.append("❌ Password should contain at least one digit.")
if re.search(r'[!@#$%&*]', password):
    score +=1
else: feedback.append("❌Password should contain at least one special character(!@#$%&*).")
if score == 4:
    feedback.append(" ✅Your password is Strong.")
elif score == 3 :
    feedback.append("🟡Your password is medium strenght. It could be strong.")
else:
    feedback.append("Your password is weak. Please make it stronger.")

if feedback: 
       st.markdown("## Impeovement Suggesions")
       for tip in feedback:
          st.write(tip)
       else:
          st.info("Please enter your password to get started")