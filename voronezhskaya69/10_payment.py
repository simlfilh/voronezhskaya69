import streamlit as st

st.title("💵 Оплата проживания")
st.divider()

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
                    <h3>ОПЛАТА</h3> 
                </div>
            </div> 
        <p>Первичная оплата при заселении в общежитие производится до конца семестра, далее - 
        ежемесячно, до 10 числа каждого месяца.</p>
        <p>📅 Пример: Оплата за сентябрь до 10 сентября, оплата за октябрь до 10 октября и т.д.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>ШАГ 1</h3> 
                </div>
            </div>
        <p>В личном кабинете студента в разделе "Сведения обо мне" перейти 
        во вкладку "Мои договоры".</p>
    </div>
            """, unsafe_allow_html=True)
st.image("оплата общежития/1.png")

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>ШАГ 2</h3> 
                </div>
            </div>
        <p>Выбрать актуальный договор для оплаты, нажать "Печать квитанции". 
        После этого перед вами откроется окно с квитанцией.</p>
    </div>
            """, unsafe_allow_html=True)
st.image("оплата общежития/2.png")

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>ШАГ 3</h3> 
                </div>
            </div>
        <p>Проверить все данные на актуальность и корректность.</p>
    </div>
            """, unsafe_allow_html=True)
st.image("оплата общежития/3.png")

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>ШАГ 4</h3> 
                </div>
            </div>
        <p>Отсканировать через приложение Сбербанка QR-код "ИЗВЕЩЕНИЕ".</p>
    </div>
            """, unsafe_allow_html=True)
st.image("оплата общежития/4.png")

st.markdown("""
    <div class="colored-container">
        <p>Как только QR-код будет прочитан, перед вами всплывут окна для ввода и проверки данных
         и окно для подтверждения оплаты. Внимательно ознакомьтесь со всей информацией.</p>
        <p>Если у вас возникнут вопросы, обращайтесь к старосте своего этажа или напишите нашему Боту 
        Поддержки в tg.</p>
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
