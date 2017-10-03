# BAYS Web Scraper & Summarizer

This repo contains utilities to scrape and summarize game scores from the Boston Area Youth Soccer website.

As President of Concord-Carlisle Youth Soccer, I really don't care about the outcome of any single youth soccer game. But I am interested in using game outcomes to answer questions like:

* Is there CCYS team this is always winning or losing by big margins, that needs to be moved to another section?
* In aggregate, are we doing a good job placing our teams in competitive sections?
* (Are any towns habitually sand-bagging?)

## Key functions and classes:

### get\_town\_info:

#### get\_town\_table: 

This function takes a 3-letter town code (like 'CON') and returns a dataframe with the town team's current win/loss/draw, GF/GA statistics.



