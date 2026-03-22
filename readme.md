# Zomato Restaurant Data Pipeline

An end-to-end ETL pipeline built with Python that extracts, cleans, loads and visualizes Zomato restaurant data.

## Project Structure

```
zomato_project/
├── extract.py        # Reads raw CSV data
├── transform.py      # Cleans and structures data
├── load.py           # Loads clean data into SQLite database
├── visualize.py      # Generates matplotlib visualizations
├── main.py           # Runs the full pipeline
├── zomato.csv        # Raw dataset
├── zomato.db         # Output database (auto-created)
└── zomato_analysis.png  # Output dashboard (auto-created)
```

## Tech Stack

- Python
- Pandas
- Matplotlib
- SQLite

## Pipeline Steps

### 1. Extract
Reads raw Zomato CSV data using Pandas.

### 2. Transform
- Removes duplicate rows
- Drops rows with missing cuisines or city
- Filters out unrated restaurants (rating = 0)
- Renames columns for consistency
- Selects only relevant columns

### 3. Load
Saves the cleaned data into a SQLite database (`zomato.db`) in a table called `restaurants`.

### 4. Visualize
Generates 6 charts saved as `zomato_analysis.png`:
- Top 10 most common cuisines
- Rating distribution
- Average cost for two by city
- Online delivery vs table booking comparison
- Price range distribution
- Top 10 cities by restaurant count

## How to Run

1. Install dependencies:
```bash
pip install pandas matplotlib
```

2. Run the pipeline:
```bash
python main.py
```

## Key Findings

- North Indian and Chinese cuisines are the most common
- Most restaurants fall in the 3.0 - 4.0 rating range
- Budget restaurants make up the majority of listings
- Online delivery is more common than table booking