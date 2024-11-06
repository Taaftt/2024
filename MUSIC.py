import streamlit as st
import pandas as pd

# Carga el archivo CSV "top_hiphop_artists_tracks.csv" en un DataFrame de pandas.
df = pd.read_csv("top_hiphop_artists_tracks.csv")

# Crea una nueva columna con el enlace completo de Spotify
base_url = "https://open.spotify.com/intl-es/track/"
df['spotify_link'] = base_url + df['Track ID']

# Título general de la aplicación
st.title("Hip Hop Songs")

# Selección del top
st.subheader("Selecciona el top de canciones a mostrar")
top_n = st.slider("Elige el número de canciones (Top N)", min_value=10, max_value=100, step=10)

# Ordena las canciones por la columna de popularidad
# Asegúrate de que la columna que representa popularidad se llame "Popularity" (ajusta si tiene otro nombre)
df_sorted = df.sort_values(by="Popularity", ascending=False)

# Filtra el DataFrame para obtener solo el top seleccionado
df_top_n = df_sorted.head(top_n)

# Selección de artista
st.subheader("Filtra por artista")
artistas = df_top_n['Artist'].unique()
artista_seleccionado = st.selectbox("Selecciona un artista", ["Todos"] + list(artistas))

# Filtra las canciones por el artista seleccionado, si se eligió alguno específico
if artista_seleccionado != "Todos":
    df_top_n = df_top_n[df_top_n['Artist'] == artista_seleccionado]

# Mostrar las canciones filtradas con enlaces
st.subheader(f"Top {top_n} canciones de Hip Hop")
for i in range(len(df_top_n)):
    song = df_top_n['Track Name'].iloc[i]
    link = df_top_n['spotify_link'].iloc[i]
    artist = df_top_n['Artist'].iloc[i]
    # Mostrar cada canción con el nombre del artista y un enlace clickeable
    st.markdown(f"**{song}** - {artist} [Escuchar en Spotify]({link})", unsafe_allow_html=True)

