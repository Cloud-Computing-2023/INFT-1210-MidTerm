from flask import Flask

app = Flask(__name__)
# COSC-1209 Implementing Devops Solution- Pipeline on ECS
# Define your student ID number
student_id = "100873273"

# Define your name
developer_name = "Viviana Lopes"

# Define company name
company_name = "Wild Rydes"

# Define route to display company name, developer's name, and student ID
@app.route('/')
def about():
    return f"Company Name: {company_name}<br>" \
           f"Developer: {developer_name}<br>" \
           f"Student ID: {student_id}"

if __name__ == '__main__':
    app.run(debug=True)
