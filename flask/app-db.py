from flask import Flask
from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager
import json

dbConnection = "dbname='postgres' user='postgres' host='live-score.cfrcolph1w1u.us-east-2.rds.amazonaws.com' password='postgres'"

# pool define with 10 live connections
connectionpool = SimpleConnectionPool(1,10,dsn=dbConnection)

@contextmanager
def getcursor():
    con = connectionpool.getconn()
    try:
        yield con.cursor()
    finally:
        connectionpool.putconn(con)

app = Flask(__name__)
app.debug = True


@app.route('/livescore', methods=['GET'])
def view_score():
    try:
        # with here will take care of put connection when its done
        with getcursor() as cur:
            cur.execute("SELECT match.id, striker.name as striker, playerscorecard.striker_4, playerscorecard.striker_6, playerscorecard.striker_strikerate FROM match inner join SCORE on SCORE.ID = match.SCORE_ID inner join playerscorecard on playerscorecard.s_id = SCORE.scorecard_id inner join players as striker on striker.id = playerscorecard.striker where match.id = 1 limit 1")
            result_set = cur.fetchall()
            return json.dumps({"socre" : [{'match_id' : x[0], 'striker_batsman': x[1], 'striker_4': x[2], 'striker_6': x[3], 'striker_strikerate': float((x[4]))} for x in result_set]})
    except Exception as e:
        print("error in executing with exception: ", e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)