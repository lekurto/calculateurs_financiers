import streamlit as st
import pandas as pd

st.title("Calculatrice d'intérêts")
st.write("Prototype d'app de calcul")

capital_initial = st.number_input("Entrez votre capital de départ", value = 100000)
taux = st.slider("Entrez le taux d'intérêt annuel moyen (en pourcentage)", min_value = 0.0, max_value = 20.0, value = 6.0, step = 0.1, help = "Pour 2%, entrez 2")
nb_annees = st.slider("Entrez le nombre d'années", min_value = 1, max_value = 100, value = 10, step = 1)

capital_final = round(capital_initial * (1+taux/100) ** nb_annees)

st.write("Capital final : ", capital_final)

interets_simples = round(capital_initial * taux/100 * nb_annees)
interets_composes = round(capital_final - interets_simples - capital_initial)

st.write("Ce montant se décompose en :")
st.write("Dépôt initial : ", capital_initial)
st.write("Intérêts sur ce dépôt : ", interets_simples)
st.write("Intérêts sur les intérêts : ", interets_composes)


df = pd.DataFrame()

df['annee'] = 0
df['capi_debut'] = 0
df['taux'] = 0

for i in range(0, nb_annees +1):
    df.loc[i, 'capi_debut'] = capital_initial
    df.loc[i, 'taux'] = taux
    df.loc[i, 'annee'] = round(i)
    df.loc[i, 'capi_debut'] = df.loc[i, 'capi_debut'] * (1 + df.loc[i, 'taux']/100) ** (df.loc[i, 'annee'] )

df.style.format(decimal=',').format(thousands=" ")

col1, col2 = st.columns(2)
with col1:
    st.bar_chart(df)
with col2:
    st.dataframe(df)

# for x in range(1, nb_annees):

