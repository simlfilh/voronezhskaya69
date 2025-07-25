import streamlit as st

st.title("👫 Заселение в общежитие СПбГЭУ №4")
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
            <div class="highlight-green">
                <div class="text-indent-content">
                    <h3>Информация о заселении первокурсников в общежитие</h3>
                </div>
            </div>
        <p>Уважаемые первокурсники!</p>
        <p>Сообщаем Вам, что заселение в общежития бакалавров, 
        специалистов и магистрантов 1 года обучения, в том числе студентов льготных категорий, 
        проводится согласно предварительно составленным спискам.</p>
        <br>
        <p>Списки ранжируются с учетом набранных баллов ЕГЭ.</p>
        <p>❗️ Ежегодно конкурсный балл меняется, следите за списками по 
        <a href="https://priem.unecon.ru/stat/stat_hotel_grafik.php">ссылке</a>.</p>
        <br>
        <p>• Списки заселяющихся в общежития будут размещены на сайте после опубликования приказов о зачислении на 1 курс.</p>
        <p>• Первоначальная оплата проживания в общежитии производится за семестр.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <div class="highlight-red">
            <div class="text-indent-content">
                <h3>❗️ Начало заселения в общежития СПбГЭУ 25.08.2025.</h3>
            </div>
        </div>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-green">
                <div class="text-indent-content">
                    <h3>Для выбора общежития и даты заселения первокурсникам необходимо:</h3>
                </div>
            </div>
        <p><b>1.</b> Найти ФИО в списке на заселение по 
        <a href="https://priem.unecon.ru/stat/stat_hotel_grafik.php">ссылке</a>.</p>
        <p><b>2.</b> В личном кабинете абитуриента подтвердить: общежитие, дату заселения, комнату;</p>
        <p><b>3. Для заселения необходимо прибыть с 10:00 до 17:00 в день, указанный в личном кабинете</b>, 
        по адресу выбранного общежития.</p>
        <p><b>4.</b> Студенты, не включенные в список на заселение, обеспечиваются общежитием после 05.09.2024 
        при наличии свободных мест (обращаться в чат Жилищно-бытового управления через Личный кабинет).</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <br>
        <p>❗️ Общежитие для поступивших на программы среднего профессионального образования (СПО) 
        предоставляется только детям-сиротам, достигшим 17-летнего возраста. 
        Список документов см. ниже (Перечень документов, необходимых для заселения в общежитие 
        поступивших на программы бакалавриата и специалитета).</p>
        <br>
        <p>❗️ Оформление договора найма жилого помещения производится только при наличии всех  документов из списка.</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Перечень документов, необходимых для заселения в общежитие для граждан Российской Федерации, 
                    поступивших на программы бакалавриата и специалитета:</h3>
                </div>
            </div>
        <p><b>1.</b> Паспорт с регистрацией по месту жительства (исключается г. Санкт-Петербург и ближайшая 
        территория Ленинградской области) + копия;</p>
        <p><b>2.</b> Медицинская справка (форма 086) с результатами флюорографического обследования + копия;</p>
        <p><b>3.</b> Копия сертификата о профилактических прививках;</p>
        <p><b>4.</b> Страховой полис;</p>
        <p><b>5.</b> ИНН + копия;</p>
        <p><b>6.</b> СНИЛС + копия;</p>
        <p><b>7.</b> 2 фотографии (формат 3х4, светлый фон);</p>
        <p><b>8.</b> Приписное свидетельство или военный билет (для юношей);</p>
        <p><b>9.</b> Документы, подтверждающие льготы + копии;</p>
        <p><b>10.</b> Студентам, не достигшим 18-летнего возраста дополнительно предоставить 
        НОТАРИАЛЬНО ЗАВЕРЕННОЕ СОГЛАСИЕ РОДИТЕЛЕЙ (ОПЕКУНОВ) 
        на заключение договора найма жилого помещения в общежитии 
        (<a href="https://unecon.ru/wp-content/uploads/2022/05/obrazec_soglasiya_dlya_roditeley_opekunov_0.pdf">образец заявления</a>).</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <h3>Перечень документов, необходимых для заселения 
                    в общежитие для граждан иностранных государств:</h3>
                </div>
            </div>
        <p><b>1.</b> Паспорт (с нотариально заверенным переводом на русский язык либо переводом, заверенным 
        подписью руководителя Управления международного сотрудничества и печатью);</p>
        <p><b>2.</b> Медицинская справка с результатами флюорографического обследования + копия;</p>
        <p><b>3.</b> Студентам, не достигшим 18-летнего возраста дополнительно предоставить НОТАРИАЛЬНО 
        ЗАВЕРЕННОЕ СОГЛАСИЕ РОДИТЕЛЕЙ (ОПЕКУНОВ) на заключение договора найма жилого помещения в общежитии 
        (<a href="https://unecon.ru/wp-content/uploads/2022/05/obrazec_soglasiya_dlya_roditeley_opekunov_0.pdf">образец заявления</a>);</p>
        <p><b>4.</b> Студенты ближнего зарубежья справку о зачислении получают у заведующего общежитием.</p>
        <br>
        <p>❗️ Студентам дальнего зарубежья необходимо дополнительно получить выписку из приказа о зачислении 
        с указанием сроков обучения в Управлении международного сотрудничества по адресу: 
        <p>  📍 наб. канала Грибоедова, д. 30/32, лестница №3, этаж 1; лестница №2, этаж 2.</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("""
    <div class="colored-container">
            <div class="highlight-red">
                <div class="text-indent-content">
                    <h3>Временная регистрация</h3>
                </div>
            </div>
        <p>Получение временной регистрации происходит в течение 1-2 месяцев.</p>
        <p>Первыми временную регистрацию получают юноши, после - девушки.</p>
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

st.markdown("🆘 Свяжитесь со студенческим советом через соответствующий раздел")
