import streamlit as st

st.set_page_config(page_title="Low-Fi Nance Band", page_icon="🎸", layout="wide")
st.title("STEMist Hackathon - Project")
st.markdown("## [Low-Fi Nance Band](https://github.com/mukund1606/Low-Fi-Nance-Band)")
st.subheader("Project Description - ")
st.markdown(
    """- The Low-Fi Nance Band is a set of virtual Instruments and lyrics generator.
- This project uses Python web-scraping techinques to scrape chatGPT to generate lyrics."""
)
st.divider()

st.subheader("Team Members - ")
st.markdown(
    """
    - [Anupam Tiwari](https://github.com/anupam-tiwari)
    - [Jennica](https://github.com/JennicaANK)
    - [Mukund Mittal](https://github.com/mukund1606)
    - [Nina Chung](https://github.com/chungy1)
    """
)

st.divider()

st.header("Idea Inspiration - ")
st.markdown("""""")

st.divider()

st.header("What is Does - ")
st.markdown(
    """
            - Low-Fi Nance Band is a set of virtual instruments and lyrics generator.
            
            - It provides a platform for users to create their own music and lyrics.
            
            - It also provides users a virtual experience of playing instruments.
            """
)

st.divider()

st.header("Technologies Used - ")
st.markdown(
    """
            - We used python as our programming language because of its simplicity, easy to use and vast support of libraries.
            - Used streamlit to create the front-end of our project.
            - Used selenium to scrape chatGPT to generate lyrics.
            - Also, we used openCV to create a virtual experience of playing instruments.
            - And, at last, we created little fun tool (Virtual Painter) to let users draw on the screen.
            """
)

st.divider()

st.header("Challenges we ran into - ")
st.markdown(
    """
            #### We faced many challenges while building this project. Some of them are -
            - We faced many challenges while scraping chatGPT to generate lyrics as chatGPT is not a static website so we had to use selenium to scrape it.
            - Next we had challange taking video input from the user and then processing it to create a virtual experience of playing instruments.
                - For this we used WebRTC (Web Real-Time Communication) to take video input from the user and pass it to the OpenCV to process it.
            - Next, challenge was to create sounds of the instruments. For this we used PyGame library to play sounds.
            - And, at last, we had challenge to combine all the parts together to create a single project.
                - For this we used streamlit to create the front-end of our project.
                
            """
)

st.divider()

st.header("Accomplishments we are proud of - ")
st.markdown(
    """
            #### After facing many challenges, we were able to accomplish many things. 
            - We were able to scrape chatGPT to generate lyrics. We used cookies to bypass the login page of chatGPT.
            - We were able to create a virtual experience of playing instruments. We used 60fps to create a smooth experience.
            - We were able to create a little fun tool (Virtual Painter) to let users draw on the screen.
            
            """
)

st.divider()

st.header("What we learned - ")
st.markdown(
    """
            #### We learned many new things while building this project. Some of them are -
            - We learned how to use selenium to scrape dynamic websites.
            - We learned how to use WebRTC to take video input from the user.
            - We learned how to use streamlit to create the front-end of our project.
            """
)

st.divider()

st.header("What's next for Low-Fi Nance Band - ")
st.markdown(
    """
            #### After completing this project, we have few ideas to improve it. Some of them are -
            - We can add more instruments to our project.
            - We can add real-time play with friends feature to our project.
            - We can also add more fun tools to our project.
            - And, at last, we can improve the UI of our project and host it on a cloud platform.
            """
)

st.divider()

st.header("Installation and Setup - ")
st.caption("To run this project on your local machine, follow the steps given below -")
"""
```bash
git clone git@github.com:mukund1606/Low-Fi-Nance-Band.git
cd Low-Fi-Nance-Band
python3 -m venv venv -r packages.txt
sudo apt install < packages.txt # Not Sure About This. I am Windows User
```

### Setup Environment Variables for ChatGPT Lyrics Generation
#### Obtaining SESSION_TOKEN for ChatGPT

1. Go to https://chat.openai.com/chat and open the developer tools by `F12`.
2. Find the `__Secure-next-auth.session-token` cookie in `Application` > `Storage` > `Cookies` > `https://chat.openai.com`.
3. Copy the value in the `Cookie Value` field.
"""
st.image("src/assets/SESSION.png", caption="SESSION_TOKEN")

"""

#### Get Conversation ID from URL(Optional)"""

st.image("src/assets/CONVERSATION.png", caption="CONVERSATION_ID")
"""

### .env File -
```bash 
SESSION_TOKEN="SESSION_TOKEN"
CONVERSATION_ID="CONVERSATION_ID"
```"""


st.divider()


st.header("Project Demo -")
st.caption("Now Let's dive into the demo of our project.")
st.caption("")
st.markdown(
    """<iframe src="https://www.youtube.com/embed/4DacWibbhYM" style="width:100%;aspect-ratio:16/9;" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>""",
    unsafe_allow_html=True,
)
st.divider()
