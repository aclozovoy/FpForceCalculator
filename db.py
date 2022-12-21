# CONNECT TO DATABASE
def db_conn():

    import pymysql

    host = 'fp-database.cl7ay4156fuf.us-west-2.rds.amazonaws.com'
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
    ip_address VARCHAR(100) NOT NULL,
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
    ip_address VARCHAR(100) NOT NULL,
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
    TitleLength INT,
    ProjectLength INT,
    LocationLength INT,
    ClientLength INT,
    CompanyLength INT,
    EngineerLength INT,
    DateLength INT,
    NotesLength INT
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

    cursor = db_conn()

    ip_addr = request.access_route[-1]

    sql = f'''
    INSERT INTO pageviews (ip_address, page)
    VALUES ('{ip_addr}', '{page}');
    '''

    cursor.execute(sql)
    cursor.connection.commit()
    cursor.fetchall()

    return cursor


# LOG PRINTOUT DATA IN DATABASE
def db_printout(cursor, Sds, Wp, units, R, Omega0, R_mu, z, h, Ta, Hf, Ip, Car, Rpo, Omegaop, CompNum, CompType, Fp, OopFp, info_log):
    from flask import request

    # cursor = db_conn()

    ip_addr = request.access_route[-1]

    sql = f'''
    INSERT INTO printouts (ip_address, Sds, Wp, units, R, Omega0, R_mu, z, h, Ta, Hf, Ip, Car, Rpo, Omegaop, ComponentNumber, ComponentType, Fp, OopFp, TitleLength, ProjectLength, LocationLength, ClientLength, CompanyLength, EngineerLength, DateLength, NotesLength)
    VALUES ('{ip_addr}', '{Sds}', '{Wp}', '{units}', '{R}', '{Omega0}', '{R_mu}', '{z}', '{h}', '{Ta}', '{Hf}', '{Ip}', '{Car}', '{Rpo}', '{Omegaop}', '{CompNum}', '{CompType}', '{Fp}', '{OopFp}', '{info_log[0]}', '{info_log[1]}', '{info_log[2]}', '{info_log[3]}', '{info_log[4]}', '{info_log[5]}', '{info_log[6]}', '{info_log[7]}');
    '''

    cursor.execute(sql)
    cursor.connection.commit()
    cursor.fetchall()
    
    return



