# BAYS Web Scraper & Summarizer

This project contains utilities to scrape and summarize game scores from the Boston Area Youth Soccer website.

As President of Concord-Carlisle Youth Soccer, I really don't care about the outcome of any single youth soccer game. But I am interested in using game outcomes to answer questions like:

* Are there any CCYS teams that are winning or losing by big margins, that need to be moved to another section?
* In aggregate, are we doing a good job placing our teams in competitive sections?
* (Are any towns habitually sand-bagging?)

These utilities are written in Python 3.

## Key functions and classes:

### get\_town\_info:

#### get\_town\_table: 

This function takes a 3-letter town code (like 'CON') and returns a dataframe with the town team's current win/loss/draw, GF/GA statistics.



## Data Sources

BAYS team info and game scores: https://bays.org/

School-age population by town: https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?src=CF