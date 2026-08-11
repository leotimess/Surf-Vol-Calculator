import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="SURFBOARDS",
    page_icon="🏄",
    layout="wide"
)


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Anton&family=Bebas+Neue&family=DM+Sans:wght@400;500;600;700;800&display=swap');


/* ==========================================================
   FUNDO
   ========================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 50% 35%,
            rgba(0, 170, 215, 0.12),
            transparent 38%
        ),
        linear-gradient(
            180deg,
            #03151e 0%,
            #061d28 50%,
            #063d4f 100%
        );

    color: #f5f3e9;
}


/* ==========================================================
   ÁREA PRINCIPAL
   ========================================================== */

.block-container {
    max-width: 1450px !important;
    padding-top: 35px !important;
    padding-bottom: 30px !important;
}


/* ==========================================================
   ESCONDER ELEMENTOS STREAMLIT
   ========================================================== */

#MainMenu {
    visibility: hidden;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* ==========================================================
   TÍTULO
   ========================================================== */

.surf-title {
    font-family: 'Anton', sans-serif;

    font-size: clamp(60px, 7vw, 92px);

    letter-spacing: 4px;

    line-height: 0.85;

    color: #f5f3e9;

    text-shadow:
        0 4px 0 #087c9e,
        0 8px 25px rgba(0,0,0,0.35);
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
   CAIXAS
   ========================================================== */

div[data-testid="stVerticalBlockBorderWrapper"] {

    background:
        linear-gradient(
            145deg,
            rgba(7, 42, 54, 0.94),
            rgba(3, 25, 34, 0.94)
        ) !important;

    border: 1px solid rgba(16, 164, 201, 0.35) !important;

    border-radius: 18px !important;

    box-shadow:
        0 20px 60px rgba(0,0,0,0.22) !important;

    padding: 25px !important;
}


/* ==========================================================
   TÍTULOS
   ========================================================== */

.panel-title {
    font-family: 'Bebas Neue', sans-serif;

    font-size: 34px;

    letter-spacing: 2px;

    color: #f5f3e9;

    margin-bottom: 15px;
}


/* ==========================================================
   PERGUNTAS
   ========================================================== */

.question-label {

    font-family: 'DM Sans', sans-serif;

    font-size: 13px;

    font-weight: 800;

    letter-spacing: 1.3px;

    color: #c6dfe5;

    margin-top: 12px;

    margin-bottom: 0;
}


.question-help {

    font-family: 'DM Sans', sans-serif;

    font-size: 10px;

    font-weight: 600;

    color: #5ea9b9;

    margin-top: 2px;
}


/* ==========================================================
   SLIDERS
   ========================================================== */

div[data-testid="stSlider"] {

    margin-top: -5px !important;

    margin-bottom: 7px !important;
}


div[data-testid="stSlider"]
[data-baseweb="slider"]
> div
> div {

    background-color: #174e5f !important;
}


div[data-testid="stSlider"]
[data-baseweb="slider"]
> div
> div
> div {

    background-color: #08a7d2 !important;
}


div[data-testid="stSlider"]
[role="slider"] {

    width: 20px !important;

    height: 20px !important;

    background-color: #f5f3e9 !important;

    border: 3px solid #08a7d2 !important;

    box-shadow:
        0 0 0 4px rgba(8,167,210,0.12),
        0 3px 10px rgba(0,0,0,0.4) !important;
}


/* ==========================================================
   RADIO
   ========================================================== */

div[data-testid="stRadio"] label {

    color: #eaf5f7 !important;

    font-weight: 700 !important;
}


/* ==========================================================
   BOTÃO
   ========================================================== */

div[data-testid="stButton"] > button {

    width: 100%;

    min-height: 58px;

    border-radius: 10px;

    border: 1px solid #12a9d2;

    background:
        linear-gradient(
            135deg,
            #08a7d1,
            #087fa4
        );

    color: white;

    font-family: 'Bebas Neue', sans-serif;

    font-size: 23px;

    letter-spacing: 2px;

    transition: 0.2s;
}


div[data-testid="stButton"] > button:hover {

    background:
        linear-gradient(
            135deg,
            #14bce7,
            #0792b9
        );

    transform: translateY(-2px);
}


/* ==========================================================
   RECOMENDAÇÃO
   ========================================================== */

.rec-label {

    font-family: 'DM Sans', sans-serif;

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 2px;

    color: #19b8df;

    margin-top: 8px;
}


.rec-board {

    font-family: 'Bebas Neue', sans-serif;

    font-size: 43px;

    letter-spacing: 2px;

    color: #f5f3e9;

    line-height: 1;

    margin-top: 5px;
}


.rec-volume {

    font-family: 'Anton', sans-serif;

    font-size: 72px;

    color: #12b9e2;

    line-height: 1;

    margin-top: 12px;
}


.rec-description {

    font-family: 'DM Sans', sans-serif;

    font-size: 13px;

    line-height: 1.6;

    color: #c6dfe5;

    margin-top: 20px;
}


.rec-line {

    height: 1px;

    width: 100%;

    background: rgba(255,255,255,0.08);

    margin: 20px 0;
}


/* ==========================================================
   INFORMAÇÕES
   ========================================================== */

.info-box {

    background: rgba(8, 61, 76, 0.65);

    border-left: 3px solid #08a7d1;

    border-radius: 6px;

    padding: 9px 12px;

    margin-top: 8px;
}


.info-name {

    font-size: 9px;

    font-weight: 800;

    letter-spacing: 1.5px;

    color: #65b8c9;
}


.info-value {

    font-size: 13px;

    font-weight: 700;

    color: #f5f3e9;

    margin-top: 2px;
}


/* ==========================================================
   PLACEHOLDER
   ========================================================== */

.placeholder {

    height: 510px;

    display: flex;

    align-items: center;

    justify-content: center;

    text-align: center;

    color: #5c909d;

    font-family: 'DM Sans', sans-serif;

    font-size: 13px;

    line-height: 1.8;
}


/* ==========================================================
   RECOMENDAÇÃO NATIVA
   ========================================================== */

.recommendation-label {

    font-family: 'DM Sans', sans-serif;

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 2px;

    color: #19b8df;

    margin-top: 8px;

    margin-bottom: 5px;
}


.recommendation-board {

    font-family: 'Bebas Neue', sans-serif;

    font-size: 43px;

    letter-spacing: 2px;

    color: #f5f3e9;

    line-height: 1;

    margin-bottom: 18px;
}


.recommendation-volume-label {

    font-family: 'DM Sans', sans-serif;

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 2px;

    color: #19b8df;

    margin-bottom: 3px;
}


.recommendation-volume {

    font-family: 'Anton', sans-serif;

    font-size: 72px;

    color: #12b9e2;

    line-height: 1;

    margin-bottom: 20px;
}


.recommendation-description {

    font-family: 'DM Sans', sans-serif;

    font-size: 13px;

    line-height: 1.6;

    color: #c6dfe5;

    margin-bottom: 20px;
}


.recommendation-divider {

    width: 100%;

    height: 1px;

    background: rgba(255,255,255,0.08);

    margin: 18px 0;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# CABEÇALHO
# ============================================================

st.markdown(
    """
    <div class="surf-title">
        SURFBOARDS
    </div>

    <div class="surf-subtitle">
        FIND YOUR VOLUME.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# COLUNAS
# ============================================================

col_esquerda, col_centro, col_direita = st.columns(
    [1.05, 1.35, 1.05],
    gap="large"
)


# ============================================================
# PERFIL
# ============================================================

with col_esquerda:

    with st.container(border=True):

        st.markdown(
            '<div class="panel-title">SEU PERFIL</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="question-label">SEU PESO</div>',
            unsafe_allow_html=True
        )

        peso = st.slider(
            "Peso",
            min_value=40,
            max_value=150,
            value=75,
            step=1,
            format="%d kg",
            label_visibility="collapsed"
        )


        st.markdown(
            '<div class="question-label">SUA ALTURA</div>',
            unsafe_allow_html=True
        )

        altura = st.slider(
            "Altura",
            min_value=140,
            max_value=210,
            value=175,
            step=1,
            format="%d cm",
            label_visibility="collapsed"
        )


        st.markdown(
            '<div class="question-label">NÍVEL DE SURF</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="question-help">
                1 = INICIANTE &nbsp; • &nbsp; 5 = PRO
            </div>
            """,
            unsafe_allow_html=True
        )

        nivel = st.slider(
            "Nível",
            min_value=1,
            max_value=5,
            value=2,
            step=1,
            format="%d",
            label_visibility="collapsed"
        )


        st.markdown(
            """
            <div class="question-label">
                QUANTAS VEZES VOCÊ SURFA POR MÊS?
            </div>
            """,
            unsafe_allow_html=True
        )

        frequencia = st.slider(
            "Frequência",
            min_value=0,
            max_value=30,
            value=4,
            step=1,
            format="%d vezes",
            label_visibility="collapsed"
        )


        st.markdown(
            """
            <div class="question-label">
                VOCÊ JÁ SURFOU?
            </div>
            """,
            unsafe_allow_html=True
        )

        ja_surfou = st.radio(
            "Experiência",
            ["SIM", "NÃO"],
            horizontal=True,
            label_visibility="collapsed"
        )


        st.markdown("<br>", unsafe_allow_html=True)


        calcular = st.button(
            "🏄  CALCULAR MEU VOLUME",
            use_container_width=True
        )


# ============================================================
# CÁLCULO
# ============================================================

if calcular:

    if ja_surfou == "NÃO":

        volume = 100

        tipo_prancha = "SOFTBOARD"

        descricao = (
            "Como você ainda não surfou, recomendamos "
            "uma softboard entre 90 e 110 litros. "
            "O maior volume proporciona mais estabilidade "
            "e facilita o aprendizado."
        )

    else:

        coeficientes = {
            1: 0.65,
            2: 0.50,
            3: 0.42,
            4: 0.36,
            5: 0.32
        }

        cf = coeficientes[nivel]


        if frequencia >= 5:

            multiplicador = -1.5

        elif frequencia <= 2:

            multiplicador = 3

        else:

            multiplicador = 0


        volume = peso * cf + multiplicador


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

else:

    volume = None

    tipo_prancha = None

    descricao = None


# ============================================================
# PRANCHA CENTRAL
# ============================================================

with col_centro:

    if volume is None:

        board_height = 500

        board_width = 100

    else:

        board_height = int(
            max(
                450,
                min(
                    560,
                    450 + volume * 2
                )
            )
        )


        board_width = int(
            max(
                85,
                min(
                    145,
                    78 + volume * 1.25
                )
            )
        )


    if volume is None:

        board_text = ""

    else:

        board_text = f"{volume:.1f} LITROS"


    board_html = f"""
<!DOCTYPE html>

<html>

<head>

<style>

html,
body {{

    margin: 0;

    padding: 0;

    width: 100%;

    height: 100%;

    overflow: hidden;

    background: transparent;
}}


.scene {{

    width: 100%;

    height: 600px;

    display: flex;

    justify-content: center;

    align-items: center;

    position: relative;
}}


.glow {{

    position: absolute;

    width: 320px;

    height: 590px;

    border-radius: 50%;

    background:
        radial-gradient(
            ellipse,
            rgba(0,180,220,0.18),
            transparent 70%
        );

    filter: blur(20px);
}}


.wave {{

    position: absolute;

    width: 100%;

    height: 100px;

    bottom: 40px;

    opacity: 0.16;

    background:
        repeating-linear-gradient(
            -12deg,
            transparent 0px,
            transparent 28px,
            #078baa 29px,
            #078baa 48px,
            transparent 49px,
            transparent 75px
        );
}}


.board {{

    position: relative;

    width: {board_width}px;

    height: {board_height}px;

    border-radius:
        55% 55% 48% 48%
        /
        13% 13% 10% 10%;

    background:
        linear-gradient(
            90deg,
            #cfcbbd 0%,
            #efede1 13%,
            #fffef5 50%,
            #efede1 87%,
            #cfcbbd 100%
        );

    box-shadow:

        0 25px 45px rgba(0,0,0,0.5),

        inset 6px 0 8px
            rgba(255,255,255,0.7),

        inset -6px 0 8px
            rgba(0,0,0,0.12);

    z-index: 5;

    transition:
        width 0.5s ease,
        height 0.5s ease;
}}


.stringer {{

    position: absolute;

    width: 3px;

    height: 90%;

    top: 5%;

    left: 50%;

    transform: translateX(-50%);

    background: #a8b2b1;

    opacity: 0.75;
}}


.board-text {{

    position: absolute;

    left: 50%;

    top: 50%;

    transform:
        translate(-50%, -50%)
        rotate(-90deg);

    font-family: 'Anton', Arial Black, sans-serif;

    font-size: 29px;

    font-weight: 900;

    letter-spacing: 2px;

    color: #078eaf;

    white-space: nowrap;

    text-align: center;

    z-index: 10;
}}


.fin {{

    position: absolute;

    bottom: -31px;

    left: 50%;

    transform: translateX(-50%);

    width: 34px;

    height: 50px;

    background: #102a33;

    clip-path:
        polygon(
            50% 100%,
            0 0,
            100% 0
        );
}}

</style>

</head>


<body>

<div class="scene">

    <div class="glow"></div>

    <div class="wave"></div>

    <div class="board">

        <div class="stringer"></div>

        <div class="board-text">
            {board_text}
        </div>

        <div class="fin"></div>

    </div>

</div>

</body>

</html>
"""


    components.html(
        board_html,
        height=600,
        scrolling=False
    )


# ============================================================
# RECOMENDAÇÃO
# ============================================================

with col_direita:

    with st.container(border=True):

        st.markdown(
            '<div class="panel-title">RECOMENDAÇÃO</div>',
            unsafe_allow_html=True
        )


        # ====================================================
        # ANTES DE CALCULAR
        # ====================================================

        if not calcular:

            # IMPORTANTE:
            # Aqui usamos HTML somente em um único markdown.
            # Não existem elementos Streamlit dentro do HTML.

            st.markdown(
                """
                <div style="
                    height:510px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    text-align:center;
                    color:#5c909d;
                    font-family:'DM Sans',sans-serif;
                    font-size:13px;
                    line-height:1.8;
                ">

                    <div>

                        <div style="
                            font-size:50px;
                            margin-bottom:15px;
                        ">
                            🌊
                        </div>

                        <div style="
                            font-weight:800;
                        ">
                            AJUSTE SEU PERFIL
                        </div>

                        <div>
                            E DESCUBRA
                        </div>

                        <div style="
                            font-weight:800;
                        ">
                            SUA PRANCHA IDEAL
                        </div>

                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        # ====================================================
        # RESULTADO
        # ====================================================

        else:

            st.markdown(
                '<div class="recommendation-label">'
                'SUA PRANCHA IDEAL'
                '</div>',
                unsafe_allow_html=True
            )


            st.markdown(
                f'<div class="recommendation-board">'
                f'{tipo_prancha}'
                f'</div>',
                unsafe_allow_html=True
            )


            st.markdown(
                '<div class="recommendation-divider"></div>',
                unsafe_allow_html=True
            )


            st.markdown(
                '<div class="recommendation-volume-label">'
                'VOLUME RECOMENDADO'
                '</div>',
                unsafe_allow_html=True
            )


            st.markdown(
                f'<div class="recommendation-volume">'
                f'{volume:.1f}L'
                f'</div>',
                unsafe_allow_html=True
            )


            st.markdown(
                f'<div class="recommendation-description">'
                f'{descricao}'
                f'</div>',
                unsafe_allow_html=True
            )


            st.markdown(
                '<div class="recommendation-divider"></div>',
                unsafe_allow_html=True
            )


            st.markdown(
                f"""
                <div class="info-box">

                    <div class="info-name">
                        PESO
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
                <div class="info-box">

                    <div class="info-name">
                        ALTURA
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
                <div class="info-box">

                    <div class="info-name">
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
                <div class="info-box">

                    <div class="info-name">
                        FREQUÊNCIA
                    </div>

                    <div class="info-value">
                        {frequencia}x por mês
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
        margin-top:30px;
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
