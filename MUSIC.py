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
            </div>
            <div style="text-align: center; margin-top: 10px;">
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
