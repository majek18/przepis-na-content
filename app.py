import streamlit as st

st.set_page_config(page_title="Oferta", layout="wide")

st.markdown("""
<style>

/* ukrycie elementów streamlit */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* tło */
.stApp {
    background-color: #EFE7C6;
}

/* BANER */
.banner {
    position: relative;
    height: 230px;
    border-radius: 30px;
    background: #EFE7C6;
    overflow: hidden;
    margin-bottom: 60px;
}

/* kolorowe koła */

.circle{
position:absolute;
border-radius:50%;
}

.c1{
width:220px;
height:220px;
background:#F0D45B;
left:-60px;
bottom:-50px;
}

.c2{
width:260px;
height:260px;
background:#6EA6C2;
left:160px;
top:-70px;
}

.c3{
width:200px;
height:200px;
background:#174B88;
right:180px;
top:10px;
}

.c4{
width:230px;
height:230px;
background:#1F3E4A;
right:10px;
bottom:-40px;
}

/* niebieski prostokąt */
.rect{
position:absolute;
width:240px;
height:140px;
background:#67B4E5;
border-radius:22px;
left:50%;
transform:translateX(-50%);
bottom:20px;
}

/* tekst banera */
.banner-text{
position:absolute;
z-index:10;
left:40px;
top:40px;
}

.banner-title{
font-size:40px;
font-weight:800;
color:#174B88;
margin:0;
}

.banner-sub{
font-size:18px;
color:#1F3E4A;
margin-top:10px;
}

/* OFERTA */

.offer-container{
display:flex;
justify-content:center;
gap:40px;
margin-top:20px;
}

/* prostokąty */

.offer{
width:220px;
height:260px;
background:#A9D2F2;
border-radius:28px;
display:flex;
align-items:center;
justify-content:center;
font-size:28px;
font-weight:700;
color:#174B88;
transition:0.25s;
box-shadow:0 6px 16px rgba(0,0,0,0.08);
}

/* hover */

.offer:hover{
background:#8CC0E8;
transform:translateY(-8px);
box-shadow:0 16px 30px rgba(0,0,0,0.15);
cursor:pointer;
}

</style>

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

<div class="offer-container">

<div class="offer">Opcja 1</div>
<div class="offer">Opcja 2</div>
<div class="offer">Opcja 3</div>

</div>

""", unsafe_allow_html=True)
