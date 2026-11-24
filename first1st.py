import streamlit as st
st.title("Students Information System")
st.header("Student Details")
st.write("GWIZA MUCYO Lionel")
st.text("RWANDA CODING ACADEMY")
st.subheader("Personal Information")
st.markdown("**Welcome to my application!**")
st.markdown("**This is bold text**")
st.markdown("*This is italic text*")
st.markdown("~~This is crossed-out text~~")
st.caption("Created by a Lionel.")
st.markdown("*This is for PYTHON*")
st.code("""
name = "Lionel"
age = 18
print(name)
""", language="python")
st.markdown("*This is for HTML*")
st.code("""
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Hello World</h1>
    <p>Welcome to my website.</p>
</body>
</html>
""", language="html")
st.markdown("*This is for JAVASCRIPT*")
st.code("""
let name = "Lionel";
let age = 18;
console.log("My name is " + name);
console.log("My age is " + age);
""", language="javascript")
st.latex("This is about latex:  x^2 + y^2 = z^2")
st.title("Button Example")
if st.button("Click"):
    st.write("You clicked the button!, that was a button")
    
st.title("User Registration")
name = st.text_input("Enter your name:")
st.write("Your name is:", name)

age=st.number_input("Enter your age:",min_value=0,max_value=100,step=1)
st.write("Your age is :",age)

agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("Thank you for agreeing!")
else:
    st.write("Please agree to continue.")

language = st.selectbox(
    "Choose your programming language:",
    ["Python", "JavaScript", "C", "Java","C++","other more"]
)
st.write("You selected:", language)  

gender = st.radio(
    "Select an option:",
    ["Male", "Female","Rather not say"]
)
st.write("Selected:", gender) 

description = st.text_area("Write about yourself:")
st.write("Your description:", description)
#nothing else