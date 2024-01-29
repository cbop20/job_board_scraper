import os
import psycopg2
from app import BuiltInCoScraper
from app import IndeedScraper
from app import YCombScraper
from quart import Quart,jsonify
from quart_cors import cors
from concurrent.futures import ThreadPoolExecutor
import logging

app = Quart(__name__)
app = cors(app, allow_origin="*")

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(message)s",
    )

def connect_db():
    conn = psycopg2.connect(
        host='postgres',
        port=os.environ.get('DB_PORT'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME')
    )
    return conn, conn.cursor()
@app.route("/get_opportunities",methods=['GET'])
async def get_opportunities():
    try:
        configure_logging()

        insert_script = "INSERT INTO opportunities (company_name,title,link,info) VALUES (%s, %s, %s, %s)"


        connection, cursor = connect_db()

        ycomb = YCombScraper.YCombScrape(connection,cursor,True,insert_script)
        built_in = BuiltInCoScraper.BuiltInScrape(connection,cursor,True,insert_script)
        indeed = IndeedScraper.IndeedScrape(connection,cursor,True,insert_script)

        built_in.scrape()
        ycomb.scrape()
        indeed.scrape()


        cursor.close()
        connection.close()
        return "sucess"
    except Exception as ex:
        print(ex)
        return 'error'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.getenv('FLASK_PORT'),debug=True)