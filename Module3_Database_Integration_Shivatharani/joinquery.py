import mysql.connector
import time

conn = mysql.connector.connect(

    host="localhost",

    user="root",

    password="shivatharani@17",

    database="college_db"
)

cursor = conn.cursor()

start = time.time()

cursor.execute("""

SELECT

e.enrollment_id,

s.first_name,

s.last_name,

c.course_name

FROM enrollments e

JOIN students s

ON e.student_id=s.student_id

JOIN courses c

ON e.course_id=c.course_id

""")

rows = cursor.fetchall()

end = time.time()

print("Queries Executed = 1")

print("Execution Time =", end-start)

for row in rows:

    print(row)

conn.close()