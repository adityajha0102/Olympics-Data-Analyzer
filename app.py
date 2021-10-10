import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import seaborn as sns
import helper
import preprocessor
from page_design import *

df = pd.read_csv('Olympic_data/athlete_events.csv')
region_df = pd.read_csv('Olympic_data/noc_regions.csv')

df = preprocessor.preprocess(df, region_df)
st.sidebar.title("Olympics Data Analysis")
header1(" ")
header1(" ")

st.sidebar.image(
    'https://e7.pngegg.com/pngimages/1020/402/png-clipart-2024-summer-olympics-brand-circle-area-olympic-rings'
    '-olympics-logo-text-sport.png')
st.sidebar.header(" ")
st.sidebar.header(" ")
user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Table', 'Overall Analysis', 'Country-wise Analysis', 'Athlete-wise Analysis')
)

# st.dataframe(df)

if user_menu == 'Medal Table':

    st.image("images/image1.jpg")
    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")

    st.sidebar.header("Medal tally")

    years, country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)
    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)

    if selected_year == 'Overall' and selected_country == 'Overall':
        # st.title('Overall Tally')
        header1('Medal Table')

    if selected_year != 'Overall' and selected_country == 'Overall':
        # st.title('Medal Tally in '+str(selected_year)+' Olympics')
        s = 'Medal Table in ' + str(selected_year) + ' Olympics'
        header1(s)

    if selected_year == "Overall" and selected_country != "Overall":
        # st.title(selected_country+" overall performance")
        s = selected_country + "'s overall performance"
        header1(s)

    if selected_year != "Overall" and selected_country != "Overall":
        # st.title(selected_country+"'s performance in "+str(selected_year)+' Olympics')
        s = selected_country + "'s performance in " + str(selected_year) + ' Olympics'
        header1(s)

    header1(" ")
    header1(" ")
    st.table(medal_tally.style.set_properties(color="#FF3131"))

if user_menu == 'Overall Analysis':
    # No. of Olympics played till date
    editions = df['Year'].unique().shape[
                   0] - 1    # -1 because 1906 olympic was played in athens but later it was not considered by the commitee because the 4 year cycle was not followed

    # NO of cities in which olympics was played
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]  # there are many problems due to historical territories and stuff

    header1('Top Statistics')
    header1(" ")
    header1(" ")
    header1(" ")

    col1, col2, col3 = st.columns(3)

    with col1:
        header2("Editions")
        header2(editions)

    with col2:
        header2("Hosts")
        header2(cities)

    with col3:
        header2("Sports")
        header2(sports)

    header1(" ")
    header1(" ")

    col1, col2, col3 = st.columns(3)

    with col1:
        header2("Events")
        header2(events)

    with col2:
        header2("Nations")
        header2(cities)

    with col3:
        header2("Athletes")
        header2(athletes)

    nations_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nations_over_time, x="Edition", y="region")

    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")

    header3("Participating Nations over the years")

    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x="Edition", y="Event")

    header1(" ")
    header1(" ")
    header1(" ")

    header3("Events over the years")

    st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x="Edition", y="Name")

    header1(" ")
    header1(" ")

    header3("Athletes over the years")

    st.plotly_chart(fig)

    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")

    header3("No of Events over time(Every Sport)")

    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")

    fig, ax = plt.subplots(figsize=(20, 20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])

    ax = sns.heatmap(
        x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
        annot=True)

    st.pyplot(fig)

    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")

    header3("Most Decorated Athletes")

    header1(" ")
    header1(" ")

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    selected_sport = st.selectbox('Select a Sport', sport_list)
    x = helper.most_successful(df, selected_sport)

    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")

    st.table(x)

if user_menu == 'Country-wise Analysis':
    st.sidebar.title('Country-wise Analysis')
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    st.image("images/countries1.jpg")

    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")

    selected_country = st.sidebar.selectbox('Select a country', country_list)

    country_df = helper.yearwise_medal_tally(df, selected_country)
    fig = px.line(country_df, x="Year", y="Medal")

    # st.title(selected_country + " Medal Tally over the years")
    s = selected_country + " Medal Tally over the years"
    header4(s)

    st.plotly_chart(fig)

    # st.title(selected_country + " Excels in the following sports")
    s = selected_country + " Excels in the following sports"

    header1(" ")
    header1(" ")
    header1(" ")

    header4(s)

    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")

    pt = helper.country_event_heatmap(df, selected_country)
    fig, ax = plt.subplots(figsize=(20, 20))

    ax = sns.heatmap(pt, annot=True)

    st.pyplot(fig)

    # st.title('Top 10 athletes of '+selected_country)
    header1(" ")
    header1(" ")
    header1(" ")

    s = 'Top athletes of ' + selected_country

    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")
    header4(s)

    top10_df = helper.most_successful_countrywise(df, selected_country)

    header1(" ")
    header1(" ")

    st.table(top10_df.style.set_properties(color="#FF3131"))

if user_menu == 'Athlete-wise Analysis':

    st.image("images/athlete1.jpg")

    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")

    athlete_df = df.drop_duplicates(['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],
                             show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)

    # st.title("Distribution of Age")
    header4("Distribution of Age")
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo',
                     'Cricket', 'Ice Hockey']

    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    # st.title("Distribution of Age wrt Sports(Gold Medalist)")

    header1(" ")
    header4("Distribution of Age wrt Sports(Gold Medalist)")

    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    # st.title("Height vs Weight")
    header1(" ")

    header4("Height vs Weight")

    header1(" ")
    header1(" ")

    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = helper.weight_v_height(df, selected_sport)
    fig, ax = plt.subplots()
    ax = sns.scatterplot(temp_df['Weight'], temp_df['Height'], hue=temp_df['Medal'], style=temp_df['Sex'], s=60)

    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")

    st.pyplot(fig)

    # st.title("Men Vs Women participation over the Years")
    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")
    header1(" ")

    header4("Men Vs Women participation over the Years")

    final = helper.men_v_women(df)

    fig = px.line(final, x='Year', y=['Male', 'Female'])
    fig.update_layout(autosize=False, width=1000, height=600)

    st.plotly_chart(fig)
