# 🍷 Wine Data Dashboard

> **FROM GRAPES TO GLASS: A WINE DATA EXPLORATION**

An interactive analytics dashboard built with Python and Dash that explores wine data collected from various wine brands across different countries. The project combines Exploratory Data Analysis (EDA) with Natural Language Processing (NLP) to uncover insights about wine characteristics, pricing, food pairings, and consumer reviews.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [NLP Model](#nlp-model)
- [Dashboard Tabs](#dashboard-tabs)

---

## Overview

This case study focuses on analysing data collected from various wine brands across different countries (Australia, Chile, France, Italy, New Zealand, Portugal, Spain, and USA). The dashboard provides interactive visualizations with dynamic filters for country, wine style, and price range, enabling users to explore wine trends and patterns at a glance.

---

## Features

- 🌍 **Multi-country wine data** covering 8 countries and 4,600+ wines
- 🔍 **Dynamic filters** — filter by Country, Wine Style, and Price Range ($0–$3,250)
- 📊 **Interactive charts** — histograms, 3D scatter plots, bar charts, pie charts, and box plots
- 🍽️ **Food pairing analysis** — discover the most popular food pairings per country
- 🤖 **NLP Review Classification** — zero-shot classification of wine reviews using a HuggingFace transformer model
- 📱 **Responsive UI** built with Dash Bootstrap Components

---

## Project Structure

```
Wine_Data_Dashbord/
├── dashboard.py                        # Main Dash application (entry point)
├── requirements.txt                    # Python dependencies
├── assets/                             # Dashboard logo images
│   ├── logo1.png
│   └── logo New.png
├── Wine_Stats/                         # Raw country-specific wine CSV files
│   ├── Australia.csv
│   ├── Chile.csv
│   ├── France.csv
│   ├── Italy.csv
│   ├── New_Zealand.csv
│   ├── Portugal.csv
│   ├── Spain.csv
│   └── USA.csv
├── notebooks/                          # Data preparation notebooks & processed data
│   ├── Data Preparation.ipynb          # Data cleaning and processing pipeline
│   └── data/processed/
│       └── process_wine_data.csv       # Cleaned dataset used by the dashboard
└── HuggingFaceModel/                   # NLP model for review classification
    ├── HuggingFace Model.ipynb         # Zero-shot classification notebook
    └── wine_data_reviews_with_labels.csv  # Reviews with NLP-generated labels
```

---

## Tech Stack

| Category | Libraries |
|---|---|
| **Web Framework** | Dash, Dash Bootstrap Components |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly Express, Plotly Graph Objects, Matplotlib |
| **NLP / ML** | HuggingFace Transformers, PyTorch, Tokenizers |
| **Notebooks** | Jupyter, IPython, IPyKernel |
| **Utilities** | Requests, Pillow, PyYAML |

---

## Installation

### Prerequisites

- Python 3.8+
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/YasithaNV2001/Wine_Data_Dashbord.git
cd Wine_Data_Dashbord

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Usage

```bash
# Run the dashboard
python dashboard.py
```

Then open your browser and navigate to **http://127.0.0.1:8050/**

---

## Data

The primary dataset (`notebooks/data/processed/process_wine_data.csv`) contains **4,624 rows** and the following key features per wine:

| Field | Description |
|---|---|
| Name | Wine name |
| Rating | Rating out of 5 |
| NumberOfRatings | Total number of user ratings |
| Price | Price in USD |
| Region | Wine region |
| Winery | Producer/winery name |
| Wine Style | Style category (e.g., Red, White, Rosé, Sparkling) |
| Alcohol | Alcohol content (%) |
| Bold / Tannin / Sweet / Acidic | Flavour profile scores |
| Food | Recommended food pairings |
| Country | Country of origin |

Raw per-country CSV files are stored in the `Wine_Stats/` directory.

---

## NLP Model

Wine reviews are classified using a **zero-shot classification** pipeline from HuggingFace:

- **Model:** `cross-encoder/nli-distilroberta-base`
- **Task:** Classify what each review "talks about" (e.g., food combinations, taste, aroma)
- **Output:** `HuggingFaceModel/wine_data_reviews_with_labels.csv` — reviews annotated with predicted labels
- **Notebook:** `HuggingFaceModel/HuggingFace Model.ipynb`

---

## Dashboard Tabs

| Tab | Description |
|---|---|
| **Price Analysis** | Price distribution histogram by country and 3D scatter plot of ratings |
| **Food & Alcohol Analysis** | Popular food pairings per country and alcohol content box plots |
| **Wine Styles** | Pie chart showing distribution of wine style categories |
| **NLP Analysis** | Bar chart of review category distribution from NLP classification |

