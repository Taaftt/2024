import streamlit as st
import pandas as pd

# Cargar el archivo CSV "top_hiphop_artists_tracks.csv" en un DataFrame de pandas
df = pd.read_csv("top_hiphop_artists_tracks.csv")

# Añadir enlace de Spotify usando el ID de la canción
base_url = "https://open.spotify.com/intl-es/track/"
df['spotify_link'] = base_url + df['Track ID']

# Diccionario de URLs de imágenes para el top 10 de canciones y top 3 artistas
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

top_3_artist_images = {
    'Drake': "https://raw.githubusercontent.com/Taaftt/2024/main/images/DRAKE.jfif",
    'Travis Scott': "https://raw.githubusercontent.com/Taaftt/2024/main/images/TRAVIS.jpg",
    'Eminem': "https://raw.githubusercontent.com/Taaftt/2024/main/images/MNM.jpg"
}

# Título principal
st.title("SPOTIFY HIP-HOP")
st.subheader("100 Canciones más escuchadas del hip-hop")
st.image("https://raw.githubusercontent.com/Taaftt/2024/main/images/CLASSICS-Hip-Hop-FTR-Header-1-1440x1440.jpg")

# Mostrar un selector para elegir el número de canciones a mostrar
top_n = st.slider("Selecciona el número de canciones a mostrar (Top N)", min_value=10, max_value=100, step=10)

# Ordenar las canciones por popularidad y filtrar el top N
df_sorted = df.sort_values(by="Popularity", ascending=False)
df_top_n = df_sorted.head(top_n)

# Mostrar las canciones en una tabla
st.subheader(f"Top {top_n} canciones de Hip Hop")
for i, row in df_top_n.iterrows():
    # Mostrar imagen si es del top 10
    if i < 10:
        st.image(image_urls_top_10.get(i + 1), width=100)

    # Mostrar información básica de la canción
    st.write(f"**{i + 1}. {row['Track Name']}** - {row['Artist']}")
    st.write(f"[Escuchar en Spotify]({row['spotify_link']})")

# Mostrar un botón para ver los artistas más populares
if st.button("Artistas con más apariciones"):
    st.subheader("Top 3 Artistas con más apariciones en el Top 100")

    # Calcular los artistas con más apariciones en el top 100
    top_100_df = df_sorted.head(100)
    artist_counts = top_100_df['Artist'].value_counts().head(3)

    # Mostrar los artistas con imágenes y conteo de canciones
    for artist, count in artist_counts.items():
        st.image(top_3_artist_images.get(artist, ""), width=100)
        st.write(f"**{artist}**: {count} canciones")
    
    # Descripción breve de los artistas
    st.subheader("Descripción de los Top 3 Artistas")
    st.write("""
    - **Drake**: Rapero canadiense famoso por mezclar rap y R&B, con éxitos como "Hotline Bling".
    - **Travis Scott**: Conocido por su estilo único y sus álbumes como *Astroworld*.
    - **Eminem**: Reconocido mundialmente, con temas como "Lose Yourself" y "Stan".
    """)

