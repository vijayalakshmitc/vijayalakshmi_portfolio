#required libraries
import streamlit as st
import base64
import smtplib, ssl

#send mail function
def mail():
    st.header("Need Assistance ???")
    st.title("Let's work together")
    name,email = st.beta_columns([6,13])
    name = name.text_input("Your Name")
    email = email.text_input("Your Email")
    message = st.text_input("Your Message")
    return name,email,message


# Function about me page
def about_me():

    #About me
    
    st.subheader("I specialize in Machine learning algorithms, Data Pipelines.")
    
    my_expander3 = st.beta_expander("Some of the Clients I have worked with", expanded=True)
    
    
    with my_expander3:
        d,e = st.beta_columns(2)
        d.image("isha.jpeg",caption="Isha Foundations")
        e.image("nccab.png",caption="NCC AB")
        f,g = st.beta_columns(2)
        f.image("kmc.jpeg",caption="Kaveri Medical Center")
        g.image("luxin.png",caption="Luxin Group AB")
        a,b,c = st.beta_columns(3)
        a.image("agile.png", caption="Agile Health")
        b.image("aj.png",caption="A J Hospital")
        c.image("employchain.jpeg",caption="Employchain AB")
    
    

    my_expander1 = st.beta_expander("Experience", expanded=True)
    with my_expander1:
        st.markdown(""" ### My 3+ years experience, For more details head over to my [linkedin profile](https://www.linkedin.com/in/nikhil-ramesh-5125b7139/)""")
        st.markdown("""| Organization        | Role           | Date  | Place
        | ---------------------------------------------- |:--------------:| -----------------:| -----------------:|
        | NCC AB                                         | Master Thesis | 01/2021 – Present | Gothenburg, Sweden |
        | BlockchainX AB                                 | Data Scientist | 07/2020 – 12/2020 | Jönköping, Sweden |
        | Agile Health Medexpert Software Solutions      | Junior Software Developer | 08/2018 – 04/2019 | Bangalore, India |
        | Agile Health Medexpert Software Solutions      | Software Engineer | 08/2017 – 07/2018 | Bangalore, India |
        """)
    my_expander2 = st.beta_expander("Skills & Tools", expanded=True)  
    with my_expander2:
        st.markdown(""" Python / Core Java / SQL / AWS / Tableau / KNIME / Machine Learning / Deep Learning / ETL / Object Oriented Programming / Ruby/ Ruby on Rails/ Testing and Agile Methodologies / HTML / CSS / JavaScript / Django / Git / MIRTH / Microsoft Office / Postman / Android Studio / Visual Studio code / SQL Developer. """)
    
    my_expander_p = st.beta_expander("Some of the Projects I have worked with", expanded=True)
    with my_expander_p:
        a,b = st.beta_columns(2)
        a.image("leaf.jpeg",caption="Leaf Feature Extraction (2017)")
        a.markdown("""[Click here to know more](https://www.youtube.com/)""")
        b.image("Hospital.jpeg", caption="Hospital managament System (2018)")
        b.markdown("""[Click here to know more](https://www.youtube.com/)""")
        c,d = st.beta_columns(2)
        c.image("LIS.png",caption="Lab Information System and Radiology Information System (2018)")
        c.markdown("""[Click here to know more](https://www.youtube.com/)""")
        d.image("allergy.jpeg",caption="Allergen Identification(2019)")
        d.markdown("""[Click here to know more](https://www.youtube.com/)""")
        e,f = st.beta_columns(2)
        e.image("doctor.jpeg",caption="Doctor Appointment Application (2019)")
        e.markdown("""[Click here to know more](https://www.youtube.com/)""")
        f.image("jobmatch.jpeg",caption="Job Matching App (2020)")
        f.markdown("""[Click here to know more](https://www.youtube.com/)""")
        g,h = st.beta_columns(2)
        g.image("lane.jpeg",caption="Lane Detection for self driving car (2020)")
        g.markdown("""[Click here to know more](https://www.youtube.com/)""")
        h.image("treeclasify.jpeg",caption="Tree classification using CNN (2020)")
        h.markdown("""[Click here to know more](https://www.youtube.com/)""")
        i, j= st.beta_columns(2)
        i.image("bim.jpeg",caption="BIM Class Detection Bot (2021)")
        i.markdown("""[Click here to know more](https://www.youtube.com/)""")

# #background image 
# main_bg = "sample.jpg"
# main_bg_ext = "jpg"



# st.markdown(
#     f"""
#     <style>
#     .reportview-container {{
#         background: url(data:{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
#     }}
   
#     </style>
#     """,
#     unsafe_allow_html=True
# )


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "iamnikhilramesh@gmail.com"  # Enter your address
receiver_email = "nikhilramesh835@gmail.com"  # Enter receiver address
password = "Mallamma.1"
st.title("NIkhil's Portfolio")
#Side bar details
st.sidebar.title("NIkhil's Portfolio")
st.sidebar.image("photo.jpeg",caption="Master Thesis Student at NCC AB")
st.sidebar.markdown(""" ## Address & Contact Info
#### 98 Kärrhöksgatan,55612 Sweden  
#### _ :email: iamnikhilramesh@gamil.com _
#### _ :phone: +46 - 764439519 _
#### _ [Instagram](https://www.instagram.com/iamnikhilramesh/)  [Linkedin](https://www.linkedin.com/in/nikhil-ramesh-5125b7139/)  [Github](https://github.com/Iamnikhilramesh) _

 """)
about_me()

my_expander_p = st.beta_expander("Connect with me", expanded=True)
with my_expander_p:
    name,email,message = mail()
    message = """
    Subject: Portfolio

    This message is sent from Website""" + "Name : " + name + ", email : "+ email + "Message : " + message
    if st.button('Submit'):
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            st.success("Thank you for your request, Will get back to you soon")
        except Exception as e:
            print(e)

