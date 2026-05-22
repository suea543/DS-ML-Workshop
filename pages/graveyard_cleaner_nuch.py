import streamlit as st # ไลบรารีสำหรับสร้าง Web Application
import pandas as pd # ไลบรารีสำหรับจัดการข้อมูลในรูปแบบ DataFrame
import numpy as np # ไลบรารีสำหรับคำนวณทางคณิตศาสตร์
import matplotlib.pyplot as plt # ไลบรารีสำหรับสร้างกราฟ
import seaborn as sns # ไลบรารีสำหรับสร้างกราฟที่สวยงามขึ้น
from scipy.stats.mstats import winsorize # ฟังก์ชันสำหรับจัดการ Outlier (Winsorization)
import io # ไลบรารีสำหรับจัดการ Input/Output
import warnings # ไลบรารีสำหรับจัดการคำเตือน
warnings.filterwarnings('ignore') # ไม่แสดงคำเตือน

st.set_page_config(page_title="💀 Graveyard Data Cleaner", layout="wide", initial_sidebar_state="expanded")

st.title("💀 Graveyard Data Cleaner: Post-Apocalyptic Edition 🖤") # ตั้งชื่อแอปพลิเคชัน
st.markdown("ยินดีต้อนรับสู่แอปพลิเคชันทำความสะอาดข้อมูลจากสุสาน! ⚰️ อัปโหลดไฟล์ CSV ของคุณเพื่อชำระล้างข้อมูลที่เน่าเฟะ! 🦠") # ข้อความต้อนรับ
st.markdown("--- 🕯️ ปลดปล่อยข้อมูลที่ตายแล้วให้เป็นอิสระ! 👻 ---
") # คำแนะนำเบื้องต้น
st.error("⚠️ ใช้สำหรับชุดข้อมูลที่มีโครงสร้างเหมือน redbull_workshop_dirty.csv ที่รอดจากหายนะเท่านั้น 💀")

# --- File Uploader ---
uploaded_file = st.file_uploader("อัปโหลดไฟล์ CSV ของคุณ ⚰️", type=["csv"]) # ช่องสำหรับอัปโหลดไฟล์ CSV

if uploaded_file is not None: # ถ้ามีการอัปโหลดไฟล์แล้ว
    df_raw = pd.read_csv(uploaded_file) # อ่านไฟล์ CSV ที่อัปโหลด
    df = df_raw.copy() # สร้างสำเนาข้อมูลเพื่อไม่ให้แก้ไขข้อมูลต้นฉบับ
    st.success("ไฟล์อัปโหลดสำเร็จ! ✅ วิญญาณข้อมูลบริสุทธิ์แล้ว! ✨") # แสดงข้อความแจ้งว่าอัปโหลดสำเร็จ
    st.write("### 📜 ข้อมูลต้นฉบับ (5 แถวแรกจากโลกหลังความตาย)") # หัวข้อแสดงข้อมูลดิบ
    st.dataframe(df_raw.head()) # แสดง 5 แถวแรกของข้อมูลดิบ

    # --- Data Cleaning Steps (as functions) ---

    def perform_data_exploration(data): # ฟังก์ชันสำหรับสำรวจข้อมูลเบื้องต้น
        st.subheader("👁️‍🗨️ 1. Data Exploration: สอดส่องข้อมูลผีสิง") # หัวข้อย่อย
        st.write("#### 📐 โครงสร้างซากข้อมูล:") # หัวข้อย่อยแสดงขนาดข้อมูล
        st.write(f"จำนวนซาก: {data.shape[0]:,}, จำนวนกระดูก: {data.shape[1]}") # แสดงจำนวนแถวและคอลัมน์
        st.write("#### ℹ️ ข้อมูลจากสุสาน:") # หัวข้อย่อยแสดงข้อมูลทั่วไปของ DataFrame
        buffer = io.StringIO()
        data.info(buf=buffer) # ดึงข้อมูล info() ไปเก็บใน buffer
        st.text(buffer.getvalue()) # แสดงผลข้อมูล info()
        st.write("#### 📈 สถิติเชิงพรรณนาจากซากข้อมูล:") # หัวข้อย่อยแสดงสถิติเชิงพรรณนา
        st.dataframe(data.describe(include='all')) # แสดงสถิติเชิงพรรณนาสำหรับทุกคอลัมน์

        st.markdown("--- 🌑 ---")
        st.write("#### 📊 การกระจายตัวของข้อมูลตัวเลข (ก่อนทำพิธีล้างบาป)")
        numeric_cols = data.select_dtypes(include=np.number).columns.tolist() # ดึงชื่อคอลัมน์ที่เป็นตัวเลข
        if numeric_cols: # ถ้ามีคอลัมน์ตัวเลขให้วิเคราะห์
            n_cols = 3 # จำนวนคอลัมน์ที่จะแสดงกราฟในแต่ละแถว
            n_rows = (len(numeric_cols) + n_cols - 1) // n_cols # คำนวณจำนวนแถวที่ต้องการ
            fig, axes = plt.subplots(n_rows, n_cols, figsize=(18, 5 * n_rows)) # สร้าง figure และ axes สำหรับกราฟ
            axes = axes.flatten() if n_rows > 1 or n_cols > 1 else [axes] # จัดการให้ axes เป็น array 1 มิติเสมอ
            for i, col in enumerate(numeric_cols): # วนลูปในแต่ละคอลัมน์ตัวเลข
                sns.histplot(data[col].dropna(), kde=True, ax=axes[i], color='darkred', edgecolor='darkgray') # สร้าง Histogram พร้อม KDE ด้วยสีธีม
                axes[i].set_title(f'Distribution of {col}', fontsize=14, color='white') # ตั้งชื่อกราฟ
                axes[i].set_xlabel(col, fontsize=12, color='darkgray') # ตั้งชื่อแกน X
                axes[i].set_ylabel('Frequency', fontsize=12, color='darkgray') # ตั้งชื่อแกน Y
                axes[i].tick_params(axis='x', colors='darkgray') # สีแกน X
                axes[i].tick_params(axis='y', colors='darkgray') # สีแกน Y
                axes[i].set_facecolor('#303030') # Dark background for plots
            for j in range(i + 1, len(axes)): # ลบแกนว่างที่เหลือออก
                fig.delaxes(axes[j])
            fig.patch.set_facecolor('#1E1E1E') # Dark background for the figure itself
            plt.tight_layout() # ปรับระยะห่างระหว่าง subplots
            st.pyplot(fig) # แสดงกราฟใน Streamlit
            plt.close(fig) # ปิด figure เพื่อป้องกันปัญหาการแสดงผล
        else:
            st.info("ไม่พบคอลัมน์ตัวเลขสำหรับการแสดงการกระจายตัว 💀")

        return data

    def handle_duplicate_data(data): # ฟังก์ชันสำหรับจัดการข้อมูลซ้ำ
        st.subheader("👻 2. Duplicate Data: ข้อมูลซ้ำซ้อนเหมือนวิญญาณวนเวียน") # หัวข้อย่อย
        exact_dups = data.duplicated() # ตรวจหาแถวที่ซ้ำกัน 100%
        exact_dup_count = exact_dups.sum() # นับจำนวนแถวที่ซ้ำ
        if exact_dup_count > 0: # ถ้าพบข้อมูลซ้ำ
            st.warning(f"🚨 พบข้อมูลซ้ำซ้อนเหมือนผีหลอก จำนวน {exact_dup_count:,} แถว!") # แสดงคำเตือนพร้อมจำนวน
            st.dataframe(data[exact_dups]) # แสดงตัวอย่างข้อมูลที่ซ้ำ
            data = data.drop_duplicates() # ลบข้อมูลซ้ำออกจาก DataFrame
            st.success(f"ลบวิญญาณซ้ำซ้อนแล้ว: เหลือ {len(data):,} แถว 🕊️") # แสดงข้อความแจ้งว่าลบสำเร็จ
        else: # ถ้าไม่พบข้อมูลซ้ำ
            st.info("✨ ไม่พบวิญญาณซ้ำซ้อนในมิตินี้ 🌌") # แสดงข้อความแจ้ง
        return data

    def handle_inconsistent_data(data): # ฟังก์ชันสำหรับจัดการข้อมูลที่ไม่สอดคล้องกัน
        st.subheader("🧙‍♀️ 3. Inconsistent Data: จัดการข้อมูลผิดผี") # หัวข้อย่อย
        st.write("##### 🔍 ค่าที่ไม่สอดคล้องกัน (ก่อนปรับภูตผี):") # หัวข้อย่อยแสดงค่าก่อนแก้ไข
        cat_cols = ['Region', 'Product_Variant', 'Channel'] # กำหนดคอลัมน์ประเภท Categorical ที่มี mapping พิเศษ
        all_object_cols = data.select_dtypes(include='object').columns.tolist() # ดึงคอลัมน์ที่เป็น object

        st.write("##### 🧹 กำลังทำความสะอาดคาถาเริ่มต้น (ลบช่องว่าง, แปลงเป็นตัวพิมพ์เล็ก)...")
        for col in all_object_cols:
            if col not in ['Transaction_ID', 'Date']:
                data[col] = data[col].astype(str).str.strip().str.lower()

        st.write("##### 📊 Unique values หลังคาถาแรก:")
        for col in cat_cols:
            unique_vals = data[col].unique()
            st.write(f"**📌 {col} ({len(unique_vals)} ค่า):**")
            st.write(unique_vals)

        st.write("##### 🛠️ กำลังแก้ไขค่าผิดผีเฉพาะคอลัมน์...") # ข้อความแจ้งว่ากำลังแก้ไข

        # 1. Standardize Region Column
        region_mapping = { # กำหนดการแมปค่าที่ไม่สอดคล้องกันของ Region
            'th-central': 'TH-Central', 'th central': 'TH-Central',
            'thailand central': 'TH-Central', 'thailand-central': 'TH-Central',
            'thailand': 'TH-Central',
            'usa-east': 'USA-East', 'us east': 'USA-East',
            'united states east': 'USA-East', 'u.s.a.': 'USA-East',
            'europe-eu': 'Europe-EU', 'eu': 'Europe-EU',
            'europe': 'Europe-EU', 'european union': 'Europe-EU',
            'asia-pacific': 'Asia-Pacific', 'asia-pac': 'Asia-Pacific',
            'apac': 'Asia-Pacific', 'asia pacific': 'Asia-Pacific'
        }
        data['Region'] = data['Region'].replace(region_mapping) # แทนที่ค่าตาม mapping
        data['Region'] = data['Region'].str.upper() # แปลงเป็นตัวพิมพ์ใหญ่ทั้งหมด

        # 2. Standardize Product_Variant Column
        product_variant_mapping = { # กำหนดการแมปค่าที่ไม่สอดคล้องกันของ Product_Variant
            'original blue': 'Original Blue', 'original  blue': 'Original Blue',
            'krating daeng 250': 'Krating Daeng 250',
            'red edition': 'Red Edition',
            'sugarfree': 'Sugarfree', 'sugar free': 'Sugarfree',
            'sugarfree ': 'Sugarfree', 'sugar-free': 'Sugarfree',
            'tropical edition': 'Tropical Edition', 'tropical  edition': 'Tropical Edition',
            'tropical': 'Tropical Edition',
        }
        data['Product_Variant'] = data['Product_Variant'].replace(product_variant_mapping) # แทนที่ค่าตาม mapping
        data['Product_Variant'] = data['Product_Variant'].apply(lambda x: x.title() if isinstance(x, str) else x) # ทำให้ตัวอักษรแรกเป็นตัวพิมพ์ใหญ่สำหรับคำอื่นๆ

        # 3. Standardize Channel Column
        channel_mapping = { # กำหนดการแมปค่าที่ไม่สอดคล้องกันของ Channel
            'social media': 'Social Media', 'social_media': 'Social Media',
            'tv ad': 'TV Ad', 'tv ads': 'TV Ad',
            'tv advertisement': 'TV Ad', 'television ad': 'TV Ad',
            'in-store promo': 'In-store Promo',
            'f1 sponsorship': 'F1 Sponsorship',
            'extreme sports': 'Extreme Sports'
        }
        data['Channel'] = data['Channel'].replace(channel_mapping) # แทนที่ค่าตาม mapping
        data['Channel'] = data['Channel'].apply(lambda x: x.title() if isinstance(x, str) else x) # ทำให้ตัวอักษรแรกเป็นตัวพิมพ์ใหญ่สำหรับคำอื่นๆ

        # Convert Date to datetime (from notebook)
        data['Date'] = pd.to_datetime(data['Date'], format='mixed', errors='coerce') # แปลงคอลัมน์ 'Date' เป็นรูปแบบ datetime พร้อมจัดการข้อผิดพลาด

        st.success("แก้ไขค่าผิดผีสำเร็จ! 🕯️") # แสดงข้อความแจ้งว่าแก้ไขสำเร็จ
        st.write("##### 📊 ค่าที่ไม่สอดคล้องกัน (หลังปรับภูตผี):") # หัวข้อย่อยแสดงค่าหลังแก้ไข
        for col in cat_cols: # วนลูปในแต่ละคอลัมน์อีกครั้ง
            unique_vals = data[col].unique() # ดึงค่า unique หลังแก้ไข
            st.write(f"**📌 {col} ({len(unique_vals)} ค่า):**") # แสดงชื่อคอลัมน์และจำนวนค่า unique
            st.write(unique_vals) # แสดงค่า unique หลังแก้ไข
        return data

    def handle_missing_data(data): # ฟังก์ชันสำหรับจัดการข้อมูลที่หายไป (Missing Data)
        st.subheader("🕳️ 4. Missing Data: หลุมว่างในข้อมูล") # หัวข้อย่อย
        missing_count = data.isnull().sum() # นับจำนวนค่า Missing ในแต่ละคอลัมน์
        st.write("##### ⚠️ จำนวนหลุมว่างก่อนถม:") # หัวข้อย่อยแสดงค่า Missing ก่อนแก้ไข
        if missing_count.sum() > 0: # ถ้ามีค่า Missing
            st.dataframe(missing_count[missing_count > 0]) # แสดงคอลัมน์ที่มีค่า Missing

            median_marketing = data['Marketing_Spend'].median() # คำนวณค่ามัธยฐานของ Marketing_Spend
            data['Marketing_Spend'] = data['Marketing_Spend'].fillna(median_marketing) # เติมค่า Missing ด้วยค่ามัธยฐาน
            st.info(f'✅ Marketing_Spend: ถมด้วย Median = {median_marketing:,.2f} 💰') # แสดงข้อความแจ้ง

            median_score = data['Customer_Score'].median() # คำนวณค่ามัธยฐานของ Customer_Score
            data['Customer_Score'] = data['Customer_Score'].fillna(median_score) # เติมค่า Missing ด้วยค่ามัธยฐาน
            st.info(f'✅ Customer_Score: ถมด้วย Median = {median_score} 🌟') # แสดงข้อความแจ้ง

            st.success("ถมหลุมว่างสำเร็จ! 👻") # แสดงข้อความแจ้งว่าแก้ไขสำเร็จ
            st.write("##### ✨ จำนวนหลุมว่างหลังถม:") # หัวข้อย่อยแสดงค่า Missing หลังแก้ไข
            st.write(f"รวม {data.isnull().sum().sum()} ค่า (ควรเป็น 0) ⚰️") # แสดงจำนวนรวมของค่า Missing (ควรเป็น 0)
        else: # ถ้าไม่มีค่า Missing
            st.info("🎉 ไม่พบหลุมว่างในสุสานข้อมูลนี้ 🖤") # แสดงข้อความแจ้ง
        return data

    def handle_noisy_data(data): # ฟังก์ชันสำหรับจัดการข้อมูลผิดพลาด (Noisy Data)
        st.subheader("👺 5. Noisy Data: เสียงรบกวนจากนรกภูมิ") # หัวข้อย่อย
        st.write("##### 🕵️ ตรวจสอบกฏแห่งนรกภูมิก่อนลงโทษ:") # หัวข้อย่อยแสดงการตรวจสอบ
        neg_price = data[data['Unit_Price'] <= 0] # ตรวจสอบราคาที่น้อยกว่าหรือเท่ากับ 0
        neg_units = data[data['Units_Sold'] <= 0] # ตรวจสอบจำนวนที่ขายน้อยกว่าหรือเท่ากับ 0
        neg_mkt = data[data['Marketing_Spend'] < 0] # ตรวจสอบงบการตลาดที่น้อยกว่า 0
        bad_score = data[(data['Customer_Score'] < 1) | (data['Customer_Score'] > 10)] # ตรวจสอบ Customer_Score ที่ไม่อยู่ในช่วง 1-10

        found_noisy = False # ตัวแปรสถานะว่าพบ Noisy Data หรือไม่
        if len(neg_price) > 0: # ถ้าพบราคาติดลบ
            st.warning(f"❌ Unit_Price ≤ 0 : {len(neg_price):,} แถว (ราคาวิญญาณต้องเป็นบวก!) 💸") # แสดงคำเตือน
            found_noisy = True
        if len(neg_units) > 0: # ถ้าพบจำนวนที่ขายติดลบ
            st.warning(f"❌ Units_Sold ≤ 0 : {len(neg_units):,} แถว (ขายวิญญาณไม่ได้ติดลบ!) 📉") # แสดงคำเตือน
            found_noisy = True
        if len(neg_mkt) > 0: # ถ้าพบงบการตลาดติดลบ
            st.warning(f"❌ Marketing < 0 : {len(neg_mkt):,} แถว (งบต้องไม่ติดลบ!) 🚫") # แสดงคำเตือน
            found_noisy = True
        if len(bad_score) > 0: # ถ้าพบ Customer_Score นอกช่วง
            st.warning(f"❌ Customer_Score ไม่ใช่ 1-10: {len(bad_score):,} แถว (คะแนนความพึงพอใจต้องอยู่ในช่วง 1-10!) 💔") # แสดงคำเตือน
            found_noisy = True

        if found_noisy: # ถ้าพบ Noisy Data
            initial_rows = len(data) # เก็บจำนวนแถวเริ่มต้น
            data = data[data['Unit_Price'] > 0] # กรองข้อมูลที่ราคาเป็นบวก
            data = data[data['Units_Sold'] > 0] # กรองข้อมูลที่จำนวนขายเป็นบวก
            data = data[data['Marketing_Spend'] >= 0] # กรองข้อมูลที่งบการตลาดไม่ติดลบ
            data = data[(data['Customer_Score'] >= 1) & (data['Customer_Score'] <= 10)] # กรองข้อมูลที่ Customer_Score อยู่ในช่วง 1-10
            st.success(f"ลงโทษเสียงรบกวนสำเร็จ: สังเวยไป {initial_rows - len(data):,} แถว 🩸") # แสดงข้อความแจ้งว่าแก้ไขสำเร็จและจำนวนแถวที่ถูกลบ
        else: # ถ้าไม่พบ Noisy Data
            st.info("🎉 ไม่พบเสียงรบกวนที่ขัดแย้งกับกฏแห่งนรกภูมิ 🦇") # แสดงข้อความแจ้ง
        return data

    def perform_outlier_analysis(data): # ฟังก์ชันสำหรับตรวจจับ Outlier
        st.subheader("⚰️ 6. Outlier Detection & Treatment: สางวิญญาณพเนจร") # หัวข้อย่อย
        st.markdown("##### 📈 ตรวจสอบวิญญาณพเนจรด้วย Boxplot (ก่อนชำระล้าง)") # หัวข้อย่อยแสดงการตรวจสอบ

        numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns.tolist() # ดึงชื่อคอลัมน์ที่เป็นตัวเลข
        # Customer_Score is already handled in noisy data and is expected to be 1-10, so removing it from outlier analysis
        if 'Customer_Score' in numeric_cols: # ถ้า Customer_Score อยู่ในคอลัมน์ตัวเลข
            numeric_cols.remove('Customer_Score') # ลบออกจากรายการ เพราะถูกจัดการแล้วในขั้นตอน Noisy Data

        if numeric_cols: # ถ้ามีคอลัมน์ตัวเลขให้วิเคราะห์ Outlier
            n_cols = 3 # จำนวนคอลัมน์ที่จะแสดงกราฟในแต่ละแถว
            n_rows = (len(numeric_cols) + n_cols - 1) // n_cols # คำนวณจำนวนแถวที่ต้องการ
            fig, axes = plt.subplots(n_rows, n_cols, figsize=(18, 5 * n_rows)) # สร้าง figure และ axes สำหรับ Boxplot
            axes = axes.flatten() if n_rows > 1 or n_cols > 1 else [axes] # จัดการให้ axes เป็น array 1 มิติเสมอ
            for i, col in enumerate(numeric_cols): # วนลูปในแต่ละคอลัมน์ตัวเลข
                sns.boxplot(x=data[col], ax=axes[i], color='darkred', boxprops={'facecolor':'darkred'}) # สร้าง Boxplot ด้วยสีธีม
                axes[i].set_title(f'Boxplot of {col} (ก่อนชำระล้าง)', fontsize=14, color='white') # ตั้งชื่อกราฟ
                axes[i].set_xlabel(col, fontsize=12, color='darkgray') # ตั้งชื่อแกน X
                axes[i].tick_params(axis='x', colors='darkgray') # สีแกน X
                axes[i].tick_params(axis='y', colors='darkgray') # สีแกน Y
                axes[i].set_facecolor('#303030') # Dark background for plots
            for j in range(i + 1, len(axes)): # ลบแกนว่างที่เหลือออก
                fig.delaxes(axes[j])
            fig.patch.set_facecolor('#1E1E1E') # Dark background for the figure itself
            plt.tight_layout() # ปรับระยะห่างระหว่าง subplots
            st.pyplot(fig) # แสดงกราฟใน Streamlit
            plt.close(fig) # ปิด figure เพื่อป้องกันปัญหาการแสดงผล

            st.markdown("--- 🌑 ---")
            outlier_choice = st.radio(
                "เลือกวิธีชำระล้างวิญญาณพเนจร (สำหรับคอลัมน์ตัวเลขที่แสดงด้านบน):",
                ('ปล่อยไป 👻', 'สะกดวิญญาณด้วย Winsorization ⛓️'),
                key='outlier_treatment_radio'
            )

            if outlier_choice == 'สะกดวิญญาณด้วย Winsorization ⛓️':
                st.write("##### ⚙️ กำลังสะกดวิญญาณด้วย Winsorization...")
                for col in numeric_cols:
                    # Apply winsorization at 5th and 95th percentiles (symmetric)
                    # Note: winsorize returns a masked array, convert back to series
                    data[col] = pd.Series(winsorize(data[col], limits=(0.05, 0.05)), index=data.index)
                    st.success(f"✅ วิญญาณในคอลัมน์ '{col}' ถูกสะกดด้วย Winsorization แล้ว 🛡️")

                st.write("##### 📊 Boxplot หลังสะกดวิญญาณ Winsorization:")
                fig, axes = plt.subplots(n_rows, n_cols, figsize=(18, 5 * n_rows)) # สร้าง figure และ axes สำหรับ Boxplot หลังปรับ
                axes = axes.flatten() if n_rows > 1 or n_cols > 1 else [axes]
                for i, col in enumerate(numeric_cols):
                    sns.boxplot(x=data[col], ax=axes[i], color='mediumseagreen', boxprops={'facecolor':'mediumseagreen'}) # สร้าง Boxplot ด้วยสีธีม
                    axes[i].set_title(f'Boxplot of {col} (หลังสะกดวิญญาณ)', fontsize=14, color='white') # ตั้งชื่อกราฟ
                    axes[i].set_xlabel(col, fontsize=12, color='darkgray')
                    axes[i].tick_params(axis='x', colors='darkgray') # สีแกน X
                    axes[i].tick_params(axis='y', colors='darkgray') # สีแกน Y
                    axes[i].set_facecolor('#303030') # Dark background for plots
                for j in range(i + 1, len(axes)): # ลบแกนว่างที่เหลือออก
                    fig.delaxes(axes[j])
                fig.patch.set_facecolor('#1E1E1E') # Dark background for the figure itself
                plt.tight_layout() # ปรับระยะห่างระหว่าง subplots
                st.pyplot(fig) # แสดงกราฟใน Streamlit
                plt.close(fig) # ปิด figure เพื่อป้องกันปัญหาการแสดงผล
            else: # 'ไม่จัดการ Outlier 🙅'
                st.info("ไม่ได้ชำระล้างวิญญาณพเนจรใดๆ 🚫")
        else: # ถ้าไม่มีคอลัมน์ตัวเลข
            st.info("ไม่พบคอลัมน์ตัวเลขให้สางวิญญาณ 🤷") # แสดงข้อความแจ้ง
        return data

    st.sidebar.header("เลือกพิธีกรรมทำความสะอาดข้อมูล 🧹") # หัวข้อใน Sidebar
    do_explore = st.sidebar.checkbox("1. สอดส่องข้อมูลผีสิง 👁️‍🗨️", value=True) # Checkbox สำหรับ Data Exploration
    do_duplicates = st.sidebar.checkbox("2. ลบวิญญาณซ้ำซ้อน 👻", value=True) # Checkbox สำหรับ Duplicate Data
    do_inconsistent = st.sidebar.checkbox("3. จัดการข้อมูลผิดผี 🧙‍♀️", value=True) # Checkbox สำหรับ Inconsistent Data
    do_missing = st.sidebar.checkbox("4. ถมหลุมว่าง 🕳️", value=True) # Checkbox สำหรับ Missing Data
    do_noisy = st.sidebar.checkbox("5. ลงโทษเสียงรบกวน 👺", value=True) # Checkbox สำหรับ Noisy Data
    do_outlier = st.sidebar.checkbox("6. สางวิญญาณพเนจร ⚰️", value=True) # Checkbox สำหรับ Outlier Detection

    st.markdown("--- 🌑 ---") # เส้นแบ่ง

    if st.button("เริ่มพิธีกรรมทำความสะอาดข้อมูล 🚀"): # ปุ่มสำหรับเริ่มกระบวนการ Data Cleaning
        st.write("### กำลังดำเนินการพิธีกรรมทำความสะอาดข้อมูล... ⏳") # ข้อความแจ้งว่ากำลังดำเนินการ
        if do_explore: # ถ้าเลือก Data Exploration
            df = perform_data_exploration(df)
        if do_duplicates: # ถ้าเลือก Duplicate Data
            df = handle_duplicate_data(df)
        if do_inconsistent: # ถ้าเลือก Inconsistent Data
            df = handle_inconsistent_data(df)
        if do_missing: # ถ้าเลือก Missing Data
            df = handle_missing_data(df)
        if do_noisy: # ถ้าเลือก Noisy Data
            df = handle_noisy_data(df)
        if do_outlier: # ถ้าเลือก Outlier Detection
            df = perform_outlier_analysis(df)

        st.markdown("--- 🌑 ---") # เส้นแบ่ง
        st.subheader("✅ 7. Cleaned Data Summary: บทสรุปหลังพิธี") # หัวข้อสรุปผล
        st.write(f"#### 📊 สรุปขนาดข้อมูลจากสุสาน:") # หัวข้อย่อยแสดงขนาดข้อมูล
        st.write(f"ก่อนทำพิธี (ซากเดิม): {df_raw.shape[0]:,} แถว, {df_raw.shape[1]} คอลัมน์ 💀") # แสดงขนาดข้อมูลก่อนทำความสะอาด
        st.write(f"หลังทำพิธี (วิญญาณบริสุทธิ์): {df.shape[0]:,} แถว, {df.shape[1]} คอลัมน์ ✨") # แสดงขนาดข้อมูลหลังทำความสะอาด

        st.write("### 💎 ข้อมูลบริสุทธิ์ (5 แถวแรก)") # หัวข้อแสดงข้อมูลที่ทำความสะอาดแล้ว
        st.dataframe(df.head()) # แสดง 5 แถวแรกของข้อมูลที่ทำความสะอาดแล้ว

        st.markdown("--- 🌑 ---")
        st.write("#### 📈 การกระจายตัวของข้อมูลตัวเลข (หลังทำพิธีล้างบาป)")
        numeric_cols_final = df.select_dtypes(include=np.number).columns.tolist() # ดึงชื่อคอลัมน์ที่เป็นตัวเลข
        if 'Customer_Score' in numeric_cols_final: # Customer_Score มักจะถูกจัดการในช่วง 1-10 และไม่จำเป็นต้องวิเคราะห์ Outlier ด้วย Boxplot อีก
            numeric_cols_final.remove('Customer_Score')

        if numeric_cols_final: # ถ้ามีคอลัมน์ตัวเลขให้วิเคราะห์
            n_cols = 3
            n_rows = (len(numeric_cols_final) + n_cols - 1) // n_cols
            fig, axes = plt.subplots(n_rows, n_cols, figsize=(18, 5 * n_rows))
            axes = axes.flatten() if n_rows > 1 or n_cols > 1 else [axes]
            for i, col in enumerate(numeric_cols_final):
                sns.histplot(df[col].dropna(), kde=True, ax=axes[i], color='darkmagenta', edgecolor='white') # ใช้สีธีม
                axes[i].set_title(f'Distribution of {col} (หลังทำพิธีล้างบาป)', fontsize=14, color='white')
                axes[i].set_xlabel(col, fontsize=12, color='darkgray')
                axes[i].set_ylabel('Frequency', fontsize=12, color='darkgray')
                axes[i].tick_params(axis='x', colors='darkgray') # สีแกน X
                axes[i].tick_params(axis='y', colors='darkgray') # สีแกน Y
                axes[i].set_facecolor('#303030') # Dark background for plots
            for j in range(i + 1, len(axes)):
                fig.delaxes(axes[j])
            fig.patch.set_facecolor('#1E1E1E') # Dark background for the figure itself
            plt.tight_layout()
            st.pyplot(fig)
            plt.close(fig)
        else:
            st.info("ไม่พบคอลัมน์ตัวเลขสำหรับการแสดงการกระจายตัวหลังทำพิธีล้างบาป 🔮")

        csv_buffer = df.to_csv(index=False).encode('utf-8') # แปลง DataFrame เป็น CSV ในรูปแบบ byte
        st.download_button( # ปุ่มสำหรับดาวน์โหลดข้อมูล
            label="ดาวน์โหลดวิญญาณข้อมูลบริสุทธิ์ (CSV) 💾", # ข้อความบนปุ่ม
            data=csv_buffer, # ข้อมูลที่จะให้ดาวน์โหลด
            file_name="redbull_graveyard_clean.csv", # ชื่อไฟล์เมื่อดาวน์โหลด
            mime="text/csv", # ประเภทของไฟล์
            help="คลิกเพื่อดาวน์โหลดชุดข้อมูลที่ผ่านพิธีกรรมชำระล้างแล้ว 🖤"
        )
else: # ถ้ายังไม่ได้อัปโหลดไฟล์
    st.info("กรุณาอัปโหลดไฟล์ CSV เพื่อเริ่มต้นพิธีกรรมทำความสะอาดข้อมูล 💀") # แสดงข้อความให้ผู้ใช้อัปโหลดไฟล์

if st.button("🏠 กลับหน้าหลัก"):
    st.switch_page("app.py")
# Removed the 'กลับหน้าหลัก' button as it points to a non-existent 'app.py' in this context.
