def transform(data):
    print("\nTransforming data...")
 
    # Fix 1 - Drop duplicates
    data = data.drop_duplicates()
 
    # Fix 2 - Drop rows where cuisines or city is missing
    data = data.dropna(subset=['Cuisines', 'City'])
 
    # Fix 3 - Remove rows with 0 rating (unrated restaurants)
    data = data[data['Aggregate rating'] > 0]
 
    # Fix 4 - Rename columns to be cleaner
    data = data.rename(columns={
        'Restaurant Name'    : 'restaurant_name',
        'City'               : 'city',
        'Cuisines'           : 'cuisines',
        'Average Cost for two' : 'avg_cost',
        'Has Online delivery': 'online_delivery',
        'Has Table booking'  : 'table_booking',
        'Aggregate rating'   : 'rating',
        'Rating text'        : 'rating_text',
        'Price range'        : 'price_range',
        'Votes'              : 'votes',
        'Country Code'       : 'country_code'
    })
 
    # Fix 5 - Keep only useful columns
    data = data[[
        'restaurant_name', 'city', 'cuisines', 'avg_cost',
        'online_delivery', 'table_booking', 'rating',
        'rating_text', 'price_range', 'votes', 'country_code'
    ]]
 
    # Fix 6 - Reset index
    data = data.reset_index(drop=True)
 
    print(f"Transformation complete! Clean rows: {len(data)}")
    return data