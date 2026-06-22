import streamlit as st

st.title("🏠 Общежитие СПбГЭУ №4")
st.divider()

st.subheader("Приветствуем вас, дорогие студенты, в нашем общежитии!")
st.subheader("Мы рады, что вы стали частью нашей дружной студенческой семьи!")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
        <style>
            .colored-container {
               background-color: #FFFFFF;  
               border-radius: 10px;      
               padding: 20px;            
               margin-bottom: 10px;      
               color: black !important;  
               line-height: 1.0;
               font-size: 21px;
            }
            .image-container {
               background-color: #FFFFFF; 
               border-radius: 10px;      
               padding: 20px;            
               margin-bottom: 10px;      
               height: 100%;           
               display: flex;
               align-items: center;     
               justify-content: center; 
            }
            .image-container img {
               max-width: 100%;
               max-height: 100%;
               border-radius: 5px;     
               object-fit: contain;    
            }
            .highlight-green {
                background-color: #C8E6C9; 
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
                position: relative;
            }
            .highlight-blue {
                background-color: #B3E5FC;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
                position: relative;
            }
            .text-indent-content {
                position: relative;
                color: black;
                line-height: 1.4;
            }
        </style>
        <div class="colored-container">
            <h3>Адрес: Санкт-Петербург, Воронежская ул., д. 69</h3>
                <div class="text-indent-content">
                    <p class="highlight-blue">Наиболее удобные маршруты:</p>
                </div>
            <br>  
            <p>→ от м. Обводный канал 10 минут пешком</p>
            <br>
        </div>
                """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class="colored-container">
            <h3>Мы в Яндекс Картах ⬇️</h3>
        </div>
                """, unsafe_allow_html=True)
    st.components.v1.html("""
        <div style="position:relative;overflow:hidden;">
            <a href="https://yandex.ru/maps/2/saint-petersburg/?utm_medium=mapframe&utm_source=maps" 
                style="color:#eee;font-size:12px;position:absolute;top:0px;">
                Санкт‑Петербург
            </a>
            <a href="https://yandex.ru/maps/2/saint-petersburg/?indoorLevel=1&ll=30.347349%2C59.912171&mode=routes&rtext=59.914713%2C30.349703~59.909938%2C30.343024&rtt=mt&ruri=ymapsbm1%3A%2F%2Ftransit%2Fstop%3Fid%3Dstation__9805886~ymapsbm1%3A%2F%2Forg%3Foid%3D1071665634&utm_medium=mapframe&utm_source=maps&z=16.8" 
                style="color:#eee;font-size:12px;position:absolute;top:14px;">
                Яндекс Карты
            </a>
            <iframe 
                src="https://yandex.ru/map-widget/v1/?indoorLevel=1&ll=30.347349%2C59.912171&mode=routes&rtext=59.914713%2C30.349703~59.909938%2C30.343024&rtt=mt&ruri=ymapsbm1%3A%2F%2Ftransit%2Fstop%3Fid%3Dstation__9805886~ymapsbm1%3A%2F%2Forg%3Foid%3D1071665634&z=16.8"
                width="100%" 
                height="400" 
                frameborder="1" 
                allowfullscreen="true" 
                style="position:relative;border-radius: 10px;border: none;">
            </iframe>
        </div>
                    """, height=440)
st.divider()


col3, col4 = st.columns([1, 2])
with col4:
    st.markdown("""
        <div class="colored-container">
            <h3>Об общежитии</h3>
            <p>• Блочный тип проживания (2-3 комнаты по 2-3 человека, собственный санузел на блок)</p>  
            <p>• 16 этажей | 644 места</p>
            <p>• На каждом этаже кухня, оснащенная электрическими плитами и столами</p>
            <p>• Общая прачечная</p>
            <p>• Интернет</p>
            <p>• 10-15 минут пешком от метро</p>
        </div>
                """, unsafe_allow_html=True)
with col3:
    st.image("здание_общежития_в69.jpg",
             use_container_width=True)
st.divider()

st.markdown("*❗️ Пожалуйста, прежде чем связываться с администрацией, ознакомьтесь со всей информацией на сайте.*")
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

st.markdown("🆘 Свяжитесь со студенческим советом через соответствующий раздел")
