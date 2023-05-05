-- Created with and exported from QuickDBD: https://www.quickdatabasediagrams.com/, and edited by Roberto Barron,
-- Luis Paul Garay, Alonso Lozano, Daniel Murillo, and Antonio Nava.

-- The database creation went through three different stages:
-- first: the creation of the table schemas,
-- second: the import/insertion of the data into the tables,
-- and third: the addition of FK constraints.





-- HELPFUL TOOLS:
-- To select the tables when needed:
SELECT * FROM responses;
SELECT * FROM agree_disagree_likert;
SELECT * FROM impact_likert;
SELECT * FROM q5_responses;
SELECT * FROM q30_responses;
SELECT * FROM educ_responses;
SELECT * FROM race_responses;
SELECT * FROM gender_responses;
SELECT * FROM income_cat_responses;
SELECT * FROM voter_category_responses;

-- To drop tables when needed:
DROP TABLE "responses";
DROP TABLE "agree_disagree_likert";
DROP TABLE "impact_likert";
DROP TABLE "q5_responses";
DROP TABLE "q30_responses";
DROP TABLE "educ_responses";
DROP TABLE "race_responses";
DROP TABLE "gender_responses";
DROP TABLE "income_cat_responses";
DROP TABLE "voter_category_responses";





-- FIRST STAGE: Creation of the table schema.
-- Created a table schema for 10 tables —every variable has the 'NOT NULL' instruction, as there were no
-- missing values—:

-- 1. Created a main table for all the participant responses with 'RespID' as the PK:
CREATE TABLE "responses" (
    "RespId" INT   NOT NULL,
    "q3_1" INT   NOT NULL,
    "q3_2" INT   NOT NULL,
    "q3_3" INT   NOT NULL,
    "q3_4" INT   NOT NULL,
    "q3_5" INT   NOT NULL,
    "q3_6" INT   NOT NULL,
    "q4_1" INT   NOT NULL,
    "q4_2" INT   NOT NULL,
    "q4_3" INT   NOT NULL,
    "q4_4" INT   NOT NULL,
    "q4_5" INT   NOT NULL,
    "q4_6" INT   NOT NULL,
    "q5" INT   NOT NULL,
    "q30" INT   NOT NULL,
    "pp_age" INT   NOT NULL,
    "educ" INT   NOT NULL,
    "race" INT   NOT NULL,
    "gender" INT   NOT NULL,
    "income_cat" INT   NOT NULL,
    "voter_category" INT   NOT NULL,
    CONSTRAINT "pk_responses" PRIMARY KEY (
        "RespId"
     )
);

-- 2. Created a table for the agree/disagree Likert scale of question 3 with 'ID' as the PK:
CREATE TABLE "agree_disagree_likert" (
    "ID" INT   NOT NULL,
    "agree_disagree_response" VARCHAR   NOT NULL,
    CONSTRAINT "pk_agree_disagree_likert" PRIMARY KEY (
        "ID"
     )
);

-- 3. Created a table for the impact Likert scale of question 4 with 'ID' as the PK:
CREATE TABLE "impact_likert" (
    "ID" INT   NOT NULL,
    "impact_response" VARCHAR   NOT NULL,
    CONSTRAINT "pk_impact_likert" PRIMARY KEY (
        "ID"
     )
);

-- 4. Created a table for the possible responses for question 5 with 'ID' as the PK:
CREATE TABLE "q5_responses" (
    "ID" INT   NOT NULL,
    "q5_responses" VARCHAR   NOT NULL,
    CONSTRAINT "pk_q5_responses" PRIMARY KEY (
        "ID"
     )
);

-- 5. Created a table for the possible responses for question 30 with 'ID' as the PK:
CREATE TABLE "q30_responses" (
    "ID" INT   NOT NULL,
    "q30_responses" VARCHAR   NOT NULL,
    CONSTRAINT "pk_q30_responses" PRIMARY KEY (
        "ID"
     )
);

-- 6. Created a table for the education responses (demographic question) with 'ID' as the PK:
CREATE TABLE "educ_responses" (
    "ID" INT   NOT NULL,
    "educ_responses" VARCHAR   NOT NULL,
    CONSTRAINT "pk_educ_responses" PRIMARY KEY (
        "ID"
     )
);

-- 7. Created a table for the race responses (demographic question) with 'ID' as the PK:
CREATE TABLE "race_responses" (
    "ID" INT   NOT NULL,
    "race_responses" VARCHAR   NOT NULL,
    CONSTRAINT "pk_race_responses" PRIMARY KEY (
        "ID"
     )
);

-- 8. Created a table for the gender responses (demographic question) with 'ID' as the PK:
CREATE TABLE "gender_responses" (
    "ID" INT   NOT NULL,
    "gender_responses" VARCHAR   NOT NULL,
    CONSTRAINT "pk_gender_responses" PRIMARY KEY (
        "ID"
     )
);

-- 9. Created a table for the household income responses (demographic question) with 'ID' as the PK:
CREATE TABLE "income_cat_responses" (
    "ID" INT   NOT NULL,
    "income_cat_responses" VARCHAR   NOT NULL,
    CONSTRAINT "pk_income_cat_responses" PRIMARY KEY (
        "ID"
     )
);

-- 10. Created a table for the voter category (assigned by the authors of the survey) with 'ID' as the PK:
CREATE TABLE "voter_category_responses" (
    "ID" INT   NOT NULL,
    "voter_category_responses" VARCHAR   NOT NULL,
    CONSTRAINT "pk_voter_category_responses" PRIMARY KEY (
        "ID"
     )
);





-- SECOND STAGE: Import/insertion of the data into the tables.
-- To avoid errors due to violating the FK constraints specified in the third stage of this process, the data
-- was imported/inserted before the FK constraints were specified.

-- Table 1: Used the 'Import/Export Data...' pgAdmin option to import the data of the main table 'responses'
-- from a CSV file.

-- Table 2: Specified the agree/disagree Likert scale values of question 3 and inserted them into the
-- 'agree_disagree_likert' table:
INSERT INTO agree_disagree_likert ("ID", "agree_disagree_response")
VALUES (1, 'Strongly agree'),
(2, 'Somewhat agree'),
(3, 'Somewhat disagree'),
(4, 'Strongly disagree');

-- Table 3: Specified the impact Likert scale values of question 4 and inserted them into the 'impact_likert'
-- table:
INSERT INTO impact_likert ("ID", "impact_response")
VALUES (1, 'A significant impact'),
(2, 'Somewhat of an impact'),
(3, 'Just a slight impact'),
(4, 'No impact at all');

-- Table 4: Specified the possible responses for question 5 and inserted them into the 'q5_responses' table:
INSERT INTO q5_responses ("ID", "q5_responses")
VALUES (1, 'Who wins the election really matters'),
(2, 'Things will be pretty much the same');

-- Table 5: Specified the possible responses for question 30 and inserted them into the 'q30_responses' table:
INSERT INTO q30_responses ("ID", "q30_responses")
VALUES (1, 'Republican'),
(2, 'Democrat'),
(3, 'Independent'),
(4, 'Another party'),
(5, 'No preference');

-- Table 6: Specified the three education level possible responses (demographic question) and inserted them into
-- the 'educ_responses' table:
INSERT INTO educ_responses ("ID", "educ_responses")
VALUES (1, 'College'),
(2, 'High school or less'),
(3, 'Some college');

-- Table 7: Specified the four race possible responses (demographic question) and inserted them into the
-- 'race_responses' table:
INSERT INTO race_responses ("ID", "race_responses")
VALUES (1, 'Black'),
(2, 'Hispanic'),
(3, 'Other/Mixed'),
(4, 'White');

-- Table 8: Specified the two gender possible responses (demographic question) and inserted them into the
-- 'gender_responses' table:
INSERT INTO gender_responses ("ID", "gender_responses")
VALUES (1, 'Female'),
(2, 'Male');

-- Table 9: Specified the four household income possible responses (demographic question) and inserted them into
-- the 'income_cat_responses' table:
INSERT INTO income_cat_responses ("ID", "income_cat_responses")
VALUES (1, 'Less than $40k'),
(2, '$40-75k'),
(3, '$75-125k'),
(4, '$125k or more');

-- Table 10: Specified the three voter categories that were assigned by the authors of the survey and inserted
-- them into the 'voter_category_responses' table:
INSERT INTO voter_category_responses ("ID", "voter_category_responses")
VALUES (1, 'Always'),
(2, 'Sporadic'),
(3, 'Rarely/Never');





-- THIRD STAGE: addition of FK constraints.
-- This section contains the FKs constraints that were added after creating the tables and importing/inserting
-- the data. Adding those constraints at the end worked better because it meant that all of the tables could be
-- created without any problems and updated in any order and it wouldn't cause any errors. Should the code be
-- edited for future analyses, it would also be easier to edit/scale it.

-- Altered the 'responses' table to add a constraint to turn its 'q3_1' column into a FK that referenced the
-- 'ID' column from the 'agree_disagree_likert' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_q3_1" FOREIGN KEY("q3_1")
REFERENCES "agree_disagree_likert" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'q3_2' column into a FK that referenced the
-- 'ID' column from the 'agree_disagree_likert' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_q3_2" FOREIGN KEY("q3_2")
REFERENCES "agree_disagree_likert" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'q3_3' column into a FK that referenced the
-- 'ID' column from the 'agree_disagree_likert' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_q3_3" FOREIGN KEY("q3_3")
REFERENCES "agree_disagree_likert" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'q3_4' column into a FK that referenced the
-- 'ID' column from the 'agree_disagree_likert' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_q3_4" FOREIGN KEY("q3_4")
REFERENCES "agree_disagree_likert" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'q3_5' column into a FK that referenced the
-- 'ID' column from the 'agree_disagree_likert' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_q3_5" FOREIGN KEY("q3_5")
REFERENCES "agree_disagree_likert" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'q3_6' column into a FK that referenced the
-- 'ID' column from the 'agree_disagree_likert' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_q3_6" FOREIGN KEY("q3_6")
REFERENCES "agree_disagree_likert" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'q4_1' column into a FK that referenced the
-- 'ID' column from the 'impact_likert' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_q4_1" FOREIGN KEY("q4_1")
REFERENCES "impact_likert" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'q4_2' column into a FK that referenced the
-- 'ID' column from the 'impact_likert' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_q4_2" FOREIGN KEY("q4_2")
REFERENCES "impact_likert" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'q4_3' column into a FK that referenced the
-- 'ID' column from the 'impact_likert' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_q4_3" FOREIGN KEY("q4_3")
REFERENCES "impact_likert" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'q4_4' column into a FK that referenced the
-- 'ID' column from the 'impact_likert' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_q4_4" FOREIGN KEY("q4_4")
REFERENCES "impact_likert" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'q4_5' column into a FK that referenced the
-- 'ID' column from the 'impact_likert' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_q4_5" FOREIGN KEY("q4_5")
REFERENCES "impact_likert" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'q4_6' column into a FK that referenced the
-- 'ID' column from the 'impact_likert' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_q4_6" FOREIGN KEY("q4_6")
REFERENCES "impact_likert" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'q5' column into a FK that referenced the 'ID'
-- column from the 'q5_responses' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_q5" FOREIGN KEY("q5")
REFERENCES "q5_responses" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'q30' column into a FK that referenced the 'ID'
-- column from the 'q30_responses' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_q30" FOREIGN KEY("q30")
REFERENCES "q30_responses" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'educ' column into a FK that referenced the
-- 'ID' column from the 'educ_responses' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_educ" FOREIGN KEY("educ")
REFERENCES "educ_responses" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'race' column into a FK that referenced the
-- 'ID' column from the 'race_responses' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_race" FOREIGN KEY("race")
REFERENCES "race_responses" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'gender' column into a FK that referenced the
-- 'ID' column from the 'gender_responses' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_gender" FOREIGN KEY("gender")
REFERENCES "gender_responses" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'income_cat' column into a FK that referenced
-- the 'ID' column from the 'income_cat_responses' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_income_cat" FOREIGN KEY("income_cat")
REFERENCES "income_cat_responses" ("ID");

-- Altered the 'responses' table to add a constraint to turn its 'voter_category' column into a FK that
-- referenced the 'ID' column from the 'voter_category_responses' table (the relationship is many-to-one).
ALTER TABLE "responses" ADD CONSTRAINT "fk_responses_voter_category" FOREIGN KEY("voter_category")
REFERENCES "voter_category_responses" ("ID");
