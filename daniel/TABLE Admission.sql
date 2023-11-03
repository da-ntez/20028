from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name)

# Database connection configuration
server = 'mwangi'
database = 'mwang'
username = 'your_username'
password = 'your_password'
driver = '{ODBC Driver 17 for SQL Server}'  # Use the appropriate ODBC driver

@app.route('/api/admission', methods=['POST'])
def handle_admission():
    try:
        # Get admission data from the request
        data = request.form
        full_name = data.get('full_name')
        next_of_kin = data.get('next_of_kin')
        marks_attained = data.get('marks_attained')
        county = data.get('county')
        ethnicity = data.get('ethnicity')

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
        INSERT INTO Admission (FullName, NextOfKin, MarksAttained, County, Ethnicity)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (full_name, next_of_kin, marks_attained, county, ethnicity))

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({'message': 'Admission data saved successfully'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
