import streamlit as st

st.title("👫 Студенческий совет общежития СПбГЭУ №4")
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
        .highlight-blue-2 {
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
        <p><b>Студенческий совет общежития</b> является органом студенческого самоуправления в общежитии СПбГЭУ, 
        образованным по инициативе обучающихся в целях учета мнения обучающихся по вопросам реализации молодежной 
        политики и воспитательной деятельности в сфере социальной поддержки и социальной защиты обучающихся, 
        проживающих в общежитиях, и утвержденный решением администрации Университета.</p> 
        <p>Целями деятельности органов студенческого самоуправления в общежитиях СПбГЭУ являются формирование у 
        обучающихся активной гражданской позиции, сознательного и ответственного отношения к возможностям своей 
        социальной самоорганизации и культурно-нравственного саморазвития, развитие умений и навыков самоуправления 
        и подготовка обучающихся к компетентному и ответственному участию в жизни общества.</p> 
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <p><b>Задачами деятельности органов студенческого самоуправления в общежитиях СПбГЭУ являются:</b></p>
                </div>
            </div>
        <p>—  учет мнения обучающихся, проживающих в общежитии;</p>
        <p>—  организация взаимодействия администрации СПбГЭУ и студенческих общежитий в части улучшения 
        жилищных условий проживания обучающихся совместно с ПО;</p>
        <p>—  содействие обучающимся в решении социальных вопросов, связанных с проживанием в общежитии 
        совместно с ПО;</p>
        <p>—  организация просветительских, культурно-досуговых, спортивно-оздоровительных и адаптационных 
        мероприятий для обучающихся, проживающих в общежитии;</p>
        <p>—  противодействие деструктивной идеологии в студенческой среде.</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.header("Председатель студенческого совета")
col1, col2 = st.columns([1, 3])
with col1:
    st.image("администрация_в69/председатель_в69.jpg", width=250)
with col2:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3>Староста общежития</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/id301176965" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Садовников Иван Алексеевич</b></p>
                </div>  
            <p>📞 <a href="tel:+79187200649">+79187200649</a></p>
            <br>
            <br>
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.header("Старосты")

# 2 ЭТАЖ
col7, col8 = st.columns([1, 3])
with col7:
    st.image("администрация_в69/староста_2_в69.jpg", width=250)
with col8:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 2 этажа</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/sharknn7" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Пустоселова Алина Александровна</b></p>
                </div>
            <p>📞 <a href="tel:+79614842341">+79614842341</a></p>
            <br>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 3 ЭТАЖ
col9, col10 = st.columns([1, 3])
with col9:
    st.image("администрация_в69/староста_3_в69.jpg", width=250)
with col10:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 3 этажа</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/the.state_of_mind" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Ахмеров Рамиз Чингизович</b></p>
                </div>
            <p>📞 <a href="tel:+79270181587">+79270181587</a></p>
            <br>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 4 ЭТАЖ
col11, col12 = st.columns([1, 3])
with col11:
    st.image("администрация_в69/староста_4_в69.jpg", width=250)
with col12:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 4 этажа</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/soul1alenka" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Колесник Алёна Александровна</b></p>
                </div>
            <p>📞 <a href="tel:+79024418797">+79024418797</a></p>
            <br>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 5 ЭТАЖ
col13, col14 = st.columns([1, 3])
with col13:
    st.image("администрация_в69/староста_5_в69.jpg", width=250)
with col14:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 5 этажа</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/d.vycheslavovich" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Юрку Данил Вячеславович</b></p>
                </div>
            <p>📞 <a href="tel:+79140449813">+79140449813</a></p>
            <br>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 6 ЭТАЖ
col15, col16 = st.columns([1, 3])
with col15:
    st.image("администрация_в69/староста_6_в69.jpg", width=250)
with col16:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 6 этажа</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/a.m.i_mm" target="_blank" style="margin-left: 5px; font-size: 25px;">                        <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Мурашкинцев Артем</b></p>
                </div>
            <p>📞 <a href="tel:+79313949429">+79313949429</a></p>
            <br>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 7 ЭТАЖ
col17, col18 = st.columns([1, 3])
with col17:
    st.image("администрация_в69/староста_7_в69.jpg", width=250)
with col18:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 7 этажа</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/pascalova" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Паскалова Мария Владимировна</b></p>
                </div>
            <p>📞 <a href="tel:+79313736473">+79313736473</a></p>
            <br>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 8 ЭТАЖ
col19, col20 = st.columns([1, 3])
with col19:
    st.image("администрация_в69/староста_8_в69.jpg", width=250)
with col20:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 8 этажа</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/id301176965" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Садовников Иван Алексеевич</b></p>
                </div>
            <p>📞 <a href="tel:+79187200649">+79187200649</a></p>
            <br>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 9 ЭТАЖ
col21, col22 = st.columns([1, 3])
with col21:
    st.image("администрация_в69/староста_9_в69.jpg", width=250)
with col22:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 9 этажа</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/vikysha16" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Булаенко Виктория Викторовна</b></p>
                </div>
            <p>📞 <a href="tel:+79841480460">+79841480460</a></p>
            <br>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 10 ЭТАЖ
col23, col24 = st.columns([1, 3])
with col23:
    st.image("администрация_в69/староста_10_в69.jpg", width=250)
with col24:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 10 этажа</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/bbbbbqqqq" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Катаев Роман Иванович</b></p>
                </div>
            <p>📞 <a href="tel:+79824603837">+79824603837</a></p>
            <br>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 11 ЭТАЖ
col25, col26 = st.columns([1, 3])
with col25:
    st.image("администрация_в69/староста_11_в69.jpg", width=250)
with col26:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 11 этажа</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/trusniibravler228" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Пержан Даниил Сергеевич</b></p>
                </div>
            <p>📞 <a href="tel:+79112760582">+79112760582</a></p>
            <br>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 12 ЭТАЖ
col27, col28 = st.columns([1, 3])
with col27:
    st.image("администрация_в69/староста_12_в69.jpg", width=250)
with col28:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 12 этажа</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/imsssssssss" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Степанова Мария Михайловна</b></p>
                </div>
            <p>📞 <a href="tel:+79621113290">+79621113290</a></p>
            <br>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 13 ЭТАЖ
col27, col28 = st.columns([1, 3])
with col27:
    st.image("администрация_в69/староста_13_в69.jpg", width=250)
with col28:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 13 этажа</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/upwaix" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Ларионов Данила Сергеевич</b></p>
                </div>
            <p>📞 <a href="tel:+79633388235">+79633388235</a></p>
            <br>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 14 ЭТАЖ
col27, col28 = st.columns([1, 3])
with col27:
    st.image("администрация_в69/староста_14_в69.jpg", width=250)
with col28:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 14 этажа</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/abelyshevv" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Белышев Александр</b></p>
                </div>
            <p>📞 <a href="tel:+79133787709">+79133787709</a></p>
            <br>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 15 ЭТАЖ
col27, col28 = st.columns([1, 3])
with col27:
    st.image("администрация_в69/староста_15_в69.jpg", width=250)
with col28:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 15 этажа</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.com/id422491561" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Гриценко Илья Павлович</b></p>
                </div>
            <p>📞 <a href="tel:+79531000737">+79531000737</a></p>
            <br>
            <br>
        </div>
                """, unsafe_allow_html=True)

# 16 ЭТАЖ
col27, col28 = st.columns([1, 3])
with col27:
    st.image("администрация_в69/староста_16_в69.jpg", width=250)
with col28:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue-2">
                    <div class="text-indent-content">
                        <h3>Староста 16 этажа</h3> 
                    </div>
                </div>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
                <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                    <a href="https://vk.ru/ariat" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i></a>
                    <p style="margin: 0; font-size: 23px;"><b>Атоян Арианна Самвеловна</b></p>
                </div>
            <p>📞 <a href="tel:+79881807020">+79881807020</a></p>
            <br>
            <br>
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
