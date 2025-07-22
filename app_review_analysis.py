import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
from textblob import TextBlob
import os

# Download stopwords if not already
nltk.download('stopwords')

# Load data
apps_df = pd.read_csv('data/googleplaystore.csv')
reviews_df = pd.read_csv('data/googleplaystore_user_reviews.csv')

# Clean apps_df
apps_df.dropna(how='any', inplace=True)
apps_df = apps_df[apps_df['Rating'] <= 5.0]

# Clean Size column
apps_df['Size'] = apps_df['Size'].replace('Varies with device', np.nan)
apps_df.dropna(subset=['Size'], inplace=True)

def convert_size(size):
    size = size.replace(',', '').replace('+', '')
    if 'M' in size:
        return float(size.replace('M', '')) * 1e6
    elif 'k' in size:
        return float(size.replace('k', '')) * 1e3
    else:
        return np.nan

apps_df['Size'] = apps_df['Size'].apply(convert_size)

# Preprocess reviews_df
reviews_df.dropna(subset=['Translated_Review'], inplace=True)

# Sentiment classification using TextBlob
def get_sentiment(text):
    analysis = TextBlob(str(text))
    return 'Positive' if analysis.sentiment.polarity > 0 else 'Negative' if analysis.sentiment.polarity < 0 else 'Neutral'

reviews_df['Sentiment_Predicted'] = reviews_df['Translated_Review'].apply(get_sentiment)

# Save processed data for Tableau
reviews_df.to_csv('data/processed_reviews.csv', index=False)
apps_df.to_csv('data/processed_apps.csv', index=False)

print("Data cleaned and sentiment analysis done. Processed files saved in /data.")


# WordCloud for Positive Reviews
positive_reviews = ' '.join(reviews_df[reviews_df['Sentiment_Predicted'] == 'Positive']['Translated_Review'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positive_reviews)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud - Positive Reviews')
plt.show()
