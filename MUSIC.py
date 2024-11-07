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

# Título grande con diseño
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 60px; font-weight: bold; margin-bottom: 5px;'>
            SPOTIFY HIP-HOP
        </h1>
        <h2 style='font-size: 35px; color: gray; margin-top: 0;'>
            100 Canciones más escuchadas del hip-hop
        </h2>
    </div>
    """, 
    unsafe_allow_html=True)

# Imagen principal
st.image("https://raw.githubusercontent.com/Taaftt/2024/main/images/CLASSICS-Hip-Hop-FTR-Header-1-1440x1440.jpg", use_column_width=True)

# Configuración de columnas para dividir el espacio en contenido principal y botón derecho
col1, col2 = st.columns([3, 1])

with col1:
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
            artist = df_top_n['Artist'].iloc[i]
            link = df_top_n['spotify_link'].iloc[i]
            
            # Obtener la imagen correspondiente al top, si existe
            image_url = image_urls_top_10.get(i + 1)  # i + 1 representa la posición en el top

            # Diseño de tarjeta
            st.markdown(f"""
                <div style="border: 2px solid #1DB954; padding: 20px; margin: 10px 0; border-radius: 10px; text-align: center; background-color: #f7f7f7;">
                    <img src="{image_url}" style="width: 150px; height: 150px; border-radius: 50%; margin-bottom: 15px;">
                    <h3 style="margin: 0; font-size: 24px;">{i+1}. {song}</h3>
                    <p style="color: #333; font-size: 18px; margin: 5px 0;">{artist}</p>
                    <a href="{link}" style="color: #1DB954; font-weight: bold; font-size: 16px; text-decoration: none;">Escuchar en Spotify</a>
                </div>
            """, unsafe_allow_html=True)
    else:
        # Diseño simple sin imágenes para otros tops
        for i in range(len(df_top_n)):
            song = df_top_n['Track Name'].iloc[i]
            link = df_top_n['spotify_link'].iloc[i]
            artist = df_top_n['Artist'].iloc[i]
            
            # Mostrar cada canción con el nombre del artista y un enlace clickeable
            st.markdown(f"{i+1}.- **{song}** - {artist} [Escuchar en Spotify]({link})", unsafe_allow_html=True)

# Columna derecha con botón para mostrar artistas
with col2:
    st.write(" ")
    st.write(" ")
    # Botón para ver los artistas con más apariciones
    if st.button("Artistas con más apariciones"):
        st.subheader("Artistas con más apariciones en el Top 100")

        # Filtramos el DataFrame al Top 100 y contamos las apariciones de cada artista
        top_100_df = df_sorted.head(100)
        artist_counts = top_100_df['Artist'].value_counts().head(10)

        # Mostramos los artistas con más apariciones en el Top 100
        for artist, count in artist_counts.items():
            st.markdown(f"**{artist}**: {count} canciones")
