# Group Project: Stock Price Prediction App

The following group assignment is a 5-member project we were tasked to either develop an analytic project, a dashboard visualization project and a IoT project using python.
Our group decided to develop a Stock Price Prediction App. 

Using the yfinance library, stock data is retrieved and stored within the program where machine learning was performed on said data using the MLP Regressor model from the Sci-kit library.
Charts were then developed to visualize the stock price over time, scatter plots on the correlation between actual and predicted price before visualizing the predicted stock price made by the model.

Said predicted price is then compared to the current price to either recommend buying or not buying the stock at that time. (Of course, this is *NOT* financial advice :D)

In order for users to interact and try out this app in a user-friendly way, Streamlit was used to deploy this web app. 

Try our project out at: [Stock Prediction App](https://bap-group-project.streamlit.app/).
