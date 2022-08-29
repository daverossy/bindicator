#!/usr/bin/python
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os


def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn


def create_db_table():
    try:
        conn = connect_to_db()
        #conn.execute('''DROP TABLE bin_calendar''')
        conn.execute('''
            CREATE TABLE bin_calendar (
                entry_id INTEGER PRIMARY KEY NOT NULL,
                bin_colour TEXT NOT NULL,
                collection_date TEXT NOT NULL
            );
        ''')

        conn.commit()
        print("Bin calendar table created successfully")
    except:
        print("Bin calendar table creation failed")
    finally:
        conn.close()


def add_collection_date(collection):
    message = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO bin_calendar (
                bin_colour, 
                collection_date) 
            VALUES (?, ?)''', (collection['bin_colour'], collection['collection_date']))
        conn.commit()
        message["status"] = "Collection date added successfully"
    except:
        conn().rollback()
        message["status"] = "Cannot add collection date"
    finally:
        conn.close()

    return message


def get_collection_bin_colour():
    collections = []
    current_date = datetime.today().strftime('%d-%m-%Y')
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM bin_calendar WHERE collection_date = ?", (current_date,))
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            collection = {"bin_colour": i["bin_colour"], "collection_date": i["collection_date"]}
            collections.append(collection)

    except:
        collections = []

    return collections


def delete_collection_date(collection_date):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from bin_calendar WHERE collection_date = ?", (collection_date,))
        conn.commit()
        message["status"] = "Collection date deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete collection date"
    finally:
        conn.close()

    return message


create_db_table()


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/api/current_bin', methods=['GET'])
def api_get_collection_bin_colour():
    return jsonify(get_collection_bin_colour())


@app.route('/api/add_collection_date', methods=['POST'])
def api_add_collection_date():
    collection = request.get_json()
    return jsonify(add_collection_date(collection))


@app.route('/api/delete_collection_date/<collection_date>', methods=['DELETE'])
def api_delete_collection_date(collection_date):
    return jsonify(delete_collection_date(collection_date))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 6000))
    app.run(debug=False, host='0.0.0.0', port=port)
