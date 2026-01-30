import streamlit as st
from utils import get_playlist_id, get_playlist_duration, format_time

st.set_page_config(page_title="YouTube Playlist Calculator", page_icon="📺")

st.title("📺 Playlist Duration Calculator")
st.write("See exactly how long that YouTube playlist is—and how much time you save at 2x speed!!")

with st.expander("⚙️ API Settings", expanded=False):
    st.caption("You need a YouTube Data API Key to use this app.")
    api_key = st.text_input("Enter API Key", type="password", help="Get this from Google Cloud Console")

url = st.text_input("🔗 Paste YouTube Playlist URL", placeholder="https://www.youtube.com/playlist?list=...")

if st.button("Calculate Duration", type="primary"):
    if not api_key:
        st.error("⚠️ Please enter your API Key in the settings above.")
    elif not url:
        st.error("⚠️ Please paste a URL first.")
    else:
        with st.spinner("Fetching video details from YouTube..."):
            try:
                pl_id = get_playlist_id(url)

                if pl_id:
                    total_seconds, video_count = get_playlist_duration(api_key, pl_id)

                    time_1x = format_time(total_seconds)
                    time_1_5x = format_time(total_seconds / 1.5)
                    time_2x = format_time(total_seconds / 2)

                    with st.container(border=True):
                        st.subheader(f"✅ Found {video_count} videos")
                        st.divider()

                        col1, col2, col3 = st.columns(3)

                        with col1:
                            st.metric(label="🐢 Normal Speed (1x)", value=time_1x)
                        with col2:
                            st.metric(label="🐇 1.5x Speed", value=time_1_5x)
                        with col3:
                            st.metric(label="🚀 2x Speed", value=time_2x)
                
                else:
                    st.error("❌ Invalid Playlist URL. Please check the link.")
            
            except Exception as e:
                st.error(f"Something went wrong: {e}")