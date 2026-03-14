import streamlit as st

st.set_page_config(
    page_title="Oferta współpracy",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------
# STATE
# -----------------------
if "selected_option" not in st.session_state:
    st.session_state.selected_option = None

# -----------------------
# STYLE
# -----------------------
st.markdown("""
<style>
/* Ukrycie elementów Streamlit */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Global */
html, body, [class*="css"]  {
    font-family: "Inter", sans-serif;
}

.stApp {
    background-color: #EFE7C6;
}

/* Ważne: pełna szerokość strony */
.block-container {
    max-width: 100% !important;
    padding-top: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    padding-bottom: 3rem !important;
}

/* Sekcja z marginesami dla reszty treści */
.content-wrap {
    padding-left: 32px;
    padding-right: 32px;
    padding-top: 28px;
}

/* Pływająca cena */
.price-box {
    position: fixed;
    top: 16px;
    right: 16px;
    z-index: 99999;
    background: #23589A;
    color: white;
    padding: 14px 18px;
    border-radius: 20px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.18);
    min-width: 150px;
    text-align: right;
}

.price-label {
    font-size: 14px;
    font-weight: 500;
    opacity: 0.95;
    margin-bottom: 4px;
}

.price-value {
    font-size: 28px;
    font-weight: 800;
    line-height: 1;
}

/* Baner full width */
.banner {
    width: 100%;
    min-height: 300px;
    background: #E8E1BE;
    position: relative;
    overflow: hidden;
    border-radius: 0 0 28px 28px;
    box-shadow: 0 12px 32px rgba(31, 62, 74, 0.08);
}

.banner-inner {
    position: relative;
    width: 100%;
    min-height: 300px;
    padding: 42px 32px 36px 32px;
    display: flex;
    align-items: flex-start;
    justify-content: flex-start;
    z-index: 2;
}

.banner-copy {
    position: relative;
    z-index: 5;
    max-width: 560px;
}

.banner-title {
    margin: 0;
    font-size: 46px;
    font-weight: 800;
    color: #174B88;
    line-height: 1.05;
}

.banner-sub {
    margin-top: 14px;
    font-size: 18px;
    color: #1F3E4A;
    line-height: 1.5;
}

/* Kształty w banerze */
.shape {
    position: absolute;
    border-radius: 999px;
}

.shape-yellow {
    width: 260px;
    height: 260px;
    background: #EBCF58;
    left: -70px;
    bottom: -55px;
}

.shape-blue1 {
    width: 330px;
    height: 330px;
    background: #6F9FBE;
    left: 190px;
    top: -85px;
}

.shape-blue2 {
    width: 230px;
    height: 230px;
    background: #1F4F91;
    right: 210px;
    top: 12px;
}

.shape-dark {
    width: 290px;
    height: 290px;
    background: #203E4C;
    right: 24px;
    bottom: -48px;
}

.shape-rect {
    position: absolute;
    width: 270px;
    height: 150px;
    background: #70AFE0;
    border-radius: 26px;
    left: 50%;
    bottom: 22px;
    transform: translateX(-50%);
}

/* Nagłówek sekcji */
.section-title {
    font-size: 32px;
    font-weight: 800;
    color: #174B88;
    margin-bottom: 8px;
}

.section-sub {
    font-size: 16px;
    color: #1F3E4A;
    margin-bottom: 28px;
}

/* Przyciski opcji */
.stButton > button {
    width: 100%;
    min-height: 220px;
    border-radius: 28px;
    background: #A7C8E7;
    color: #174B88;
    font-size: 24px;
    font-weight: 800;
    border: none;
    box-shadow: 0 8px 18px rgba(23, 75, 136, 0.08);
    transition: all 0.25s ease;
}

.stButton > button:hover {
    background: #91BCE0;
    color: #174B88;
    transform: translateY(-6px);
    box-shadow: 0 16px 30px rgba(23, 75, 136, 0.16);
    border: none;
}

.stButton > button:focus:not(:active) {
    border: none;
    box-shadow: 0 0 0 3px rgba(23, 75, 136, 0.18);
    color: #174B88;
}

/* Moduł konfiguratora */
.config-card {
    margin-top: 26px;
    background: rgba(255,255,255,0.38);
    border: 1px solid rgba(23, 75, 136, 0.10);
    border-radius: 26px;
    padding: 24px;
    box-shadow: 0 10px 24px rgba(31, 62, 74, 0.06);
}

.config-title {
    font-size: 28px;
    font-weight: 800;
    color: #174B88;
    margin-bottom: 6px;
}

.config-sub {
    font-size: 16px;
    color: #1F3E4A;
    margin-bottom: 18px;
}

/* Checkboxy */
div[data-testid="stCheckbox"] {
    background: rgba(255,255,255,0.28);
    padding: 10px 12px;
    border-radius: 16px;
    margin-bottom: 10px;
    border: 1px solid rgba(23, 75, 136, 0.08);
}

div[data-testid="stCheckbox"] label p {
    font-size: 16px !important;
    color: #1F3E4A !important;
    font-weight: 500 !important;
}

/* Podsumowanie */
.summary-box {
    background: #F6F0D2;
    border-radius: 22px;
    padding: 20px;
    border: 1px solid rgba(23, 75, 136, 0.08);
}

.summary-title {
    font-size: 22px;
    font-weight: 800;
    color: #174B88;
    margin-bottom: 14px;
}

.summary-line {
    color: #1F3E4A;
    font-size: 15px;
    margin-bottom: 8px;
    line-height: 1.4;
}

.summary-total {
    margin-top: 14px;
    font-size: 24px;
    font-weight: 800;
    color: #174B88;
}

/* Mobile */
@media (max-width: 768px) {
    .content-wrap {
        padding-left: 16px;
        padding-right: 16px;
        padding-top: 18px;
    }

    .banner {
        min-height: 240px;
        border-radius: 0 0 22px 22px;
    }

    .banner-inner {
        min-height: 240px;
        padding: 24px 16px 24px 16px;
    }

    .banner-title {
        font-size: 30px;
    }

    .banner-sub {
        font-size: 15px;
        max-width: 280px;
    }

    .shape-yellow {
        width: 180px;
        height: 180px;
        left: -60px;
        bottom: -45px;
    }

    .shape-blue1 {
        width: 210px;
        height: 210px;
        left: 85px;
        top: -55px;
    }

    .shape-blue2 {
        width: 150px;
        height: 150px;
        right: 88px;
        top: 20px;
    }

    .shape-dark {
        width: 190px;
        height: 190px;
        right: -20px;
        bottom: -36px;
    }

    .shape-rect {
        width: 170px;
        height: 95px;
        bottom: 18px;
    }

    .price-box {
        top: 10px;
        right: 10px;
        min-width: 126px;
        padding: 12px 14px;
        border-radius: 16px;
    }

    .price-label {
        font-size: 12px;
    }

    .price-value {
        font-size: 22px;
    }

    .section-title {
        font-size: 24px;
    }

    .section-sub {
        font-size: 14px;
        margin-bottom: 20px;
    }

    .stButton > button {
        min-height: 150px;
        font-size: 20px;
        border-radius: 22px;
    }

    .config-card {
        padding: 18px;
        border-radius: 22px;
    }

    .config-title {
        font-size: 22px;
    }

    .summary-total {
        font-size: 22px;
    }
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# BANNER
# -----------------------
st.markdown("""
<div class="banner">
    <div class="shape shape-yellow"></div>
    <div class="shape shape-blue1"></div>
    <div class="shape shape-blue2"></div>
    <div class="shape shape-dark"></div>
    <div class="shape-rect"></div>

    <div class="banner-inner">
        <div class="banner-copy">
            <h1 class="banner-title">Oferta współpracy</h1>
            <div class="banner-sub">
                Wybierz opcję najlepiej dopasowaną do Twoich potrzeb i skonfiguruj usługę pod swój projekt.
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------
# CONTENT START
# -----------------------
st.markdown('<div class="content-wrap">', unsafe_allow_html=True)

st.markdown('<div class="section-title">Dostępne opcje</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Kliknij wybraną opcję, aby zobaczyć szczegóły i dodatki.</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    if st.button("Opcja 1", key="opcja_1"):
        st.session_state.selected_option = "Opcja 1"

with col2:
    if st.button("Opcja 2", key="opcja_2"):
        st.session_state.selected_option = "Opcja 2"

with col3:
    if st.button("Opcja 3", key="opcja_3"):
        st.session_state.selected_option = "Opcja 3"

total_price = 0
selected_items = []

if st.session_state.selected_option == "Opcja 1":
    st.markdown("""
    <div class="config-card">
        <div class="config-title">Konfigurator — Opcja 1</div>
        <div class="config-sub">Zaznacz dodatki, a cena zaktualizuje się automatycznie.</div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.35, 1], gap="large")

    with left:
        add_montaz = st.checkbox("Montaż podstawowy +100 zł (do 2 minut)")
        add_dzwiek = st.checkbox("Dodanie dźwięku +50 zł")
        add_napisy = st.checkbox("Dodanie napisów +40 zł")
        add_efekty = st.checkbox("Dodanie efektów specjalnych +60 zł")

    if add_montaz:
        total_price += 100
        selected_items.append("Montaż podstawowy — 100 zł")

    if add_dzwiek:
        total_price += 50
        selected_items.append("Dodanie dźwięku — 50 zł")

    if add_napisy:
        total_price += 40
        selected_items.append("Dodanie napisów — 40 zł")

    if add_efekty:
        total_price += 60
        selected_items.append("Dodanie efektów specjalnych — 60 zł")

    with right:
        st.markdown('<div class="summary-box">', unsafe_allow_html=True)
        st.markdown('<div class="summary-title">Podsumowanie</div>', unsafe_allow_html=True)

        if selected_items:
            for item in selected_items:
                st.markdown(f'<div class="summary-line">• {item}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="summary-line">Nie wybrano jeszcze żadnych dodatków.</div>', unsafe_allow_html=True)

        st.markdown(f'<div class="summary-total">Razem: {total_price} zł</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.selected_option == "Opcja 2":
    st.markdown("""
    <div class="config-card">
        <div class="config-title">Opcja 2</div>
        <div class="config-sub">Tutaj możemy później dodać osobny zakres usługi i osobny cennik.</div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_option == "Opcja 3":
    st.markdown("""
    <div class="config-card">
        <div class="config-title">Opcja 3</div>
        <div class="config-sub">Tutaj możemy później dodać trzeci wariant oferty.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# FLOATING PRICE
# -----------------------
st.markdown(f"""
<div class="price-box">
    <div class="price-label">Cena końcowa</div>
    <div class="price-value">{total_price} zł</div>
</div>
""", unsafe_allow_html=True)
