import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
likes_df = pd.read_csv("top_20_by_likes.csv")
engage_df = pd.read_csv("top_10_by_engagement.csv")

st.set_page_config(page_title="Instagram Influencers Dashboard", layout="wide")

st.title("📱 Influencer Dashboard – Instagram")
st.markdown("Visualize os influenciadores com maior impacto para engajamento de marcas.")

# Seção: Top Influencers por Total de Likes
st.subheader("🔥 Top 20 Influencers por Total de Likes")

fig_likes = px.bar(
    likes_df.sort_values(by="total_likes_num", ascending=True),
    x="total_likes_num",
    y="channel_info",
    orientation="h",
    color="country",
    labels={"total_likes_num": "Total de Likes", "channel_info": "Influenciador"},
    title="Total de Likes por Influenciador" 
)
st.plotly_chart(fig_likes, use_container_width=True)

# Seção: Top Influencers por Engajamento
st.subheader("📈 Top 10 Influencers com Maior Engajamento por Like")

fig_engage = px.bar(
    engage_df.sort_values(by="engagement_rate_like", ascending=True),
    x="engagement_rate_like",
    y="channel_info",
    orientation="h",
    color="country",
    labels={"engagement_rate_like": "Engajamento (likes/seguidores)", "channel_info": "Influenciador"},
    title="Engajamento por Influenciador"
)
st.plotly_chart(fig_engage, use_container_width=True)

# Tabela com Filtros
st.subheader("🔍 Tabela Interativa")
with st.expander("Visualizar dados completos"):
    st.dataframe(engage_df)

# Seção: Justificativa Estratégica
st.subheader("🎯 Por que usar esses influenciadores?")
st.markdown("""
Usar influenciadores com **alta taxa de engajamento** e **ótimo score de influência** é uma forma eficaz de:
- Alcançar milhões de seguidores que **confiam** nessas personalidades
- Garantir **interações reais** e não apenas alcance superficial
- Construir **autoridade de marca** em diferentes países
- Potencializar campanhas de marketing com **ROI mensurável**
""")
