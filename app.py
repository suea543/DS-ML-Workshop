import streamlit as st

st.set_page_config(
    page_title="💀 Graveyard Main Page", 
    page_icon="💀", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

st.title("💀 หน้าหลักแห่งสุสาน 🕯️")
st.write("### Boot Camp: Data Science and Machine Learning แห่งโลกหลังความตาย 👻")
st.markdown('### 💀 :coffin: 🐦‍⬛ ยมทูตแห่งข้อมูลมาแล้ว! 🪓 ✝️')
# For Grim Reaper or Tombstone images, you would use st.image(image_url)
# Example (uncomment and replace with actual URLs):
# st.image("https://example.com/grim_reaper.png", width=200)
# st.image("https://example.com/tombstone.png", width=150)

st.info("☠️ 7 วันแห่งการฝึกฝนอย่างเข้มข้นสู่การชำระล้างข้อมูล 🔪")

# --- Navigation Buttons (Theme-adjusted text) ---
if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ (จากโลกคนเป็น) "):
    st.switch_page("page/app1_discount_calc.py")
elif st.button("🖤 การทำความสะอาดข้อมูลของอืออ"):
    st.switch_page("dark_clean_อืออ.py")
elif st.button("⚰️ การทำความสะอาดข้อมูลของ nuch"):
    st.switch_page("graveyard_cleaner_nuch.py")
elif st.button("🧼 การทำความสะอาดข้อมูลของ clean_app"):
    st.switch_page("clean_app.py")
elif st.button("✨ การทำความสะอาดข้อมูลของอือ"):
    st.switch_page("enhanced_clean_อือ.py")






