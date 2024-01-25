import os
from dotenv import load_dotenv
import psycopg2
from app import BuiltInCoScraper
from app import IndeedScraper
from app import YCombScraper
from flask import Flask,jsonify
from flask_cors import CORS, cross_origin


load_dotenv('../../.env')

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')
insert_script = "INSERT INTO opportunities (company_name,title,link,info) VALUES (%s, %s, %s, %s)"
@app.route("/")
@cross_origin()
def index():
    try:
        conn = psycopg2.connect(
            host= db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_name
        )

        cursor = conn.cursor()

        built_in = BuiltInCoScraper.BuiltInScrape(conn,cursor,True,insert_script)
        indeed = IndeedScraper.IndeedScrape(conn,cursor,True,insert_script)
        ycomb = YCombScraper.YCombScrape(conn,cursor,True,insert_script)

        indeed.scrape()
        ycomb.scrape()
        built_in.scrape()
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(host=os.getenv('FLASK_HOST'),port=os.getenv('FLASK_PORT'),debug=True)