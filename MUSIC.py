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
    
# Imagen principal
st.image("https://raw.githubusercontent.com/Taaftt/2024/main/images/Utopia.jfif", use_column_width=True)

# Título grande con diseño
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 60px; font-weight: bold; margin-bottom: 5px;'>
            Spotify CLASSICS
        </h1>
        <h2 style='font-size: 35px; color: gray; margin-top: 0;'>
            100 Greatest Hip-Hop Songs of the Streaming Era
        </h2>
    </div>
    """, 
    unsafe_allow_html=True
)

# Texto descriptivo
st.write("MAY 20, 2024")
st.write("Instant Vintage")
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
        st.markdown(f"{i+1}.- **{song}** - {artist} [Escuchar en Spotify]({link})", unsafe_allow_html=True)
else:
    # Diseño simple sin imágenes para otros tops
    for i in range(len(df_top_n)):
        song = df_top_n['Track Name'].iloc[i]
        link = df_top_n['spotify_link'].iloc[i]
        artist = df_top_n['Artist'].iloc[i]
        
        # Mostrar cada canción con el nombre del artista y un enlace clickeable
        st.markdown(f"{i+1}.- **{song}** - {artist} [Escuchar en Spotify]({link})", unsafe_allow_html=True)
