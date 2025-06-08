import pandas as pd
from textblob import TextBlob

def run_sentiment_analysis(input_file='cleaned_reviews.csv', output_file='sentiment_analysis.csv'):
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Run preprocess_reviews.py first.")
        return None
    
    def get_textblob_sentiment(text):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            return 'positive', polarity
        elif polarity < 0:
            return 'negative', -polarity
        else:
            return 'neutral', 0.0
    
    df['sentiment_label'], df['sentiment_score'] = zip(*df['review'].apply(get_textblob_sentiment))
    
    df.to_csv(output_file, index=False)
    print(f"Sentiment analysis saved to {output_file}. Total reviews: {len(df)}")
    
    summary = df.groupby(['bank', 'rating'])['sentiment_score'].mean().reset_index()
    print("Sentiment summary by bank and rating:\n", summary)
    
    return df

if __name__ == "__main__":
    run_sentiment_analysis()