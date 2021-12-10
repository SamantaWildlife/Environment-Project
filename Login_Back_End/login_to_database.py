from typing import List
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from SQL_deets import HOST, USER, PASSWORD
import re

app = Flask(__name__)

app.secret_key = 'Kettle123'
def _connect_to_db(db_name: str):
    cnx = mysql.connector.connect(host=HOST,
                                  user=USER,
                                  password=PASSWORD,
                                  auth_plugin='mysql_native_password',
                                  database=db_name)
    return cnx


# @app.route('/user_login_details/', methods=['GET', 'POST'])
# def login():
#     # Output message if something goes wrong...
#     msg = "Oops something's gone wrong"
#     return render_template('login_form.html', msg='')


def get_username_password():
    db_connection = None

db_name = "user_login_details"
db_connection = _connect_to_db(db_name)
print(f'Connected to the Database {db_name}')




if db_connection:
    db_connection.close()
    print('DB Connection is now closed.')

get_username_password()

    #     cursor = db_connection.cursor()
    #
    #     query = f"""SELECT teamMember, `12-13`, `13-14`,
    #     `14-15`, `15-16`, `16-17`, `17-18`
    #     FROM nano.salon_bookings WHERE bookingDate = '{date}'"""
    #
    #     cursor.execute(query)
    #     result = cursor.fetchall()  # returns a list of tuples
    #
    #     # Map list of record tuples into availability dicts
    #     availability = map_values(result)
    #
    #     print(availability)
    #
    #     cursor.close()
    #
    #     return availability
    #
    # except Exception:
    #     raise DBConnectionError('Failed to read the data from DB')
    #
    # finally:
    #     if db_connection:
    #         db_connection.close()
    #         print('DB Connection is now closed.')
    #
    #
    # # Check if account exists using MySQL
    # cursor = db_connection.cursor()
    # cursor.execute('SELECT * FROM user_account WHERE username = %s AND password = %s', (username, password,))
    # # Fetch one record and return result
    # account = cursor.fetchone()
    #
    #
    #
    #
    #
    #
    #
