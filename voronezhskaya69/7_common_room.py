import streamlit as st

st.title("🧺 Бытовое пространство")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.image("рекреации_в69/прачечная_в69.jpg")
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
                        <h3>🧺 Прачечная | 1 ЭТАЖ</h3> 
                    </div>
                </div>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://t.me/Landromaticbot" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-telegram"></i></a>
                    <p style="margin: 0; font-size: 21px;">Оплата: в банкомате на 1-ом этаже или через 
                    телеграм-бот "Ландроматик"</p>
                </div>
        </div>
                """, unsafe_allow_html=True)
st.divider()

col4, col5 = st.columns([1, 2])
with col4:
    st.image("рекреации_в69/работник_бельевой_в69.jpg")
with col5:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>🛌 Бельевая | 1 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>Работник бельевой: Иванова Любовь Викторовна</p>  
            <br> 
            <p>В бельевой можно получить/поменять:</p>  
            <p>• подушку</p>
            <p>• одеяло</p>
            <p>• покрывало</p>
            <p>• шторы</p>
            <p>• наматрасник</p>
            <p>• полный комплект постельного белья</p>
            <br>
            <p>Постельное белье меняется 1 раз в неделю бесплатно: отдали грязное - тут же получили чистое.</p>
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>👕 Сушильные комнаты | 5, 6, 7, 10, 16 ЭТАЖИ</h3> 
                </div>
            </div> 
        <br>
        <p>🕐 24/7</p>
        <p>🔑 Ключ на охране</p> 
        <br>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>🔐 Камера хранения | 14, 15 ЭТАЖИ</h3> 
                </div>
            </div>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("**Контакты для связи:**")
st.write("Заведующий общежитием: Бровкина Наталья Анатольевна 👩🏼‍💼")
st.markdown("""
    <p>📞 <a href="tel:+78124589730,4938">(812) 458-97-30 доб. 4938</a></p>
            """, unsafe_allow_html=True)
st.write("Заместитель заведующего общежитием: Ерофеева Ангелина Олеговна 👩🏼‍💼")
st.markdown("""
    <p>📞 <a href="tel:+78124589730,4947">(812) 458-97-30 доб. 4947</a></p>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("🆘 Свяжитесь со студенческим советом через соответствующий раздел")
