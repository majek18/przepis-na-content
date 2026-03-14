import streamlit as st

st.set_page_config(page_title="Oferta", layout="wide")

# stan kliknięcia
if "selected_option" not in st.session_state:
    st.session_state.selected_option = None

# ceny dodatków dla opcji 1
base_price = 0
montaz_podstawowy = 100
dzwiek = 50
napisy = 40
efekty = 60

st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp {
    background-color: #EFE7C6;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* pływająca cena */
.price-box {
    position: fixed;
    top: 20px;
    right: 30px;
    z-index: 9999;
    background: rgba(23, 75, 136, 0.96);
    color: white;
    padding: 16px 22px;
    border-radius: 18px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.18);
    min-width: 170px;
    text-align: center;
}

.price-label {
    font-size: 14px;
    opacity: 0.9;
    margin-bottom: 4px;
}

.price-value {
    font-size: 30px;
    font-weight: 800;
    line-height: 1;
}

/* baner */
.banner {
    position: relative;
    height: 230px;
    border-radius: 30px;
    background: #EFE7C6;
    overflow: hidden;
    margin-bottom: 50px;
    box-shadow: 0 10px 28px rgba(31, 62, 74, 0.08);
}

.circle {
    position: absolute;
    border-radius: 50%;
}

.c1 {
    width: 220px;
    height: 220px;
    background: #F0D45B;
    left: -60px;
    bottom: -50px;
}

.c2 {
    width: 260px;
    height: 260px;
    background: #6EA6C2;
    left: 160px;
    top: -70px;
}

.c3 {
    width: 200px;
    height: 200px;
    background: #174B88;
    right: 180px;
    top: 10px;
}

.c4 {
    width: 230px;
    height: 230px;
    background: #1F3E4A;
    right: 10px;
    bottom: -40px;
}

.rect {
    position: absolute;
    width: 240px;
    height: 140px;
    background: #67B4E5;
    border-radius: 22px;
    left: 50%;
    transform: translateX(-50%);
    bottom: 20px;
}

.banner-text {
    position: absolute;
    z-index: 10;
    left: 40px;
    top: 40px;
}

.banner-title {
    font-size: 40px;
    font-weight: 800;
    color: #174B88;
    margin: 0;
}

.banner-sub {
    font-size: 18px;
    color: #1F3E4A;
    margin-top: 10px;
}

/* kafelki */
.offer-row {
    display: flex;
    justify-content: center;
    gap: 34px;
    margin-top: 10px;
    margin-bottom: 35px;
}

.offer-button {
    border: none;
    background: transparent;
    padding: 0;
}

.offer-card {
    width: 210px;
    height: 250px;
    background: #A9D2F2;
    border-radius: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    font-weight: 800;
    color: #174B88;
    transition: 0.25s ease;
    box-shadow: 0 6px 16px rgba(0,0,0,0.08);
    cursor: pointer;
}

.offer-card:hover {
    background: #8CC0E8;
    transform: translateY(-8px);
    box-shadow: 0 16px 30px rgba(0,0,0,0.15);
}

.offer-card.selected {
    background: #8CC0E8;
    outline: 3px solid #174B88;
}

/* sekcja konfiguratora */
.config-box {
    background: rgba(255,255,255,0.35);
    border: 1px solid rgba(23, 75, 136, 0.12);
    border-radius: 26px;
    padding: 28px 28px 20px 28px;
    margin-top: 18px;
    box-shadow: 0 10px 24px rgba(31, 62, 74, 0.06);
}

.config-title {
    font-size: 30px;
    font-weight: 800;
    color: #174B88;
    margin-bottom: 8px;
}

.config-sub {
    color: #1F3E4A;
    font-size: 16px;
    margin-bottom: 20px;
}

.summary-box {
    background: #F7F2D8;
    border-radius: 20px;
    padding: 18px 20px;
    color: #1F3E4A;
    margin-top: 14px;
}

.summary-line {
    font-size: 16px;
    margin-bottom: 8px;
}

.summary-total {
    font-size: 22px;
    font-weight: 800;
    color: #174B88;
    margin-top: 12px;
}

/* checkbox labels */
div[data-testid="stCheckbox"] label p {
    font-size: 17px !important;
    color: #1F3E4A !important;
}

/* przyciski streamlit */
.stButton > button {
    width: 210px;
    height: 250px;
    border-radius: 28px;
    background: #A9D2F2;
    color: #174B88;
    font-size: 28px;
    font-weight: 800;
    border: none;
    box-shadow: 0 6px 16px rgba(0,0,0,0.08);
    transition: 0.25s ease;
}

.stButton > button:hover {
    background: #8CC0E8;
    color: #174B88;
    border: none;
    transform: translateY(-8px);
}

@media (max-width: 900px) {
    .offer-row {
        flex-direction: column;
        align-items: center;
    }
    .price-box {
        right: 15px;
        top: 15px;
        min-width: 140px;
    }
}
</style>
""", unsafe_allow_html=True)

# baner
st.markdown("""
<div class="banner">
    <div class="circle c1"></div>
    <div class="circle c2"></div>
    <div class="circle c3"></div>
    <div class="circle c4"></div>
    <div class="rect"></div>

    <div class="banner-text">
        <h1 class="banner-title">Oferta współpracy</h1>
        <div class="banner-sub">Wybierz opcję najlepiej dopasowaną do Twoich potrzeb</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 3 opcje
col1, col2, col3 = st.columns([1, 1, 1], gap="large")

with col1:
    if st.button("Opcja 1", key="opcja1"):
        st.session_state.selected_option = "Opcja 1"

with col2:
    if st.button("Opcja 2", key="opcja2"):
        st.session_state.selected_option = "Opcja 2"

with col3:
    if st.button("Opcja 3", key="opcja3"):
        st.session_state.selected_option = "Opcja 3"

# konfigurator dla opcji 1
total_price = 0
selected_items = []

if st.session_state.selected_option == "Opcja 1":
    st.markdown("""
    <div class="config-box">
        <div class="config-title">Skonfiguruj Opcję 1</div>
        <div class="config-sub">Zaznacz dodatki, a cena zaktualizuje się automatycznie.</div>
    </div>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([1.2, 1], gap="large")

    with col_left:
        add_montaz = st.checkbox("Montaż podstawowy +100 zł (do 2 minut)")
        add_dzwiek = st.checkbox("Dodanie dźwięku +50 zł")
        add_napisy = st.checkbox("Dodanie napisów +40 zł")
        add_efekty = st.checkbox("Dodanie efektów specjalnych +60 zł")

    if add_montaz:
        total_price += montaz_podstawowy
        selected_items.append("Montaż podstawowy — 100 zł")

    if add_dzwiek:
        total_price += dzwiek
        selected_items.append("Dodanie dźwięku — 50 zł")

    if add_napisy:
        total_price += napisy
        selected_items.append("Dodanie napisów — 40 zł")

    if add_efekty:
        total_price += efekty
        selected_items.append("Dodanie efektów specjalnych — 60 zł")

    with col_right:
        st.markdown('<div class="summary-box">', unsafe_allow_html=True)
        st.markdown("### Podsumowanie")
        if selected_items:
            for item in selected_items:
                st.markdown(f'<div class="summary-line">• {item}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="summary-line">Nie wybrano jeszcze dodatków.</div>', unsafe_allow_html=True)

        st.markdown(f'<div class="summary-total">Cena końcowa: {total_price} zł</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.selected_option == "Opcja 2":
    st.markdown("""
    <div class="config-box">
        <div class="config-title">Opcja 2</div>
        <div class="config-sub">Tu później możemy dodać osobny konfigurator.</div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.selected_option == "Opcja 3":
    st.markdown("""
    <div class="config-box">
        <div class="config-title">Opcja 3</div>
        <div class="config-sub">Tu później możemy dodać osobny konfigurator.</div>
    </div>
    """, unsafe_allow_html=True)

# pływająca cena
st.markdown(f"""
<div class="price-box">
    <div class="price-label">Cena końcowa</div>
    <div class="price-value">{total_price} zł</div>
</div>
""", unsafe_allow_html=True)
