import mysql.connector
import time

print("Program Started")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shivatharani@17",
    database="college_db"
)

print("Connected Successfully")

cursor = conn.cursor()

query_count = 0

start = time.time()

# Query 1
cursor.execute("SELECT * FROM enrollments")

query_count += 1

enrollments = cursor.fetchall()

print("\nEnrollments Found:", len(enrollments))

# N additional queries
for e in enrollments:

    student_id = e[1]

    cursor.execute(
        "SELECT first_name,last_name FROM students WHERE student_id=%s",
        (student_id,)
    )

    student = cursor.fetchone()

    print(student)

    query_count += 1

end = time.time()

print("\nTotal Queries Executed =", query_count)

print("Execution Time =", end-start)

conn.close()