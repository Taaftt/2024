import streamlit as st
import pandas as pd

# Carga el archivo CSV "top_hiphop_artists_tracks.csv" en un DataFrame de pandas.
df = pd.read_csv("top_hiphop_artists_tracks.csv")

# Crea una nueva columna con el enlace completo de Spotify
base_url = "https://open.spotify.com/intl-es/track/"
df['spotify_link'] = base_url + df['Track ID']

# Diccionario con URLs de imágenes para el top 10, asignadas manualmente
image_urls_top_10 = {
    1: "https://raw.githubusercontent.com/Taaftt/2024/main/images/Utopia.jfif",
    2: "https://raw.githubusercontent.com/Taaftt/2024/main/images/Vultures.png",
    3: "https://raw.githubusercontent.com/Taaftt/2024/main/images/One%20dance.jpg",
    4: "https://raw.githubusercontent.com/Taaftt/2024/main/images/Redrum.jfif",
    5: "https://raw.githubusercontent.com/Taaftt/2024/main/images/Utopia.jfif",
    6: "https://raw.githubusercontent.com/Taaftt/2024/main/images/Utopia.jfif",
    7: "https://raw.githubusercontent.com/Taaftt/2024/main/images/withouth%20me.jfif",
    8: "https://raw.githubusercontent.com/Taaftt/2024/main/images/Hyv.jfif",
    9: "https://raw.githubusercontent.com/Taaftt/2024/main/images/the%20dogs.jfif",
    10: "https://raw.githubusercontent.com/Taaftt/2024/main/images/gunna.jpg"
}
    

# Título general de la aplicación
st.title("Hip Hop Songs")

# Selección del top
st.subheader("Selecciona el top de canciones a mostrar")
top_n = st.slider("Elige el número de canciones (Top N)", min_value=10, max_value=100, step=10)

# Ordena las canciones por la columna de popularidad
df_sorted = df.sort_values(by="Popularity", ascending=False)

# Filtra el DataFrame para obtener solo el top seleccionado
df_top_n = df_sorted.head(top_n)

# Mostrar las canciones con un diseño específico para el top 10
st.subheader(f"Top {top_n} canciones de Hip Hop")

if top_n == 10:
    for i in range(len(df_top_n)):
        song = df_top_n['Track Name'].iloc[i]
        link = df_top_n['spotify_link'].iloc[i]
        artist = df_top_n['Artist'].iloc[i]
        
        # Obtener la imagen correspondiente al top, si existe
        image_url = image_urls_top_10.get(i + 1)  # i + 1 representa la posición en el top

        # Mostrar imagen y detalles de la canción si hay una imagen asociada
        if image_url:
            st.image(image_url, width=150)  # Ajusta el tamaño de la imagen
        st.markdown(f"{i+1}**{song}** - {artist} [Escuchar en Spotify]({link})", unsafe_allow_html=True)
else:
    # Diseño simple sin imágenes para otros tops
    for i in range(len(df_top_n)):
        song = df_top_n['Track Name'].iloc[i]
        link = df_top_n['spotify_link'].iloc[i]
        artist = df_top_n['Artist'].iloc[i]
        
        # Mostrar cada canción con el nombre del artista y un enlace clickeable
        st.markdown(f"**{song}** - {artist} [Escuchar en Spotify]({link})", unsafe_allow_html=True)
