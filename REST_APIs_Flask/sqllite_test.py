import sqlite3


connection = sqlite3.connect('data.db')
cursor = connection.cursor() #Resposible for executing query and store the result

create_table ="CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users =[
    (2, 'adam', 'as2df'),
    (3, 'piotr', 'as23df'),
    (4, 'wojciech', 'a32sdf')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()