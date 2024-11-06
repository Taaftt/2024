import streamlit as st
import pandas as pd

# Carga el archivo CSV "top 100 streamed_songs.csv" en un DataFrame de pandas.
df = pd.read_csv("top_hiphop_artists_tracks.csv")

# Crea una nueva columna con el enlace completo de Spotify
base_url = "https://open.spotify.com/intl-es/track/"
df['spotify_link'] = base_url + df['Track ID']

# Titulo
st.title("Mejores 100 canciones de Spotify")
# Descripción
st.write("Explora los mejores temas")

# Mostrar los enlaces en formato interactivo usando st.markdown
st.subheader("Canciones y Enlaces a Spotify")
for i in range(len(df)):
    song = df['Track Name'].iloc[i]
    link = df['spotify_link'].iloc[i]
    # Mostrar cada canción como un enlace clickeable
    st.markdown(f"[{song}]({link})", unsafe_allow_html=True)
    # Menú desplegable para seleccionar un artista
artistas = df['Artist'].unique()
artista_seleccionado = st.selectbox("Selecciona un artista", artistas)

# Filtrar las canciones según el artista seleccionado
df_filtrado = df[df['Artist'] == artista_seleccionado]

# Mostrar los enlaces en formato interactivo usando st.markdown
st.subheader(f"Canciones de {artista_seleccionado}")
for i in range(len(df_filtrado)):
    song = df_filtrado['Track Name'].iloc[i]
    link = df_filtrado['spotify_link'].iloc[i]
    # Mostrar cada canción como un enlace clickeable
    st.markdown(f"[{song}]({link})", unsafe_allow_html=True)
