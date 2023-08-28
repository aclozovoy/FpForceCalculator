# CONNECT TO DATABASE
def db_conn():

    import pymysql

    host = 'acl-database.cl7ay4156fuf.us-west-2.rds.amazonaws.com'
    user = 'admin'

    try:
        with open('localpass.txt') as f:
            password = f.readline().strip('\n')
    except:
        import os
        endpoint = os.environ['DB_PASSWORD']
        password = endpoint
        

    connection = pymysql.connect(
                    host = host,
                    user = user,
                    password = password)

    cursor = connection.cursor()


    # USE DATABASE
    sql = '''USE fpdatabase;'''
    cursor.execute(sql)
    cursor.fetchall()

    # CREATE PAGEVIEWS TABLE
    sql = '''
    CREATE TABLE IF NOT EXISTS pageviews (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME DEFAULT NOW(),
    visitor_id CHAR(64) NOT NULL,
    page VARCHAR(100) NOT NULL
    );
    '''
    cursor.execute(sql)
    cursor.fetchall()

    # CREATE PRINTOUTS TABLE
    sql = '''
    CREATE TABLE IF NOT EXISTS printouts (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME DEFAULT NOW(),
    visitor_id CHAR(64) NOT NULL,
    Sds DECIMAL(7,3),
    Wp DECIMAL(7,3),
    units VARCHAR(10),
    R DECIMAL(5,3),
    Omega0 DECIMAL(5,3),
    R_mu DECIMAL(5,3),
    z DECIMAL(7,3),
    h DECIMAL(7,3),
    Ta DECIMAL(5,3),
    Hf DECIMAL(5,3),
    Ip DECIMAL(2,1),
    Car DECIMAL(5,3),
    Rpo DECIMAL(5,3),
    Omegaop DECIMAL(5,3),
    ComponentNumber INT,
    ComponentType VARCHAR(250),
    Fp DECIMAL(9,3),
    OopFp DECIMAL(9,3),
    Title TINYINT,
    Project TINYINT,
    Location TINYINT,
    Client TINYINT,
    Company TINYINT,
    Engineer TINYINT,
    Date TINYINT,
    Notes TINYINT
    );
    '''
    cursor.execute(sql)
    cursor.fetchall()

    # CREATE FEEDBACK TABLE
    sql = '''
    CREATE TABLE IF NOT EXISTS feedback (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME DEFAULT NOW(),
    visitor_id CHAR(64) NOT NULL,
    feedback VARCHAR(10000) NOT NULL
    );
    '''
    cursor.execute(sql)
    cursor.fetchall()


    # COMMIT CHANGES
    cursor.connection.commit()
    cursor.fetchall()

    return cursor



# LOG PAGE VIEWS IN DATABASE
def db_pages(page):
    from flask import request
    from hashlib import sha256

    cursor = db_conn()

    ip_addr = request.access_route[-1]
    ip_addr_hash = sha256(ip_addr.encode('utf-8')).hexdigest()

    sql = f'''
    INSERT INTO pageviews (visitor_id, page)
    VALUES ('{ip_addr_hash}', '{page}');
    '''

    cursor.execute(sql)
    cursor.connection.commit()
    cursor.fetchall()

    return cursor


# LOG PRINTOUT DATA IN DATABASE
def db_printout(cursor, Sds, Wp, units, R, Omega0, R_mu, z, h, Ta, Hf, Ip, Car, Rpo, Omegaop, CompNum, CompType, Fp, OopFp, info_log):
    from flask import request
    from hashlib import sha256

    # cursor = db_conn()

    ip_addr = request.access_route[-1]
    ip_addr_hash = sha256(ip_addr.encode('utf-8')).hexdigest()

    sql = f'''
    INSERT INTO printouts (visitor_id, Sds, Wp, units, R, Omega0, R_mu, z, h, Ta, Hf, Ip, Car, Rpo, Omegaop, ComponentNumber, ComponentType, Fp, OopFp, Title, Project, Location, Client, Company, Engineer, Date, Notes)
    VALUES ('{ip_addr_hash}', '{Sds}', '{Wp}', '{units}', '{R}', '{Omega0}', '{R_mu}', '{z}', '{h}', '{Ta}', '{Hf}', '{Ip}', '{Car}', '{Rpo}', '{Omegaop}', '{CompNum}', '{CompType}', '{Fp}', '{OopFp}', '{info_log[0]}', '{info_log[1]}', '{info_log[2]}', '{info_log[3]}', '{info_log[4]}', '{info_log[5]}', '{info_log[6]}', '{info_log[7]}');
    '''

    cursor.execute(sql)
    cursor.connection.commit()
    cursor.fetchall()
    
    return



# LOG FEEDBACK IN DATABASE
def db_feedback(cursor, feedback):
    from flask import request
    from hashlib import sha256

    # cursor = db_conn()

    ip_addr = request.access_route[-1]
    ip_addr_hash = sha256(ip_addr.encode('utf-8')).hexdigest()

    sql = f'''
    INSERT INTO feedback (visitor_id, feedback)
    VALUES ('{ip_addr_hash}', '{feedback}');
    '''

    cursor.execute(sql)
    cursor.connection.commit()
    cursor.fetchall()
    
    return
