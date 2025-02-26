from flask import Flask, request, render_template, redirect

import mysql.connector

try:
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="student_db"
    )
    print("✅ Database connected successfully!")
    conn.close()
except mysql.connector.Error as err:
    print(f"❌ Database connection failed: {err}")

app = Flask(__name__)

# Database Connection
def get_db_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="student_db"
    )

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        course = request.form["course"]

        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", (name, age, course))
        db.commit()
        cursor.close()
        db.close()

        return redirect("/")
    
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    db.close()

    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

