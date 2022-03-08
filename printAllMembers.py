import pypyodbc
DBfile = '.\\TennisClub.mdb'
#DBfile = '.\\TennisClub.accdb'
#the following line requires 32 bit python and seems to be the only one that works in labs in college
conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ='+DBfile)
#this line will work on 64 bit python idle with 64bit msaccess drivers
#conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+DBfile)
myCursor = conn.cursor()
SQL = "select * from member"
rows = myCursor.execute(SQL)
for row in rows: # cursors are iterable
    print(row[1],row[2],row[3],row[4])

