#db.py
import os
import psycopg2
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}/.s.PGSQL.5432'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = psycopg2.connect(user=db_user, password=db_password,
                                host=unix_socket, database='kants'
                                )
    except psycopg2.OperationalError as e:
        print(e)

    return conn


def get_songs():
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM target;')
        songs = cursor.fetchall()
        if songs > 0:
            got_songs = jsonify(songs)
        else:
            got_songs = 'No Songs in DB'
    conn.commit()
    conn.close()
    return got_songs