# Flight Data Analysis

## Overview
This project aims to analyze flight data from Kayak, focusing on the differences between Main Cabin and Comfort Plus flight prices. Through the process of data gathering, cleaning, and analysis, we examine various trends, correlations, and other interesting features of the dataset.

## Requirements
You'll need to install the necessary Python libraries. This can be done by running:

```
pip install -r requirements.txt
```
## How to run
First, we gather up-to-date flight information from Kayak by running the scraping script:
```
python scrape.py
```
Then, open the flight_data_analysis.ipynb Jupyter notebook and run all cells. The notebook contains the code for data cleaning, formatting, and analysis, along with explanations and visualizations.

## Features
The analysis covers:

* A visual representation of the distribution of Main Cabin and Comfort Plus flight prices.
* A statistical significance test comparing Main Cabin and Comfort Plus flight prices.
* An examination of the correlation between flight duration and flight prices.
* Comparison of prices for nonstop flights and flights with stops.
* A calculation of the confidence intervals for the mean prices of Main Cabin and Comfort Plus.

## Conclusion and Future Approaches

To further enhance this analysis, the accumulation of historical data is necessary. With historical data, we can observe and predict trends over time. Some ways to gather historical data could be through defining a CRON job that runs scrape.py daily, or exploring available APIs that can supply this data.

## Notes
The project uses Kayak for data scraping, as Delta's website has advanced anti-scraping measures.
The accuracy of the data obtained from Kayak might need verification.
In the future, it might be worth exploring APIs for data gathering.
An idea for a future project could be to create an API for this scraped data, potentially using a platform like RapidAPI.