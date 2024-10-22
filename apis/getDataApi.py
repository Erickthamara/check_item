import os
from dotenv import load_dotenv
from flask import Flask,jsonify,request
from flask_cors import CORS
import psycopg2

# Load environment variables from .env file
load_dotenv()


conn = psycopg2.connect(database=os.getenv("DATABASE"),
                        user = os.getenv("USER"), 
                        password = os.getenv("PASSWORD"),
                        host =os.getenv("HOST"), 
                        port = os.getenv("PORT"))

cursor=conn.cursor()

app=Flask(__name__)

CORS(app)


@app.route('/api/checks',methods=['GET'])
def get_data():
    try:
       cursor.execute('SELECT * FROM check_item.all_transactions ORDER BY "Entry No" DESC')
       response=cursor.fetchall()
       conn.commit
    #    print(f'DATA IS {response}')
    except Exception as e:
        # print(f'Error is {e}')
        pass


    return jsonify(response),200

if __name__=='__main__':
    app.run(debug=True)
