import streamlit as st
import time
import PyPDF2

# 1. КОНФІГУРАЦІЯ
st.set_page_config(page_title="AI HR Assistant PRO", page_icon="💼", layout="wide")

# Стиль (без прокруток)
st.markdown("""
    <style>
    .verdict-container {
        background-color: #f0f7ff;
        padding: 25px;
        border-radius: 12px;
        border-left: 8px solid #007bff;
        color: #212529;
        font-size: 1.1rem !important;
        line-height: 1.6;
        width: 100%;
        white-space: pre-wrap;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 AI HR Assistant (Demo Mode)")
st.info("Режим презентації: Система працює в автономному режимі для демонстрації UI.")

col1, col2 = st.columns([1, 1])

with col1:
    st.write("### 📂 Вхідні дані")
    uploaded_file = st.file_uploader("Оберіть файл резюме (PDF)", type="pdf")
    vacancy_name = st.text_input("Назва посади", "Frontend Developer (React)")
    vacancy_desc = st.text_area("Вимоги вакансії", height=200, 
        value="Шукаємо спеціаліста з досвідом React, JavaScript та знанням англійської на рівні B2.")

with col2:
    st.write("### 📊 Результат аналізу")
    placeholder = st.empty()
    placeholder.info("Завантажте файл та натисніть кнопку для аналізу.")

if st.button("🚀 ЗАПУСТИТИ ШІ-АНАЛІЗ", use_container_width=True):
    if not uploaded_file:
        st.warning("Будь ласка, завантажте PDF файл.")
    else:
        # Імітація роботи ШІ
        with st.spinner('ШІ аналізує документ за допомогою Gemini 2.0...'):
            time.sleep(3) # "Думаємо" 3 секунди для реалістичності
            
            # Демо-дані для красивого скріншота
            demo_score = 85
            demo_verdict = """
### ✅ Сильні сторони:
* **Технічний стек:** Кандидат має глибокі знання React та сучасного JavaScript (ES6+), що повністю відповідає вакансії.
* **Досвід:** 3 роки комерційного досвіду в розробці інтерфейсів.
* **Освіта:** Профільна технічна освіта та наявність актуальних сертифікатів.

### ⚠️ Зона уваги:
* **Англійська мова:** У резюме вказано рівень B1, тоді як вакансія вимагає B2. Потрібна додаткова перевірка на співбесіді.

### 📝 Висновок:
Кандидат є дуже перспективним. Рекомендую призначити технічне інтерв'ю.
            """
            
            placeholder.empty()
            with col2:
                st.success("Аналіз успішно завершено!")
                st.metric("Відповідність (Score)", f"{demo_score}%")
                st.progress(demo_score / 100)
                st.markdown(f'<div class="verdict-container">{demo_verdict}</div>', unsafe_allow_html=True)
                st.balloons()

st.sidebar.markdown("---")
st.sidebar.write("⚡ **Статус API:** Connected (Mock)")
st.sidebar.write("🤖 **Модель:** Gemini 2.0 Flash")
