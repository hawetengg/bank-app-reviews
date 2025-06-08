import pandas as pd

def verify_data(input_file='cleaned_reviews.csv'):
    try:
        df = pd.read_csv(input_file)
        print("Missing values per column:")
        print(df.isnull().sum())
        print(f"Total reviews: {len(df)}")
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Ensure preprocess_reviews.py has been run.")

if __name__ == "__main__":
    verify_data()