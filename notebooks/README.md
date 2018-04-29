
These Jupyter notebooks contain backend testing/experimentation for future implementation on the website.



### [kaggle_predictor.ipynb](kaggle_predictor.ipynb) 
  * This is the main notebook.  It is how we simulate and test the tourney with different indicators.  This file provides the basis for "bracket_generator.py" in the django project (django\app\generate_bracket.py)

### [csv_generator.ipynb](csv_generator.ipynb)
  * code for creating a master csv file from all the data we have
  * [output csv](../csvs/kaggle/regular_season_stats.csv)
  
### [normalize.ipynb](normalize.ipynb)
  * noramlize stats and invert opponent stats
  * [output csv](../csvs/kaggle/normalized_stats.csv)

### [graphs.ipynb](Graphs.ipynb)
  * experimenting with different indicators to see how they interact/correlate

### [statistical_method.ipynb](statistical_method.ipynb)
  * experimenting with Ordinary Least Squares regression model to best indicators and weights
