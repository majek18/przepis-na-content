import streamlit as st

st.set_page_config(page_title="Oferta", layout="wide")

st.markdown("""
<style>
/* Tło całej strony */
.stApp {
    background-color: #F3EFCB;
}

/* Usunięcie dużych odstępów u góry */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* Baner */
.banner {
    position: relative;
    height: 260px;
    border-radius: 28px;
    background: #F3EFCB;
    overflow: hidden;
    margin-bottom: 40px;
    box-shadow: 0 10px 30px rgba(20, 40, 60, 0.08);
}

.circle {
    position: absolute;
    border-radius: 50%;
    opacity: 1;
}

.c1 {
    width: 260px;
    height: 260px;
    background: #F0D45B;
    left: -70px;
    bottom: -60px;
}

.c2 {
    width: 300px;
    height: 300px;
    background: #6EA6C2;
    left: 180px;
    top: -70px;
}

.c3 {
    width: 220px;
    height: 220px;
    background: #174B88;
    right: 170px;
    top: 10px;
}

.c4 {
    width: 250px;
    height: 250px;
    background: #1F3E4A;
    right: 20px;
    bottom: -40px;
}

.rect {
    position: absolute;
    width: 260px;
    height: 160px;
    background: #67B4E5;
    border-radius: 24px;
    left: 50%;
    transform: translateX(-50%);
    bottom: 28px;
}

.banner-content {
    position: relative;
    z-index: 2;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 32px 44px;
}

.banner-title {
    font-size: 44px;
    font-weight: 800;
    color: #174B88;
    margin: 0;
    line-height: 1.05;
    max-width: 520px;
}

.banner-subtitle {
    font-size: 18px;
    color: #1F3E4A;
    margin-top: 14px;
    max-width: 520px;
}

/* Karty oferty */
.offer-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 28px;
    margin-top: 10px;
}

.offer-card {
    background: #A9D2F2;
    border-radius: 28px;
    min-height: 340px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    transition: transform 0.25s ease, box-shadow 0.25s ease, background 0.25s ease;
    box-shadow: 0 8px 20px rgba(23, 75, 136, 0.08);
    cursor: pointer;
}

.offer-card:hover {
    transform: translateY(-8px);
    background: #8CC0E8;
    box-shadow: 0 18px 32px rgba(23, 75, 136, 0.18);
}

.offer-card span {
    font-size: 34px;
    font-weight: 800;
    color: #174B88;
}

/* Responsywność */
@media (max-width: 900px) {
    .offer-grid {
        grid-template-columns: 1fr;
    }

    .offer-card {
        min-height: 220px;
    }

    .banner {
        height: 300px;
    }

    .banner-title {
        font-size: 34px;
    }
}
</style>

<div class="banner">
    <div class="circle c1"></div>
    <div class="circle c2"></div>
    <div class="circle c3"></div>
    <div class="circle c4"></div>
    <div class="rect"></div>

    <div class="banner-content">
        <h1 class="banner-title">Oferta współpracy</h1>
        <div class="banner-subtitle">
            Wybierz opcję najlepiej dopasowaną do Twoich potrzeb.
        </div>
    </div>
</div>

<div class="offer-grid">
    <div class="offer-card"><span>Opcja 1</span></div>
    <div class="offer-card"><span>Opcja 2</span></div>
    <div class="offer-card"><span>Opcja 3</span></div>
</div>
""", unsafe_allow_html=True)
