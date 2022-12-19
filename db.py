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
    # sql = sql + '''
    # CREATE TABLE IF NOT EXISTS printouts (
    # id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    # timestamp TIMESTAMP DEFAULT NOW(),
    # ip_address VARCHAR(100) NOT NULL,
    # page_name VARCHAR(100) NOT NULL,
    # Sds
    # Wp
    # units
    # R
    # Omega0
    # R_mu
    # z
    # h
    # Ta
    # Hf
    # Ip
    # Car
    # Rpo
    # Omegaop
    # CompNum
    # CompType
    # Fp
    # OopFp
    # )
    # '''
    # cursor.execute(sql)
    # cursor.fetchall()



    # COMMIT CHANGES
    cursor.execute(sql)
    cursor.connection.commit()
    cursor.fetchall()

    return cursor






# LOG PAGE VIEWS IN DATABASE
def db_pages(page):
    from flask import request

    cursor = db_conn()

    ip_addr = request.remote_addr

    sql = f'''
    INSERT INTO pageviews (ip_address, page)
    VALUES ('{ip_addr}', '{page}');
    '''

    cursor.execute(sql)
    cursor.connection.commit()
    cursor.fetchall()
    
    return