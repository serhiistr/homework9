from app import app
from flask import render_template
from models.models import Plant, Salon, Employee



@app.route("/all-info")
def all_info():
    plants = Plant.get_data()
    employees = Employee.get_data()
    salons = Salon.get_data()

    return render_template("all_info.html", plants=plants, employees=employees, salons=salons)





