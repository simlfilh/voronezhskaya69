import streamlit as st

st.title("👩🏽‍💻 Руководство общежития СПбГЭУ №4")
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
            padding: 10px;
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
        <p><b>Администрация общежития</b> — это группа сотрудников, отвечающих за организацию проживания студентов, 
            поддержание порядка, безопасность и решение бытовых вопросов.</p>
        <br>
        <p>В администрацию общежития входят:</p>
        <p>• заведующий общежитием;</p>
        <p>• заместитель заведующего общежитием;</p>
        <p>• паспортист;</p>
        <p>• заведующий хозяйственной частью.</p>
        <br>
        <p>В общежитии также организовано студенческое самоуправление в виде Студенческого совета общежития.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p>Студенты могут обращаться к администрации общежития по широкому кругу вопросов, связанных с проживанием, бытовыми условиями и соблюдением правил.</p>
        <br>
        <p class="highlight-blue"><b>1.</b> Организационные вопросы.</p>
        <p class="highlight-blue"><b>2.</b> Бытовые проблемы.</p>
        <p class="highlight-blue"><b>3.</b> Коммунальные услуги и оплата.</p>
        <p class="highlight-blue"><b>4.</b> Безопасность.</p>
        <p class="highlight-blue"><b>5.</b> Инфраструктура и благоустройство.</p>
    </div>
            """, unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])
with col1:
    st.image("администрация_в69/заведующий_в69.jpg", width=250)
with col2:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3> Заведующий общежитием | Паспортист</h3> 
                    </div>
                </div>
            <br>
            <p><b>Бровкина Наталья Анатольевна<b></p>  
            <br>  
            <p>📞 <a href="tel:+78124589730,4938">(812) 458-97-30 доб. 4938</a></p>
            <p>📩 <a href="mailto:ov69@unecon.ru">ov69@unecon.ru</a></p>
        </div>
                """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <div class="highlight-green">
            <div class="text-indent-content">
                <h3>🕐 Часы приёма студентов</h3> 
            </div>
        </div>
    <br>
    <p>ПН: 8:00 — 16:00</p>  
    <p>ВТ: 8:00 — 16:00</p>  
    <p>СР: 8:00 — 16:00</p>
    <p>ЧТ: приема нет</p>
    <p>ПТ: 8:00 — 16:00</p>
    <br>
    <p>🍜 ОБЕД: 13:00 — 14:00</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

col3, col4 = st.columns([1, 3])
with col3:
    st.image("администрация_в69/комендант_в69.jpg", width=250)
with col4:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Заместитель заведующего общежитием</h3> 
                    </div>
                </div>
            <br>
            <p><b>Ерофеева Ангелина Олеговна<b></p>
            <br>
            <p>📞 <a href="tel:+78124589730,4947">(812) 458-97-30 доб. 4947</a></p>
            <p>📩 <a href="mailto:erofeeva.a@unecon.ru">erofeeva.a@unecon.ru</a></p>
        </div>
                """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <div class="highlight-green">
            <div class="text-indent-content">
                <h3>🕐 Часы приёма студентов</h3> 
            </div>
        </div>
    <p>ПН: 10:00 — 18:00</p>  
    <p>ВТ: 10:00 — 18:00</p>  
    <p>СР: 10:00 — 18:00</p>
    <p>ЧТ: 10:00 — 18:00</p>
    <p>ПТ: 10:00 — 18:00</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

col5, col6 = st.columns([1, 3])
with col5:
    st.image("администрация_в69/завхоз_в69.jpg", width=250)
with col6:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Заведующий хозяйственной частью</h3> 
                    </div>
                </div>
            <br>
            <p><b>Пяткина Ольга Алексеевна<b></p>
            <br> 
            <p>📞 -</p>  
            <p>📩 -</p>
        </div>
                """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <div class="highlight-green">
            <div class="text-indent-content">
                <h3>🕐 Часы приёма студентов</h3> 
            </div>
        </div>
    <p>ПН: 9:00 — 17:00</p>  
    <p>ВТ: 9:00 — 17:00</p>  
    <p>СР: 9:00 — 17:00</p>
    <p>ЧТ: 9:00 — 17:00</p>
    <p>ПТ: 9:00 — 17:00</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("""
    <div class="colored-container">
        <p>🚪 Вся администрация общежития расположена на первом этаже общежития.</p>
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
