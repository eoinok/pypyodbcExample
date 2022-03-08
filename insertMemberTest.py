import pypyodbc
DBfile = '.\\TennisClub.accdb'
conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+DBfile)
myCursor = conn.cursor()
SQL = "insert into member(firstname, surname, dateofbirth, membertype) values ('Eoin','OK','Senior','01/01/2010')"
row = myCursor.execute(SQL)
myCursor.commit()
print("row inserted")

