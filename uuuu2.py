import sqlite3

con = sqlite3.conect('school.sqlite')
cur = con.cursor()

que_insert = '''
INSERT INTO school (name, surname, mark) VALUES
       ('Василий', 'Пупкин', 3)'''

cur.execute(que_insert)
con.commit()

con.close()
