from extract import extract
from transform import transform
from load import load
from visualize import visualize
 
# ─────────────────────────────────────────
#  ZOMATO ETL PIPELINE
# ─────────────────────────────────────────
 
# Step 1 - Extract
data = extract("zomato.csv")
 
# Step 2 - Transform
data = transform(data)
 
# Step 3 - Load
load(data)
 
# Step 4 - Visualize
visualize(data)
 
print("\nPipeline complete!")
print("Database : zomato.db  -> table: restaurants")
print("Dashboard: zomato_analysis.png")