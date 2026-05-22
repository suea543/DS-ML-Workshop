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
    /* Target Streamlit's main content area if needed for broader centering,
       but st.columns below is usually more robust for block-level centering. */
    /* .css-1d391kg.e16z1uVg1 {
        display: flex;
        flex-direction: column;
        align-items: center;
    } */

    .main-content-box {
        border: 3px solid yellow;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px; /* Space from top */
        margin-bottom: 20px; /* Space from bottom */
        width: 100%; /* Take full width of its parent flex item */
        max-width: 800px; /* Optional: limit width of the box */
        background-color: #1a1a1a; /* Dark background for the container */
        box-sizing: border-box; /* Include padding and border in the element's total width and height */
        text-align: center; /* Center text and inline elements within the box */
    }

    /* Adjust button styling within the container for better centering */
    .main-content-box .stButton > button {
        width: auto; /* Allow buttons to size based on content */
        min-width: 250px; /* Give buttons a minimum width */
        padding-left: 20px;
        padding-right: 20px;
        margin-top: 10px;
        margin-bottom: 10px;
        display: inline-block; /* Make button inline-block to respect text-align: center of parent */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Using st.columns to create a central empty column and place the content within the middle column
col1, col2, col3 = st.columns([1, 6, 1])

with col2: # All content will be placed within the central column
    st.markdown('<div class="main-content-box">', unsafe_allow_html=True)

    st.title("💀 หน้าหลักแห่งสุสาน 🕯️")
    st.write("### 👻 Boot Camp: Data Science and Machine Learning 👻")
    st.markdown('### 💀 :coffin: 🐦‍⬛ ยมทูตแห่งข้อมูลมาแล้ว! 🪓 ✝️')
    # For Grim Reaper or Tombstone images, you would use st.image(image_url)
    # Example (uncomment and replace with actual URLs):
    # st.image("https://example.com/grim_reaper.png", width=200)
    # st.image("https://example.com/tombstone.png", width=150)

    st.info("☠️ 7 วันแห่งการฝึกฝนอย่างเข้มข้นสู่การชำระล้างข้อมูล 🔪")

    # --- Navigation Buttons (Theme-adjusted text) ---
    if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
        st.switch_page("pages/app1_discount_calc.py")
    elif st.button("🖤 การทำความสะอาดข้อมูลของอืออ"):
        st.switch_page("pages/dark_clean_อืออ.py")
    elif st.button("⚰️ การทำความสะอาดข้อมูลของ nuch"):
        st.switch_page("pages/graveyard_cleaner_nuch.py")
    elif st.button("🧼 การทำความสะอาดข้อมูล"):
        st.switch_page("pages/clean_app.py")

    st.markdown('</div>', unsafe_allow_html=True)
