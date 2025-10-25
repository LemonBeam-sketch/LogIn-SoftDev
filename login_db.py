from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        role = request.form.get("role")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        student_num = request.form.get("student_num")
        password = request.form.get("password")

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="AttendScan_DB"
        )
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            last_name VARCHAR(255),
            email VARCHAR(255),
            student_num CHAR(7)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS instructors (
            id INT AUTO_INCREMENT PRIMARY KEY,
            last_name VARCHAR(255),
            email VARCHAR(255),
            password VARCHAR(255)
        )
        """)

        if role == "student":
            student_num = request.form.get("student_num")
            cursor.execute(
                "INSERT INTO students (last_name, email, student_num) VALUES (%s, %s, %s)",
                (last_name, email, student_num)
            )
        elif role == "instructor":
            password = request.form.get("password")
            cursor.execute(
                "INSERT INTO instructors (last_name, email, password) VALUES (%s, %s, %s)",
                (last_name, email, password)
            )

        conn.commit()
        cursor.close()
        conn.close()

        return "Data successfully inserted!"

    return render_template('login_module.html')

if __name__ == '__main__':
    app.run(debug=True)