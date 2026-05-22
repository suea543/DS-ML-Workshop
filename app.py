import streamlit as st

st.set_page_config(
    page_title="💀 Graveyard Main Page",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom CSS for a bordered and centered container
st.markdown(
    """
    <style>
    .main-content-box {
        border: 3px solid yellow;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        margin-bottom: 20px;
        width: 100%;
        max-width: 800px;
        background-color: #1a1a1a;
        box-sizing: border-box;
        text-align: center;
    }
    /* Streamlit buttons by default take full width of their parent. */
    /* To center them when they are not full width, we use st.columns for each button. */
    </style>
    """,
    unsafe_allow_html=True
)

# Using st.columns to create a central empty column and place the content within the middle column
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    st.markdown('<div class="main-content-box">', unsafe_allow_html=True)

    st.title("💀 หน้าหลักแห่งสุสาน 🕯️")
    st.write("### 👻 Boot Camp: Data Science and Machine Learning 👻")
    st.markdown('### 💀 :coffin: 🐦‍⬛ ยมทูตแห่งข้อมูลมาแล้ว! 🪓 ✝️')

    st.info("☠️ 7 วันแห่งการฝึกฝนอย่างเข้มข้นสู่การชำระล้างข้อมูล 🔪")

    # --- Navigation Buttons (Theme-adjusted text) ---
    # Each button wrapped in st.columns for explicit centering
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"): # Button for app1_discount_calc
            st.switch_page("pages/app1_discount_calc")

    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if st.button("🖤 การทำความสะอาดข้อมูลของอืออ"): # Button for dark_clean_อืออ
            st.switch_page("pages/dark_clean_อืออ")

    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if st.button("⚰️ การทำความสะอาดข้อมูลของ nuch"): # Button for graveyard_cleaner_nuch
            st.switch_page("pages/graveyard_cleaner_nuch")

    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if st.button("🧼 การทำความสะอาดข้อมูล"): # Button for clean_app
            st.switch_page("pages/clean_app")

    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if st.button("✨ การทำความสะอาดข้อมูลของอือ (เวอร์ชันปรับปรุง)"): # Button for enhanced_clean_อือ
            st.switch_page("pages/enhanced_clean_อือ")

    st.markdown('</div>', unsafe_allow_html=True)
