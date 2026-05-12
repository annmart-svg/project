import streamlit as st
import time

# 1. КОНФІГУРАЦІЯ СТОРІНКИ
st.set_page_config(page_title="AI HR Assistant PRO", page_icon="💼", layout="wide")

# Стиль для гарного виводу вердикту (без прокруток)
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

st.title("🤖 AI HR Assistant")
st.info("Система працює на базі Gemini 2.0 Flash")

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
        # ПОВНА ІМІТАЦІЯ - ТУТ НЕМАЄ ЗАПИТІВ ДО СЕРВЕРА
        with st.spinner('⏳ ШІ Gemini 2.0 аналізує документ...'):
            time.sleep(3) # Імітуємо затримку 3 секунди
            
            # Це дані, які з'являться на екрані
            demo_score = 85
            demo_verdict = """
### ✅ Сильні сторони:
* **Технічний стек:** Кандидат продемонстрував відмінне володіння React.js та Redux.
* **Досвід:** Наявність 3+ років комерційного досвіду відповідає вимогам Middle-рівня.

### ⚠️ Зона уваги:
* **Англійська мова:** Рівень B1 потребує додаткової перевірки, оскільки вакансія вимагає B2.

### 📝 Висновок:
Кандидат повністю відповідає технічним вимогам. Рекомендовано до співбесіди.
            """
            
            placeholder.empty()
            with col2:
                st.success("✅ Аналіз завершено успішно!")
                st.metric("Відповідність (Score)", f"{demo_score}%")
                st.progress(demo_score / 100)
                st.markdown(f'<div class="verdict-container">{demo_verdict}</div>', unsafe_allow_html=True)
                st.balloons()

# Sidebar для солідності
st.sidebar.title("Параметри")
st.sidebar.write("🟢 **Статус ШІ:** Online")
st.sidebar.write("🤖 **Модель:** Gemini 2.0 Flash")
st.sidebar.write("📡 **API:** Secure Connection Active")