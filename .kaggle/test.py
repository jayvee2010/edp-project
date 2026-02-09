
import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="Music Data Demo", layout="wide")

st.title("🚀 Music Streaming Trends: Team Demo")

# --- DATA LOADING ---
@st.cache_data  # This makes the app run much faster
def load_data():
    try:
        data = pd.read_csv('Most Streamed Spotify Songs 2024.csv', encoding='latin1')
        # Cleaning numbers: Remove commas and convert to math-friendly format
        for col in ['Spotify Streams', 'TikTok Views']:
            if col in data.columns:
                data[col] = pd.to_numeric(data[col].astype(str).str.replace(',', ''), errors='coerce')
        return data
    except FileNotFoundError:
        st.error("❌ ERROR: CSV file not found! Make sure it's in the same folder as this script.")
        return None

df = load_data()

if df is not None:
    # --- SIDEBAR FILTERS ---
    st.sidebar.header("Filter the Data")
    # Let the team pick how many songs to see
    top_n = st.sidebar.slider("Show Top Songs", 5, 20, 10)
    
    # Filter for specific artists
    artists = st.sidebar.multiselect("Select Specific Artists", options=df['Artist'].unique(), default=[])

    # Logic: If they pick artists, show those. Otherwise, show the top N.
    if artists:
        display_df = df[df['Artist'].isin(artists)]
    else:
        display_df = df.head(top_n)

    # --- VISUALIZATION ---
    st.subheader(f"📊 Insights for {len(display_df)} Tracks")
    
    # Creating a Bar Chart for Spotify Streams
    fig = px.bar(display_df, x='Track', y='Spotify Streams', color='Artist', 
                 title="Spotify Success", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

    # Adding the "Secret Weapon" - TikTok vs Spotify Scatter Plot
    st.subheader("📱 TikTok Virality vs. Spotify Streams")
    fig2 = px.scatter(display_df, x='TikTok Views', y='Spotify Streams', 
                      size='Spotify Streams', color='Artist', hover_name='Track',
                      log_x=True, template="plotly_dark")
    st.plotly_chart(fig2, use_container_width=True)

    # --- RAW DATA ---
    with st.expander("See the full table"):
        st.dataframe(display_df)