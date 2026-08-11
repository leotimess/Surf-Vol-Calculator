import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="SURFBOARDS",
    page_icon="🏄",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

/* ==========================================================
   FONTES
   ========================================================== */

@import url('https://fonts.googleapis.com/css2?family=Anton&family=Bebas+Neue&family=DM+Sans:wght@400;500;600;700;800&display=swap');


/* ==========================================================
   FUNDO
   ========================================================== */

.stApp {

    background:
        radial-gradient(
            circle at 50% 35%,
            rgba(0, 170, 215, 0.10),
            transparent 38%
        ),
        linear-gradient(
            180deg,
            #03151e 0%,
            #061d28 48%,
            #063d4f 100%
        );

    color: #f4f4ee;

    font-family: 'DM Sans', sans-serif;
}


/* ==========================================================
   ESPAÇAMENTO PRINCIPAL
   ========================================================== */

.block-container {

    max-width: 1450px !important;

    padding-top: 35px !important;

    padding-bottom: 30px !important;
}


/* ==========================================================
   ESCONDER MENU / FOOTER
   ========================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}


/* ==========================================================
   TÍTULO
   ========================================================== */

.surf-title {

    font-family: 'Anton', sans-serif;

    font-size: clamp(60px, 7vw, 95px);

    letter-spacing: 4px;

    line-height: 0.85;

    color: #f5f3e9;

    text-shadow:
        0 4px 0 #087c9e,
        0 8px 25px rgba(0,0,0,0.35);

    margin: 0;
}


.surf-subtitle {

    font-family: 'DM Sans', sans-serif;

    font-size: 15px;

    font-weight: 800;

    letter-spacing: 4px;

    color: #16b4dc;

    margin-top: 10px;

    margin-bottom: 35px;
}


/* ==========================================================
   COLUNAS / PAINÉIS
   ========================================================== */

/*
   O Streamlit cria as colunas como elementos próprios.
   Aqui estilizamos os elementos internos sem colocar
   HTML ao redor dos widgets.
*/

[data-testid="column"] {

    border-radius: 18px;

}


/* ==========================================================
   PAINEL ESQUERDO
   ========================================================== */

.profile-panel {

    background: rgba(5, 32, 43, 0.88);

    border: 1px solid rgba(18, 164, 202, 0.35);

    border-radius: 18px;

    padding: 25px;

    min-height: 625px;

    box-shadow:
        0 20px 60px rgba(0,0,0,0.20);

}


/* ==========================================================
   TÍTULO DOS PAINÉIS
   ========================================================== */

.panel-title {

    font-family: 'Bebas Neue', sans-serif;

    font-size: 34px;

    letter-spacing: 2px;

    color: #f5f3e9;

    margin-bottom: 20px;
}


/* ==========================================================
   LABELS
   ========================================================== */

.question {

    font-family: 'DM Sans', sans-serif;

    font-size: 13px;

    font-weight: 800;

    letter-spacing: 1.5px;

    color: #b9d5dc;

    text-transform: uppercase;

    margin-top: 17px;

    margin-bottom: 3px;
}


.helper {

    font-size: 11px;

    color: #5faabb;

    margin-bottom: 3px;
}


/* ==========================================================
   SLIDERS
   ========================================================== */

div[data-testid="stSlider"] {

    margin-top: -4px;

    margin-bottom: 5px;
}


/* trilho */

div[data-testid="stSlider"] [data-baseweb="slider"] > div > div {

    background-color: #174d5e !important;
}


/* parte preenchida */

div[data-testid="stSlider"] [data-baseweb="slider"] > div > div > div {

    background-color: #08a5d0 !important;
}


/* bolinha */

div[data-testid="stSlider"] [role="slider"] {

    width: 19px !important;

    height: 19px !important;

    background: #f5f3e9 !important;

    border: 3px solid #08a5d0 !important;

    box-shadow:
        0 0 0 4px rgba(8,165,208,0.12),
        0 3px 10px rgba(0,0,0,0.35) !important;
}


/* valor */

div[data-testid="stSlider"] div[data-testid="stWidgetLabel"] {

    color: transparent !important;
}


/* ==========================================================
   RADIO
   ========================================================== */

div[data-testid="stRadio"] label {

    color: #eaf5f7 !important;

    font-weight: 700 !important;
}


div[data-testid="stRadio"] [data-baseweb="radio"] {

    background: #0d3543;

    border-radius: 8px;

    padding: 8px 15px;
}


/* ==========================================================
   BOTÕES
   ========================================================== */

.stButton > button {

    width: 100%;

    min-height: 54px;

    border-radius: 10px;

    border: 1px solid rgba(20,174,214,0.45);

    background: #0c3543;

    color: #edf8fa;

    font-family: 'DM Sans', sans-serif;

    font-size: 14px;

    font-weight: 800;

    letter-spacing: 1px;

    transition: all 0.15s ease;
}


.stButton > button:hover {

    background: #078eaf;

    border-color: #18c1e7;

    color: white;

    transform: translateY(-2px);
}


/* ==========================================================
   BOTÃO PRINCIPAL
   ========================================================== */

.calculate-button .stButton > button {

    background:
        linear-gradient(
            135deg,
            #08a7d1,
            #087fa4
        );

    border: none;

    min-height: 58px;

    font-family: 'Bebas Neue', sans-serif;

    font-size: 22px;

    letter-spacing: 2px;

    box-shadow:
        0 10px 30px rgba(0,150,200,0.18);
}


.calculate-button .stButton > button:hover {

    background:
        linear-gradient(
            135deg,
            #13b9e2,
            #0791b9
        );

}


/* ==========================================================
   ÁREA CENTRAL
   ========================================================== */

.board-container {

    height: 625px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 18px;

    position: relative;

    overflow: hidden;

    background:
        radial-gradient(
            ellipse at center,
            rgba(0,166,207,0.13),
            transparent 60%
        );
}


/* ==========================================================
   RECOMENDAÇÃO
   ========================================================== */

.recommendation-panel {

    background:
        linear-gradient(
            145deg,
            rgba(8,53,67,0.94),
            rgba(4,29,40,0.94)
        );

    border: 1px solid rgba(18,164,202,0.38);

    border-radius: 18px;

    min-height: 625px;

    padding: 30px;

    box-shadow:
        0 20px 60px rgba(0,0,0,0.20);
}


.rec-label {

    font-size: 11px;

    font-weight: 800;

    letter-spacing: 2px;

    color: #19b7df;
}


.rec-title {

    font-family: 'Bebas Neue', sans-serif;

    font-size: 43px;

    letter-spacing: 2px;

    color: #f5f3e9;

    line-height: 1;

    margin-top: 8px;
}


.rec-volume {

    font-family: 'Anton', sans-serif;

    font-size: 72px;

    color: #16b9e2;

    line-height: 1;

    margin-top: 22px;
}


.rec-unit {

    color: #9bcbd5;

    font-size: 13px;

    font-weight: 800;

    letter-spacing: 2px;
}


.rec-description {

    color: #c5dfe5;

    font-size: 14px;

    line-height: 1.65;

    margin-top: 25px;
}


.rec-line {

    height: 1px;

    background: rgba(255,255,255,0.08);

    margin: 25px 0;
}


.info {

    background: rgba(10,60,75,0.55);

    border-left: 3px solid #08a5d0;

    border-radius: 7px;

    padding: 12px 15px;

    margin-top: 10px;
}


.info-label {

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 1.5px;

    color: #65b8c9;
}


.info-value {

    font-size: 14px;

    font-weight: 700;

    color: white;

    margin-top: 3px;
}


.placeholder {

    min-height: 520px;

    display: flex;

    align-items: center;

    justify-content: center;

    text-align: center;

    color: #5d929f;

    font-size: 14px;

    line-height: 1.7;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# CABEÇALHO
# ============================================================

st.markdown(
    """
    <div class="surf-title">SURFBOARDS</div>
    <div class="surf-subtitle">FIND YOUR VOLUME.</div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LAYOUT
# ============================================================

col_left, col_center, col_right = st.columns(
    [1.05, 1.35, 1.05],
    gap="large"
)


# ============================================================
# PAINEL ESQUERDO
# ============================================================

with col_left:

    # Caixa visual do painel
    st.markdown(
        """
        <div class="profile-panel">
            <div class="panel-title">SEU PERFIL</div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # PESO
    # --------------------------------------------------------

    st.markdown(
        '<div class="question">SEU PESO</div>',
        unsafe_allow_html=True
    )

    peso = st.slider(
        "Peso",
        min_value=40,
        max_value=150,
        value=75,
        step=1,
        format="%d kg",
        label_visibility="visible"
    )


    # --------------------------------------------------------
    # ALTURA
    # --------------------------------------------------------

    st.markdown(
        '<div class="question">SUA ALTURA</div>',
        unsafe_allow_html=True
    )

    altura = st.slider(
        "Altura",
        min_value=140,
        max_value=210,
        value=175,
        step=1,
        format="%d cm",
        label_visibility="visible"
    )


    # --------------------------------------------------------
    # NÍVEL
    # --------------------------------------------------------

    st.markdown(
        '<div class="question">NÍVEL DE SURF</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="helper">1 = INICIANTE &nbsp;&nbsp; • &nbsp;&nbsp; 5 = PRO</div>',
        unsafe_allow_html=True
    )

    nivel = st.slider(
        "Nível",
        min_value=1,
        max_value=5,
        value=2,
        step=1,
        format="%d",
        label_visibility="visible"
    )


    # --------------------------------------------------------
    # FREQUÊNCIA
    # --------------------------------------------------------

    st.markdown(
        '<div class="question">QUANTAS VEZES VOCÊ SURFA POR MÊS?</div>',
        unsafe_allow_html=True
    )

    frequencia = st.slider(
        "Frequência",
        min_value=0,
        max_value=30,
        value=4,
        step=1,
        format="%d vezes",
        label_visibility="visible"
    )


    # --------------------------------------------------------
    # EXPERIÊNCIA
    # --------------------------------------------------------

    st.markdown(
        '<div class="question">VOCÊ JÁ SURFOU?</div>',
        unsafe_allow_html=True
    )

    ja_surfou = st.radio(
        "Você já surfou?",
        ["SIM", "NÃO"],
        horizontal=True,
        label_visibility="visible"
    )


    st.markdown("<br>", unsafe_allow_html=True)


    # --------------------------------------------------------
    # BOTÃO
    # --------------------------------------------------------

    st.markdown(
        '<div class="calculate-button">',
        unsafe_allow_html=True
    )

    calcular = st.button(
        "🏄  CALCULAR MEU VOLUME",
        key="calcular"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# PRANCHA CENTRAL
# ============================================================

with col_center:

    # --------------------------------------------------------
    # SVG DA PRANCHA
    # --------------------------------------------------------

    board_html = """
    <!DOCTYPE html>

    <html>

    <head>

    <style>

    * {
        box-sizing: border-box;
    }

    body {

        margin: 0;

        width: 100vw;

        height: 625px;

        overflow: hidden;

        background: transparent;

        display: flex;

        justify-content: center;

        align-items: center;

        font-family: Arial;
    }


    .scene {

        width: 100%;

        height: 100%;

        position: relative;

        display: flex;

        justify-content: center;

        align-items: center;
    }


    /* brilho */

    .glow {

        position: absolute;

        width: 300px;

        height: 600px;

        border-radius: 50%;

        background:
            radial-gradient(
                ellipse,
                rgba(0,170,220,0.20),
                transparent 68%
            );

        filter: blur(18px);
    }


    /* ondas */

    .wave {

        position: absolute;

        width: 100%;

        height: 100px;

        opacity: 0.18;

        background:
            repeating-linear-gradient(
                -12deg,
                transparent 0px,
                transparent 28px,
                #0b8daa 29px,
                #0b8daa 48px,
                transparent 49px,
                transparent 75px
            );

        left: 0;

        bottom: 60px;
    }


    .wave2 {

        bottom: 140px;

        opacity: 0.08;
    }


    /* prancha */

    .board {

        width: 112px;

        height: 475px;

        position: relative;

        z-index: 5;

        border-radius:
            54% 54% 47% 47%
            /
            13% 13% 10% 10%;

        background:
            linear-gradient(
                90deg,
                #d1cec0 0%,
                #f0eee1 13%,
                #fffef3 50%,
                #f0eee1 87%,
                #d1cec0 100%
            );

        box-shadow:

            0 25px 45px rgba(0,0,0,0.48),

            inset 6px 0 9px rgba(255,255,255,0.65),

            inset -6px 0 9px rgba(0,0,0,0.12);
    }


    /* stringer */

    .stringer {

        position: absolute;

        top: 5%;

        left: 50%;

        transform: translateX(-50%);

        width: 3px;

        height: 90%;

        background: #a8b3b2;

        opacity: 0.7;
    }


    /* logo */

    .logo {

        position: absolute;

        top: 46%;

        left: 50%;

        transform:
            translate(-50%, -50%)
            rotate(-90deg);

        font-family: Arial Black;

        font-size: 26px;

        letter-spacing: 3px;

        color: #078eaf;
    }


    /* quilha */

    .fin {

        position: absolute;

        bottom: -34px;

        left: 50%;

        transform: translateX(-50%);

        width: 34px;

        height: 52px;

        background:
            linear-gradient(
                90deg,
                #172d35,
                #071922
            );

        clip-path:
            polygon(
                50% 100%,
                0 0,
                100% 0
            );
    }


    </style>

    </head>


    <body>

        <div class="scene">

            <div class="glow"></div>

            <div class="wave"></div>

            <div class="wave wave2"></div>

            <div class="board">

                <div class="stringer"></div>

                <div class="logo">
                    SURF
                </div>

                <div class="fin"></div>

            </div>

        </div>

    </body>

    </html>
    """

    components.html(
        board_html,
        height=625,
        scrolling=False
    )


# ============================================================
# CÁLCULO
# ============================================================

if calcular:

    if ja_surfou == "NÃO":

        volume = 100

        tipo_prancha = "SOFTBOARD"

        descricao = (
            "Como você ainda não surfou, o ideal é começar "
            "com uma prancha bastante estável. Uma softboard "
            "entre 90 e 110 litros facilita o aprendizado, "
            "a remada e o equilíbrio."
        )

    else:

        # ----------------------------------------------------
        # COEFICIENTES ORIGINAIS
        # ----------------------------------------------------

        coeficientes = {

            1: 0.65,

            2: 0.50,

            3: 0.42,

            4: 0.36,

            5: 0.32
        }

        cf = coeficientes[nivel]


        # ----------------------------------------------------
        # FREQUÊNCIA ORIGINAL
        # ----------------------------------------------------

        if frequencia >= 5:

            multiplicador = -1.5

        elif frequencia <= 2:

            multiplicador = 3

        else:

            multiplicador = 0


        # ----------------------------------------------------
        # FÓRMULA ORIGINAL
        # ----------------------------------------------------

        volume = peso * cf + multiplicador


        # ----------------------------------------------------
        # TIPO DE PRANCHA
        # ----------------------------------------------------

        if nivel == 1:

            tipo_prancha = "FUNBOARD"

            descricao = (
                "Mais estabilidade e volume para facilitar "
                "a remada, o equilíbrio e a evolução."
            )

        elif nivel == 2:

            tipo_prancha = "FUNBOARD"

            descricao = (
                "Um ótimo equilíbrio entre estabilidade, "
                "velocidade e facilidade de uso."
            )

        elif nivel == 3:

            tipo_prancha = "HYBRID"

            descricao = (
                "Uma opção versátil para quem já possui "
                "boa base e quer começar a buscar mais performance."
            )

        elif nivel == 4:

            tipo_prancha = "SHORTBOARD"

            descricao = (
                "Mais responsiva e com menos volume, indicada "
                "para quem já possui bastante controle."
            )

        else:

            tipo_prancha = "PERFORMANCE"

            descricao = (
                "Menor volume e maior responsividade para "
                "surfistas experientes buscando performance."
            )


# ============================================================
# RECOMENDAÇÃO
# ============================================================

with col_right:

    # --------------------------------------------------------
    # PAINEL
    # --------------------------------------------------------

    st.markdown(
        '<div class="recommendation-panel">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="panel-title">RECOMENDAÇÃO</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # ANTES DE CALCULAR
    # --------------------------------------------------------

    if not calcular:

        st.markdown(
            """
            <div class="placeholder">

                <div>

                    <div style="
                        font-size:55px;
                        margin-bottom:15px;
                    ">
                        🌊
                    </div>

                    <strong>
                        AJUSTE SEU PERFIL
                    </strong>

                    <br>

                    E DESCUBRA<br>

                    <strong>
                        SUA PRANCHA IDEAL.
                    </strong>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # DEPOIS DE CALCULAR
    # --------------------------------------------------------

    else:

        st.markdown(
            '<div class="rec-label">SUA PRANCHA IDEAL</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="rec-title">{tipo_prancha}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="rec-line"></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="rec-label">VOLUME RECOMENDADO</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="rec-volume">{volume:.1f}L</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="rec-line"></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="rec-description">{descricao}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="rec-line"></div>',
            unsafe_allow_html=True
        )


        # ----------------------------------------------------
        # INFORMAÇÕES
        # ----------------------------------------------------

        st.markdown(
            f"""
            <div class="info">

                <div class="info-label">
                    SEU PESO
                </div>

                <div class="info-value">
                    {peso} kg
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            f"""
            <div class="info">

                <div class="info-label">
                    SUA ALTURA
                </div>

                <div class="info-value">
                    {altura} cm
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            f"""
            <div class="info">

                <div class="info-label">
                    NÍVEL
                </div>

                <div class="info-value">
                    {nivel}/5
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            f"""
            <div class="info">

                <div class="info-label">
                    FREQUÊNCIA
                </div>

                <div class="info-value">
                    {frequencia}x por mês
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# RODAPÉ
# ============================================================

st.markdown(
    """
    <div style="
        text-align:center;
        margin-top:35px;
        color:#477f8c;
        font-size:10px;
        font-weight:700;
        letter-spacing:3px;
    ">
        SURFBOARDS • FIND YOUR VOLUME
    </div>
    """,
    unsafe_allow_html=True
)
