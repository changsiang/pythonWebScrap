import pymysql as mysql
from datetime import datetime


def insert_town_info(town_name):
    # Open database connection
    conn = mysql.connect('localhost', 'root', 'password', 'hdb_data')

    # prepare a cursor object using cursor() method
    cursor = conn.cursor()

    sql = 'INSERT INTO town (town, entry_date) VALUES ("%s", "%s")' % (
        town_name, datetime.now().isoformat())

    # execute the command and commit change
    try:
        cursor.execute(sql)
        conn.commit()
    except mysql.Error:
        conn.rollback()
        print('SQL Error! ', mysql.Error.__traceback__())
    finally:
        # disconnect from server
        conn.close()

def get_town_list():
    # Open database connection
    conn = mysql.connect('localhost', 'root', 'password', 'hdb_data')

    # prepare a cursor object using cursor() method
    cursor = conn.cursor()
    town_list = []
    sql = 'SELECT * FROM town'
    try:
        # Execute the command
        cursor.execute(sql)
        # Fatch all the results
        results = cursor.fetchall()
        if results.__len__() > 0:
            for result in results:
                town_list.append(result[0])
    except mysql.Error:
        print('Query Error! ', mysql.Error.__traceback__())
    finally:
        conn.close()

    return town_list

def get_all_project_hyperlink():
    # Open database connection
    conn = mysql.connect('localhost', 'root', 'password', 'hdb_data')

    # prepare a cursor object using cursor() method
    cursor = conn.cursor()
    project_hyperlink = []
    sql = 'SELECT hyperlink FROM project'
    try:
        # Execute the command
        cursor.execute(sql)
        # Fatch all the results
        results = cursor.fetchall()
        if results.__len__() > 0:
            for result in results:
                project_hyperlink.append(result[0])
    except mysql.Error:
        print('Query Error! ', mysql.Error.__traceback__())
    finally:
        conn.close()

    return project_hyperlink

def get_all_block_hyperlink():
    # Open database connection
    conn = mysql.connect('localhost', 'root', 'password', 'hdb_data')

    # prepare a cursor object using cursor() method
    cursor = conn.cursor()
    block_hyperlink = []
    sql = 'SELECT hyperlink FROM blocks'
    try:
        # Execute the command
        cursor.execute(sql)
        # Fatch all the results
        results = cursor.fetchall()
        if results.__len__() > 0:
            for result in results:
                block_hyperlink.append(result[0])
    except mysql.Error:
        print('Query Error! ', mysql.Error.__traceback__())
    finally:
        conn.close()

    return block_hyperlink

def insert_project_info(period_id, town, project_name, room_type, units_offered, hyperlink):
    # Open database connection
    conn = mysql.connect('localhost', 'root', 'password', 'hdb_data')

    # prepare a cursor object using cursor() method
    cursor = conn.cursor()

    sql = 'INSERT INTO Project (town, project_name, room_type, last_updated, units_offered, hyperlink, period_id) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (
        town, project_name, room_type, datetime.now().isoformat(), units_offered, hyperlink, period_id)

    # execute insert command
    try:
        cursor.execute(sql)
        conn.commit()
    except mysql.Error:
        conn.rollback()
        print('SQL Error! ', mysql.Error.__traceback__())
    finally:
        # disconnect from server
        conn.close()


def insert_project_hx_data(project_name, room_type, units_available, chinese_quota, malay_quota, others_quota):
    # Open database connection
    conn = mysql.connect('localhost', 'root', 'password', 'hdb_data')

    # prepare a cursor object using cursor() method
    cursor = conn.cursor()

    sql = 'INSERT INTO project_hx_data (project_name, room_type, units_available, chinese_quota, malay_quota, others_quota, last_updated) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (
        project_name, room_type, units_available, chinese_quota, malay_quota, others_quota, datetime.now().isoformat())

    # execute insert command
    try:
        cursor.execute(sql)
        conn.commit()
    except mysql.Error:
        conn.rollback()
        print('SQL Error! ', mysql.Error.__traceback__())
    finally:
        # disconnect from server
        conn.close()


def get_project_name_by_hyperlink(hyperlink):
    # Open database connection
    conn = mysql.connect('localhost', 'root', 'password', 'hdb_data')

    # prepare a cursor object using cursor() method
    cursor = conn.cursor()
    sql = 'SELECT project_name FROM project WHERE hyperlink = "%s"' % (
        hyperlink)
    try:
        # Execute the command
        cursor.execute(sql)
        # Fatch all the results
        results = cursor.fetchmany(size=1)
        return str(results[0])[2:-3]
    except mysql.Error:
        print('Query get_project_name_bY_hyperlink Error! ',
              mysql.Error.__traceback__())
    finally:
        conn.close


def insert_block_info(postal_code, block_number, project_name, street, status, hyperlink):
    address = 'Block ' + block_number + ' ' + street + ' Singapore ' + postal_code
    # Open database connection
    conn = mysql.connect('localhost', 'root', 'password', 'hdb_data')

    # prepare a cursor object using cursor() method
    cursor = conn.cursor()

    sql = 'INSERT INTO blocks (postal_code, block_number, project_name, address, status, last_updated, hyperlink) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (
        postal_code, block_number, project_name, address, status, datetime.now().isoformat(), hyperlink)
    try:
        cursor.execute(sql)
        conn.commit()
    except mysql.Error:
        print('insert at insert_block_info Error!', mysql.Error.__traceback__())
    finally:
        conn.close()

def insert_units_info(block, floor, unit, project_name, isTaken, date_taken, date_updated, room_type, price, year_of_lease, size):
    # Open database connection
    conn = mysql.connect('localhost', 'root', 'password', 'hdb_data')

    # prepare a cursor object using cursor() method
    cursor = conn.cursor()

    sql = 'INSERT INTO units (block, floor, unit, project_name, isTaken, date_taken, date_updated, room_type, price, year_of_lease, size) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (
        block, floor, unit, project_name, isTaken, date_taken, date_updated, room_type, price, year_of_lease, size)
    try:
        cursor.execute(sql)
        conn.commit()
    except mysql.Error:
        print('insert at insert_unit_info Error!', mysql.Error.__traceback__())
    finally:
        conn.close()
