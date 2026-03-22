import matplotlib.pyplot as plt
import pandas as pd

def visualize(data):
    print("\nGenerating visualizations...")

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle("Zomato Restaurant Data Analysis", fontsize=18, fontweight='bold', y=1.01)

    # ─────────────────────────────────────────
    # Chart 1 - Top 10 Cuisines
    # ─────────────────────────────────────────
    all_cuisines = data['cuisines'].str.split(',').explode().str.strip()
    top_cuisines = all_cuisines.value_counts().head(10)

    axes[0, 0].barh(top_cuisines.index[::-1], top_cuisines.values[::-1], color='steelblue')
    axes[0, 0].set_title("Top 10 Most Common Cuisines")
    axes[0, 0].set_xlabel("Number of Restaurants")
    axes[0, 0].set_ylabel("Cuisine")

    # ─────────────────────────────────────────
    # Chart 2 - Rating Distribution
    # ─────────────────────────────────────────
    axes[0, 1].hist(data['rating'], bins=20, color='coral', edgecolor='white')
    axes[0, 1].set_title("Rating Distribution")
    axes[0, 1].set_xlabel("Rating")
    axes[0, 1].set_ylabel("Number of Restaurants")

    # ─────────────────────────────────────────
    # Chart 3 - Average Cost by City (Top 10)
    # ─────────────────────────────────────────
    top_cities = data.groupby('city')['avg_cost'].mean().sort_values(ascending=False).head(10)

    axes[0, 2].bar(top_cities.index, top_cities.values, color='mediumseagreen')
    axes[0, 2].set_title("Average Cost for Two (Top 10 Cities)")
    axes[0, 2].set_xlabel("City")
    axes[0, 2].set_ylabel("Average Cost")
    axes[0, 2].tick_params(axis='x', rotation=45)

    # ─────────────────────────────────────────
    # Chart 4 - Online Delivery vs Table Booking
    # ─────────────────────────────────────────
    delivery_counts = data['online_delivery'].value_counts()
    booking_counts  = data['table_booking'].value_counts()

    x = ['Has Feature', 'No Feature']
    delivery_vals = [delivery_counts.get('Yes', 0), delivery_counts.get('No', 0)]
    booking_vals  = [booking_counts.get('Yes', 0),  booking_counts.get('No', 0)]

    width = 0.35
    x_pos = range(len(x))
    axes[1, 0].bar([p - width/2 for p in x_pos], delivery_vals, width, label='Online Delivery', color='steelblue')
    axes[1, 0].bar([p + width/2 for p in x_pos], booking_vals,  width, label='Table Booking',  color='coral')
    axes[1, 0].set_title("Online Delivery vs Table Booking")
    axes[1, 0].set_xticks(list(x_pos))
    axes[1, 0].set_xticklabels(x)
    axes[1, 0].set_ylabel("Number of Restaurants")
    axes[1, 0].legend()

    # ─────────────────────────────────────────
    # Chart 5 - Price Range Distribution
    # ─────────────────────────────────────────
    price_labels = {1: 'Budget', 2: 'Mid-range', 3: 'Premium', 4: 'Luxury'}
    price_counts = data['price_range'].value_counts().sort_index()
    price_counts.index = [price_labels.get(i, i) for i in price_counts.index]

    axes[1, 1].pie(price_counts.values, labels=price_counts.index,
                   autopct='%1.1f%%', colors=['steelblue','coral','mediumseagreen','gold'],
                   startangle=140)
    axes[1, 1].set_title("Price Range Distribution")

    # ─────────────────────────────────────────
    # Chart 6 - Top 10 Cities by Restaurant Count
    # ─────────────────────────────────────────
    top_cities_count = data['city'].value_counts().head(10)

    axes[1, 2].barh(top_cities_count.index[::-1], top_cities_count.values[::-1], color='mediumpurple')
    axes[1, 2].set_title("Top 10 Cities by Restaurant Count")
    axes[1, 2].set_xlabel("Number of Restaurants")
    axes[1, 2].set_ylabel("City")

    # ─────────────────────────────────────────
    # Save
    # ─────────────────────────────────────────
    plt.tight_layout()
    plt.savefig("zomato_analysis.png", dpi=150, bbox_inches='tight')
    print("Visualizations saved to zomato_analysis.png")
    plt.show()