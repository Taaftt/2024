import streamlit as st
import pandas as pd

# Cargar el archivo CSV en un DataFrame de pandas
df = pd.read_csv("top_hiphop_artists_tracks.csv")

# Crear enlaces de Spotify
base_url = "https://open.spotify.com/intl-es/track/"
df['spotify_link'] = base_url + df['Track ID']

# URLs de imágenes para el top 10
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

# Diccionario de imágenes para el top 3 de artistas
top_3_artist_images = {
    'Drake': "https://raw.githubusercontent.com/Taaftt/2024/main/images/DRAKE.jfif",
    'Travis Scott': "https://raw.githubusercontent.com/Taaftt/2024/main/images/TRAVIS.jpg",
    'Eminem': "https://raw.githubusercontent.com/Taaftt/2024/main/images/MNM.jpg"
}

# Mostrar encabezado y descripción
st.title("SPOTIFY HIP-HOP")
st.subheader("100 Canciones más escuchadas del hip-hop")
st.image("https://raw.githubusercontent.com/Taaftt/2024/main/images/CLASSICS-Hip-Hop-FTR-Header-1-1440x1440.jpg", use_column_width=True)

# Estado para alternar la vista
if 'show_artists' not in st.session_state:
    st.session_state['show_artists'] = False

if st.session_state['show_artists']:
    st.subheader("Top 3 Artistas con más apariciones en el Top 100")
    df_sorted = df.sort_values(by="Popularity", ascending=False)
    top_100_df = df_sorted.head(100)
    artist_counts = top_100_df['Artist'].value_counts().head(3)

    for artist, count in artist_counts.items():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(top_3_artist_images.get(artist, ""), width=100)
        with col2:
            st.write(f"**{artist}**: {count} canciones")

    st.subheader("Descripción de las Carreras de los Top 3 Artistas")
    st.write("""
    - **Drake**: Rapero canadiense conocido por mezclar rap y R&B. Con éxitos como "Hotline Bling".
    - **Travis Scott**: Conocido por su estilo y sus producciones innovadoras, como *Astroworld*.
    - **Eminem**: Uno de los raperos más influyentes, con temas como "Lose Yourself" y "Stan".
    """)
else:
    # Selector para el top de canciones
    st.subheader("Selecciona el top de canciones a mostrar")
    top_n = st.slider("Elige el número de canciones (Top N)", min_value=10, max_value=100, step=10)
    
    # Ordenar las canciones por popularidad y filtrar el top N
    df_sorted = df.sort_values(by="Popularity", ascending=False)
    df_top_n = df_sorted.head(top_n)

    st.subheader(f"Top {top_n} canciones de Hip Hop")

    # Mostrar top 10 con imágenes y enlaces
    for i in range(len(df_top_n)):
        song = df_top_n['Track Name'].iloc[i]
        artist = df_top_n['Artist'].iloc[i]
        link = df_top_n['spotify_link'].iloc[i]
        image_url = image_urls_top_10.get(i + 1, "")

        col1, col2 = st.columns([1, 3])
        with col1:
            if image_url:
                st.image(image_url, width=80)
        with col2:
            st.write(f"**{i+1}. {song}** - {artist}")
            st.write(f"[Escuchar en Spotify]({link})")  # Este enlace se mostrará debajo de los detalles del cuadro

    # Botón para alternar la vista a los artistas
    if st.button("Artistas con más apariciones"):
        st.session_state['show_artists'] = True

