import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Netflix Dashboard",
    page_icon="🎬",
    layout="wide"
)

# ==========================================
# TITLE
# ==========================================

st.title("🎬 Netflix Interactive Dashboard")

st.markdown("Analyze Netflix Movies and TV Shows using interactive visualizations.")

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.header("Upload Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Upload Netflix CSV File",
    type=["csv"]
)

# ==========================================
# LOAD DATASET
# ==========================================

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # ==========================================
    # DATA PREVIEW
    # ==========================================

    st.subheader("📄 Dataset Preview")

    st.dataframe(df.head())

    # ==========================================
    # DATASET METRICS
    # ==========================================

    st.subheader("📊 Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    # ==========================================
    # MOVIES VS TV SHOWS
    # ==========================================

    st.subheader("🎥 Movies vs TV Shows")

    fig1, ax1 = plt.subplots()

    sns.countplot(
        x='type',
        data=df,
        ax=ax1
    )

    st.pyplot(fig1)

    # ==========================================
    # RELEASE YEAR TREND
    # ==========================================

    st.subheader("📈 Content Release Trend")

    fig2, ax2 = plt.subplots(figsize=(10,5))

    df['release_year'].value_counts().sort_index().plot(ax=ax2)

    plt.xlabel("Release Year")
    plt.ylabel("Number of Releases")

    st.pyplot(fig2)

    # ==========================================
    # TOP 10 COUNTRIES
    # ==========================================

    st.subheader("🌍 Top 10 Countries")

    fig3, ax3 = plt.subplots(figsize=(10,5))

    df['country'].value_counts().head(10).plot(
        kind='bar',
        ax=ax3
    )

    st.pyplot(fig3)

    # ==========================================
    # RATING DISTRIBUTION
    # ==========================================

    st.subheader("⭐ Rating Distribution")

    fig4, ax4 = plt.subplots(figsize=(10,5))

    sns.countplot(
        y='rating',
        data=df,
        order=df['rating'].value_counts().index,
        ax=ax4
    )

    st.pyplot(fig4)

    # ==========================================
    # GENRE ANALYSIS
    # ==========================================

    st.subheader("🎭 Top Genres")

    genres = df['listed_in'].str.split(',', expand=True).stack()

    fig5, ax5 = plt.subplots(figsize=(10,5))

    genres.value_counts().head(10).plot(
        kind='bar',
        ax=ax5
    )

    st.pyplot(fig5)

    # ==========================================
    # FINAL INSIGHTS
    # ==========================================

    st.subheader("🔍 Key Insights")

    st.write("""
    - Netflix contains more Movies than TV Shows.
    - Content increased rapidly after 2015.
    - The United States contributes the highest amount of content.
    - TV-MA is one of the most common ratings.
    - Drama and International Movies are among the top genres.
    """)

    # ==========================================
    # SUCCESS MESSAGE
    # ==========================================

    st.success("Dashboard Loaded Successfully!")

else:

    st.info("👈 Upload a Netflix CSV file from the sidebar to begin.")