import pandas as pd
from dateutil.parser import parse

def preprocess_reviews(input_file='raw_reviews.csv', output_file='cleaned_reviews.csv'):
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Run scrape_reviews.py first.")
        return None
    
    # Remove duplicates
    df = df.drop_duplicates(subset=['review', 'date', 'bank'])
    
    # Handle missing data
    df = df.dropna(subset=['review', 'rating'])
    
    # Validate ratings
    df = df[df['rating'].isin([1, 2, 3, 4, 5])]
    
    # Normalize dates
    def normalize_date(date_str):
        try:
            return parse(date_str).strftime('%Y-%m-%d')
        except:
            return None
    df['date'] = df['date'].apply(normalize_date)
    df = df.dropna(subset=['date'])
    
    # Ensure columns
    df = df[['review', 'rating', 'date', 'bank', 'source']]
    
    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}. Total reviews: {len(df)}")
    
    return df

if __name__ == "__main__":
    preprocess_reviews()