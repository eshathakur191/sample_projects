import pandas as pd
import numpy as np

# 1. EXTRACT: Get the raw data
def extract_data():
    """Simulates loading raw data from a source (like a CSV or API)."""
    raw_data = {
        'product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Mouse'],
        'price': [1200, 25, np.nan, 75, 25],  # Contains a missing value (NaN)
        'quantity': [2, 5, 1, 3, 2]
    }
    return pd.DataFrame(raw_data)

# 2. TRANSFORM: Clean and fix the data
def transform_data(df):
    """Cleans data and calculates a new revenue column."""
    # Fill missing prices with a default value of 150
    df['price'] = df['price'].fillna(150)
    
    # Calculate Total Revenue
    df['total_revenue'] = df['price'] * df['quantity']
    
    # Group by product to combine duplicate items (like the Mouse)
    cleaned_df = df.groupby('product').sum().reset_index()
    return cleaned_df

# 3. LOAD: Save the processed data
def load_data(df):
    """Simulates saving the finished data to a file or database."""
    output_file = 'sales_summary.csv'
    df.to_csv(output_file, index=False)
    print(f"🎉 Pipeline successful! Data saved to '{output_file}'")
    print(df)

# --- RUN THE PIPELINE ---
if __name__ == "__main__":
    # Chain the steps together
    raw_df = extract_data()
    processed_df = transform_data(raw_df)
    load_data(processed_df)
