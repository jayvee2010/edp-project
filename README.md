# 🎵 Spotify Music Streaming Trends — EDA Project 2024

> An in-depth Exploratory Data Analysis of global music streaming behaviour across Spotify, YouTube, TikTok, and more — built for *EDA Using Python*, Batch 2025–29.

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1DB954?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Made with Pandas](https://img.shields.io/badge/Pandas-150460?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![View Website](https://img.shields.io/badge/Live-Website-1DB954?style=flat-square)](https://dancing-bienenstitch-c1068b.netlify.app)
[![View Dataset](https://img.shields.io/badge/Kaggle-Dataset-20BEFF?style=flat-square)](https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024)

---

## 📖 About the Project

This project explores the **Most Streamed Spotify Songs of 2024** — a real-world dataset spanning **4,600 tracks**, **1,999 artists**, and **29 features** across 8 streaming platforms. The goal was to uncover hidden patterns in how music travels across the internet: which platforms drive streams, when artists should release, what languages dominate, which collaborations outperform, and how fan loyalty actually works.

The analysis pipeline covers the full EDA lifecycle — data cleaning, preprocessing, feature engineering, statistical analysis, and publication-ready visualisations — all rendered into an interactive presentation website.

**Try the live presentation →** [dancing-bienenstitch-c1068b.netlify.app](https://dancing-bienenstitch-c1068b.netlify.app)

---

## 👥 The Team

| Member | Role | Responsibilities |
|---|---|---|
| **Jayvee Shah** | Frontend Lead | Built the interactive presentation website (HTML/CSS/JS) |
| **Krish Joshi** | Visualisation Lead | Designed and generated all 9 graphs and the animated bar race |
| **Jui Dixit** | Data Cleaning | Parsing, null handling, encoding fixes, and column normalisation |
| **Drishti Heda** | Data Cleaning | Data validation, deduplication, and cross-dataset reconciliation |

> All four members contributed to the analysis process and report writing.

---

## 🛠 Tech Stack

| Category | Tools |
|---|---|
| **Language** | Python 3.12 |
| **Core Libraries** | `pandas`, `numpy` |
| **Visualisation** | `matplotlib`, `seaborn` |
| **Language Detection** | `langdetect` |
| **Normalization** | `scikit-learn` (MinMaxScaler) |
| **Notebook** | Google Colab / Jupyter |
| **Presentation Website** | HTML5 · CSS3 · Vanilla JS |
| **Deployment** | Netlify |

---

## 📊 Dataset

| Property | Value |
|---|---|
| **Primary Source** | [Most Streamed Spotify Songs 2024](https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024) by nelgiriyewithana |
| **Tracks Analysed** | 4,600 |
| **Unique Artists** | 1,999 |
| **Features** | 29 columns |
| **Platforms Covered** | Spotify, YouTube, TikTok, Apple Music, Pandora, Soundcloud, Deezer, Amazon Music |
| **Total Streams** | ~2.0 Trillion |
| **Top Song** | Blinding Lights — The Weeknd (4.28B streams) |

---

## 📁 Project Structure

```
edp-project/
├── edp_project.ipynb          # Full analysis notebook (Colab-compatible)
├── spotify_final_clean_version_v2.csv  # Secondary / cleaned dataset
├── .kaggle/
│   └── Most Streamed Spotify Songs 2024.csv  # Original Kaggle dataset
└── edp website/               # Presentation website
    ├── index.html             # Hero + Stats + Key Findings
    ├── analysis.html          # Methodology + Phase breakdown
    ├── graphs.html            # All 9 visualisations with lightbox
    └── about.html             # Team + Tech stack + Rubric
```

---

## 📈 Analysis & Graphs (9 Visualisations)

All charts were built with **Matplotlib + Seaborn** inside Google Colab and embedded into the website.

| # | Graph | Type | Key Insight |
|---|---|---|---|
| 1 | **Top 10 Most Streamed Songs** | Animated horizontal bar race | Blinding Lights leads at 4.28B streams |
| 2 | **Platform Battle** | Bar + Pie | Spotify holds ~40% of all streaming volume |
| 3 | **Genre / Era Evolution Timeline** | Multi-line (2018–2024) | TikTok-era songs show multi-platform dominance |
| 4 | **Biggest Collaborations of 2024** | Horizontal bar | 671 collab tracks (14.6%) analysed; featured artists boost streams significantly |
| 5 | **Top 15 Most Streamed Albums** | Horizontal bar | Un Verano Sin Ti and The Tortured Poets Department lead |
| 6 | **Language Distribution** | Pie + Bar side-by-side | English dominates at 40%; Spanish is a distant second |
| 7 | **Artist Loyalty Index** | Horizontal bar + colourmap | Composite score = playlist adds ÷ streams (Spotify) + likes ÷ views (YouTube & TikTok) |
| 8 | **Release Timing Analysis** | Bar + line overlay | Friday is the best day to release; May–August releases outperform |
| 9 | **Shazam Discovery Rate** | Bubble scatter (quadrant) | Four discovery quadrants: Viral Hit, Organic Discovery, Playlist Driven, Under the Radar |

---

## 🔍 Key Findings

1. **Platform dominance** — Spotify accounts for the largest share of total streaming volume, but YouTube and TikTok together capture nearly as much attention.

2. **Friday release effect** — Songs released on Fridays consistently average higher Spotify streams than any other day of the week, confirming industry patterns.

3. **Collaboration premium** — Tracks with a featured artist (14.6% of dataset) show meaningfully higher average streams than solo releases.

4. **TikTok as a discovery engine** — High TikTok Views + lower Spotify Streams is a clear "organic discovery" signal — songs that spread on TikTok before hitting playlists.

5. **English-language heavy** — 40% of charting songs are English; Indonesian, Spanish, and Portuguese complete the top non-English languages.

6. **Fanbase loyalty varies wildly** — The Artist Loyalty Index (playlist-adds ÷ streams ratio) shows some artists maintain devoted fanbases despite lower raw streams.

---

## 🌐 Live Presentation Website

**→ [dancing-bienenstitch-c1068b.netlify.app](https://dancing-bienenstitch-c1068b.netlify.app)**

The website has four pages:

- **`/`** — Hero section with project stats (4,600 songs, 2T total streams, 4.28B top song) and six key findings cards
- **`/analysis`** — Full methodology walkthrough with code snippets, a 5-phase project timeline, and a findings table
- **`/graphs`** — Filterable grid of all 9 visualisations with a lightbox viewer
- **`/about`** — Team section with avatar cards, full tech stack, project rubric breakdown (18 marks), and dataset credits

---

## 🚀 Running the Notebook

Open `edp_project.ipynb` in Google Colab or Jupyter and run cells sequentially.

```bash
# Install dependencies (if running locally)
pip install pandas numpy matplotlib seaborn langdetect scikit-learn

# Open in Colab — just upload the .ipynb file and run all cells
```

---

## 📝 License

This project was created for academic purposes as part of the *EDA Using Python* course, Batch 2025–29. Dataset used under [Kaggle's terms](https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024).

---

Built with 🎵 by **Drishti Heda · Jayvee Shah · Jui Dixit · Krish Joshi**
