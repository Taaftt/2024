import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carga el archivo CSV "database_titanic.csv" en un DataFrame de pandas.
df = pd.read_csv("top 100 streamed_songs.csv")

#Titulo
st.title("Mejores 100 canciones de spotify")
#descripcion
st.write("Explora los mejores temass")


# Mostrar los enlaces en formato interactivo usando st.markdown
st.subheader("Canciones y Enlaces a Spotify")
for i in range(len(df)):
    song = df['name'].iloc[i]
    link = df['spotify_url'].iloc[i]
    # Mostrar cada canción como un enlace clickeable
    st.markdown(f"[{song}]({link})")
