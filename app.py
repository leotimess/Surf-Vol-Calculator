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

@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500;600;700;800&display=swap');


/* =========================================================
   FUNDO GERAL
   ========================================================= */

.stApp {
    background:
        radial-gradient(
            circle at 50% 45%,
            rgba(0, 155, 200, 0.10),
            transparent 35%
        ),
        linear-gradient(
            180deg,
            #061923 0%,
            #071c27 48%,
            #073b4c 100%
        );

    color: #f4f7f8;
    font-family: 'DM Sans', sans-serif;
}


/* =========================================================
   ESCONDER ELEMENTOS PADRÃO DO STREAMLIT
   ========================================================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}


/* =========================================================
   CONTAINER PRINCIPAL
   ========================================================= */

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}


/* =========================================================
   ONDAS DE FUNDO
   ========================================================= */

.wave-background {
    position: fixed;
    left: -5%;
    bottom: -40px;

    width: 110%;
    height: 32vh;

    opacity: 0.30;

    background:
        repeating-linear-gradient(
            -8deg,
            transparent 0px,
            transparent 42px,
            rgba(0, 145, 185, 0.35) 43px,
            rgba(0, 145, 185, 0.35) 65px,
            transparent 66px,
            transparent 105px
        );

    filter: blur(1px);

    z-index: 0;

    pointer-events: none;
}


/* =========================================================
   TÍTULO
   ========================================================= */

.title {
    font-family: 'Bebas Neue', sans-serif;

    font-size: clamp(60px, 7vw, 100px);

    letter-spacing: 3px;

    line-height: 0.85;

    color: #f5f2e8;

    text-shadow:
        0 3px 0 #087fa5,
        0 6px 18px rgba(0,0,0,0.35);

    margin-bottom: 8px;
}


.subtitle {
    font-family: 'DM Sans', sans-serif;

    font-size: 18px;

    font-weight: 700;

    letter-spacing: 3px;

    color: #19b5dd;

    margin-bottom: 45px;
}


/* =========================================================
   PAINÉIS
   ========================================================= */

.panel {
    background: rgba(5, 29, 40, 0.86);

    border: 1px solid rgba(19, 164, 202, 0.35);

    border-radius: 18px;

    padding: 28px;

    min-height: 580px;

    box-shadow:
        0 20px 60px rgba(0,0,0,0.18),
        inset 0 1px 0 rgba(255,255,255,0.03);

    backdrop-filter: blur(10px);
}


.panel-title {
    font-family: 'Bebas Neue', sans-serif;

    font-size: 32px;

    letter-spacing: 2px;

    color: #f4f4ef;

    margin-bottom: 28px;
}


/* =========================================================
   PERGUNTAS
   ========================================================= */

.question {
    font-size: 14px;

    font-weight: 800;

    letter-spacing: 1.4px;

    color: #b9d7df;

    text-transform: uppercase;

    margin-top: 25px;

    margin-bottom: 5px;
}


.value {
    font-family: 'Bebas Neue', sans-serif;

    font-size: 30px;

    color: #ffffff;

    letter-spacing: 1px;

    margin-bottom: -3px;
}


.helper {
    font-size: 12px;

    color: #5fc5dc;

    margin-top: -5px;

    margin-bottom: 5px;
}


/* =========================================================
   SLIDERS
   ========================================================= */

div[data-baseweb="slider"] {
    padding-top: 8px;
    padding-bottom: 15px;
}


/* trilho */

div[data-baseweb="slider"] > div > div {
    background-color: #164e60 !important;
}


/* parte preenchida */

div[data-baseweb="slider"] > div > div > div {
    background-color: #0ba4d0 !important;
}


/* bolinha */

div[data-baseweb="slider"] [role="slider"] {
    width: 20px !important;

    height: 20px !important;

    border-radius: 50% !important;

    background: #f5f2e8 !important;

    border: 3px solid #0aa5cf !important;

    box-shadow:
        0 0 0 4px rgba(10,165,207,0.12),
        0 3px 10px rgba(0,0,0,0.35) !important;
}


/* =========================================================
   BOTÕES
   ========================================================= */

.stButton > button {

    width: 100%;

    min-height: 48px;

    border-radius: 10px;

    border: 1px solid rgba(25,181,221,0.35);

    background: #103745;

    color: #eaf6f8;

    font-family: 'DM Sans', sans-serif;

    font-weight: 800;

    letter-spacing: 1px;

    transition:
        transform 0.15s ease,
        background 0.15s ease,
        border 0.15s ease;
}


.stButton > button:hover {

    background: #0c8fb7;

    border-color: #18b9e2;

    color: white;

    transform: translateY(-2px);
}


.stButton > button:focus {

    box-shadow: none;

}


/* =========================================================
   BOTÃO CALCULAR
   ========================================================= */

.calculate-button button {

    background:
        linear-gradient(
            135deg,
            #08a6d2,
            #087fa7
        ) !important;

    border: none !important;

    color: white !important;

    font-size: 16px !important;

    min-height: 58px !important;

    border-radius: 12px !important;

    box-shadow:
        0 8px 25px rgba(0,150,200,0.20);

}


.calculate-button button:hover {

    background:
        linear-gradient(
            135deg,
            #13b8e3,
            #0990b9
        ) !important;

    transform: translateY(-2px);

}


/* =========================================================
   BOTÕES SIM / NÃO
   ========================================================= */

.choice-active button {

    background: #079cc7 !important;

    border-color: #19c0e7 !important;

}


.choice-inactive button {

    background: #103745 !important;

}


/* =========================================================
   PRANCHA CENTRAL
   ========================================================= */

.board-area {

    min-height: 580px;

    display: flex;

    align-items: center;

    justify-content: center;

    position: relative;

    overflow: hidden;

    border-radius: 18px;
}


/* brilho atrás da prancha */

.board-glow {

    position: absolute;

    width: 330px;

    height: 600px;

    border-radius: 50%;

    background:
        radial-gradient(
            ellipse,
            rgba(0,174,220,0.18),
            transparent 70%
        );

    filter: blur(20px);
}


/* prancha */

.board {

    position: relative;

    width: 105px;

    height: 500px;

    background:
        linear-gradient(
            90deg,
            #d8d5c5 0%,
            #f8f4e5 18%,
            #fffdf1 50%,
            #f8f4e5 82%,
            #d8d5c5 100%
        );

    border-radius:
        52% 52% 46% 46%
        / 18% 18% 11% 11%;

    box-shadow:

        0 30px 50px rgba(0,0,0,0.45),

        inset -7px 0 12px rgba(0,0,0,0.10),

        inset 7px 0 12px rgba(255,255,255,0.65);

    transform: rotate(0deg);

    z-index: 2;
}


/* linha central */

.board::before {

    content: "";

    position: absolute;

    left: 50%;

    top: 5%;

    transform: translateX(-50%);

    width: 3px;

    height: 90%;

    background: #aab8b8;

    opacity: 0.7;

}


/* logo da prancha */

.board-logo {

    position: absolute;

    left: 50%;

    top: 50%;

    transform:
        translate(-50%, -50%)
        rotate(-90deg);

    font-family: 'Bebas Neue', sans-serif;

    font-size: 27px;

    letter-spacing: 4px;

    color: #0789ad;

    font-weight: bold;

}


/* quilha */

.fin {

    position: absolute;

    bottom: -45px;

    left: 50%;

    transform: translateX(-50%);

    width: 38px;

    height: 65px;

    background:
        linear-gradient(
            90deg,
            #102b36,
            #071923
        );

    clip-path:
        polygon(
            15% 0,
            85% 0,
            100% 100%,
            50% 82%,
            0 100%
        );

    filter:
        drop-shadow(
            0 10px 5px rgba(0,0,0,0.4)
        );
}


/* =========================================================
   RECOMENDAÇÃO
   ========================================================= */

.recommendation {

    background:
        linear-gradient(
            145deg,
            rgba(10,56,70,0.96),
            rgba(5,31,42,0.96)
        );

    border: 1px solid rgba(21,171,210,0.40);

    border-radius: 18px;

    padding: 30px;

    min-height: 580px;

    box-shadow:
        0 20px 60px rgba(0,0,0,0.20);
}


.rec-label {

    font-size: 12px;

    font-weight: 800;

    letter-spacing: 2px;

    color: #1bb5dd;

    text-transform: uppercase;

    margin-bottom: 10px;
}


.rec-title {

    font-family: 'Bebas Neue', sans-serif;

    font-size: 44px;

    letter-spacing: 2px;

    line-height: 0.95;

    color: #f8f4e8;

    margin-bottom: 20px;
}


.rec-volume {

    font-family: 'Bebas Neue', sans-serif;

    font-size: 76px;

    line-height: 0.9;

    color: #19b9e0;

    text-shadow:
        0 5px 25px rgba(0,160,210,0.20);
}


.rec-unit {

    font-size: 18px;

    font-weight: 700;

    color: #9ed7e3;

}


.rec-description {

    font-size: 15px;

    line-height: 1.7;

    color: #c8e0e5;

    margin-top: 25px;
}


.rec-divider {

    height: 1px;

    background: rgba(255,255,255,0.08);

    margin: 25px 0;
}


/* =========================================================
   INFO BOX
   ========================================================= */

.info-box {

    background: rgba(9,50,63,0.75);

    border-radius: 12px;

    padding: 15px 18px;

    margin-top: 12px;

    border-left: 3px solid #0ca5cf;

}


.info-label {

    font-size: 11px;

    letter-spacing: 1.4px;

    color: #68c5d8;

    font-weight: 800;
}


.info-value {

    font-size: 17px;

    color: white;

    font-weight: 700;

    margin-top: 3px;
}


/* =========================================================
   RESPONSIVO
   ========================================================= */

@media (max-width: 900px) {

    .title {
        font-size: 65px;
    }

    .panel,
    .recommendation,
    .board-area {
        min-height: auto;
    }

    .board-area {
        padding: 50px 0;
    }

    .board {
        height: 400px;
        width: 85px;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# FUNDO
# ============================================================

st.markdown(
    '<div class="wave-background"></div>',
    unsafe_allow_html=True
)


# ============================================================
# TÍTULO
# ============================================================

st.markdown(
    """
    <div class="title">SURFBOARDS</div>
    <div class="subtitle">FIND YOUR VOLUME.</div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# VARIÁVEIS
# ============================================================

if "calculado" not in st.session_state:
    st.session_state.calculado = False

if "surfou" not in st.session_state:
    st.session_state.surfou = True


# ============================================================
# LAYOUT
# ============================================================

col_left, col_board, col_right = st.columns(
    [1.15, 1.25, 1.15],
    gap="large"
)


# ============================================================
# PAINEL ESQUERDO
# ============================================================

with col_left:

    st.markdown(
        """
        <div class="panel">
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
        "peso",
        min_value=30,
        max_value=150,
        value=75,
        step=1,
        label_visibility="collapsed"
    )

    st.markdown(
        f"""
        <div class="value">{peso} <span style="
            font-family:'DM Sans';
            font-size:14px;
            color:#20b4d8;
        ">kg</span></div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # NÍVEL
    # --------------------------------------------------------

    st.markdown(
        '<div class="question">NÍVEL DE SURF</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="helper">1 = INICIANTE &nbsp;&nbsp;&nbsp; 5 = PRO</div>',
        unsafe_allow_html=True
    )

    nivel = st.slider(
        "nível",
        min_value=1,
        max_value=5,
        value=2,
        step=1,
        label_visibility="collapsed"
    )

    nomes_nivel = {
        1: "INICIANTE",
        2: "BÁSICO",
        3: "INTERMEDIÁRIO",
        4: "AVANÇADO",
        5: "PRO"
    }

    st.markdown(
        f"""
        <div class="value">
            {nivel}
            <span style="
                font-family:'DM Sans';
                font-size:14px;
                color:#20b4d8;
            ">
                — {nomes_nivel[nivel]}
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # FREQUÊNCIA
    # --------------------------------------------------------

    st.markdown(
        '<div class="question">QUANTAS VEZES VOCÊ SURFA?</div>',
        unsafe_allow_html=True
    )

    freq = st.slider(
        "frequência",
        min_value=0,
        max_value=30,
        value=4,
        step=1,
        label_visibility="collapsed"
    )

    st.markdown(
        f"""
        <div class="value">
            {freq}
            <span style="
                font-family:'DM Sans';
                font-size:14px;
                color:#20b4d8;
            ">
                vezes / mês
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # JÁ SURFOU?
    # --------------------------------------------------------

    st.markdown(
        '<div class="question">VOCÊ JÁ SURFOU?</div>',
        unsafe_allow_html=True
    )

    sim_col, nao_col = st.columns(2)

    with sim_col:

        sim = st.button(
            "SIM",
            use_container_width=True
        )

        if sim:
            st.session_state.surfou = True
            st.session_state.calculado = False

    with nao_col:

        nao = st.button(
            "NÃO",
            use_container_width=True
        )

        if nao:
            st.session_state.surfou = False
            st.session_state.calculado = False


    # --------------------------------------------------------
    # CALCULAR
    # --------------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="calculate-button">',
        unsafe_allow_html=True
    )

    calcular = st.button(
        "🏄  CALCULAR VOLUME",
        use_container_width=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    if calcular:
        st.session_state.calculado = True

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# PRANCHA CENTRAL
# ============================================================

with col_board:

    st.markdown(
        """
        <div class="board-area">

            <div class="board-glow"></div>

            <div class="board">

                <div class="board-logo">
                    SURF
                </div>

                <div class="fin"></div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CÁLCULO
# ============================================================

cf = {
    1: 0.65,
    2: 0.50,
    3: 0.42,
    4: 0.36,
    5: 0.32
}


if freq >= 5:
    mult = -1.5

elif freq <= 2:
    mult = 3

else:
    mult = 0


litro = peso * cf[nivel] + mult


# ============================================================
# RECOMENDAÇÃO
# ============================================================

with col_right:

    if not st.session_state.calculado:

        st.markdown(
            """
            <div class="recommendation">

                <div class="rec-label">
                    SUA PRÓXIMA PRANCHA
                </div>

                <div class="rec-title">
                    RECOMENDAÇÃO
                </div>

                <div class="rec-description">
                    Ajuste seu perfil ao lado e clique em
                    <strong>CALCULAR VOLUME</strong> para descobrir
                    qual volume combina melhor com você.
                </div>

                <div class="rec-divider"></div>

                <div class="info-box">
                    <div class="info-label">DICA</div>
                    <div class="info-value">
                        O volume é calculado de acordo com seu peso,
                        nível e frequência.
                    </div>
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        # ----------------------------------------------------
        # SEM EXPERIÊNCIA
        # ----------------------------------------------------

        if not st.session_state.surfou:

            st.markdown(
                """
                <div class="recommendation">

                    <div class="rec-label">
                        PRIMEIRA PRANCHA
                    </div>

                    <div class="rec-title">
                        SOFTBOARD
                    </div>

                    <div class="rec-volume">
                        90–110
                    </div>

                    <div class="rec-unit">
                        LITROS
                    </div>

                    <div class="rec-description">
                        Como você ainda não surfou, a melhor opção
                        é começar com uma <strong>softboard</strong>
                        de bastante volume.
                        <br><br>
                        Mais estabilidade, facilidade para remar
                        e uma experiência muito mais tranquila
                        para aprender.
                    </div>

                    <div class="rec-divider"></div>

                    <div class="info-box">
                        <div class="info-label">RECOMENDAÇÃO</div>
                        <div class="info-value">
                            Softboard • 90–110 L
                        </div>
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        # ----------------------------------------------------
        # COM EXPERIÊNCIA
        # ----------------------------------------------------

        else:

            # Escolha aproximada do tipo de prancha
            # sem alterar o cálculo original.

            if nivel == 1:
                tipo = "FUNBOARD"
                descricao = (
                    "Uma prancha estável e amigável para continuar "
                    "evoluindo sua remada, equilíbrio e leitura de onda."
                )

            elif nivel == 2:
                tipo = "FUNBOARD"
                descricao = (
                    "Um ótimo equilíbrio entre estabilidade e "
                    "performance para continuar evoluindo."
                )

            elif nivel == 3:
                tipo = "FISH / FUN"
                descricao = (
                    "Mais liberdade e resposta na onda, sem abrir "
                    "mão de um bom volume para remar."
                )

            elif nivel == 4:
                tipo = "SHORTBOARD"
                descricao = (
                    "Uma opção mais performance, com menos volume "
                    "e maior resposta para manobras."
                )

            else:
                tipo = "SHORTBOARD"
                descricao = (
                    "Uma prancha mais agressiva e responsiva, "
                    "pensada para quem já domina bem o surf."
                )


            st.markdown(
                f"""
                <div class="recommendation">

                    <div class="rec-label">
                        SUA PRANCHA IDEAL
                    </div>

                    <div class="rec-title">
                        {tipo}
                    </div>

                    <div class="rec-volume">
                        {litro:.1f}
                    </div>

                    <div class="rec-unit">
                        LITROS
                    </div>

                    <div class="rec-description">
                        {descricao}
                    </div>

                    <div class="rec-divider"></div>

                    <div class="info-box">

                        <div class="info-label">
                            SEU PERFIL
                        </div>

                        <div class="info-value">
                            {peso} kg • Nível {nivel} •
                            {freq}x / mês
                        </div>

                    </div>

                    <div class="info-box">

                        <div class="info-label">
                            VOLUME CALCULADO
                        </div>

                        <div class="info-value">
                            {litro:.2f} litros
                        </div>

                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# RODAPÉ
# ============================================================

st.markdown(
    """
    <div style="
        text-align:center;
        margin-top:40px;
        color:#4c8998;
        font-size:11px;
        letter-spacing:2px;
    ">
        SURFBOARDS • FIND YOUR VOLUME
    </div>
    """,
    unsafe_allow_html=True
)