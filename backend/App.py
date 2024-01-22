import os
from dotenv import load_dotenv
import psycopg2
from BuiltInCoScraper import BuiltInScrape
from IndeedScraper import IndeedScrape
from YCombScraper import YCombScraper
def main():

    load_dotenv('../.env')

    # Now you can access the variables using os.environ
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_name = os.environ.get('DB_NAME')

    conn = psycopg2.connect(
        host= db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name
    )

    insert_script = "INSERT INTO opportunities (company_name,title,link,info) VALUES (%s, %s, %s, %s)"

    cursor = conn.cursor()

    # built_in_url = "https://www.builtincolorado.com/jobs/dev-engineering/entry-level/mid-level"
    # BuiltInScrape(conn,cursor,built_in_url,True,insert_script)

    # IndeedScrape(conn,cursor,indeed_scraper_url,False,insert_script)

    url = ""
    YCombScraper(conn,cursor,url,False,insert_script)
    cursor.close()
    conn.close()
    return
if __name__ == "__main__":
    main()