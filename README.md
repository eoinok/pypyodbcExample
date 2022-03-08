# pypyodbc Example - Save and Retrieve data from an MSAccess Database

This example allows you to both insert data into a Microsoft Access Database and retrieve Data from a Microsoft Access Database

The example requires you to install pypyodbc which is a pure python implementation of a wrapper to the native OS odbc drivers.

To to be able to use this example you must have Microsoft Access installed. The example uses the Microsoft Access Driver (*.mdb, *.accdb) 

This driver is installed on Windows when you install Microsoft Access.

In order to install pypyodc type the following line from within your Command Line Interface
(the -t . switches insures that pypyodbc is installed into the current folder)

```
pip install pypyodbc -t .
```

Once this package is installed you can try the programs insertTCMemberTest.py and printAllMembers.py

The programs should insert a new member of the tennis club into the table called member and print all the members of the club to the screen.

# Part 1

Adapt a previous TKInter GUI Interface you have built to allow it to capture details about a new member of the Tennisclub database as follows

![alt text](TennisGUI.png)

Make sure to add appropriate comments to your program at the beginning indicating the filename, a description, the date and your name.

When you have completed Part 1 make sure to do a git add, git commit and git push.

# Part 2

Take code from the insertTCMemberTest.py and add a function to the GUI Class you have built in part 1 so that when the button is clicked the details of the new Tennis Club member which the user entered are inserted into the Member table of the TennisClub Database

To do this you will need to call the get() method on each of the TKinter entry object to get the values entered by the user, assign the results of each of those get functions to appropriate simple python variables.

Construct a valid SQL insert into statement by concatenating the the variables into the correct positions together with single quotes.

Print the SQL to make sure it looks correct.

When you are happy the SQL would work (you can test it in MSAccess), add the lines which will execute the SQL statements against the ODBC Connection.

When you have completed Part 2 make sure to do a git add, git commit and git push.


# Part 3

Add another function so that when that button is clicked all the Members of the tennis club that are stored in the Member table of the tennisclub database are printed to the Screen

When you have completed Part 3 make sure to do a git add, git commit and git push.

