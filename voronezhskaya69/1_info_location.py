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
            <h3 class="highlight-blue">Адрес: Санкт-Петербург, Воронежская ул., д. 69</h3>
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
            <h3>Мы в Google Maps ⬇️</h3>
        </div>
                """, unsafe_allow_html=True)
    st.components.v1.html("""
        <iframe 
            src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d4000.402274430029!2d30.342280122318808!3d59.91220917275017!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0x4696304c97ab5355%3A0x66d8c4333f3a046c!2z0J7QsdCy0L7QtNC90YvQuSDQutCw0L3QsNC7LCDQodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQsw!3m2!1d59.91303!2d30.351233899999997!4m5!1s0x4696304ec741c531%3A0xf41970b226624491!2z0JLQvtGA0L7QvdC10LbRgdC60LDRjyDRg9C70LjRhtCwLCA2OSwg0KHQsNC90LrRgi3Qn9C10YLQtdGA0LHRg9GA0LM!3m2!1d59.909928199999996!2d30.3429394!5e0!3m2!1sru!2sru!4v1751398129302!5m2!1sru!2sru" 
            width="600" height="450" 
            style="border:0; border-radius: 10px;"
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade">
        </iframe>
                    """, height=440)
st.divider()

col3, col4 = st.columns([1, 2])
with col4:
    st.markdown("""
        <div class="colored-container">
            <h3>Об общежитии</h3>
            <p>• Блочный тип проживания (размещение по 2-3 человека в комнате)</p>  
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
    <p>📞 <a href="tel:+78124589730,4938">(812) 458-97-30 доб. 4938</a></p>
            """, unsafe_allow_html=True)
st.write("Заместитель заведующего общежитием: Ерофеева Ангелина Олеговна 👩🏼‍💼")
st.markdown("""
    <p>📞 <a href="tel:+78124589730,4947">(812) 458-97-30 доб. 4947</a></p>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("🆘 Свяжитесь со студенческим советом через соответствующий раздел")
