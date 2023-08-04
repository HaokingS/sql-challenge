# Data Management Task

## EmployeeSQL
1. **Data folder** : Contains 6 table in .csv format
2. **Images folder** : Bonus task to identify the range of salary and average salary by job title
3. **employeed_erd.png** : Contained the Entity Relational Diagram of the 6 table on Data Fodler
4. **employees_query_BigQuery.sql** : Contained query to solve 8 task provided on BigQuery
5. **employees_query_PostgreSQL.sql** : Contained query to solve 8 task provided on PostgreSQL
6. **employees_schemata.sql** : Contained query to create the schema of sql_challenge
7. **python-sql analysis.ipynb** : Notebook that connected to local database (PostgreSQL) to run the query for the 8 task and bonus-task for further analysis

## Backend
The backend section contains code responsible for interacting with APIs and serving data to the frontend.
1. **query.py** : contains query to retrieve data from API
2. **main.py** : FastAPI code to provide endpoint to access database

## Frontend
The frontend section offers a user interface with pagination, facilitating a smooth user experience (reduce lag when fetching many data)
1. Retrieve data from the database based on predefined queries, providing quick access to common data requests.
2. Allow users to customize data retrieval based on their preferences, ensuring a personalized experience.

## Web Scraping
The web scraping section includes coding scripts to scrape data from the mobbi website (https://www.mobbi.id/). The scraped data is stored in both .py and .ipynb files and is connected to a local database.

### Scraping Process
The Python scripts extract data from the mobbi website, capturing valuable information for analysis.
The data resulting from the web scraping process is saved in a .csv file for further analysis.
