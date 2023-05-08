#  What do non-voters look like in the USA? (*Project 3*)

This repository contains a visualization project that depicts some of the most interesting results of a survey about American citizens who tend not to vote.

## Authors

Daniel Ramón Murillo Antuna [@daniel-r-murillo-antuna](https://www.github.com/daniel-r-murillo-antuna)<br>
Luis Paul Garay Acosta [@PaulGaray777](https://github.com/PaulGaray777)<br>
Jorge Alonso Lozano Tena [@loncho9](https://github.com/loncho9)<br>
Roberto Gerónimo Barrón Olvera [@barronr03](https://github.com/barronr03)


## Repository and project description

Is democracy still an effective political system in the 21st century? While that question can have an unimaginable number of answers, what is clear is that nation states need to better understand how it works nowadays and how it is constantly evolving. Just before the 2020 presidential elections in the US, Ipsos, contracted by FiveThirtyEight, polled American citizens online about their voting opinions and behavious in order to have a clearer picture of the electorate. This poll is the perfect oportunity to analyze democracy, as by analyzing the behavior and opinions of US citizens leading up to upcoming elections, people can better understand the current situation of political systems. But... *Why America?*

### Our objectives:

- Firstly, the US is one of the largest democracies in the world, and its political system has a significant impact on the global political landscape. Understanding the preferences and opinions of US citizens can help us gain insight into the political climate of the country, the current situation of democracy as a political system, and the potential impact of the election outcomes on domestic and international affairs.
- Secondly, analyzing the behavior and opinions of US citizens can help political parties, candidates, and policymakers tailor their campaigns and policies to better align with the needs and expectations of voters. By understanding what issues are most important to voters, for example, political parties can develop more effective platforms that resonate with the electorate.
- Finally, understanding the behavior and opinions of US citizens is important for promoting democratic values and principles. In a democracy, it is essential that citizens are informed, engaged, and included in the political process. By analyzing their behavior and opinions, we can identify areas where there may be a lack of understanding, engagement and/or inclusion, and develop strategies to better promote greater participation and civic engagement.
Overall, analyzing the behavior and opinions of US citizens leading up to the elections is an important and timely topic that has significant implications for the country and the world at large.

### Why did we choose this topic?

Given that the next US and Mexico presidential elections are fast approaching, we know that democracy, political behavior, and opinions are not just a hot topic, but the key to understand the possible effects the elections might have on society in the coming years.

### Our project's rationale:

There are currently very few open source tools available on the web to visualize recent political trends, and while there are some available, those tools tend to be designed by their own researchers and data team. Therefore, many of the tools available make it hard for citizens to be as objective as possible. We wanted to contribute initially with a more neutral app that could be used to visualize the FiveThirtyEight data, but that could also be scalable and applicable to similar datasets generated by different sources.

### Finding "the" dataset:

Polls tend to focus on voters, especially on the months before an election. However, the FiveThirtyEight dataset includes data from citizens who don't often cast their vote. Moreover, this survey considered a probability-based online panel that was recruited to be representative of the US population. Representativeness is very hard to achieve, particularly online. This poll surpassed that limitation by conducting poll from September 15th to the 25th, 2020. They also made sure to correct the oversampling of young, Black and Hispanic respondents, and weighted the responses according to the general population benchmarks from the US Census Bureau’s Current Population Survey March 2019 Supplement. FiveThirtyEight asserted that the voter file company Aristotle then matched respondents to a voter file to more accurately understand their voting history and included respondents who did not match the voter file, but described themselves as voting “rarely” or “never”. This survey avoided underrepresenting non-voters, who, as previously highlighted, are less likely to be included in the voter file to begin with.

### The *Non_voters_USA* project displays:

This repository showcases a dashboard that portrays the data of 9 crucial questions of the poll that relate to our objectives. The building of the dashboard went through different stages:

#### Project proposal:
1. Title: Non-voters USA dashboard. <-- *Although that's the name of our repository, we ended up giving this README file a longer clearer title that reflected how much our project developed*
2. Team members: Roberto Barrón, Luis Paul Garay, Alonso Lozano and Daniel Murillo. 
3. Project description/outline: Code visualizations to better reflect the differences between different voter categories in the US, particularly regular voters vs. non-voters. <--- *Outline accomplished and surpassed*
4. Reearch question to answer: What are the differences between the profiles per type of voter (Rarely or never votes; Sometimes votes; and always votes). <--- *Question answered*
5. Dataset to be used: We have chosen a survey conducted by Ipsos and FiftyThirtyEight, a probability-based online panel that was recruited to be representative of the US. Link to GitHub: https://github.com/fivethirtyeight/data/tree/master/non-voters <--- *Dataset used*
6. Rough breakdown of tasks: <--- *Accurate*
a. Visual inspirations and dashboard sketch.
b. Data cleansing of the original dataset.
c. Database creation (SQL)
d. Creation of the API.
e. Dashboard coding (JavaScript)
f. User testing.
g. Presentation.

#### Project development and changes:
The original sketch was this one: ![image](https://github.com/loncho95/Non_voters_USA/blob/main/Resources/visual-inspirations/final-design-sketch.png)
We edited the layout while developing the dashboard due to two main reasons: one, aesthetics, and two, some charts were not as appropriate to be included or didn't give as rich of an information. We realized that we could not used a bubble chart because the x axis of all the questions we were interested in were either categorical variables or integers. Therefore, a bubble chart was not the way to go. We thought of replacing the bubble chart with bar charts, but we decided against it because the doughnut charts are more visually accessible and the user tends to get the data we wanted to portray quicker. We wanted to create a minimalist dashboard, but we definitely wanted to add more color and information. However, in general, time was not enough to add more information and improve the layout much more than we did, so, in that regard, we set the bar too high. On a similar note, we wanted to use the Chart.JS library to graph, but we ended up using different ones because we found it too hard to configure —*we suspect it had to do with the new version that came out not long ago*. Moreover, the visualizations of the sketch and the way of stacking the information was too inelegant and hard to understand initally. We think we improved a lot in that area once we finished out dashboard.

#### Creating a tailored API:

We used SQL, the SQLAlchemy ORM, [the Quick Database Diagrams (QuickDBD) app](https://www.quickdatabasediagrams.com/) Python, Pandas, Flask, and Flask-CORS to first, clean the data, then, build an Entity Relationship Diagram (ERD), a schema, and a local database, and last, create an API with personalized routes for each of the questions. At the end, 8 unique end routes were created (one to display the whole database, another one to include all the demographic data about the respondents, four to reestructure information from four of those nine questions, and a final one to locally run the dashboard with Flask-CORS. All our code is thoroughly commented, so that you understand what each piece is doing.

#### Charting:

We wanted to use the clearest and richest visualizations, and some questions, such as number 3 and 4, are so complex that considering a chart with only two axes would have led us to lose most of the valuable information. Therefore, we chose a [Plotly.JS](https://plotly.com/) treemap to represent the demographic questions, [Plotly.JS](https://plotly.com/) heatmaps to depict questions that had three axes, and [Google Charts](https://developers.google.com/chart) doughnut charts to graph easier to read information, which had at least one axis filled with string values.

#### Connecting the API to our charts = dashboarding:

We used JavaScript and HTML to create the interactive data visualizations mentioned in the previous paragraph. The API integrates Python for efficient data structuring, and restructures the data in a way that the end routes generate the desirable format of the JSONs. More importantly, we restructured the data so that we could compare the answers of three voter categories defined by the researchers of this survey: 'always' —also called *regular voters* in this project— voters or citizens who always vote, 'sporadic' voters or citizens who voted in at least two elections, but fewer than all-but-one, and 'rarely/never' voters —also called *non-voters* in this project— or those who voted in one or none of the elections in which they were eligible to vote. The dashboard lets the user easily filter the charts by those three categories. In order to create those filters, we used functions and [D3.JS](https://d3js.org/) to extract the voter categories and only the objects we needed, which were then turned into arrays to feed the charts. The HTML file was created with the help of [Bootstrap v5.3](https://getbootstrap.com/). Once again, all our code is thoroughly commented, so that you find it easy to understand and scale.

![image](https://github.com/loncho95/Non_voters_USA/blob/0c642638b9ccb17d8c223e4eece635b92e28e0bd/Resources/dashboard-images/dashboard-1.png)
![image](https://github.com/loncho95/Non_voters_USA/blob/0c642638b9ccb17d8c223e4eece635b92e28e0bd/Resources/dashboard-images/dashboard-2.png)
![image](https://github.com/loncho95/Non_voters_USA/blob/0c642638b9ccb17d8c223e4eece635b92e28e0bd/Resources/dashboard-images/dashboard-3.png)
![image](https://github.com/loncho95/Non_voters_USA/blob/0c642638b9ccb17d8c223e4eece635b92e28e0bd/Resources/dashboard-images/dashboard-4.png)
![image](https://github.com/loncho95/Non_voters_USA/blob/0c642638b9ccb17d8c223e4eece635b92e28e0bd/Resources/dashboard-images/dashboard-5.png)
![image](https://github.com/loncho95/Non_voters_USA/blob/0c642638b9ccb17d8c223e4eece635b92e28e0bd/Resources/dashboard-images/dashboard-6.png)


### Conclusions:

First of all, our dashboard is an efficient tool for visualizing key insights related to voter demographics. Second, the data outlines important trends that can inform future research and outreach efforts. The most important trends we found include a clear difference in education levels between regular voters and those who rarely or never vote. Specifically, regular voters have a higher proportion (46% vs. 29% of non-voters) of individuals with a college degree, while non-voters tend to have a higher proportion (44% vs. 23% of regular voters) of individuals with a high school education or less. There is a significant difference in income levels between those two groups: it seems that non-voters are more likely to be worse off than those who always vote. Furthermore, non-voters tend to have higher proportions of ethnic minorities than *always* voters, and there is no perceptible difference based on gender.
Moreover, some notable similarities in the views of different statements among non-voters were that they tend to view society as becoming too soft and femenine and that the media is more interested in money than communicating the truth. Non-voters also tend believe that politicians do not care about them, at least in a higher proportion than regular voters. Another trend is that non-voters tend to have a higher perception that elections and public or government institutions have little impact on their lives. This is a significant concern, as it highlights a potential lack of engagement, trust, and probably *inclusion* in the democratic process.
Finally, our dashboard strongly suggests a reason for not voting: a higher proportion of non-voters believe that, regardless of the election results, things will remain the same. This sentiment is less prevalent among regular voters.
A key takeaway of this project is that future analyses need to delve even more into more characteristics of non-voters, not only more qualitatively, but also they need to study the interaction between the democratic system and the citizens.

### The *Resources* folder:

It contains the dashboard images, the files used to clean the data, the full poll and our selected questions, the images that inspired our visualizations, and the original CSV file of the poll.

### The *app* folder:

It has the API we developed, a clean CSV with the data we used, and the HTML and JavaScript codes of our dashboard.

### The *database* folder:

It contains the physical ERD of our database and the schema.

### Final words:

We hope you, user, find our dashboard of good use because we know we have.

## Data Reference
Amelia Thomson-DeVeaux, Jasmine Mithani and Laura Bronner's *Why Many Americans Don't Vote*. Accessed on 07 May 2023 from [https://projects.fivethirtyeight.com/non-voters-poll-2020-election/](https://projects.fivethirtyeight.com/non-voters-poll-2020-election/)

The FiveThirtyEight dataset Github repository: [https://github.com/fivethirtyeight/data/tree/master/non-voters](https://github.com/fivethirtyeight/data/tree/master/non-voters)

```#Thank you for reading me!```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)



















