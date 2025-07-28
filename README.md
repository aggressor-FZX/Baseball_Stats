# Baseball Stats and Player Performance Prediction Project

## Overview

This project analyzes over 100 years of baseball statistics, primarily using the Lahman Baseball Database and additional Statcast data, to build predictive models of player performance. The goal is to identify key factors that influence a player's next-year batting and pitching outcomes, which can be valuable for fantasy baseball team optimization or deeper baseball analytics.

## Data Sources

- **Lahman Baseball Database CSV files:** Historical baseball player stats including batting, pitching, fielding, and metadata.
- **Statcast API Data:** Advanced pitching statistics and metrics starting from 2016, retrieved via the `pybaseball` Python package.
- **MySQL Database:** CSV files are ingested into MySQL for structured querying and relational joins.

## Key Components

### 1. Data Preparation and SQL Integration
- CSV files are renamed and loaded into a MySQL database using SQLAlchemy.
- Batting and fielding statistics are aggregated by player and year to reduce duplicates.
- Data cleaning includes handling missing values and malformed headers.

### 2. Custom Data Structures for Player Stats
- A hierarchical `CareerTree` structure models players and their yearly statistics using Python classes.
- Alternative linked-list implementations are explored to manage player and year data efficiently.

### 3. Exploratory Data Analysis & Visualization
- Individual player stats (e.g., Barry Bonds) are plotted over time to visualize trends in hits, home runs, etc.

### 4. Predictive Modeling with Linear Regression
- Models are trained to predict next-year player stats (e.g., runs, hits, home runs) based on current year features.
- Feature importance is evaluated to interpret which stats most influence future performance.
- Model metrics such as Mean Absolute Error (MAE) and R-squared (R²) score assess prediction quality.

### 5. Pitching Data Analysis
- Pitching statistics are merged with Statcast advanced metrics like velocity and spin rate.
- Dimensionality reduction and data cleaning are applied before further analysis.
- Explorations into pitcher performance characteristics and grouping.

## Usage Instructions

1. Ensure all CSV data files are located in the project directory.
2. Set up a MySQL database and provide access credentials in `Access_sql.py`.
3. Run the data ingestion scripts to load CSVs into MySQL.
4. Execute the Jupyter notebook cells sequentially for data loading, structure building, analysis, and modeling.
5. Visualize individual player stats or overall model results using provided plotting functions.

## Dependencies

- Python 3.x
- pandas
- numpy
- matplotlib
- scikit-learn
- sqlalchemy
- mysql-connector-python
- pybaseball

## Future Work

- Expand analysis to include fielding and pitching performance predictions.
- Integrate real-time Statcast API data for up-to-date analysis.
- Explore more complex models such as random forests or neural networks.
- Improve handling of missing and inconsistent data.

## Author

Jeffrey Calderon

---

*This project serves as a foundation for baseball analytics and machine learning applications using publicly available datasets and demonstrates integration of SQL, Python data structures, and statistical modeling.*
