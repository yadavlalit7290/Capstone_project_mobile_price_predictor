## Capstone_project_mobile_price_predictor
I built a Machine Learning End to End project to predict the price of mobile phones. I collected data from the smartprix website and scraped it to create a dataframe. I cleaned the data and filled in missing values using KNN imputer. I assumed that if a fast charger was available, it would be a 15W fast charger.

I used the VotingRegressor ensemble technique to combine the predictions of multiple regression models to improve accuracy. I used the RandomForestRegressor, Ridge, ExtraTreeRegressor, and GradientBoostingRegressor models.

My model achieved an R2 score of 0.90 and a mean absolute error (MAE) of 5893. I tried to create a column for pixel per inch, but the R2 score remained at 0.90, so I didn't include it in the model because it didn't improve the accuracy.

I deployed my model to a Streamlit website, where users can enter the specifications of a mobile phone and receive a predicted price. A data dashboard page also present that shows information about the data used to train the model. The website also displays the predicted price plus and minus the MAE.
