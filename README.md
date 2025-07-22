# App Review Analysis using NLP and Tableau

This project analyzes Play Store app reviews to uncover insights using Natural Language Processing (NLP), visualization, and data cleaning techniques. The final output includes sentiment analysis and a Tableau dashboard for business storytelling.

---

## Project Overview

- **Goal:** Extract user sentiment, ratings distribution, and review trends from mobile app data.
- **Tools Used:** Python, Pandas, TextBlob, Matplotlib, Seaborn, Tableau
- **Techniques:** Data cleaning, sentiment classification, exploratory data analysis (EDA), visualization

---

## Folder Structure

app-review-analysis/
├── data/
│ ├── apps.csv
│ ├── reviews.csv
│ └── cleaned_reviews.csv
├── notebooks/
│ └── App_Review_Analysis.ipynb
├── requirements.txt
└── README.md


---

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/app-review-analysis.git
   cd app-review-analysis

2. **Create and activate a virtual environment**
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3. **Install dependencies**
pip install -r requirements.txt

4. **Run the Jupyter Notebook**
jupyter notebook notebooks/App_Review_Analysis.ipynb


## Tableau Dashboard
The cleaned data (cleaned_reviews.csv) was used to create an interactive Tableau dashboard.
Link to Tableau Public Dashboard


## Key Insights
Extracted sentiments from thousands of user reviews

Identified apps with highest/lowest average sentiment

Analyzed correlation between app rating and sentiment score

Visualized review volume by app category


## Technologies Used
Python: pandas, numpy, textblob, nltk, matplotlib, seaborn

Tableau: for interactive dashboard

Jupyter Notebook: for analysis and development


## Contributions
PRs and feedback are welcome! For major changes, please open an issue first.
