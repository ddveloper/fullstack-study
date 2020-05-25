import psycopg2

connection = psycopg2.connect('dbname=mydb')
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS table2;')
cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (2, False))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'
data = {
    'id': 3, 
    'completed': True
    }
cursor.execute(SQL, data)

cursor.execute('SELECT * from table2;')
result = cursor.fetchmany(2)
result2 = cursor.fetchone()
print('fetchmany(2)', result)
print('fetchone', result2)

connection.commit()
cursor.close()
connection.close()