from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=""
)
cursor = db.cursor(dictionary=True)

# Example route to fetch data from MySQL
@app.route('/absensi', methods=['GET'])
def get_users():
    cursor.execute("SELECT * FROM absensi")
    users = cursor.fetchall()
    return jsonify(users)

# POST endpoint to insert a new record into absensi table
@app.route('/absensi', methods=['POST'])
def add_absensi():
    data = request.get_json()

    nama = data.get('nama')
    tanggal = data.get('tanggal')
    status = data.get('status')

    if not nama or not tanggal or not status:
        return jsonify({'error': 'Missing data'}), 400

    # try:
    #     # Convert tanggal to datetime object
    #     tanggal = datetime.strptime(tanggal, '%Y-%m-%d')
    # except ValueError:
    #     return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

    query = "INSERT INTO absensi (nama, tanggal, status) VALUES (%s, %s, %s)"
    values = (nama, tanggal, status)

    cursor.execute(query, values)
    db.commit()

    return jsonify({'message': 'Record added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)