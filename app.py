import streamlit as st

st.set_page_config(
    page_title="Oferta współpracy",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------
# STATE
# -------------------------
if "selected_option" not in st.session_state:
    st.session_state.selected_option = None

# -------------------------
# STYLE
# -------------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

html, body, [class*="css"] {
    font-family: "Inter", sans-serif;
}

.stApp {
    background-color: #EFE7C6;
}

.block-container {
    max-width: 100% !important;
    padding: 0 !important;
}

.main-wrap {
    width: 100%;
}

.content-wrap {
    padding: 28px 28px 48px 28px;
}

/* floating price */
.price-box {
    position: fixed;
    top: 14px;
    right: 14px;
    z-index: 99999;
    background: #23589A;
    color: white;
    padding: 14px 16px;
    border-radius: 18px;
    min-width: 145px;
    text-align: right;
    box-shadow: 0 10px 24px rgba(0,0,0,0.18);
}

.price-label {
    font-size: 13px;
    font-weight: 500;
    opacity: 0.95;
    margin-bottom: 4px;
}

.price-value {
    font-size: 26px;
    font-weight: 800;
    line-height: 1;
}

/* banner */
.banner {
    position: relative;
    width: 100%;
    min-height: 310px;
    background: #E8E1BE;
    overflow: hidden;
    box-shadow: 0 12px 28px rgba(31, 62, 74, 0.08);
}

.banner-copy {
    position: relative;
    z-index: 5;
    padding: 42px 28px;
    max-width: 620px;
}

.banner-title {
    margin: 0;
    font-size: 48px;
    line-height: 1.05;
    font-weight: 800;
    color: #174B88;
}

.banner-sub {
    margin-top: 14px;
    font-size: 18px;
    line-height: 1.5;
    color: #1F3E4A;
}

.shape {
    position: absolute;
    border-radius: 999px;
}

.shape-yellow {
    width: 270px;
    height: 270px;
    background: #E7CF60;
    left: -80px;
    bottom: -70px;
}

.shape-blue-soft {
    width: 340px;
    height: 340px;
    background: #719FBB;
    left: 180px;
    top: -95px;
}

.shape-blue {
    width: 220px;
    height: 220px;
    background: #214E90;
    right: 220px;
    top: 14px;
}

.shape-dark {
    width: 300px;
    height: 300px;
    background: #203F4B;
    right: 14px;
    bottom: -55px;
}

.shape-rect {
    position: absolute;
    width: 280px;
    height: 155px;
    background: #73AFE0;
    border-radius: 26px;
    left: 50%;
    bottom: 28px;
    transform: translateX(-50%);
}

/* typography */
.section-title {
    font-size: 34px;
    font-weight: 800;
    color: #174B88;
    margin-bottom: 8px;
}

.section-sub {
    font-size: 16px;
    color: #1F3E4A;
    margin-bottom: 24px;
}

/* option card */
.option-card {
    background: #A7C8E7;
    border-radius: 28px;
    padding: 26px 18px 20px 18px;
    min-height: 255px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    text-align: center;
    box-shadow: 0 8px 18px rgba(23, 75, 136, 0.08);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.option-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 16px 28px rgba(23, 75, 136, 0.14);
}

.option-icon {
    width: 74px;
    height: 74px;
    border-radius: 999px;
    background: rgba(255,255,255,0.38);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 34px;
    margin-bottom: 16px;
}

.option-title {
    font-size: 28px;
    font-weight: 800;
    color: #174B88;
    margin-bottom: 8px;
}

.option-desc {
    font-size: 15px;
    line-height: 1.45;
    color: #1F3E4A;
    max-width: 250px;
    margin-bottom: 18px;
}

/* choose buttons */
.stButton > button {
    width: 100%;
    border-radius: 16px;
    border: none;
    background: #174B88;
    color: white;
    font-size: 16px;
    font-weight: 700;
    min-height: 48px;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background: #123B6D;
    color: white;
    border: none;
}

.stButton > button:focus:not(:active) {
    border: none;
    color: white;
}

/* inline mobile configurator */
.inline-config {
    margin-top: 14px;
    background: rgba(255,255,255,0.34);
    border: 1px solid rgba(23, 75, 136, 0.10);
    border-radius: 20px;
    padding: 14px;
}

.inline-config-title {
    font-size: 18px;
    font-weight: 800;
    color: #174B88;
    margin-bottom: 10px;
}

.inline-price {
    margin-top: 10px;
    font-size: 18px;
    font-weight: 800;
    color: #174B88;
}

/* desktop configurator */
.config-card {
    margin-top: 28px;
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

/* checkboxes */
div[data-testid="stCheckbox"] {
    background: rgba(255,255,255,0.30);
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

/* summary */
.summary-box {
    background: #F5EFCF;
    border-radius: 22px;
    padding: 20px;
    border: 1px solid rgba(23, 75, 136, 0.08);
}

.summary-title {
    font-size: 22px;
    font-weight: 800;
    color: #174B88;
    margin-bottom: 12px;
}

.summary-line {
    font-size: 15px;
    color: #1F3E4A;
    margin-bottom: 8px;
    line-height: 1.4;
}

.summary-total {
    margin-top: 14px;
    font-size: 24px;
    font-weight: 800;
    color: #174B88;
}

/* mobile helper */
.mobile-only {
    display: none;
}

.desktop-only {
    display: block;
}

/* responsive */
@media (max-width: 768px) {
    .content-wrap {
        padding: 18px 14px 38px 14px;
    }

    .banner {
        min-height: 235px;
    }

    .banner-copy {
        padding: 24px 16px;
        max-width: 290px;
    }

    .banner-title {
        font-size: 30px;
    }

    .banner-sub {
        font-size: 15px;
    }

    .shape-yellow {
        width: 180px;
        height: 180px;
        left: -55px;
        bottom: -50px;
    }

    .shape-blue-soft {
        width: 220px;
        height: 220px;
        left: 82px;
        top: -58px;
    }

    .shape-blue {
        width: 145px;
        height: 145px;
        right: 88px;
        top: 16px;
    }

    .shape-dark {
        width: 185px;
        height: 185px;
        right: -18px;
        bottom: -34px;
    }

    .shape-rect {
        width: 170px;
        height: 96px;
        bottom: 18px;
    }

    .price-box {
        top: 8px;
        right: 8px;
        min-width: 118px;
        padding: 11px 12px;
        border-radius: 14px;
    }

    .price-label {
        font-size: 11px;
    }

    .price-value {
        font-size: 21px;
    }

    .section-title {
        font-size: 26px;
    }

    .section-sub {
        font-size: 14px;
        margin-bottom: 18px;
    }

    .option-card {
        min-height: 215px;
        padding: 20px 14px 16px 14px;
        border-radius: 22px;
    }

    .option-icon {
        width: 62px;
        height: 62px;
        font-size: 28px;
        margin-bottom: 12px;
    }

    .option-title {
        font-size: 22px;
    }

    .option-desc {
        font-size: 14px;
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

    .mobile-only {
        display: block;
    }

    .desktop-only {
        display: none;
    }
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# HELPERS
# -------------------------
def calculate_option_1_total():
    total = 0
    selected_items = []

    if st.session_state.get("add_montaz_mobile", False) or st.session_state.get("add_montaz_desktop", False):
        total += 100
        selected_items.append("Montaż podstawowy — 100 zł")

    if st.session_state.get("add_dzwiek_mobile", False) or st.session_state.get("add_dzwiek_desktop", False):
        total += 50
        selected_items.append("Dodanie dźwięku — 50 zł")

    if st.session_state.get("add_napisy_mobile", False) or st.session_state.get("add_napisy_desktop", False):
        total += 40
        selected_items.append("Dodanie napisów — 40 zł")

    if st.session_state.get("add_efekty_mobile", False) or st.session_state.get("add_efekty_desktop", False):
        total += 60
        selected_items.append("Dodanie efektów specjalnych — 60 zł")

    return total, selected_items

# -------------------------
# BANNER
# -------------------------
st.markdown("""
<div class="main-wrap">
<div class="banner">
<div class="shape shape-yellow"></div>
<div class="shape shape-blue-soft"></div>
<div class="shape shape-blue"></div>
<div class="shape shape-dark"></div>
<div class="shape-rect"></div>

<div class="banner-copy">
<h1 class="banner-title">Oferta współpracy</h1>
<div class="banner-sub">
Wybierz opcję najlepiej dopasowaną do Twoich potrzeb i skonfiguruj usługę pod swój projekt.
</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# -------------------------
# CONTENT
# -------------------------
st.markdown('<div class="content-wrap">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Dostępne opcje</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Wybierz pakiet, a następnie skonfiguruj szczegóły.</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
<div class="option-card">
<div>
<div class="option-icon">🎬</div>
<div class="option-title">Opcja 1</div>
<div class="option-desc">Montaż i dodatki do krótkiego materiału wideo.</div>
</div>
</div>
""", unsafe_allow_html=True)

    if st.button("Wybierz opcję 1", key="opcja_1"):
        st.session_state.selected_option = "Opcja 1"

    # MOBILE: konfigurator bezpośrednio pod opcją
    st.markdown('<div class="mobile-only">', unsafe_allow_html=True)
    if st.session_state.selected_option == "Opcja 1":
        st.markdown("""
<div class="inline-config">
<div class="inline-config-title">Skonfiguruj usługę</div>
</div>
""", unsafe_allow_html=True)

        st.checkbox(
            "Montaż podstawowy +100 zł (do 2 minut)",
            key="add_montaz_mobile"
        )
        st.checkbox(
            "Dodanie dźwięku +50 zł",
            key="add_dzwiek_mobile"
        )
        st.checkbox(
            "Dodanie napisów +40 zł",
            key="add_napisy_mobile"
        )
        st.checkbox(
            "Dodanie efektów specjalnych +60 zł",
            key="add_efekty_mobile"
        )

        mobile_total, _ = calculate_option_1_total()
        st.markdown(
            f'<div class="inline-price">Cena: {mobile_total} zł</div>',
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="option-card">
<div>
<div class="option-icon">📱</div>
<div class="option-title">Opcja 2</div>
<div class="option-desc">Pakiet pod social media i publikację materiałów.</div>
</div>
</div>
""", unsafe_allow_html=True)

    if st.button("Wybierz opcję 2", key="opcja_2"):
        st.session_state.selected_option = "Opcja 2"

with col3:
    st.markdown("""
<div class="option-card">
<div>
<div class="option-icon">✨</div>
<div class="option-title">Opcja 3</div>
<div class="option-desc">Wariant rozszerzony z większą liczbą elementów.</div>
</div>
</div>
""", unsafe_allow_html=True)

    if st.button("Wybierz opcję 3", key="opcja_3"):
        st.session_state.selected_option = "Opcja 3"

# DESKTOP: konfigurator niżej
st.markdown('<div class="desktop-only">', unsafe_allow_html=True)

if st.session_state.selected_option == "Opcja 1":
    st.markdown("""
<div class="config-card">
<div class="config-title">Konfigurator — Opcja 1</div>
<div class="config-sub">Zaznacz dodatki, a cena zaktualizuje się automatycznie.</div>
</div>
""", unsafe_allow_html=True)

    left, right = st.columns([1.35, 1], gap="large")

    with left:
        st.checkbox(
            "Montaż podstawowy +100 zł (do 2 minut)",
            key="add_montaz_desktop"
        )
        st.checkbox(
            "Dodanie dźwięku +50 zł",
            key="add_dzwiek_desktop"
        )
        st.checkbox(
            "Dodanie napisów +40 zł",
            key="add_napisy_desktop"
        )
        st.checkbox(
            "Dodanie efektów specjalnych +60 zł",
            key="add_efekty_desktop"
        )

    total_price, selected_items = calculate_option_1_total()

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

elif st.session_state.selected_option == "Opcja 2":
    st.markdown("""
<div class="config-card">
<div class="config-title">Opcja 2</div>
<div class="config-sub">Tutaj możemy dodać osobny konfigurator dla drugiego pakietu.</div>
</div>
""", unsafe_allow_html=True)

elif st.session_state.selected_option == "Opcja 3":
    st.markdown("""
<div class="config-card">
<div class="config-title">Opcja 3</div>
<div class="config-sub">Tutaj możemy dodać osobny konfigurator dla trzeciego pakietu.</div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# final floating price
total_price, _ = calculate_option_1_total()

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="price-box">
<div class="price-label">Cena końcowa</div>
<div class="price-value">{total_price} zł</div>
</div>
""", unsafe_allow_html=True)
