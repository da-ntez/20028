from os import name
from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

# Database connection configuration
server = 'your_server_name.database.windows.net'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'
driver = '{ODBC Driver 17 for SQL Server}'

@app.route('/api/admission', methods=['POST'])
def handle_admission():
    try:
        # Get admission data from the request
        data = request.form
        full_name = data.get('name')
        next_of_kin = data.get('nextOfKin')
        marks_attained = data.get('marks')
        county = data.get('county')
        ethnicity = data.get('ethnicity')
        phone_number = data.get('phone number')
        nationality = data.get('nationality')
        id_no = data.get('ID no')

        # Establish a connection to the Azure SQL Database
        connection = pyodbc.connect(
            'DRIVER=' + driver +
            ';SERVER=' + server +
            ';PORT=1433;DATABASE=' + database +
            ';UID=' + username +
            ';PWD=' + password)

        cursor = connection.cursor()

        # Insert data into the database
        insert_query = """
        INSERT INTO Admission (FullName, NextOfKin, MarksAttained, County, Ethnicity, PhoneNumber, Nationality, IDNo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (full_name, next_of_kin, marks_attained, county, ethnicity, phone_number, nationality, id_no))

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({'message': 'Admission data saved successfully'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
