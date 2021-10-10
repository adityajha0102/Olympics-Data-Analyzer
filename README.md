# Olympics-Data-Analyzer

#### Created and Tested on Windows 10 with Python 3.9

#### A web app that analyses the 120 years of summer olympics data for each country as well as the performace of every athlete that has participated till date.

#### Check it out here:

#### https://olympic-data-analysis01.herokuapp.com/

## Getting started:

#### In order to get started with the Olympics Data Analyzer, just clone this repository and download the TMDB movie dataset from kaggle from the below given link.

#### https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results

#### Create a folder by the name "Olympic_data" and extract both the dataset in the folder. Now create a virtual environment with Python 3.9 and then install the packages in the requirements.txt file. Next execute the command streamlit run app.py in your terminal working in the main directory. A web app will be hosted in your local machine as in the image given below and you are done. You will see a similar image in your browser as given below.

![Screenshot (26)](https://user-images.githubusercontent.com/59216663/136691165-74ce42a8-95ec-41e3-8411-9f79983aac3a.png)

#### You are free to explore the web app and check different features and graphs. Although there are some informations that are a bit incorrect considering the history of the countries and states that do affect the dataset like USSR's disintegration into 15 different countries and many more.

## How does it work?

#### So basically we preprocessed the dataset and merged them. Then we removed the Winter Olympics data as we are going only for the summer olympics data as of now. Next, we plot different regarding overall analysis, athlete wise analysis and even country wise analysis. We finally used the analyzed data to deploy it using Streamlit in heroku.

## Contribution

#### Once you get a better understanding of the project, you will see that a lot can be done with the project. There are some issues regarding the border disputes and the times of war and many other factors that do affect the medal tally of each countries which you can work on improving. The other thing that can be done is exploring completely by yourself by going for the winter olympics and the paralympics games and integrate those data in the web app as well. What I personally feel is that you need to research a bit regarding the previous background of the countries and the olympics games as well which is freely available in different sites like wikipedia.

#### Feel free to fork this project and make your own changes too. Pull requests for any changes are accepted as well.
