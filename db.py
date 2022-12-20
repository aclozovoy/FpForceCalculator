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


    # DROP TABLE
    # sql = "DROP TABLE IF EXISTS pageviews"
    # cursor.execute(sql)
    # cursor.fetchall()

    # sql = "DROP TABLE IF EXISTS printouts"
    # cursor.execute(sql)
    # cursor.fetchall()

    # cursor.connection.commit()
    # cursor.fetchall()

 
    # CREATE PAGEVIEWS TABLE
    sql = '''
    CREATE TABLE IF NOT EXISTS pageviews (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT NOW(),
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
    timestamp TIMESTAMP DEFAULT NOW(),
    ip_address VARCHAR(100) NOT NULL,
    Sds DECIMAL(7,3),
    Wp DECIMAL(7,3),
    units VARCHAR(10),
    R DECIMAL(7,3),
    Omega0 DECIMAL(2,1),
    R_mu DECIMAL(2,1),
    z DECIMAL(9,3),
    h DECIMAL(9,3),
    Ta DECIMAL(9,3),
    Hf DECIMAL(9,3),
    Ip DECIMAL(2,1),
    Car DECIMAL(2,1),
    Rpo DECIMAL(2,1),
    Omegaop DECIMAL(2,1),
    ComponentNumber INT,
    ComponentType VARCHAR(250),
    Fp DECIMAL(9,3),
    OopFp DECIMAL(9,3)
    )
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

    return


# LOG PRINTOUT DATA IN DATABASE
def db_printout(Sds, Wp, units, R, Omega0, R_mu, z, h, Ta, Hf, Ip, Car, Rpo, Omegaop, CompNum, CompType, Fp, OopFp):
    from flask import request

    cursor = db_conn()

    ip_addr = request.access_route[-1]

    sql = f'''
    INSERT INTO printouts (ip_address, Sds, Wp, units, R, Omega0, R_mu, z, h, Ta, Hf, Ip, Car, Rpo, Omegaop, ComponentNumber, ComponentType, Fp, OopFp)
    VALUES ('{ip_addr}', '{Sds}', '{Wp}', '{units}', '{R}', '{Omega0}', '{R_mu}', '{z}', '{h}', '{Ta}', '{Hf}', '{Ip}', '{Car}', '{Rpo}', '{Omegaop}', '{CompNum}', '{CompType}', '{Fp}', '{OopFp}');
    '''

    cursor.execute(sql)
    cursor.connection.commit()
    cursor.fetchall()
    
    return



