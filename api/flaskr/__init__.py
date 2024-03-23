import os
import json
import psycopg2

from flask import Flask

DB_NAME="ogre"
DB_USER="postgres"
DB_HOST="psql-1.c1so8qiqiw95.us-east-2.rds.amazonaws.com"
DB_PASSWD=os.environ['DB_PASSWD']

conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s" % (DB_NAME, DB_USER, DB_PASSWD, DB_HOST))


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/api/health')
    def health():
        return 'All is well!'

    @app.route('/api/rankings')
    def rankings():
        cur = conn.cursor()
        cur.execute('''
        WITH RankData AS (
            SELECT name AS Character, className as Class, level,
                COALESCE((
                    SELECT COUNT(*)
                    FROM Duels
                    WHERE id = winnercharacterid
                    GROUP BY winnercharacterid
                ), 0) AS Wins,
                COALESCE((
                    SELECT COUNT(*)
                    FROM Duels
                    WHERE id = losercharacterid
                    GROUP BY losercharacterid
                ),0) AS Losses
            FROM Characters RIGHT OUTER JOIN Duels
                ON (id = winnercharacterid OR id = losercharacterid)
        )
        SELECT (Wins - Losses) as Ranking, Character, Class, Level,
                FORMAT(\'%s-%s\', Wins, Losses) as "W-L"
        FROM RankData
        ORDER BY Ranking DESC;
        ''')

        rankings_data = cur.fetchall()

        return json.dumps({
                'columns': ['#', 'Character', 'Class', 'Level', 'W-L'],
                'data': rankings_data,
        })

    @app.route('/api/accountinfo')
    def accountinfo():
        return json.dumps({
                'username': "Kujo",
                'character_columns': ['Rank', 'Name', 'Class', 'Level', 'Record'],
                'characters': [
                    [1, 'Dan the Man', 'Knight', 32, '12-43'],
                    [24, 'Bard the Bulger', 'Barbarian', 12, '10-4'],
                    [102, 'Pete the Mighty', 'Knight', 9, '1-13'],
                    [783, 'Steve', 'Wizard', 4, '0-18'],
                ],
            })

    @app.route('/api/characterinfo')
    def characterinfo():
        return json.dumps({
            'name': 'Kron the Brutal',
            'level': 78,
            'class': 'Berserker',
            'attributes': [
                ('intelligence', 2),
                ('wisdom', 1),
                ('charisma', 1),
                ('dexterity', 22),
                ('consitution', 72),
                ('vitality', 63),
            ],
        })

    @app.route('/api/duels')
    def duels():
        cur = conn.cursor()
        cur.execute('''
        SELECT FORMAT('%s', timestamp::date) as Date, FORMAT('%s', timestamp::time) as Time,
            (Select name from characters where id = winnercharacterid) as Winner,
            (select name from characters where id = losercharacterid) as Loser
        FROM Duels
        ORDER BY timestamp DESC;
        ''')

        dueling_data = cur.fetchall()

        return json.dumps({
            'columns': ['date', 'time', 'winner', 'loser'],
            'duels': dueling_data,
        })

    return app

