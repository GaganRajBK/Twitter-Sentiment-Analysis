
<h1><center>Twitter Sentiment Analysis</h1>

![frame_firefox_mac_dark (1)](https://raw.githubusercontent.com/AdityaSuresh013/Twitter-Sentiment-Analysis/main/Images/twittersentiment.PNG)

A Twitter Sentiment Analysis website made using Flask for a College Project

## Overview

This project is a sentiment analysis application for Twitter data, leveraging a dataset from Kaggle. The backend is implemented in Python, utilizing machine learning models for sentiment analysis, while the frontend is built using Flask. The application allows users to input tweets and receive sentiment predictions, categorizing them as positive or negative.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model Training](#model-training)
- [References](#references)
- [License](#license)
- [Author](#author)

## Features

- Web interface built with Flask for inputting a example tweet.
- Classify tweets into positive or negative categories.
- Visualization of prediction results.

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: scikit-learn, Pandas, NumPy, Joblib
- **Visualization**: Matplotlib, Plotly

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AdityaSuresh013/Twitter-Sentiment-Analysis.git
   cd Twitter-Sentiment-Analysis
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Flask application:**

   ```bash
   python app.py
   ```

2. **Open browser and navigate to:**

   ```
   http://127.0.0.1:5000/
   ```

3. **Enter a sample tweet to get a predicted sentiment.**

## Data

The dataset used for training the model is sourced from [Kaggle]([https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data](https://www.kaggle.com/datasets/kazanova/sentiment140)), which contains 1.6 million labeled tweets. It has the following columns:

- target: the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
- ids: The id of the tweet
- date: the date of the tweet
- flag: The query. If there is no query, then this value is NO_QUERY.
- user: the user that tweeted
- text: the text of the tweet

## Model Training

The machine learning model is trained using the dataset. Key steps involved:

1. **Data Preprocessing**: Cleaning and transforming the dataset to make it suitable for training.
2. **Feature Selection**: Selecting the most relevant features.
3. **Data Visualization**: Visualizing the cleaned dataset using Matplotlib
4. **Model Selection**: Implementing various regression models (Linear Regression, Lasso, Decision Trees) to find the best performing model.
5. **Evaluation**: Evaluating the model's performance using metrics like K Fold Cross, etc.

##  References

- [Sentiment Analysis on tweets with LSTM](https://www.analyticsvidhya.com/blog/2021/12/sentiment-analysis-on-tweets-with-lstm-for-beginners/) - A guide on implementing LSTM for sentiment analysis on tweet data.

##  License

[MIT](https://choosealicense.com/licenses/mit/) © [Gagan Raj B K](https://github.com/AdityaSuresh013)
- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- [Gagan Raj B K](https://github.com/AmbitMaharana)
