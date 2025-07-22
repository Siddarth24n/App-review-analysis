# App Review Analysis using NLP and Tableau

This project analyzes Play Store app reviews to uncover insights using Natural Language Processing (NLP), visualization, and data cleaning techniques. The final output includes sentiment analysis and a Tableau dashboard for business storytelling.

## Project Description

In an era where mobile applications are a dominant part of digital engagement, understanding user feedback is crucial to building successful apps. This project focuses on analyzing user reviews from the Google Play Store to uncover meaningful insights using **Natural Language Processing (NLP)** and **data visualization**.

As of **July 2024**, businesses heavily rely on **automated sentiment analysis** and **real-time feedback interpretation** to iterate on product development. Instead of manually reading thousands of user reviews, this project demonstrates how text data can be programmatically **cleaned**, **analyzed**, and **visualized** to generate actionable insights.

We chose this project for several reasons:
- App reviews are rich in unstructured data that hold valuable opinions from real users.
- Manual review analysis is time-consuming and unscalable.
- NLP provides scalable methods to quantify emotions and patterns in text data.
- Tableau offers an intuitive and interactive medium for business stakeholders to explore insights without technical barriers.

By combining **Python-based NLP techniques** with **Tableau dashboards**, this project enables:
- **Classification of user sentiment** across thousands of reviews.
- Identification of **recurring issues**, **feature requests**, or **positive trends**.
- A **visual storytelling platform** to share findings with non-technical teams like Product, UX, and Marketing.

### Goals & Outcomes
- Automatically determine if reviews are **positive**, **neutral**, or **negative**.
- Extract most common words/themes from each sentiment class.
- Create a visual layer that clearly communicates data-driven findings.
- Build an end-to-end pipeline that’s **reusable** and **scalable** for other app datasets.

### Key Takeaways (as of July 2024)
- **AI-enabled sentiment analysis** is no longer optional—it's foundational to modern product feedback loops.
- Visualization tools like **Tableau** bridge the gap between data teams and decision-makers.
- Unstructured text, when cleaned and analyzed, reveals product pain points and user priorities that numbers alone cannot.
- This project highlights the importance of **cross-functional collaboration** between data engineers, analysts, and business teams to drive continuous app improvement.

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
