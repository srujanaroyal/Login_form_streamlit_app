import streamlit as st

#header
st.header("Anurag University Student Management System")

#title
st.title("Welcome to Student Management System")

#subheader 
st.subheader("Manage Student records efficiently and effectively")

#horizontal line
st.markdown("-----------------------------------------------------------------")

#text
st.text("The application allows u to perform CRUD operations an student records using MYSQL database")

#write
st.write("hello streamlit")
st.write(123)
st.write([1,2,3])
st.write({"name":"Anurag","course":"BTech"})


#markdown method to format text
st.markdown("##featues of application")
st.markdown("**Bold text**")
st.markdown("*Italic text*")
st.markdown("-item1\n-item2")
st.markdown("<h3 style='color:red'>Red Text</h3>",unsafe_allow_html=True)

#caption 
st.caption("This is a caption for student management")

#code
st.code("""
def add(a,b):
    return a+b
""",language="Pyhton")

#latex method to render mathematical expression
st.latex(r'''
a^2 + b^2=c^2
''')

#divider method to seperate sections
st.divider()

#button method to create a button
if st.button("Click Me"):
    st.write("Button Clicked!")
    st.success("Operation Successfull!")
    st.balloons()
    st.snow()
else:
    st.write("Balloons not clicked yet")
    st.error("Connection error!")

st.divider()   

#text input method to get user input
name=st.text_input("Enter your name:")
st.write(f"Hello, {name}!")

if name =="":
    st.warning("Name cannot be empty!")
elif not name.isalpha():
    st.error("Invalid input please enter only alphabets(no numbers or symbols).")
else:
    st.success(f"Hello, {name}!")

st.divider()

feedback=st.text_area("enter feedback")
st.write(feedback)

st.divider()

#checkbox
if st.checkbox("I agree to terms and conditions"):
    st.write("Thank you for agreeing!")

st.divider()

#radio button
gender = st.radio("Select your gender:",("Male","Female","Other"))
st.write(f"You selected: {gender}")

st.divider()

#selectbox
country = st.selectbox("select your country",{"India","Dubai"})
st.write(f"You selected: {country}")

st.divider()

#multiselect
skills =st.multiselect(
    "Select skills",
    ["Python","SQL","ML","Streamlit"]
)
st.write("Skills:", skills)

st.divider()

# slider
age=st.slider("Select your age:",0,100,25)
st.write(f"Your age {age} years old.")

st.divider()

#file uploader to upload files
uploaded_file=st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write(f"Filename: {uploaded_file.name}")

st.divider()

#form method
#with - manages all the variables in a single block

with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age",0,100)
    submit = st.form_submit_button("Submit")
if submit:
    st.write(name, age)

st.divider()

#form submit
with st.form("Login"):
    user = st.text_input("Username")
    pwd = st.text_input("Password")
    login =st.form_submit_button("Login")
if login:
    st.write("Login Successful!")

st.divider()

#columns method
col1,col2,col3 = st.columns(3)
with col1:
    st.header("Column 1")
    st.write("This is column 1")
with col2:
    st.header("Column 2")
    st.write("This is column 2")
with col3:
    st.header("Column 3")
    st.write("This is column 3")

st.divider()

#container
container=st.container()
container.write("Inside container")
container.button("Click")
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)

st.divider()

#sidebar
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")

st.divider()

@st.cache_data
def load_data():
    return [1,2,3,4]
data = load_data()
st.write(data)

st.divider()

