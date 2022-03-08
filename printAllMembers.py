import pypyodbc
DBfile = '.\\TennisClub.accdb'
conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+DBfile)
myCursor = conn.cursor()
SQL = "select * from member"
rows = myCursor.execute(SQL)
for row in rows: # cursors are iterable
    print(row[1],row[2],row[3],row[4])

