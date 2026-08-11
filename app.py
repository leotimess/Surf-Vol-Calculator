import streamlit as st

# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="SURFBOARDS — Volume Calculator",
    page_icon="🏄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Anton&family=Bebas+Neue&family=Oswald:wght@400;500;600&display=swap');

/* ---------------------------------------------------------
   FUNDO
--------------------------------------------------------- */

.stApp {
    background:
        radial-gradient(circle at 50% 35%, rgba(0, 157, 200, 0.10), transparent 35%),
        linear-gradient(
            180deg,
            #03151e 0%,
            #061c26 48%,
            #063c4d 100%
        );
    color: white;
}

/* Remove espaço superior exagerado */

.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    max-width: 1450px !important;
}

/* ---------------------------------------------------------
   TÍTULO
--------------------------------------------------------- */

.main-title {
    font-family: 'Anton', sans-serif;
    font-size: 68px;
    letter-spacing: 3px;
    color: #f5f4ec;
    line-height: 0.9;
    margin-bottom: 4px;
}

.main-subtitle {
    font-family: 'Oswald', sans-serif;
    font-size: 21px;
    font-weight: 500;
    letter-spacing: 2px;
    color: #00a6cf;
    margin-bottom: 30px;
}

/* ---------------------------------------------------------
   CARDS
--------------------------------------------------------- */

.profile-card,
.recommendation-card {
    background: rgba(5, 35, 45, 0.88);
    border: 2px solid rgba(0, 166, 207, 0.35);
    border-radius: 4px;
    padding: 28px;
    min-height: 600px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.20);
}

.card-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 34px;
    letter-spacing: 2px;
    color: #f5f4ec;
    margin-bottom: 25px;
}

/* ---------------------------------------------------------
   LABELS
--------------------------------------------------------- */

.question-label {
    font-family: 'Oswald', sans-serif;
    font-size: 18px;
    font-weight: 600;
    letter-spacing: 1px;
    color: #eaf5f7;
    margin-top: 18px;
    margin-bottom: 5px;
}

.question-help {
    font-family: 'Oswald', sans-serif;
    font-size: 13px;
    color: #72b9c9;
    margin-bottom: 4px;
}

/* ---------------------------------------------------------
   VALOR DOS SLIDERS
--------------------------------------------------------- */

.slider-value {
    font-family: 'Anton', sans-serif;
    font-size: 25px;
    color: #00b8e6;
    text-align: right;
}

/* ---------------------------------------------------------
   SLIDERS
--------------------------------------------------------- */

/* Trilho */

div[data-baseweb="slider"] > div > div {
    background-color: #15566a !important;
}

/* Parte preenchida */

div[data-baseweb="slider"] > div > div > div {
    background-color: #00a6cf !important;
}

/* Bolinha */

div[data-baseweb="slider"] [role="slider"] {
    background-color: #f5f4ec !important;
    border: 3px solid #00a6cf !important;
    width: 20px !important;
    height: 20px !important;
    box-shadow: 0 0 12px rgba(0,166,207,0.5) !important;
}

/* ---------------------------------------------------------
   RADIO
--------------------------------------------------------- */

div[role="radiogroup"] {
    gap: 8px;
}

div[role="radiogroup"] label {
    background-color: #0b3442;
    border: 1px solid #14566a;
    border-radius: 3px;
    padding: 7px 18px;
}

div[role="radiogroup"] label:hover {
    border-color: #00a6cf;
}

/* ---------------------------------------------------------
   BOTÃO CALCULAR
--------------------------------------------------------- */

.stButton > button {
    width: 100%;
    height: 58px;
    border-radius: 3px;
    border: 2px solid #00a6cf;
    background: #078eaf;
    color: white;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 25px;
    letter-spacing: 2px;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: #00a6cf;
    border-color: #f5f4ec;
    color: white;
    transform: translateY(-2px);
}

/* ---------------------------------------------------------
   PRANCHA
--------------------------------------------------------- */

.board-area {
    min-height: 600px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;

    background:
        radial-gradient(
            ellipse at center,
            rgba(0,166,207,0.13),
            transparent 55%
        );
}

/* ondas */

.wave {
    position: absolute;
    width: 100%;
    height: 120px;
    left: 0;
    opacity: 0.25;
    background: repeating-linear-gradient(
        -15deg,
        transparent 0px,
        transparent 25px,
        #078eaf 26px,
        #078eaf 48px,
        transparent 49px,
        transparent 75px
    );
}

.wave.one {
    bottom: 60px;
}

.wave.two {
    bottom: 130px;
    opacity: 0.13;
}

/* Prancha */

.surfboard {
    position: relative;
    width: 120px;
    height: 450px;

    background:
        linear-gradient(
            90deg,
            #d9d6c7 0%,
            #f5f3e8 15%,
            #fffff5 50%,
            #f5f3e8 85%,
            #d9d6c7 100%
        );

    border-radius: 55% 55% 48% 48% / 13% 13% 10% 10%;

    box-shadow:
        0 20px 35px rgba(0,0,0,0.5),
        inset 4px 0 5px rgba(255,255,255,0.5),
        inset -4px 0 5px rgba(0,0,0,0.15);

    z-index: 5;
}

.board-stringer {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    height: 90%;
    width: 3px;
    top: 5%;
    background: #aab5b7;
    opacity: 0.7;
}

.board-logo {
    position: absolute;
    top: 42%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(-90deg);

    font-family: 'Anton', sans-serif;
    font-size: 29px;
    letter-spacing: 3px;
    color: #0796bd;
}

.board-fin {
    position: absolute;
    bottom: -28px;
    left: 50%;
    transform: translateX(-50%);

    width: 30px;
    height: 42px;

    background: #102b35;

    clip-path: polygon(
        50% 100%,
        0% 0%,
        100% 0%
    );
}

/* ---------------------------------------------------------
   RECOMENDAÇÃO
--------------------------------------------------------- */

.rec-placeholder {
    height: 500px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;

    font-family: 'Oswald', sans-serif;
    font-size: 18px;
    color: #5c8d99;
}

.rec-result {
    margin-top: 20px;
}

.rec-small {
    font-family: 'Oswald', sans-serif;
    color: #7fb9c7;
    font-size: 15px;
    letter-spacing: 1px;
}

.rec-board {
    font-family: 'Anton', sans-serif;
    font-size: 42px;
    letter-spacing: 2px;
    color: #00b8e6;
    margin: 8px 0;
}

.rec-volume {
    font-family: 'Anton', sans-serif;
    font-size: 64px;
    color: #f5f4ec;
    line-height: 1;
    margin: 15px 0;
}

.rec-description {
    font-family: 'Oswald', sans-serif;
    color: #c5e3e8;
    font-size: 17px;
    line-height: 1.5;
}

.rec-divider {
    height: 2px;
    background: #14566a;
    margin: 22px 0;
}

/* ---------------------------------------------------------
   ESCONDER ELEMENTOS DO STREAMLIT
--------------------------------------------------------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# TÍTULO
# ============================================================

st.markdown("""
<div class="main-title">SURFBOARDS</div>
<div class="main-subtitle">FIND YOUR VOLUME.</div>
""", unsafe_allow_html=True)


# ============================================================
# LAYOUT PRINCIPAL
# ============================================================

left, center, right = st.columns(
    [1.05, 1.45, 1.05],
    gap="large"
)


# ============================================================
# COLUNA ESQUERDA
# ============================================================

with left:

    st.markdown("""
    <div class="profile-card">
        <div class="card-title">SEU PERFIL</div>
    </div>
    """, unsafe_allow_html=True)

    # Peso
    st.markdown(
        '<div class="question-label">SEU PESO</div>',
        unsafe_allow_html=True
    )

    peso = st.slider(
        "peso",
        min_value=40,
        max_value=150,
        value=75,
        step=1,
        format="%d kg",
        label_visibility="collapsed"
    )

    # Altura
    st.markdown(
        '<div class="question-label">SUA ALTURA</div>',
        unsafe_allow_html=True
    )

    altura = st.slider(
        "altura",
        min_value=140,
        max_value=210,
        value=175,
        step=1,
        format="%d cm",
        label_visibility="collapsed"
    )

    # Nível
    st.markdown(
        '<div class="question-label">NÍVEL DE SURF</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="question-help">1 = INICIANTE &nbsp;&nbsp;&nbsp; 5 = PRO</div>',
        unsafe_allow_html=True
    )

    nivel = st.slider(
        "nível",
        min_value=1,
        max_value=5,
        value=2,
        step=1,
        format="%d",
        label_visibility="collapsed"
    )

    # Frequência
    st.markdown(
        '<div class="question-label">QUANTAS VEZES VOCÊ SURFA POR MÊS?</div>',
        unsafe_allow_html=True
    )

    frequencia = st.slider(
        "frequência",
        min_value=0,
        max_value=30,
        value=4,
        step=1,
        format="%d vezes",
        label_visibility="collapsed"
    )

    # Já surfou?
    st.markdown(
        '<div class="question-label">VOCÊ JÁ SURFOU?</div>',
        unsafe_allow_html=True
    )

    ja_surfou = st.radio(
        "já surfou",
        ["SIM", "NÃO"],
        horizontal=True,
        label_visibility="collapsed"
    )


# ============================================================
# COLUNA CENTRAL — PRANCHA
# ============================================================

with center:

    st.markdown("""
    <div class="board-area">

        <div class="wave one"></div>
        <div class="wave two"></div>

        <div class="surfboard">

            <div class="board-stringer"></div>

            <div class="board-logo">
                SURF
            </div>

            <div class="board-fin"></div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    # Botão
    calcular = st.button(
        "🏄 CALCULAR MEU VOLUME"
    )


# ============================================================
# CÁLCULO
# ============================================================

if calcular:

    if ja_surfou == "NÃO":

        volume = 100

        tipo_prancha = "SOFTBOARD"

        descricao = """
        Como você ainda não surfou, o ideal é começar com bastante
        estabilidade e volume. Uma softboard entre **90L e 110L**
        facilita muito o aprendizado e dá mais segurança nas primeiras ondas.
        """

    else:

        # Coeficientes originais do programa

        coeficientes = {
            1: 0.65,
            2: 0.50,
            3: 0.42,
            4: 0.36,
            5: 0.32
        }

        cf = coeficientes[nivel]

        # Ajuste pela frequência

        if frequencia >= 5:
            multiplicador = -1.5

        elif frequencia <= 2:
            multiplicador = 3

        else:
            multiplicador = 0

        volume = (peso * cf) + multiplicador

        # Classificação da prancha

        if nivel == 1:
            tipo_prancha = "FUNBOARD / MINI MALIBU"

        elif nivel == 2:
            tipo_prancha = "FUNBOARD"

        elif nivel == 3:
            tipo_prancha = "HYBRID"

        elif nivel == 4:
            tipo_prancha = "SHORTBOARD"

        else:
            tipo_prancha = "PERFORMANCE"

        descricao = f"""
        Com **{peso} kg**, nível **{nivel}/5** e surfando
        aproximadamente **{frequencia} vezes por mês**, seu volume
        calculado é de aproximadamente **{volume:.1f} litros**.
        """


# ============================================================
# COLUNA DIREITA — RECOMENDAÇÃO
# ============================================================

with right:

    st.markdown("""
    <div class="recommendation-card">

        <div class="card-title">
            RECOMENDAÇÃO
        </div>
    """, unsafe_allow_html=True)

    if not calcular:

        st.markdown("""
        <div class="rec-placeholder">
            <div>
                <div style="font-size:45px;">🌊</div>
                AJUSTE SEU PERFIL<br>
                E DESCUBRA SUA PRANCHA.
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div class="rec-result">

            <div class="rec-small">
                SUA PRANCHA IDEAL
            </div>

            <div class="rec-board">
                {tipo_prancha}
            </div>

            <div class="rec-divider"></div>

            <div class="rec-small">
                VOLUME RECOMENDADO
            </div>

            <div class="rec-volume">
                {volume:.1f}L
            </div>

            <div class="rec-divider"></div>

            <div class="rec-description">
                {descricao}
            </div>

            <div class="rec-divider"></div>

            <div class="rec-small">
                PERFIL
            </div>

            <div class="rec-description">
                Peso: <strong>{peso} kg</strong><br>
                Altura: <strong>{altura} cm</strong><br>
                Nível: <strong>{nivel}/5</strong><br>
                Surf: <strong>{frequencia}x/mês</strong>
            </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
