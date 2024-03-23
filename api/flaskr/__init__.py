import os
import json

from flask import Flask


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
        return json.dumps({
                'columns': ['#', 'Character', 'Class', 'Level', 'W-L'],
                'data': [
                            [1, 'Dan the Man', 'Knight', 32, '12-43'],
                            [2, 'Bob the Builder', 'Wizard', 76, '89-3'],
                            [3, 'Ted the Wise', 'Assassin', 103, '143-1'],
                ]
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
        return json.dumps({
            'columns': ['date', 'time', 'winner', 'loser'],
            'duels': [
                ['2024-03-13', '42:33', 'Bob the Builder', 'Steve'],
                ['2024-03-25', '21:37', 'Kron the Brutal', 'Dan the Man'],
                ['2024-01-23', '22:35', 'Kron the Brutal', 'Steve'],
                ['2023-10-18', '27:02', 'Dan the Man', 'Steve'],
                ['2023-08-29', '12:18', 'Bob the Builder', 'Dan the Man'],
                ['2023-08-03', '02:25', 'Kron the Brutal', 'Bob the Builder'],
            ],
        })

    return app

