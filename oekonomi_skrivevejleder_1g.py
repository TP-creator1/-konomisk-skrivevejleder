# Streamlit skrivevejleder til 1.g i økonomiforløb
# Tema: Økonomiske styringsinstrumenter, økonomiske mål og markedets rolle

import streamlit as st

st.title("📘 Skrivevejleder – Økonomi og politisk styring i 1.g")
st.subheader("Afsluttende skriveøvelse: Skal politikerne blande sig i markedet?")
st.write("Denne vejleder hjælper dig med at strukturere dine tanker og argumenter om økonomisk politik, styringsinstrumenter og markedets rolle.")

st.markdown("---")

# 1. Forstå emnet
tema = st.text_area("1. Hvad handler spørgsmålet om markedets rolle om? Hvordan forstår du diskussionen om stat vs. marked?")

# 2. Økonomisk viden
st.header("2. Økonomisk faglig viden")
kredslob = st.text_area("Hvordan hænger det økonomiske kredsløb sammen med politisk indblanding?")
styringsinstrumenter = st.text_area("Forklar kort de tre styringsinstrumenter: finanspolitik, pengepolitik og strukturpolitik. Hvilke mål kan de påvirke?")
mal = st.text_area("Vælg to økonomiske mål (fx inflation, beskæftigelse, balance mv.). Hvordan hænger de sammen med styringsinstrumenter?")

# 3. Politisk ideologi
st.header("3. Politisk ideologi")
ideologi = st.text_area("Hvordan vil en liberal og en socialistisk ideologi typisk se på statens rolle i økonomien? Giv konkrete eksempler.")

# 4. Argumentation
st.header("4. Argumentation – din holdning")
pastring = st.text_area("Hvad mener du selv? Hvor stor en rolle bør staten spille i styringen af økonomien?")
belæg = st.text_area("Hvad er dit belæg? (Fx: Hvilke fakta, erfaringer eller principper bygger du din holdning på?)")
refleksion = st.text_area("Reflektér: Hvad er konsekvensen af din holdning? Hvad kunne modargumentet være?")

# 5. Diskussion
st.header("5. Klar til diskussion")
diskussion = st.text_area("Skriv en afsluttende vurdering, hvor du vejer statens og markedets rolle op mod hinanden. Henvis gerne til faglig viden og ideologier.")

st.success("Gem dine svar. Brug dem til den mundtlige diskussion i klassen.")
