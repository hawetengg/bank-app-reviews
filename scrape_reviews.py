from google_play_scraper import reviews, Sort
import pandas as pd
import json
import os

# Define app IDs and banks
apps = {
    'CBE': 'com.combanketh.mobilebanking',
    'BOA': 'com.boa.boaMobileBanking',
    'Dashen': 'com.dashen.dashensuperapp'
}

def scrape_bank_reviews(app_id, bank_name, count=400):
    try:
        result, _ = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=count
        )
        reviews_data = []
        for review in result:
            reviews_data.append({
                'review': review['content'],
                'rating': review['score'],
                'date': review['at'].strftime('%Y-%m-%d'),
                'bank': bank_name,
                'source': 'Google Play'
            })
        print(f"Scraped {len(reviews_data)} reviews for {bank_name}")
        return reviews_data
    except Exception as e:
        print(f"Error scraping {bank_name}: {e}")
        return []

def main():
    all_reviews = []
    for bank, app_id in apps.items():
        print(f"Scraping reviews for {bank}...")
        reviews_data = scrape_bank_reviews(app_id, bank)
        all_reviews.extend(reviews_data)
    
    # Save raw data to JSON
    with open('raw_reviews.json', 'w') as f:
        json.dump(all_reviews, f, indent=2)
    
    # Convert to DataFrame
    df = pd.DataFrame(all_reviews)
    df.to_csv('raw_reviews.csv', index=False)
    print(f"Total scraped reviews: {len(all_reviews)}")

if __name__ == "__main__":
    main()