import streamlit as st

st.title("🏨 Гостевые блоки")
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
        <p>В общежитии №4 на 1 этаже расположены гостевые блоки.</p>
        <p>Гостевые блоки предназначены для временного расположения студентов заочной формы обучения на период 
        сессии и близких родственников (папа, мама, сестры, братья) обучающихся очной формы обучения, 
        проживающих в общежитии.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Оснащение комнаты:</h3> 
                </div>
            </div> 
        <p>В комнате есть:</p>
        <p>🛋️ Вся необходимая мебель: стол, стул, кровать с матрасом, шкаф и тумбочка.</p>
        <p>🛌 Общежитие выдает: постельное белье, подушку, одеяло, полотенце.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p>Для заселения родственника в гостевой блок студент пишет соответствующее заявление 
        у заведующего студенческим общежитием (в его отсутствие - у заместителя заведующего 
        студенческим общежитием или коменданта), оплачивает срок проживания, получает пропуск.</p>
        <p>Обязательным условием для оформления гостевого тарифа является отсутствие у студента 
        задолженности по оплате проживания в общежитии.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Стоимость</h3> 
                </div>
            </div> 
        <p>• 400 руб/сутки - для студентов заочной формы обучения;</p>
        <p>• 650 руб/сутки - для родственников студентов, проживающих в общежитии. </p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p>🚫 Студент с родителями в одном блоке жить не может.</p>
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
