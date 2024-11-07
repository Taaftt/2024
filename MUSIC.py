import streamlit as st
import pandas as pd

# Carga el archivo CSV "top_hiphop_artists_tracks.csv" en un DataFrame de pandas.
df = pd.read_csv("top_hiphop_artists_tracks.csv")

#enlace
base_url = "https://open.spotify.com/intl-es/track/"
df['spotify_link'] = base_url + df['Track ID']

#imagenes
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

# Mostrar o no
if 'show_artists' not in st.session_state:
    st.session_state['show_artists'] = False

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

#img
st.image("https://raw.githubusercontent.com/Taaftt/2024/main/images/CLASSICS-Hip-Hop-FTR-Header-1-1440x1440.jpg", use_column_width=True)

#boton
if st.session_state['show_artists']:
    # Mostrar la sección de "Artistas con más apariciones"
    st.subheader("Top 3 Artistas con más apariciones en el Top 100")

    # Aparicicones
    df_sorted = df.sort_values(by="Popularity", ascending=False)
    top_100_df = df_sorted.head(100)
    artist_counts = top_100_df['Artist'].value_counts().head(3)

    # Mostrar los artistas con img
    for artist, count in artist_counts.items():
        image_url = top_3_artist_images.get(artist, "")
        st.image(image_url, width=150, caption=f"{artist}: {count} canciones")

    #desc
    st.subheader("Descripción de las Carreras de los Top 3 Artistas")
    st.markdown("""
        - **Drake**: Rapero canadiense conocido por su habilidad para mezclar rap y R&B. Con éxitos como "Hotline Bling" y "God's Plan", ha logrado romper récords y consolidarse como uno de los artistas más importantes en el género.
        - **Travis Scott**: Reconocido por su estilo único y sus producciones innovadoras, Travis Scott ha lanzado álbumes exitosos como *Astroworld*, y es conocido por su energía en el escenario y colaboraciones con otros grandes artistas.
        - **Eminem**: Conocido como "Slim Shady", Eminem es uno de los raperos más influyentes de todos los tiempos. Su habilidad lírica y sus temas profundos en canciones como "Lose Yourself" y "Stan" le han ganado numerosos premios y una gran base de fans mundialmente.
    """)

   

else:
    # Selección del top de canciones a mostrar
    st.subheader("Selecciona el top de canciones a mostrar")
    top_n = st.slider("Elige el número de canciones (Top N)", min_value=10, max_value=100, step=10)

    # Ordena las canciones por la columna de popularidad y filtra para obtener el top seleccionado
    df_sorted = df.sort_values(by="Popularity", ascending=False)
    df_top_n = df_sorted.head(top_n)

    # Mostrar el top de canciones
    st.subheader(f"Top {top_n} canciones de Hip Hop")

    if top_n == 10:
        for i in range(len(df_top_n)):
            song = df_top_n['Track Name'].iloc[i]
            artist = df_top_n['Artist'].iloc[i]
            link = df_top_n['spotify_link'].iloc[i]

            # Obtener la imagen correspondiente al top, si existe
            image_url = image_urls_top_10.get(i + 1)

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

 
    
    if st.button("Artistas con más apariciones"):
        st.session_state['show_artists'] = True

