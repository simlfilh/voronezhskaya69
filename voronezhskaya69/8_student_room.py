import streamlit as st

st.title("🚻 Студенческое пространство")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.image("рекреации_в69/коворкинг_в69.jpg")
with col2:
    st.markdown("""
        <style>
            .colored-container {
               background-color: #FFFFFF; 
               border-radius: 10px;      
               padding: 20px;           
               margin-bottom: 20px;   
               color: black !important;
               line-height: 1.0;
               font-size: 21px;
            }
            .highlight-green {
                background-color: #C8E6C9;  
                border-radius: 10px;
                padding-left: 20px;
                margin-bottom: 20px;
                position: relative;
            }
            .highlight-red {
                background-color: #FFCDD2;  
                border-radius: 10px;
                padding-left: 20px;
                margin-bottom: 20px;
                position: relative;
            }
            .highlight-blue {
                background-color: #B3E5FC;
                border-radius: 10px;
                padding-left: 20px;
                margin-bottom: 20px;
                position: relative;
            }
            .text-indent-content {
                position: relative;
                color: black;
                line-height: 1.4;
            }
        </style>
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>1 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>💻 Коворкинг | Кафе | Зона отдыха</p> 
            <p>🕐 24/7</p>
            <p>🔑 Ключ на охране</p> 
        </div>
                """, unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.image("рекреации_в69/комната_отдыха_в69.jpg")
with col4:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>Комнаты отдыха</h3> 
                    </div>
                </div> 
            <p>2 ЭТАЖ | Комната творчества 🎨 </p> 
            <p>4 ЭТАЖ | Комната дружбы 👭🏻</p> 
            <p>8 ЭТАЖ | Комната красоты 💅🏻 </p> 
            <p>11 ЭТАЖ | Музыкальная комната 🎶 </p> 
            <p>13 ЭТАЖ | Комната времени ⏳</p> 
            <br>
            <p>🕐 24/7</p>
            <p>🔑 Ключ на охране</p> 
        </div>
                """, unsafe_allow_html=True)

col5, col6 = st.columns(2)
with col5:
    st.image("рекреации_в69/спортзал_в69.jpg")
with col6:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>1 И 3 ЭТАЖИ</h3> 
                    </div>
                </div> 
            <p>💪🏼 Спортзал №1, №2</p>
            <p>🕐 9:00 — 22:00</p>
            <p>🔑 Ключ на охране</p> 
        </div>
                """, unsafe_allow_html=True)

col7, col8 = st.columns(2)
with col7:
    st.image("рекреации_в69/учебная_комната_в69.jpg")
with col8:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>9 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>📚 Учебная комната</p>
            <p>🕐 24/7</p>
            <p>🔑 Ключ на охране</p> 
        </div>
                """, unsafe_allow_html=True)

col9, col10 = st.columns(2)
with col9:
    st.image("рекреации_в69/библиотека_в69.jpg")
with col10:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>14 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>📚 Библиотека</p>
            <p>🕐 24/7</p>
            <p>🔑 Ключ на охране</p>
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.markdown("**Контакты для связи:**")
st.write("Заведующий общежитием: Бровкина Наталья Анатольевна 👩🏼‍💼")
st.markdown("""
    <style>
        .custom-links a {
            color: white !important;
            text-decoration: none; 
        }
        .custom-links a:hover {
            color: #ccc !important;  
            text-decoration: underline; 
        }
    </style>
    <div class="custom-links">
        <p>📞 <a href="tel:+78124589730,4938">(812) 458-97-30 доб. 4938</a></p>
    </div>
""", unsafe_allow_html=True)

st.write("Заместитель заведующего общежитием: Ерофеева Ангелина Олеговна 👩🏼‍💼")
st.markdown("""
    <div class="custom-links">
        <p>📞 <a href="tel:+78124589730,4947">(812) 458-97-30 доб. 4947</a></p>
    </div>
""", unsafe_allow_html=True)
st.divider()

# st.markdown("🆘 Свяжитесь со студенческим советом через соответствующий раздел")
