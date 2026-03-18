# 🍷 Wine Data Dashboard — Interview Preparation Guide

This document explains the project in a way suitable for technical and non-technical interviews, followed by a comprehensive Question & Answer section covering every major aspect of the project.

---

## Part 1: How to Explain This Project in an Interview

### 🎯 Elevator Pitch (30 seconds)

> "I built an interactive Wine Analytics Dashboard using Python and Dash. It pulls data from 8 different countries covering 4,600+ wines, gives users dynamic filters to explore wine prices, styles, ratings, and food pairings through interactive Plotly charts. On top of that, I integrated a HuggingFace NLP model using zero-shot classification to automatically label wine review text into categories — all served through a single-page web application."

---

### 📖 Full Project Walk-Through (2–3 minutes)

#### 1. Problem Statement

Wine data exists across many countries and producers, but it is scattered and hard to explore interactively. The goal was to consolidate data from 8 countries, clean it, and build a dashboard that lets any user instantly filter and visualise wine characteristics — prices, alcohol content, food pairings, styles, and consumer reviews — without writing a single line of code.

#### 2. Data Pipeline

- **Raw data** was collected as separate CSV files for each country (Australia, Chile, France, Italy, New Zealand, Portugal, Spain, USA) stored in the `Wine_Stats/` directory.
- A **Jupyter notebook** (`notebooks/Data Preparation.ipynb`) was used to clean, normalise, and merge all country files into a single processed dataset (`notebooks/data/processed/process_wine_data.csv`) with 4,624 rows.
- Key cleaning steps included handling missing values, standardising column names, converting price and alcohol fields to numeric types, and parsing multi-valued food pairing strings into lists.
- The processed CSV is hosted on GitHub and loaded at runtime via a public URL, so the dashboard works without a local database.

#### 3. NLP Review Classification

- A separate dataset of wine reviews was classified using a **zero-shot classification pipeline** from HuggingFace Transformers.
- Model used: `cross-encoder/nli-distilroberta-base` — a lightweight NLI (Natural Language Inference) model that can classify text into arbitrary categories without task-specific training.
- Each review was classified into one of several categories (e.g., *"talks about food combinations"*, *"talks about taste"*) and stored in a new column called `talks_about`.
- The output CSV (`HuggingFaceModel/wine_data_reviews_with_labels.csv`) is then loaded by the dashboard to show the **NLP Analysis** tab.

#### 4. Dashboard Architecture

The dashboard is built with **Dash by Plotly**, a Python framework that wraps React under the hood:

- **Layout**: Built using HTML/Dash components and `dash-bootstrap-components` for a responsive grid layout.
- **Tabs**: Four analysis tabs — *Price Analysis*, *Food & Alcohol Analysis*, *Wine Styles*, *NLP Analysis*.
- **Filters**: Three global filters (Country, Wine Style, Price Range slider) that update all charts simultaneously via Dash Callbacks.
- **Callbacks**: Two reactive callbacks — one toggles the filter panel visibility, the other re-renders five charts whenever any filter changes.

#### 5. Charts and Visualisations

| Chart | Type | Insight Provided |
|---|---|---|
| Price Distribution | Histogram (colour by country) | How wine prices are distributed per country |
| Ratings vs Price | 3D Scatter Plot | Relationship between price, rating, and number of ratings |
| Popular Food Pairings | Bar Chart | Which foods are most recommended with wine |
| Alcohol Content | Box Plot (by country) | Spread and median alcohol % across countries |
| Wine Style Distribution | Pie Chart | Proportion of Red, White, Rosé, Sparkling, etc. |
| NLP Review Categories | Bar Chart | What topics consumers most write about in reviews |

#### 6. Tech Stack Summary

- **Frontend**: Dash, Dash Bootstrap Components, Plotly
- **Backend/Data**: Python, Pandas, NumPy
- **NLP**: HuggingFace Transformers, PyTorch
- **Environment**: Jupyter Notebooks, pip

---

## Part 2: Interview Q&A

### 🔹 Section A: General / Overview Questions

**Q1. Can you give a brief overview of this project?**

> This is a Wine Analytics Dashboard that combines data analysis and NLP. I collected wine data from 8 countries, cleaned and merged it into a single dataset, then built an interactive Dash web app with dynamic filters and Plotly charts. I also applied a zero-shot NLP classifier from HuggingFace to categorise wine review text, which is visualised in a dedicated tab.

---

**Q2. What was the motivation or business problem behind this project?**

> Wine data is rich but often locked in static tables or spreadsheets split by country or region. The motivation was to make that data explorable in real time — allowing someone like a sommelier, wine buyer, or data analyst to instantly filter by country, price range, or wine style and see meaningful visual patterns without technical knowledge.

---

**Q3. What does the end-to-end workflow of this project look like?**

> 1. Raw CSVs per country → Data cleaning in Jupyter Notebook → Processed CSV
> 2. Wine reviews → HuggingFace zero-shot classification → Labelled review CSV
> 3. Both CSVs hosted on GitHub → Loaded by Dash app at runtime
> 4. User opens dashboard → Applies filters → Callbacks fire → Charts update dynamically

---

### 🔹 Section B: Data and Preprocessing

**Q4. What data did you use and where did it come from?**

> The dataset contains wine information across 8 countries: Australia, Chile, France, Italy, New Zealand, Portugal, Spain, and the USA. Each country had its own CSV file with wine name, rating, number of ratings, price, region, winery, wine style, alcohol content, flavour profile scores (bold, tannin, sweet, acidic), and food pairings.

---

**Q5. How did you handle the data preparation?**

> I used a Jupyter Notebook (`Data Preparation.ipynb`) to:
> - Load all 8 country CSV files and concatenate them into one DataFrame
> - Standardise column names
> - Handle missing values (drop or impute depending on the column)
> - Convert price and alcohol content to numeric types
> - Parse the food pairings column from a string representation into a Python list
> - Save the cleaned result as `process_wine_data.csv`

---

**Q6. How is the data loaded into the dashboard — is there a database?**

> No database is used. The processed CSV files are hosted directly on GitHub as raw files and loaded into Pandas DataFrames at app startup using `pd.read_csv(url)`. This keeps the deployment simple and dependency-free.

---

**Q7. What does the processed dataset look like? What are the key columns?**

> The final dataset has 4,624 rows with columns including: `Name`, `Rating`, `Number of Ratings`, `Price`, `Region`, `Winery`, `Wine style`, `Alcohol content`, `Bold`, `Tannin`, `Sweet`, `Acidic`, `Food pairings`, and `Country`.

---

**Q8. How did you handle the food pairings column since it contains multiple values per wine?**

> The food pairings were stored as a comma-separated string per row. I converted them into Python lists during preprocessing and used Pandas' `.explode()` method in the dashboard callback to flatten the list column into individual rows before calling `.value_counts()` to count each pairing — this allows each food item per wine to be counted independently.

---

### 🔹 Section C: Dashboard and Dash Framework

**Q9. Why did you choose Dash over other frameworks like Streamlit or Flask?**

> Dash was chosen because it offers tight integration with Plotly charts and supports reactive callbacks natively, making it easy to connect filter inputs to chart outputs. It's also Python-native and produces production-quality, interactive web apps without writing any JavaScript. For a data analytics dashboard with multiple interdependent charts, Dash's callback model is very well suited.

---

**Q10. How do Dash Callbacks work in your project?**

> Dash callbacks are Python functions decorated with `@app.callback`. They declare:
> - **Outputs**: the component property to update (e.g., a chart's `figure`)
> - **Inputs**: the component properties that trigger the update (e.g., dropdown `value`, slider `value`)
>
> When any Input changes, Dash calls the function automatically and re-renders the Output. In this project, one callback updates all five charts whenever the country, wine style, or price range filters change. Another callback toggles the filter panel's visibility.

---

**Q11. How does the filter logic work?**

> The main callback receives three inputs: `selected_countries` (list), `selected_styles` (list), and `price_range` (two-element list).  
> It applies them sequentially to the DataFrame:
> 1. First filter by price range using boolean indexing
> 2. If countries are selected, filter with `.isin(selected_countries)`
> 3. If wine styles are selected, filter with `.isin(selected_styles)`  
>
> Empty lists are treated as "no filter applied" so the full dataset is shown by default.

---

**Q12. What charts are in the dashboard and what do they show?**

> - **Price Histogram**: Distribution of wine prices coloured by country — reveals price positioning differences between countries.
> - **3D Scatter Plot**: Price on X, Rating on Y, Number of Ratings on Z — shows the relationship between cost and perceived quality.
> - **Food Pairings Bar Chart**: Counts of food items recommended across all filtered wines — useful for sommeliers.
> - **Alcohol Box Plot**: Distribution of alcohol content by country — shows differences in wine strength.
> - **Wine Style Pie Chart**: Proportion breakdown of Red, White, Rosé, Sparkling, etc.
> - **NLP Bar Chart**: Counts of what topics appear most in wine reviews.

---

**Q13. How did you make the filter panel collapsible?**

> I added a "Toggle Filters" button and wired a callback to it. The callback reads the button's `n_clicks` value: if it's even, the panel is shown (display: block); if it's odd, it's hidden (display: none). The `prevent_initial_call=True` flag stops the callback firing on page load.

---

### 🔹 Section D: NLP and Machine Learning

**Q14. What is zero-shot classification and why did you use it here?**

> Zero-shot classification is a technique where a model classifies text into categories it was never explicitly trained on. It uses Natural Language Inference (NLI) — the model checks how well the text "entails" a given label hypothesis. I used it because:
> - There was no labelled training data for wine review categories
> - I didn't want to manually label hundreds of reviews
> - Pre-trained NLI models can generalise to new labels without any fine-tuning

---

**Q15. Which HuggingFace model did you use and why?**

> I used `cross-encoder/nli-distilroberta-base`. It's a smaller, distilled variant of RoBERTa fine-tuned on NLI tasks. I chose it over `facebook/bart-large-mnli` because it's faster and requires less memory, making it more practical for a research/portfolio project without GPU requirements.

---

**Q16. What categories did you classify wine reviews into?**

> Reviews were classified based on what they "talk about" — for example:
> - *"talks about food combinations"*
> - *"talks about taste and flavour"*
> - *"talks about the winery or region"*
> - *"talks about price or value"*
>
> The classifier assigns the most probable label to each review, which is stored in the `talks_about` column.

---

**Q17. How are the NLP results visualised in the dashboard?**

> The labelled review CSV is loaded at startup (not inside a callback, since it's static data). A Plotly bar chart is created once using `go.Figure([go.Bar(...)])` and the `value_counts()` of the `talks_about` column. This static figure is passed directly to the `dcc.Graph` component via the `figure` parameter — it does not need to be recomputed on filter changes because the NLP tab is independent of the wine data filters.

---

**Q18. If you were to improve the NLP component, what would you do?**

> - Use a larger model like `facebook/bart-large-mnli` for higher classification accuracy
> - Add confidence scores and show only high-confidence labels
> - Allow users to dynamically enter new label categories in the dashboard and re-classify in real time
> - Fine-tune a model on a labelled wine review dataset for domain-specific accuracy
> - Add sentiment analysis alongside topic classification

---

### 🔹 Section E: Technical and Architecture Questions

**Q19. How is the application structured?**

> The entire Dash application lives in `dashboard.py`. At the top, data is loaded and the NLP bar chart is pre-computed. Then `app.layout` defines the UI structure — header, filter panel, tabs, footer. Below that, two `@app.callback` decorated functions define all reactive behaviour. The app is run with `app.run_server(debug=True)` under the `__main__` guard.

---

**Q20. Why is data loaded at module level rather than inside a callback?**

> Loading data inside a callback would re-read the CSV from GitHub on every filter interaction, causing slow performance and unnecessary network requests. Loading it once at module startup means the DataFrame is in memory for the entire session, and callbacks only filter an in-memory object — much faster.

---

**Q21. How would you deploy this dashboard to production?**

> - Replace `debug=True` with `debug=False`
> - Use a production WSGI server like `gunicorn`: `gunicorn dashboard:server`
> - Deploy on a platform like Heroku, Render, or AWS EC2
> - Add a `Procfile` and `runtime.txt` for Heroku
> - Optionally cache data with Flask-Caching to avoid re-loading CSVs on server restarts

---

**Q22. What would you change or improve if you had more time?**

> - **Database integration**: Replace CSV files with a PostgreSQL or SQLite database for scalability
> - **User authentication**: Add login so users can save custom filters or watchlists
> - **Real-time data**: Integrate a wine API to pull live pricing and new reviews
> - **Machine learning**: Build a wine recommendation engine using collaborative filtering
> - **Testing**: Add unit tests for data preprocessing and callback logic using `pytest` and Dash's testing utilities
> - **CI/CD**: Add a GitHub Actions pipeline for linting and automated deployment

---

**Q23. How did you handle the case where filters return no data?**

> The callback applies filters sequentially. If the filtered DataFrame becomes empty, Plotly will render blank/empty charts with axis labels rather than crashing. No explicit empty-state handling was added, but this could be improved by checking `if filtered_df.empty` and returning a chart with a "No data available" annotation.

---

### 🔹 Section F: Soft Skills / Project Management

**Q24. How did you divide the work in the group?**

> This was an academic/university data science group project developed by Group 10. Responsibilities were split across team members:
> - Data collection and cleaning (raw CSVs → processed CSV)
> - NLP modelling (zero-shot classification notebook)
> - Dashboard development (Dash app layout and callbacks)
> - Visualisation design (choosing and styling the Plotly charts)

---

**Q25. What challenges did you face and how did you overcome them?**

> - **Data inconsistency across countries**: Each country CSV had slightly different column names and formats. Solved by writing a normalisation step in the data preparation notebook.
> - **Food pairings as nested data**: Pairings were stored as strings like `"['Beef', 'Lamb']"`. Used `ast.literal_eval()` to parse them into real lists, then `.explode()` to flatten for counting.
> - **NLP model speed**: Running `cross-encoder/nli-distilroberta-base` on a large review dataset was slow on CPU. Solved by running the classification notebook once offline, saving the labelled output, and loading the pre-labelled CSV in the dashboard rather than running inference live.
> - **Filter interaction edge cases**: Dropdowns returning `None` vs `[]` caused TypeErrors. Fixed by normalising inputs at the start of the callback with explicit `if input is None: input = []` guards.

---

**Q26. How would you explain this project to a non-technical interviewer?**

> "Imagine going into a wine shop where there are thousands of wines from all over the world and no easy way to compare them. I built a digital tool — like a smart wine guide — where you can pick a country, set your budget, and instantly see charts showing which wines are most popular, what foods they pair with, how strong they are, and what other customers say about them. I also used an AI language tool to automatically read customer reviews and group them by topic, so you can quickly see what people care about most when reviewing wine."

---

*This guide covers the full project scope, architecture, data pipeline, NLP component, and both technical and behavioural interview questions. Good luck! 🍷*
