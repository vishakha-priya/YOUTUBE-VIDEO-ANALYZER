import streamlit as st
from youtube_analyzer import build_youtube_agent
st.set_page_config(
    page_title="Youtube Video Analyzer",
    layout="centered"
)
st.title("🎥 AI Youtube Vedio Analyzer")

#cache-fast access,temp storage=>most freq access
@st.cache_resource
def get_agent():
    return build_youtube_agent()
agent=get_agent()

# imput box
video_url=st.text_input("Enter Youtube Video Link") #str
button=st.button("Analyze video") # True/False
if video_url and button:
    with st.spinner("analyze Video......"):
        response=agent.run(
            f"Analyze this video :{video_url}"

        )
    st.markdown("analysis report on video")
    st.markdown(response.content)