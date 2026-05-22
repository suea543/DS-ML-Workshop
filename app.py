import streamlit as st

st.set_page_config(
    page_title="💀 Graveyard Main Page",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Centering the title and subtitle
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    st.title("💀 Boot Camp 🕯️")
    st.write("### 👻 Data Science and Machine Learning 👻")
    st.markdown('### 💀 :coffin: 🐦‍⬛ 🪓 ✝️')
# For Grim Reaper or Tombstone images, you would use st.image(image_url)
# Example (uncomment and replace with actual URLs):
# st.image("https://example.com/grim_reaper.png", width=200)
# st.image("https://example.com/tombstone.png", width=150)

st.info("☠️ 7 Day Intensive Hands-on Workshop 🔪")

# --- Navigation Buttons (Theme-adjusted text) ---
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
        st.switch_page("pages/app1_discount_calc")
with col2:
    if st.button("🖤 การทำความสะอาดข้อมูล"):
        st.switch_page("pages/dark_clean_อืออ")
with col3:
    if st.button("⚰️ การทำความสะอาดข้อมูล"):
        st.switch_page("pages/graveyard_cleaner_nuch")
with col4:
    if st.button("🧼 การทำความสะอาดข้อมูล "):
        st.switch_page("pages/clean_app")
with col5:
    if st.button("✨ การทำความสะอาดข้อมูลของอือ"):
        st.switch_page("pages/enhanced_clean_อือ")
        st.switch_page("enhanced_clean_อือ")
