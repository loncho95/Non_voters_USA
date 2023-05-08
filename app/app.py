# Imported the dependencies needed:
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask_cors import CORS

# Imported Flask, jsonify, request, and render_template to create and run the API:
from flask import Flask, jsonify, request, render_template

# Set up the database:
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/project 3")

# Reflected the existing database into a new model:
Base = automap_base()

# Reflected the tables:
Base.prepare(autoload_with=engine)

Base.classes.keys()

# Saved the references to the main table:
Nonvoter = Base.classes.responses

# Created an app making sure to pass __name__:
app = Flask(__name__)
CORS(app)

# Flask routes (there are eight):

# 1. Main route:
# Defined the end point:
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"<h1>Welcome to the Non-voters USA API for <i>Project 3</i>!</h1><br/>"
        f"/api/index/ <- <i>This route leads to the main file of our dashboard: index.html</i><br/>"
        f"/api/nonvoters/ <- <i>This route has the complete JSON of our clean database</i><br/>"
        f"/api/q3/ <- <i>This route takes you to the JSON of question 3 (our first heatmap)</i><br/>"
        f"/api/q4/ <- <i>This route leads to the JSON of question 4 (our second heatmap)</i><br/>"
        f"/api/q5/ <- <i>This route has the JSON of question 5 (our bar chart)</i><br/>"
        f"/api/q30/ <- <i>This route gets you to the JSON of question 30 (our doughnut chart)</i><br/>"
        f"/api/treemap/ <- <i>This route leads to the JSON of the demographic questions that were graphed together as a treemap</i><br/>"
        )

# 2. JSON of our clean database:
# Created a Flask route to retrieve the data from the SQL database:
@app.route('/api/nonvoters/')

def get_nonvoters():
    session = Session(engine)
    results = session.query(Nonvoter).all()
    session.close()
    nonvoters = []
    for result in results:
        nonvoter_dict = {}
        nonvoter_dict['RespId'] = result.RespId
        nonvoter_dict['Q3_1'] = result.q3_1
        nonvoter_dict['Q3_3'] = result.q3_3
        nonvoter_dict['Q3_4'] = result.q3_4
        nonvoter_dict['Q3_5'] = result.q3_5
        nonvoter_dict['Q3_6'] = result.q3_6
        nonvoter_dict['Q4_1'] = result.q4_1
        nonvoter_dict['Q4_2'] = result.q4_2
        nonvoter_dict['Q4_3'] = result.q4_3
        nonvoter_dict['Q4_4'] = result.q4_4
        nonvoter_dict['Q4_5'] = result.q4_5
        nonvoter_dict['Q4_6'] = result.q4_6
        nonvoter_dict['Q5'] = result.q5
        nonvoter_dict['Q30'] = result.q30
        nonvoter_dict['ppage'] = result.pp_age
        nonvoter_dict['educ'] = result.educ
        nonvoter_dict['race'] = result.race
        nonvoter_dict['gender'] = result.gender
        nonvoter_dict['income_cat'] = result.income_cat
        nonvoter_dict['voter_category'] = result.voter_category
        nonvoters.append(nonvoter_dict)
    # Returned the JSON representation of the list of dictionaries:
    return jsonify(nonvoters)



# 3. JSON of question 3:
# Created a Flask route to retrieve the data for our first heatmap:
@app.route("/api/q3/")
def q3():
    main_df = pd.read_csv('nonvoters_data_clean.csv')

    q3_df = main_df[['RespId', 'Q3_1', 'Q3_2', 'Q3_3', 'Q3_4', 'Q3_5', 'Q3_6', 'voter_category']]

    always_q3_df = q3_df.loc[q3_df['voter_category'] == 1]
    sporadic_q3_df = q3_df.loc[q3_df['voter_category'] == 2]
    rarelynever_q3_df = q3_df.loc[q3_df['voter_category'] == 3]

    groupedby_always_q3_1_df = always_q3_df.groupby('Q3_1').count()
    groupedby_always_q3_2_df = always_q3_df.groupby('Q3_2').count()
    groupedby_always_q3_3_df = always_q3_df.groupby('Q3_3').count()
    groupedby_always_q3_4_df = always_q3_df.groupby('Q3_4').count()
    groupedby_always_q3_5_df = always_q3_df.groupby('Q3_5').count()
    groupedby_always_q3_6_df = always_q3_df.groupby('Q3_6').count()

    always_q3_1 = [round(100 * (x / groupedby_always_q3_1_df['RespId'].sum()), 2) for x in groupedby_always_q3_1_df['RespId']]
    always_q3_2 = [round(100 * (x / groupedby_always_q3_2_df['RespId'].sum()), 2) for x in groupedby_always_q3_2_df['RespId']]
    always_q3_3 = [round(100 * (x / groupedby_always_q3_3_df['RespId'].sum()), 2) for x in groupedby_always_q3_3_df['RespId']]
    always_q3_4 = [round(100 * (x / groupedby_always_q3_4_df['RespId'].sum()), 2) for x in groupedby_always_q3_4_df['RespId']]
    always_q3_5 = [round(100 * (x / groupedby_always_q3_5_df['RespId'].sum()), 2) for x in groupedby_always_q3_5_df['RespId']]
    always_q3_6 = [round(100 * (x / groupedby_always_q3_6_df['RespId'].sum()), 2) for x in groupedby_always_q3_6_df['RespId']]

    clean_always_q3_df = pd.DataFrame({
        'A': always_q3_1,
        'B': always_q3_2,
        'C': always_q3_3,
        'D': always_q3_4,
        'E': always_q3_5,
        'F': always_q3_6
    })

    clean_always_q3_df.index = clean_always_q3_df.index + 1
    clean_always_q3_df = clean_always_q3_df.T
    clean_always_q3_df = clean_always_q3_df.reset_index()
    clean_always_q3_df = clean_always_q3_df.rename(columns={'index': 'q3_group'})
    melted_clean_always_q3_df = clean_always_q3_df.melt(id_vars=['q3_group'])
    melted_clean_always_q3_df = melted_clean_always_q3_df.sort_values(by=['q3_group', 'variable'], ascending=[False, True])
    melted_clean_always_q3_df = melted_clean_always_q3_df.reset_index(drop=True)

    melted_clean_always_q3_dict = melted_clean_always_q3_df.to_dict()
    melted_clean_always_q3_dict['voter_category'] = 'always'

    groupedby_sporadic_q3_1_df = sporadic_q3_df.groupby('Q3_1').count()
    groupedby_sporadic_q3_2_df = sporadic_q3_df.groupby('Q3_2').count()
    groupedby_sporadic_q3_3_df = sporadic_q3_df.groupby('Q3_3').count()
    groupedby_sporadic_q3_4_df = sporadic_q3_df.groupby('Q3_4').count()
    groupedby_sporadic_q3_5_df = sporadic_q3_df.groupby('Q3_5').count()
    groupedby_sporadic_q3_6_df = sporadic_q3_df.groupby('Q3_6').count()

    sporadic_q3_1 = [round(100 * (x / groupedby_sporadic_q3_1_df['RespId'].sum()), 2) for x in groupedby_sporadic_q3_1_df['RespId']]
    sporadic_q3_2 = [round(100 * (x / groupedby_sporadic_q3_2_df['RespId'].sum()), 2) for x in groupedby_sporadic_q3_2_df['RespId']]
    sporadic_q3_3 = [round(100 * (x / groupedby_sporadic_q3_3_df['RespId'].sum()), 2) for x in groupedby_sporadic_q3_3_df['RespId']]
    sporadic_q3_4 = [round(100 * (x / groupedby_sporadic_q3_4_df['RespId'].sum()), 2) for x in groupedby_sporadic_q3_4_df['RespId']]
    sporadic_q3_5 = [round(100 * (x / groupedby_sporadic_q3_5_df['RespId'].sum()), 2) for x in groupedby_sporadic_q3_5_df['RespId']]
    sporadic_q3_6 = [round(100 * (x / groupedby_sporadic_q3_6_df['RespId'].sum()), 2) for x in groupedby_sporadic_q3_6_df['RespId']]

    clean_sporadic_q3_df = pd.DataFrame({
        'A': sporadic_q3_1,
        'B': sporadic_q3_2,
        'C': sporadic_q3_3,
        'D': sporadic_q3_4,
        'E': sporadic_q3_5,
        'F': sporadic_q3_6
    })

    clean_sporadic_q3_df.index = clean_sporadic_q3_df.index + 1
    clean_sporadic_q3_df = clean_sporadic_q3_df.T
    clean_sporadic_q3_df = clean_sporadic_q3_df.reset_index()
    clean_sporadic_q3_df = clean_sporadic_q3_df.rename(columns={'index': 'q3_group'})
    melted_clean_sporadic_q3_df = clean_sporadic_q3_df.melt(id_vars=['q3_group'])
    melted_clean_sporadic_q3_df = melted_clean_sporadic_q3_df.sort_values(by=['q3_group', 'variable'], ascending=[False, True])
    melted_clean_sporadic_q3_df = melted_clean_sporadic_q3_df.reset_index(drop=True)

    melted_clean_sporadic_q3_dict = melted_clean_sporadic_q3_df.to_dict()
    melted_clean_sporadic_q3_dict['voter_category'] = 'sporadic'


    groupedby_rarelynever_q3_1_df = rarelynever_q3_df.groupby('Q3_1').count()
    groupedby_rarelynever_q3_2_df = rarelynever_q3_df.groupby('Q3_2').count()
    groupedby_rarelynever_q3_3_df = rarelynever_q3_df.groupby('Q3_3').count()
    groupedby_rarelynever_q3_4_df = rarelynever_q3_df.groupby('Q3_4').count()
    groupedby_rarelynever_q3_5_df = rarelynever_q3_df.groupby('Q3_5').count()
    groupedby_rarelynever_q3_6_df = rarelynever_q3_df.groupby('Q3_6').count()

    rarelynever_q3_1 = [round(100 * (x / groupedby_rarelynever_q3_1_df['RespId'].sum()), 2) for x in groupedby_rarelynever_q3_1_df['RespId']]
    rarelynever_q3_2 = [round(100 * (x / groupedby_rarelynever_q3_2_df['RespId'].sum()), 2) for x in groupedby_rarelynever_q3_2_df['RespId']]
    rarelynever_q3_3 = [round(100 * (x / groupedby_rarelynever_q3_3_df['RespId'].sum()), 2) for x in groupedby_rarelynever_q3_3_df['RespId']]
    rarelynever_q3_4 = [round(100 * (x / groupedby_rarelynever_q3_4_df['RespId'].sum()), 2) for x in groupedby_rarelynever_q3_4_df['RespId']]
    rarelynever_q3_5 = [round(100 * (x / groupedby_rarelynever_q3_5_df['RespId'].sum()), 2) for x in groupedby_rarelynever_q3_5_df['RespId']]
    rarelynever_q3_6 = [round(100 * (x / groupedby_rarelynever_q3_6_df['RespId'].sum()), 2) for x in groupedby_rarelynever_q3_6_df['RespId']]

    clean_rarelynever_q3_df = pd.DataFrame({
        'A': rarelynever_q3_1,
        'B': rarelynever_q3_2,
        'C': rarelynever_q3_3,
        'D': rarelynever_q3_4,
        'E': rarelynever_q3_5,
        'F': rarelynever_q3_6
    })

    clean_rarelynever_q3_df.index = clean_rarelynever_q3_df.index + 1
    clean_rarelynever_q3_df = clean_rarelynever_q3_df.T
    clean_rarelynever_q3_df = clean_rarelynever_q3_df.reset_index()
    clean_rarelynever_q3_df = clean_rarelynever_q3_df.rename(columns={'index': 'q3_group'})
    melted_clean_rarelynever_q3_df = clean_rarelynever_q3_df.melt(id_vars=['q3_group'])
    melted_clean_rarelynever_q3_df = melted_clean_rarelynever_q3_df.sort_values(by=['q3_group', 'variable'], ascending=[False, True])
    melted_clean_rarelynever_q3_df = melted_clean_rarelynever_q3_df.reset_index(drop=True)

    melted_clean_rarelynever_q3_dict = melted_clean_rarelynever_q3_df.to_dict()
    melted_clean_rarelynever_q3_dict['voter_category'] = 'rarely/never'

    final_q3_dict = {'categories': ['always', 'sporadic', 'rarely/never'],
                     'q3': [melted_clean_always_q3_dict,
                            melted_clean_sporadic_q3_dict,
                            melted_clean_rarelynever_q3_dict]}
    
    return final_q3_dict



# 4. JSON of question 4:
# Created a Flask route to retrieve the data for our second heatmap:
@app.route("/api/q4/")
def q4():
    main_df = pd.read_csv('nonvoters_data_clean.csv')

    q4_df = main_df[['RespId', 'Q4_1', 'Q4_2', 'Q4_3', 'Q4_4', 'Q4_5', 'Q4_6', 'voter_category']]

    always_q4_df = q4_df.loc[q4_df['voter_category'] == 1]
    sporadic_q4_df = q4_df.loc[q4_df['voter_category'] == 2]
    rarelynever_q4_df = q4_df.loc[q4_df['voter_category'] == 3]

    groupedby_always_q4_1_df = always_q4_df.groupby('Q4_1').count()
    groupedby_always_q4_2_df = always_q4_df.groupby('Q4_2').count()
    groupedby_always_q4_3_df = always_q4_df.groupby('Q4_3').count()
    groupedby_always_q4_4_df = always_q4_df.groupby('Q4_4').count()
    groupedby_always_q4_5_df = always_q4_df.groupby('Q4_5').count()
    groupedby_always_q4_6_df = always_q4_df.groupby('Q4_6').count()

    always_q4_1 = [round(100 * (x / groupedby_always_q4_1_df['RespId'].sum()), 2) for x in groupedby_always_q4_1_df['RespId']]
    always_q4_2 = [round(100 * (x / groupedby_always_q4_2_df['RespId'].sum()), 2) for x in groupedby_always_q4_2_df['RespId']]
    always_q4_3 = [round(100 * (x / groupedby_always_q4_3_df['RespId'].sum()), 2) for x in groupedby_always_q4_3_df['RespId']]
    always_q4_4 = [round(100 * (x / groupedby_always_q4_4_df['RespId'].sum()), 2) for x in groupedby_always_q4_4_df['RespId']]
    always_q4_5 = [round(100 * (x / groupedby_always_q4_5_df['RespId'].sum()), 2) for x in groupedby_always_q4_5_df['RespId']]
    always_q4_6 = [round(100 * (x / groupedby_always_q4_6_df['RespId'].sum()), 2) for x in groupedby_always_q4_6_df['RespId']]

    clean_always_q4_df = pd.DataFrame({
        'A': always_q4_1,
        'B': always_q4_2,
        'C': always_q4_3,
        'D': always_q4_4,
        'E': always_q4_5,
        'F': always_q4_6
    })

    clean_always_q4_df.index = clean_always_q4_df.index + 1
    clean_always_q4_df = clean_always_q4_df.T
    clean_always_q4_df = clean_always_q4_df.reset_index()
    clean_always_q4_df = clean_always_q4_df.rename(columns={'index': 'q4_group'})
    melted_clean_always_q4_df = clean_always_q4_df.melt(id_vars=['q4_group'])
    melted_clean_always_q4_df = melted_clean_always_q4_df.sort_values(by=['q4_group', 'variable'], ascending=[False, True])
    melted_clean_always_q4_df = melted_clean_always_q4_df.reset_index(drop=True)

    melted_clean_always_q4_dict = melted_clean_always_q4_df.to_dict()
    melted_clean_always_q4_dict['voter_category'] = 'always'

    groupedby_sporadic_q4_1_df = sporadic_q4_df.groupby('Q4_1').count()
    groupedby_sporadic_q4_2_df = sporadic_q4_df.groupby('Q4_2').count()
    groupedby_sporadic_q4_3_df = sporadic_q4_df.groupby('Q4_3').count()
    groupedby_sporadic_q4_4_df = sporadic_q4_df.groupby('Q4_4').count()
    groupedby_sporadic_q4_5_df = sporadic_q4_df.groupby('Q4_5').count()
    groupedby_sporadic_q4_6_df = sporadic_q4_df.groupby('Q4_6').count()

    sporadic_q4_1 = [round(100 * (x / groupedby_sporadic_q4_1_df['RespId'].sum()), 2) for x in groupedby_sporadic_q4_1_df['RespId']]
    sporadic_q4_2 = [round(100 * (x / groupedby_sporadic_q4_2_df['RespId'].sum()), 2) for x in groupedby_sporadic_q4_2_df['RespId']]
    sporadic_q4_3 = [round(100 * (x / groupedby_sporadic_q4_3_df['RespId'].sum()), 2) for x in groupedby_sporadic_q4_3_df['RespId']]
    sporadic_q4_4 = [round(100 * (x / groupedby_sporadic_q4_4_df['RespId'].sum()), 2) for x in groupedby_sporadic_q4_4_df['RespId']]
    sporadic_q4_5 = [round(100 * (x / groupedby_sporadic_q4_5_df['RespId'].sum()), 2) for x in groupedby_sporadic_q4_5_df['RespId']]
    sporadic_q4_6 = [round(100 * (x / groupedby_sporadic_q4_6_df['RespId'].sum()), 2) for x in groupedby_sporadic_q4_6_df['RespId']]

    clean_sporadic_q4_df = pd.DataFrame({
        'A': sporadic_q4_1,
        'B': sporadic_q4_2,
        'C': sporadic_q4_3,
        'D': sporadic_q4_4,
        'E': sporadic_q4_5,
        'F': sporadic_q4_6
    })

    clean_sporadic_q4_df.index = clean_sporadic_q4_df.index + 1
    clean_sporadic_q4_df = clean_sporadic_q4_df.T
    clean_sporadic_q4_df = clean_sporadic_q4_df.reset_index()
    clean_sporadic_q4_df = clean_sporadic_q4_df.rename(columns={'index': 'q4_group'})
    melted_clean_sporadic_q4_df = clean_sporadic_q4_df.melt(id_vars=['q4_group'])
    melted_clean_sporadic_q4_df = melted_clean_sporadic_q4_df.sort_values(by=['q4_group', 'variable'], ascending=[False, True])
    melted_clean_sporadic_q4_df = melted_clean_sporadic_q4_df.reset_index(drop=True)

    melted_clean_sporadic_q4_dict = melted_clean_sporadic_q4_df.to_dict()
    melted_clean_sporadic_q4_dict['voter_category'] = 'sporadic'


    groupedby_rarelynever_q4_1_df = rarelynever_q4_df.groupby('Q4_1').count()
    groupedby_rarelynever_q4_2_df = rarelynever_q4_df.groupby('Q4_2').count()
    groupedby_rarelynever_q4_3_df = rarelynever_q4_df.groupby('Q4_3').count()
    groupedby_rarelynever_q4_4_df = rarelynever_q4_df.groupby('Q4_4').count()
    groupedby_rarelynever_q4_5_df = rarelynever_q4_df.groupby('Q4_5').count()
    groupedby_rarelynever_q4_6_df = rarelynever_q4_df.groupby('Q4_6').count()

    rarelynever_q4_1 = [round(100 * (x / groupedby_rarelynever_q4_1_df['RespId'].sum()), 2) for x in groupedby_rarelynever_q4_1_df['RespId']]
    rarelynever_q4_2 = [round(100 * (x / groupedby_rarelynever_q4_2_df['RespId'].sum()), 2) for x in groupedby_rarelynever_q4_2_df['RespId']]
    rarelynever_q4_3 = [round(100 * (x / groupedby_rarelynever_q4_3_df['RespId'].sum()), 2) for x in groupedby_rarelynever_q4_3_df['RespId']]
    rarelynever_q4_4 = [round(100 * (x / groupedby_rarelynever_q4_4_df['RespId'].sum()), 2) for x in groupedby_rarelynever_q4_4_df['RespId']]
    rarelynever_q4_5 = [round(100 * (x / groupedby_rarelynever_q4_5_df['RespId'].sum()), 2) for x in groupedby_rarelynever_q4_5_df['RespId']]
    rarelynever_q4_6 = [round(100 * (x / groupedby_rarelynever_q4_6_df['RespId'].sum()), 2) for x in groupedby_rarelynever_q4_6_df['RespId']]

    clean_rarelynever_q4_df = pd.DataFrame({
        'A': rarelynever_q4_1,
        'B': rarelynever_q4_2,
        'C': rarelynever_q4_3,
        'D': rarelynever_q4_4,
        'E': rarelynever_q4_5,
        'F': rarelynever_q4_6
    })

    clean_rarelynever_q4_df.index = clean_rarelynever_q4_df.index + 1
    clean_rarelynever_q4_df = clean_rarelynever_q4_df.T
    clean_rarelynever_q4_df = clean_rarelynever_q4_df.reset_index()
    clean_rarelynever_q4_df = clean_rarelynever_q4_df.rename(columns={'index': 'q4_group'})
    melted_clean_rarelynever_q4_df = clean_rarelynever_q4_df.melt(id_vars=['q4_group'])
    melted_clean_rarelynever_q4_df = melted_clean_rarelynever_q4_df.sort_values(by=['q4_group', 'variable'], ascending=[False, True])
    melted_clean_rarelynever_q4_df = melted_clean_rarelynever_q4_df.reset_index(drop=True)

    melted_clean_rarelynever_q4_dict = melted_clean_rarelynever_q4_df.to_dict()
    melted_clean_rarelynever_q4_dict['voter_category'] = 'rarely/never'

    final_q4_dict = {'categories': ['always', 'sporadic', 'rarely/never'],
                     'q4': [melted_clean_always_q4_dict,
                            melted_clean_sporadic_q4_dict,
                            melted_clean_rarelynever_q4_dict]}
    
    return final_q4_dict



# 5. JSON of question 5:
# Created a Flask route to retrieve the data for our bar chart:
@app.route('/api/q5/')
def q5():

    # Imported the data:
    main_df = pd.read_csv('nonvoters_data_clean.csv')

    # Created a new DataFrame by filtering only the columns relevant to question 5:
    q5_df = main_df[['Q5', 'voter_category']]

    # Created new DataFrames, one for each voter category by filtering the data of question 5:
    always_q5_df = q5_df.loc[q5_df['voter_category'] == 1]
    sporadic_q5_df = q5_df.loc[q5_df['voter_category'] == 2]
    rarelynever_q5_df = q5_df.loc[q5_df['voter_category'] == 3]

    # Generated a sorted question 5 DataFrame for the 'ALWAYS' voter category:
    counted_always_q5_1_df = always_q5_df.loc[always_q5_df['Q5'] == 1].count()
    counted_always_q5_2_df = always_q5_df.loc[always_q5_df['Q5'] == 2].count()

    always_q5_1 = round(100 * (counted_always_q5_1_df['Q5'] / always_q5_df['Q5'].count()), 2)
    always_q5_2 = round(100 * (counted_always_q5_2_df['Q5'] / always_q5_df['Q5'].count()), 2)

    clean_always_q5_dict = {
        'Who wins the election really matters': always_q5_1,
        'Things will pretty much be the same': always_q5_2
    }

    clean_always_q5_df = pd.DataFrame(clean_always_q5_dict.items(), columns=['q5_options', 'values'])
    clean_always_q5_dict = clean_always_q5_df.to_dict()
    clean_always_q5_dict['voter_category'] = 'always'
    clean_always_q5_dict

    # Generated a sorted question 5 DataFrame for the 'SPORADIC' voter category:
    counted_sporadic_q5_1_df = sporadic_q5_df.loc[sporadic_q5_df['Q5'] == 1].count()
    counted_sporadic_q5_2_df = sporadic_q5_df.loc[sporadic_q5_df['Q5'] == 2].count()

    sporadic_q5_1 = round(100 * (counted_sporadic_q5_1_df['Q5'] / sporadic_q5_df['Q5'].count()), 2)
    sporadic_q5_2 = round(100 * (counted_sporadic_q5_2_df['Q5'] / sporadic_q5_df['Q5'].count()), 2)

    clean_sporadic_q5_dict = {
        'Who wins the election really matters': sporadic_q5_1,
        'Things will pretty much be the same': sporadic_q5_2
    }

    clean_sporadic_q5_df = pd.DataFrame(clean_sporadic_q5_dict.items(), columns=['q5_options', 'values'])
    clean_sporadic_q5_dict = clean_sporadic_q5_df.to_dict()
    clean_sporadic_q5_dict['voter_category'] = 'sporadic'
    clean_sporadic_q5_dict

    # Generated a sorted question 5 DataFrame for the 'RARELY/NEVER' voter category:
    counted_rarelynever_q5_1_df = rarelynever_q5_df.loc[rarelynever_q5_df['Q5'] == 1].count()
    counted_rarelynever_q5_2_df = rarelynever_q5_df.loc[rarelynever_q5_df['Q5'] == 2].count()

    rarelynever_q5_1 = round(100 * (counted_rarelynever_q5_1_df['Q5'] / rarelynever_q5_df['Q5'].count()), 2)
    rarelynever_q5_2 = round(100 * (counted_rarelynever_q5_2_df['Q5'] / rarelynever_q5_df['Q5'].count()), 2)

    clean_rarelynever_q5_dict = {
        'Who wins the election really matters': rarelynever_q5_1,
        'Things will pretty much be the same': rarelynever_q5_2
    }

    clean_rarelynever_q5_df = pd.DataFrame(clean_rarelynever_q5_dict.items(), columns=['q5_options', 'values'])
    clean_rarelynever_q5_dict = clean_rarelynever_q5_df.to_dict()
    clean_rarelynever_q5_dict['voter_category'] = 'rarely/never'
    clean_rarelynever_q5_dict

    final_q5_dict = {'categories': ['always', 'sporadic', 'rarely/never'],
                        'q5': [clean_always_q5_dict,
                                clean_sporadic_q5_dict,
                                clean_rarelynever_q5_dict]}
        
    return final_q5_dict



# 6. JSON of question 30:
# Created a Flask route to retrieve the data for the doughtnut chart:
@app.route('/api/q30/')
def q30():

    # Imported the data:
    main_df = pd.read_csv('nonvoters_data_clean.csv')

    # Created a new DataFrame by filtering only the columns relevant to question 30:
    q30_df = main_df[['Q30', 'voter_category']]

    # Created new DataFrames, one for each voter category by filtering the data of question 30:
    always_q30_df = q30_df.loc[q30_df['voter_category'] == 1]
    sporadic_q30_df = q30_df.loc[q30_df['voter_category'] == 2]
    rarelynever_q30_df = q30_df.loc[q30_df['voter_category'] == 3]

    # Generated a sorted question 30 DataFrame for the 'ALWAYS' voter category:
    counted_always_q30_1_df = always_q30_df.loc[always_q30_df['Q30'] == 1].count()
    counted_always_q30_2_df = always_q30_df.loc[always_q30_df['Q30'] == 2].count()
    counted_always_q30_3_df = always_q30_df.loc[always_q30_df['Q30'] == 3].count()
    counted_always_q30_4_df = always_q30_df.loc[always_q30_df['Q30'] == 4].count()
    counted_always_q30_5_df = always_q30_df.loc[always_q30_df['Q30'] == 5].count()

    always_q30_1 = round(100 * (counted_always_q30_1_df['Q30'] / always_q30_df['Q30'].count()), 2)
    always_q30_2 = round(100 * (counted_always_q30_2_df['Q30'] / always_q30_df['Q30'].count()), 2)
    always_q30_3 = round(100 * (counted_always_q30_3_df['Q30'] / always_q30_df['Q30'].count()), 2)
    always_q30_4 = round(100 * (counted_always_q30_4_df['Q30'] / always_q30_df['Q30'].count()), 2)
    always_q30_5 = round(100 * (counted_always_q30_5_df['Q30'] / always_q30_df['Q30'].count()), 2)

    clean_always_q30_dict = {
        'Republican': always_q30_1,
        'Democrat': always_q30_2,
        'Independent': always_q30_3,
        'Another party': always_q30_4,
        'No preference': always_q30_5
    }

    clean_always_q30_df = pd.DataFrame(clean_always_q30_dict.items(), columns=['q30_options', 'values'])
    clean_always_q30_dict = clean_always_q30_df.to_dict()
    clean_always_q30_dict['voter_category'] = 'always'
    clean_always_q30_dict

    # Generated a sorted question 30 DataFrame for the 'SPORADIC' voter category:
    counted_sporadic_q30_1_df = sporadic_q30_df.loc[sporadic_q30_df['Q30'] == 1].count()
    counted_sporadic_q30_2_df = sporadic_q30_df.loc[sporadic_q30_df['Q30'] == 2].count()
    counted_sporadic_q30_3_df = sporadic_q30_df.loc[sporadic_q30_df['Q30'] == 3].count()
    counted_sporadic_q30_4_df = sporadic_q30_df.loc[sporadic_q30_df['Q30'] == 4].count()
    counted_sporadic_q30_5_df = sporadic_q30_df.loc[sporadic_q30_df['Q30'] == 5].count()

    sporadic_q30_1 = round(100 * (counted_sporadic_q30_1_df['Q30'] / sporadic_q30_df['Q30'].count()), 2)
    sporadic_q30_2 = round(100 * (counted_sporadic_q30_2_df['Q30'] / sporadic_q30_df['Q30'].count()), 2)
    sporadic_q30_3 = round(100 * (counted_sporadic_q30_3_df['Q30'] / sporadic_q30_df['Q30'].count()), 2)
    sporadic_q30_4 = round(100 * (counted_sporadic_q30_4_df['Q30'] / sporadic_q30_df['Q30'].count()), 2)
    sporadic_q30_5 = round(100 * (counted_sporadic_q30_5_df['Q30'] / sporadic_q30_df['Q30'].count()), 2)

    clean_sporadic_q30_dict = {
        'Republican': sporadic_q30_1,
        'Democrat': sporadic_q30_2,
        'Independent': sporadic_q30_3,
        'Another party': sporadic_q30_4,
        'No preference': sporadic_q30_5
    }

    clean_sporadic_q30_df = pd.DataFrame(clean_sporadic_q30_dict.items(), columns=['q30_options', 'values'])
    clean_sporadic_q30_dict = clean_sporadic_q30_df.to_dict()
    clean_sporadic_q30_dict['voter_category'] = 'sporadic'
    clean_sporadic_q30_dict

    # Generated a sorted question 30 DataFrame for the 'RARELY/NEVER' voter category:
    counted_rarelynever_q30_1_df = rarelynever_q30_df.loc[rarelynever_q30_df['Q30'] == 1].count()
    counted_rarelynever_q30_2_df = rarelynever_q30_df.loc[rarelynever_q30_df['Q30'] == 2].count()
    counted_rarelynever_q30_3_df = rarelynever_q30_df.loc[rarelynever_q30_df['Q30'] == 3].count()
    counted_rarelynever_q30_4_df = rarelynever_q30_df.loc[rarelynever_q30_df['Q30'] == 4].count()
    counted_rarelynever_q30_5_df = rarelynever_q30_df.loc[rarelynever_q30_df['Q30'] == 5].count()

    rarelynever_q30_1 = round(100 * (counted_rarelynever_q30_1_df['Q30'] / rarelynever_q30_df['Q30'].count()), 2)
    rarelynever_q30_2 = round(100 * (counted_rarelynever_q30_2_df['Q30'] / rarelynever_q30_df['Q30'].count()), 2)
    rarelynever_q30_3 = round(100 * (counted_rarelynever_q30_3_df['Q30'] / rarelynever_q30_df['Q30'].count()), 2)
    rarelynever_q30_4 = round(100 * (counted_rarelynever_q30_4_df['Q30'] / rarelynever_q30_df['Q30'].count()), 2)
    rarelynever_q30_5 = round(100 * (counted_rarelynever_q30_5_df['Q30'] / rarelynever_q30_df['Q30'].count()), 2)

    clean_rarelynever_q30_dict = {
        'Republican': rarelynever_q30_1,
        'Democrat': rarelynever_q30_2,
        'Independent': rarelynever_q30_3,
        'Another party': rarelynever_q30_4,
        'No preference': rarelynever_q30_5
    }

    clean_rarelynever_q30_df = pd.DataFrame(clean_rarelynever_q30_dict.items(), columns=['q30_options', 'values'])
    clean_rarelynever_q30_dict = clean_rarelynever_q30_df.to_dict()
    clean_rarelynever_q30_dict['voter_category'] = 'rarely/never'
    clean_rarelynever_q30_dict

    final_q30_dict = {'categories': ['always', 'sporadic', 'rarely/never'],
                        'q30': [clean_always_q30_dict,
                                clean_sporadic_q30_dict,
                                clean_rarelynever_q30_dict]}
        
    return final_q30_dict



# 7. JSON of the demographic questions:
# Created Flask route to retrieve data for the treemap:
@app.route('/api/treemap/')
def treemap():

    # Imported the data:
    main_df = pd.read_csv('nonvoters_data_clean.csv')

    # Created a new DataFrame by filtering only the columns relevant to the treemap:
    treemap_df = main_df[['educ', 'race', 'gender', 'income_cat', 'voter_category']]

    # Created new DataFrames, one for each voter category by filtering the data for the treemap:
    always_treemap_df = treemap_df.loc[treemap_df['voter_category'] == 1]
    sporadic_treemap_df = treemap_df.loc[treemap_df['voter_category'] == 2]
    rarelynever_treemap_df = treemap_df.loc[treemap_df['voter_category'] == 3]

    # Created the parent dictionaries, for all the voter categories, that were converted into DataFrames:
    parent_dict = {'labels': 'Voter',
        'values': 400,
        'parents': ''}
    parent_df = pd.DataFrame(parent_dict.items())
    parent_df = parent_df.set_index(0)
    parent_df = parent_df.T

    gender_for_parent_dict = {'labels': 'Gender',
        'values': 100,
        'parents': 'Voter'}
    gender_for_parent_df = pd.DataFrame(gender_for_parent_dict.items())
    gender_for_parent_df = gender_for_parent_df.set_index(0)
    gender_for_parent_df = gender_for_parent_df.T

    race_for_parent_dict = {'labels': 'Race',
        'values': 100,
        'parents': 'Voter'}
    race_for_parent_df = pd.DataFrame(race_for_parent_dict.items())
    race_for_parent_df = race_for_parent_df.set_index(0)
    race_for_parent_df = race_for_parent_df.T

    educ_for_parent_dict = {'labels': 'Education level',
        'values': 100,
        'parents': 'Voter'}
    educ_for_parent_df = pd.DataFrame(educ_for_parent_dict.items())
    educ_for_parent_df = educ_for_parent_df.set_index(0)
    educ_for_parent_df = educ_for_parent_df.T

    income_cat_for_parent_dict = {'labels': 'Household income',
        'values': 100,
        'parents': 'Voter'}
    income_cat_for_parent_df = pd.DataFrame(income_cat_for_parent_dict.items())
    income_cat_for_parent_df = income_cat_for_parent_df.set_index(0)
    income_cat_for_parent_df = income_cat_for_parent_df.T

    # 'ALWAYS' category:

    # EDUC:
    # For the heatmap, generated a sorted treemap dictionary for the 'ALWAYS' voter category:
    counted_always_treemap_educ_1_df = always_treemap_df.loc[always_treemap_df['educ'] == 1].count()
    counted_always_treemap_educ_2_df = always_treemap_df.loc[always_treemap_df['educ'] == 2].count()
    counted_always_treemap_educ_3_df = always_treemap_df.loc[always_treemap_df['educ'] == 3].count()

    always_treemap_educ_1 = round(100 * (counted_always_treemap_educ_1_df['educ'] / always_treemap_df['educ'].count()), 0)
    always_treemap_educ_2 = round(100 * (counted_always_treemap_educ_2_df['educ'] / always_treemap_df['educ'].count()), 0)
    always_treemap_educ_3 = round(100 * (counted_always_treemap_educ_3_df['educ'] / always_treemap_df['educ'].count()), 0)

    clean_always_treemap_educ_dict = {
        'College': int(always_treemap_educ_1),
        'High school or less': int(always_treemap_educ_2),
        'Some college': int(always_treemap_educ_3)
    }

    clean_always_treemap_educ_df = pd.DataFrame(clean_always_treemap_educ_dict.items(), columns=['labels', 'values'])
    clean_always_treemap_educ_df['parents'] = 'Education level'

    # RACE:
    # For the heatmap, generated a sorted treemap dictionary for the 'ALWAYS' voter category:
    counted_always_treemap_race_1_df = always_treemap_df.loc[always_treemap_df['race'] == 1].count()
    counted_always_treemap_race_2_df = always_treemap_df.loc[always_treemap_df['race'] == 2].count()
    counted_always_treemap_race_3_df = always_treemap_df.loc[always_treemap_df['race'] == 3].count()
    counted_always_treemap_race_4_df = always_treemap_df.loc[always_treemap_df['race'] == 4].count()

    always_treemap_race_1 = round(100 * (counted_always_treemap_race_1_df['race'] / always_treemap_df['race'].count()), 0)
    always_treemap_race_2 = round(100 * (counted_always_treemap_race_2_df['race'] / always_treemap_df['race'].count()), 0)
    always_treemap_race_3 = round(100 * (counted_always_treemap_race_3_df['race'] / always_treemap_df['race'].count()), 0)
    always_treemap_race_4 = round(100 * (counted_always_treemap_race_4_df['race'] / always_treemap_df['race'].count()), 0)

    clean_always_treemap_race_dict = {
        'Black': int(always_treemap_race_1),
        'Hispanic': int(always_treemap_race_2),
        'Other/Mixed': int(always_treemap_race_3),
        'White': int(always_treemap_race_4)
    }

    clean_always_treemap_race_df = pd.DataFrame(clean_always_treemap_race_dict.items(), columns=['labels', 'values'])
    clean_always_treemap_race_df['parents'] = 'Race'

    # GENDER:
    # For the heatmap, generated a sorted treemap dictionary for the 'ALWAYS' voter category:
    counted_always_treemap_gender_1_df = always_treemap_df.loc[always_treemap_df['gender'] == 1].count()
    counted_always_treemap_gender_2_df = always_treemap_df.loc[always_treemap_df['gender'] == 2].count()

    always_treemap_gender_1 = round(100 * (counted_always_treemap_gender_1_df['gender'] / always_treemap_df['gender'].count()), 0)
    always_treemap_gender_2 = round(100 * (counted_always_treemap_gender_2_df['gender'] / always_treemap_df['gender'].count()), 0)

    clean_always_treemap_gender_dict = {
        'Female': int(always_treemap_gender_1),
        'Male': int(always_treemap_gender_2)
    }

    clean_always_treemap_gender_df = pd.DataFrame(clean_always_treemap_gender_dict.items(), columns=['labels', 'values'])
    clean_always_treemap_gender_df['parents'] = 'Gender'

    # INCOME_CAT:
    # For the heatmap, generated a sorted treemap dictionary for the 'ALWAYS' voter category:
    counted_always_treemap_income_cat_1_df = always_treemap_df.loc[always_treemap_df['income_cat'] == 1].count()
    counted_always_treemap_income_cat_2_df = always_treemap_df.loc[always_treemap_df['income_cat'] == 2].count()
    counted_always_treemap_income_cat_3_df = always_treemap_df.loc[always_treemap_df['income_cat'] == 3].count()
    counted_always_treemap_income_cat_4_df = always_treemap_df.loc[always_treemap_df['income_cat'] == 4].count()

    always_treemap_income_cat_1 = round(100 * (counted_always_treemap_income_cat_1_df['income_cat'] / always_treemap_df['income_cat'].count()), 0)
    always_treemap_income_cat_2 = round(100 * (counted_always_treemap_income_cat_2_df['income_cat'] / always_treemap_df['income_cat'].count()), 0)
    always_treemap_income_cat_3 = round(100 * (counted_always_treemap_income_cat_3_df['income_cat'] / always_treemap_df['income_cat'].count()), 0)
    always_treemap_income_cat_4 = (100 * (counted_always_treemap_income_cat_4_df['income_cat'] / always_treemap_df['income_cat'].count()))

    clean_always_treemap_income_cat_dict = {
        'Less than $40k': int(always_treemap_income_cat_1),
        '$40-75k': int(always_treemap_income_cat_2),
        '$75-125k': int(always_treemap_income_cat_3),
        '$125k or more': int(always_treemap_income_cat_4)
    }

    clean_always_treemap_income_cat_df = pd.DataFrame(clean_always_treemap_income_cat_dict.items(), columns=['labels', 'values'])
    clean_always_treemap_income_cat_df['parents'] = 'Household income'

    # Created a list of all the 'always' category DataFrames, concatenated them, and reset the index:
    final_clean_always_treemap_list = [parent_df,
                                    gender_for_parent_df,
                                    clean_always_treemap_gender_df,
                                    race_for_parent_df,
                                    clean_always_treemap_race_df,
                                    educ_for_parent_df,
                                    clean_always_treemap_educ_df,
                                    income_cat_for_parent_df,
                                    clean_always_treemap_income_cat_df]

    final_clean_always_treemap_df = pd.concat(final_clean_always_treemap_list)
    final_clean_always_treemap_df = final_clean_always_treemap_df.reset_index(drop=True)

    # Converted the concatenated DataFrame into a dictionary and added the key 'voter_category' and value 'always':
    final_clean_always_treemap_dict = final_clean_always_treemap_df.to_dict()
    final_clean_always_treemap_dict['voter_category'] = 'always'


    # 'SPORADIC' category:

    # EDUC:
    # For the heatmap, generated a sorted treemap dictionary for the 'SPORADIC' voter category:
    counted_sporadic_treemap_educ_1_df = sporadic_treemap_df.loc[sporadic_treemap_df['educ'] == 1].count()
    counted_sporadic_treemap_educ_2_df = sporadic_treemap_df.loc[sporadic_treemap_df['educ'] == 2].count()
    counted_sporadic_treemap_educ_3_df = sporadic_treemap_df.loc[sporadic_treemap_df['educ'] == 3].count()

    sporadic_treemap_educ_1 = round(100 * (counted_sporadic_treemap_educ_1_df['educ'] / sporadic_treemap_df['educ'].count()), 0)
    sporadic_treemap_educ_2 = round(100 * (counted_sporadic_treemap_educ_2_df['educ'] / sporadic_treemap_df['educ'].count()), 0)
    sporadic_treemap_educ_3 = round(100 * (counted_sporadic_treemap_educ_3_df['educ'] / sporadic_treemap_df['educ'].count()), 0)

    clean_sporadic_treemap_educ_dict = {
        'College': int(sporadic_treemap_educ_1),
        'High school or less': int(sporadic_treemap_educ_2),
        'Some college': int(sporadic_treemap_educ_3)
    }

    clean_sporadic_treemap_educ_df = pd.DataFrame(clean_sporadic_treemap_educ_dict.items(), columns=['labels', 'values'])
    clean_sporadic_treemap_educ_df['parents'] = 'Education level'

    # RACE:
    # For the heatmap, generated a sorted treemap dictionary for the 'SPORADIC' voter category:
    counted_sporadic_treemap_race_1_df = sporadic_treemap_df.loc[sporadic_treemap_df['race'] == 1].count()
    counted_sporadic_treemap_race_2_df = sporadic_treemap_df.loc[sporadic_treemap_df['race'] == 2].count()
    counted_sporadic_treemap_race_3_df = sporadic_treemap_df.loc[sporadic_treemap_df['race'] == 3].count()
    counted_sporadic_treemap_race_4_df = sporadic_treemap_df.loc[sporadic_treemap_df['race'] == 4].count()

    sporadic_treemap_race_1 = round(100 * (counted_sporadic_treemap_race_1_df['race'] / sporadic_treemap_df['race'].count()), 0)
    sporadic_treemap_race_2 = round(100 * (counted_sporadic_treemap_race_2_df['race'] / sporadic_treemap_df['race'].count()), 0)
    sporadic_treemap_race_3 = round(100 * (counted_sporadic_treemap_race_3_df['race'] / sporadic_treemap_df['race'].count()), 0)
    sporadic_treemap_race_4 = round(100 * (counted_sporadic_treemap_race_4_df['race'] / sporadic_treemap_df['race'].count()), 0)

    clean_sporadic_treemap_race_dict = {
        'Black': int(sporadic_treemap_race_1),
        'Hispanic': int(sporadic_treemap_race_2),
        'Other/Mixed': int(sporadic_treemap_race_3),
        'White': int(sporadic_treemap_race_4)
    }

    clean_sporadic_treemap_race_df = pd.DataFrame(clean_sporadic_treemap_race_dict.items(), columns=['labels', 'values'])
    clean_sporadic_treemap_race_df['parents'] = 'Race'

    # GENDER:
    # For the heatmap, generated a sorted treemap dictionary for the 'SPORADIC' voter category:
    counted_sporadic_treemap_gender_1_df = sporadic_treemap_df.loc[sporadic_treemap_df['gender'] == 1].count()
    counted_sporadic_treemap_gender_2_df = sporadic_treemap_df.loc[sporadic_treemap_df['gender'] == 2].count()

    sporadic_treemap_gender_1 = round(100 * (counted_sporadic_treemap_gender_1_df['gender'] / sporadic_treemap_df['gender'].count()), 0)
    sporadic_treemap_gender_2 = round(100 * (counted_sporadic_treemap_gender_2_df['gender'] / sporadic_treemap_df['gender'].count()), 0)

    clean_sporadic_treemap_gender_dict = {
        'Female': int(sporadic_treemap_gender_1),
        'Male': int(sporadic_treemap_gender_2)
    }

    clean_sporadic_treemap_gender_df = pd.DataFrame(clean_sporadic_treemap_gender_dict.items(), columns=['labels', 'values'])
    clean_sporadic_treemap_gender_df['parents'] = 'Gender'

    # INCOME_CAT:
    # For the heatmap, generated a sorted treemap dictionary for the 'SPORADIC' voter category:
    counted_sporadic_treemap_income_cat_1_df = sporadic_treemap_df.loc[sporadic_treemap_df['income_cat'] == 1].count()
    counted_sporadic_treemap_income_cat_2_df = sporadic_treemap_df.loc[sporadic_treemap_df['income_cat'] == 2].count()
    counted_sporadic_treemap_income_cat_3_df = sporadic_treemap_df.loc[sporadic_treemap_df['income_cat'] == 3].count()
    counted_sporadic_treemap_income_cat_4_df = sporadic_treemap_df.loc[sporadic_treemap_df['income_cat'] == 4].count()

    sporadic_treemap_income_cat_1 = round(100 * (counted_sporadic_treemap_income_cat_1_df['income_cat'] / sporadic_treemap_df['income_cat'].count()), 0)
    sporadic_treemap_income_cat_2 = round(100 * (counted_sporadic_treemap_income_cat_2_df['income_cat'] / sporadic_treemap_df['income_cat'].count()), 0)
    sporadic_treemap_income_cat_3 = round(100 * (counted_sporadic_treemap_income_cat_3_df['income_cat'] / sporadic_treemap_df['income_cat'].count()), 0)
    sporadic_treemap_income_cat_4 = round(100 * (counted_sporadic_treemap_income_cat_4_df['income_cat'] / sporadic_treemap_df['income_cat'].count()), 0)

    clean_sporadic_treemap_income_cat_dict = {
        'Less than $40k': int(sporadic_treemap_income_cat_1),
        '$40-75k': int(sporadic_treemap_income_cat_2),
        '$75-125k': int(sporadic_treemap_income_cat_3),
        '$125k or more': int(sporadic_treemap_income_cat_4)
    }

    clean_sporadic_treemap_income_cat_df = pd.DataFrame(clean_sporadic_treemap_income_cat_dict.items(), columns=['labels', 'values'])
    clean_sporadic_treemap_income_cat_df['parents'] = 'Household income'

    # Created a list of all the 'sporadic' category DataFrames, concatenated them, and reset the index:
    final_clean_sporadic_treemap_list = [parent_df,
                                    gender_for_parent_df,
                                    clean_sporadic_treemap_gender_df,
                                    race_for_parent_df,
                                    clean_sporadic_treemap_race_df,
                                    educ_for_parent_df,
                                    clean_sporadic_treemap_educ_df,
                                    income_cat_for_parent_df,
                                    clean_sporadic_treemap_income_cat_df]

    final_clean_sporadic_treemap_df = pd.concat(final_clean_sporadic_treemap_list)
    final_clean_sporadic_treemap_df = final_clean_sporadic_treemap_df.reset_index(drop=True)

    # Converted the concatenated DataFrame into a dictionary and added the key 'voter_category' and value 'sporadic':
    final_clean_sporadic_treemap_dict = final_clean_sporadic_treemap_df.to_dict()
    final_clean_sporadic_treemap_dict['voter_category'] = 'sporadic'


    # 'RARELY/NEVER' category:

    # EDUC:
    # For the heatmap, generated a sorted treemap dictionary for the 'RARELY/NEVER' voter category:
    counted_rarelynever_treemap_educ_1_df = rarelynever_treemap_df.loc[rarelynever_treemap_df['educ'] == 1].count()
    counted_rarelynever_treemap_educ_2_df = rarelynever_treemap_df.loc[rarelynever_treemap_df['educ'] == 2].count()
    counted_rarelynever_treemap_educ_3_df = rarelynever_treemap_df.loc[rarelynever_treemap_df['educ'] == 3].count()

    rarelynever_treemap_educ_1 = round(100 * (counted_rarelynever_treemap_educ_1_df['educ'] / rarelynever_treemap_df['educ'].count()), 0)
    rarelynever_treemap_educ_2 = (100 * (counted_rarelynever_treemap_educ_2_df['educ'] / rarelynever_treemap_df['educ'].count()))
    rarelynever_treemap_educ_3 = round(100 * (counted_rarelynever_treemap_educ_3_df['educ'] / rarelynever_treemap_df['educ'].count()), 0)

    clean_rarelynever_treemap_educ_dict = {
        'College': int(rarelynever_treemap_educ_1),
        'High school or less': int(rarelynever_treemap_educ_2 + 1),
        'Some college': int(rarelynever_treemap_educ_3)
    }

    clean_rarelynever_treemap_educ_df = pd.DataFrame(clean_rarelynever_treemap_educ_dict.items(), columns=['labels', 'values'])
    clean_rarelynever_treemap_educ_df['parents'] = 'Education level'

    # RACE:
    # For the heatmap, generated a sorted treemap dictionary for the 'RARELY/NEVER' voter category:
    counted_rarelynever_treemap_race_1_df = rarelynever_treemap_df.loc[rarelynever_treemap_df['race'] == 1].count()
    counted_rarelynever_treemap_race_2_df = rarelynever_treemap_df.loc[rarelynever_treemap_df['race'] == 2].count()
    counted_rarelynever_treemap_race_3_df = rarelynever_treemap_df.loc[rarelynever_treemap_df['race'] == 3].count()
    counted_rarelynever_treemap_race_4_df = rarelynever_treemap_df.loc[rarelynever_treemap_df['race'] == 4].count()

    rarelynever_treemap_race_1 = (100 * (counted_rarelynever_treemap_race_1_df['race'] / rarelynever_treemap_df['race'].count()))
    rarelynever_treemap_race_2 = round(100 * (counted_rarelynever_treemap_race_2_df['race'] / rarelynever_treemap_df['race'].count()), 0)
    rarelynever_treemap_race_3 = round(100 * (counted_rarelynever_treemap_race_3_df['race'] / rarelynever_treemap_df['race'].count()), 0)
    rarelynever_treemap_race_4 = round(100 * (counted_rarelynever_treemap_race_4_df['race'] / rarelynever_treemap_df['race'].count()), 0)

    clean_rarelynever_treemap_race_dict = {
        'Black': int(rarelynever_treemap_race_1 + 1),
        'Hispanic': int(rarelynever_treemap_race_2),
        'Other/Mixed': int(rarelynever_treemap_race_3),
        'White': int(rarelynever_treemap_race_4)
    }

    clean_rarelynever_treemap_race_df = pd.DataFrame(clean_rarelynever_treemap_race_dict.items(), columns=['labels', 'values'])
    clean_rarelynever_treemap_race_df['parents'] = 'Race'

    # GENDER:
    # For the heatmap, generated a sorted treemap dictionary for the 'RARELY/NEVER' voter category:
    counted_rarelynever_treemap_gender_1_df = rarelynever_treemap_df.loc[rarelynever_treemap_df['gender'] == 1].count()
    counted_rarelynever_treemap_gender_2_df = rarelynever_treemap_df.loc[rarelynever_treemap_df['gender'] == 2].count()

    rarelynever_treemap_gender_1 = round(100 * (counted_rarelynever_treemap_gender_1_df['gender'] / rarelynever_treemap_df['gender'].count()), 0)
    rarelynever_treemap_gender_2 = round(100 * (counted_rarelynever_treemap_gender_2_df['gender'] / rarelynever_treemap_df['gender'].count()), 0)

    clean_rarelynever_treemap_gender_dict = {
        'Female': int(rarelynever_treemap_gender_1),
        'Male': int(rarelynever_treemap_gender_2)
    }

    clean_rarelynever_treemap_gender_df = pd.DataFrame(clean_rarelynever_treemap_gender_dict.items(), columns=['labels', 'values'])
    clean_rarelynever_treemap_gender_df['parents'] = 'Gender'

    # INCOME_CAT:
    # For the heatmap, generated a sorted treemap dictionary for the 'RARELY/NEVER' voter category:
    counted_rarelynever_treemap_income_cat_1_df = rarelynever_treemap_df.loc[rarelynever_treemap_df['income_cat'] == 1].count()
    counted_rarelynever_treemap_income_cat_2_df = rarelynever_treemap_df.loc[rarelynever_treemap_df['income_cat'] == 2].count()
    counted_rarelynever_treemap_income_cat_3_df = rarelynever_treemap_df.loc[rarelynever_treemap_df['income_cat'] == 3].count()
    counted_rarelynever_treemap_income_cat_4_df = rarelynever_treemap_df.loc[rarelynever_treemap_df['income_cat'] == 4].count()

    rarelynever_treemap_income_cat_1 = round(100 * (counted_rarelynever_treemap_income_cat_1_df['income_cat'] / rarelynever_treemap_df['income_cat'].count()), 0)
    rarelynever_treemap_income_cat_2 = (100 * (counted_rarelynever_treemap_income_cat_2_df['income_cat'] / rarelynever_treemap_df['income_cat'].count()))
    rarelynever_treemap_income_cat_3 = round(100 * (counted_rarelynever_treemap_income_cat_3_df['income_cat'] / rarelynever_treemap_df['income_cat'].count()), 0)
    rarelynever_treemap_income_cat_4 = round(100 * (counted_rarelynever_treemap_income_cat_4_df['income_cat'] / rarelynever_treemap_df['income_cat'].count()), 0)

    clean_rarelynever_treemap_income_cat_dict = {
        'Less than $40k': int(rarelynever_treemap_income_cat_1),
        '$40-75k': int(rarelynever_treemap_income_cat_2),
        '$75-125k': int(rarelynever_treemap_income_cat_3),
        '$125k or more': int(rarelynever_treemap_income_cat_4)
    }

    clean_rarelynever_treemap_income_cat_df = pd.DataFrame(clean_rarelynever_treemap_income_cat_dict.items(), columns=['labels', 'values'])
    clean_rarelynever_treemap_income_cat_df['parents'] = 'Household income'

    # Created a list of all the 'rarelynever' category DataFrames, concatenated them, and reset the index:
    final_clean_rarelynever_treemap_list = [parent_df,
                                    gender_for_parent_df,
                                    clean_rarelynever_treemap_gender_df,
                                    race_for_parent_df,
                                    clean_rarelynever_treemap_race_df,
                                    educ_for_parent_df,
                                    clean_rarelynever_treemap_educ_df,
                                    income_cat_for_parent_df,
                                    clean_rarelynever_treemap_income_cat_df]

    final_clean_rarelynever_treemap_df = pd.concat(final_clean_rarelynever_treemap_list)
    final_clean_rarelynever_treemap_df = final_clean_rarelynever_treemap_df.reset_index(drop=True)

    # Converted the concatenated DataFrame into a dictionary and added the key 'voter_category' and value 'rarelynever':
    final_clean_rarelynever_treemap_dict = final_clean_rarelynever_treemap_df.to_dict()
    final_clean_rarelynever_treemap_dict['voter_category'] = 'rarely/never'


    # Created the final treemap dictionary to be returned when running the function:
    final_treemap_dict = {'categories': ['always', 
                                        'sporadic',
                                        'rarely/never'],
                        'treemapData': [final_clean_always_treemap_dict,
                                        final_clean_sporadic_treemap_dict,
                                        final_clean_rarelynever_treemap_dict]}
    return final_treemap_dict



# 8. JSON of the index HTML file:
# Returned the file to be able to open it while running the data from the app:
@app.route('/api/index/')
def htmlFile():
    return render_template('index.html')



# To run the app:
if __name__ == "__main__":
    app.run(debug=True)