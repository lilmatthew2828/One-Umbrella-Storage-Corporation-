
listOfTablesNames = ["StaffCalendar","Salesperson","MechanicInfo","Vehicles","InvoiceHistory","CustomerInfo","Services_and_Inventory","ServiceSchedule"] # So here im making a list of all the names of the tables
def printList(list = []):
    x = int(0)
    print("List Of The Table Names: ")
    for data in list:
        print(f"{x+1}. {data}")
        x += 1
def printQueries(list = []):
    x = int(0)
    print("\nList of Example Queries For The Entered Table")
    for data in list:
        print(f"{x+1}. {data}")
        x += 1 
tableToShow = str()
def getTableName():
    table_name = str(input("Enter in a table name you would like to read from: "))
    return table_name











print()

from flask import Blueprint, render_template, request, redirect, url_for
import csv
import sqlite3
import pandas 
from tabulate import tabulate 
from flask import jsonify
views = Blueprint(__name__, "views")
# Define a function to fetch data from the database
'''
SO WHAT I NEED TO IS MAKE A FUNCTION FOR EACH TABLE THAT PRINTS it table BASED OF ITS QUERY: 
'''
sql_queries_CustomerInfo = [
    "SELECT * FROM CustomerInfo;",
    "SELECT * FROM CustomerInfo WHERE cust_id = customer_id;",
    "SELECT * FROM CustomerInfo WHERE cust_fname = 'first_name';",
    "SELECT * FROM CustomerInfo WHERE cust_lname = 'last_name';",
    "SELECT * FROM CustomerInfo WHERE cust_phonenumber = phone_number;",
    "SELECT * FROM CustomerInfo WHERE cust_address = 'address';",
    "SELECT * FROM CustomerInfo WHERE dob > 'date';",
    "SELECT * FROM CustomerInfo WHERE dob < 'date';",
    "SELECT DISTINCT cust_id FROM CustomerInfo;",
    "SELECT COUNT(*) FROM CustomerInfo;"]
def printQueries(list = []):
    x = int(0)
    print("\nList of Example Queries For The Entered Table")
    for data in list:
        print(f"{x+1}. {data}")
        x += 1 
# printQueries(sql_queries_CustomerInfo)
selected_query7 = "SELECT * from CustomerInfo ORDER BY cust_lname" 
print()
def fetch_CustomerInfo_data():
    connection = sqlite3.connect('Official_DB.db')
    data_frame = pandas.read_sql(selected_query7, connection)
    connection.close()
    return data_frame

@views.route("/fetch_CustomerInfo_data", methods=["GET"])
def fetch_CustomerInfo_data_route():
    CustomerInfo_data = fetch_CustomerInfo_data()
    CustomerInfo_list = CustomerInfo_data.to_dict(orient="records")
    return jsonify(CustomerInfo_list)


# ================================================================================================================================================================================================================================================
sql_queries_invoiceHistory = [
    "SELECT * FROM InvoiceHistory;",
    "SELECT * FROM InvoiceHistory WHERE invoice_id = 'invoice_id';",
    "SELECT * FROM InvoiceHistory WHERE invoice_price = price;",
    "SELECT * FROM InvoiceHistory WHERE service_date = 'YYYYMMDD';",
    "SELECT * FROM InvoiceHistory WHERE service_date < 'YYYYMMDD';",
    "SELECT * FROM InvoiceHistory WHERE service_date > 'YYYYMMDD';",
    "SELECT * FROM InvoiceHistory WHERE invoice_price < value;",
    "SELECT * FROM InvoiceHistory WHERE invoice_price > value;",
    "SELECT DISTINCT invoice_id FROM InvoiceHistory;",
    "SELECT COUNT(*) FROM InvoiceHistory;"]
def printQueries(list = []):
    x = int(0)
    print("\nList of Example Queries For The Entered Table")
    for data in list:
        print(f"{x+1}. {data}")
        x += 1 
# printQueries(sql_queries_invoiceHistory)
selected_query6 = "SELECT * from invoiceHistory" 

def fetch_invoiceHistory_data():
    connection = sqlite3.connect('Official_DB.db')
    data_frame = pandas.read_sql(selected_query6, connection)
    connection.close()
    return data_frame

@views.route("/fetch_invoiceHistory_data", methods=["GET"])
def fetch_invoiceHistory_data_route():
    invoiceHistory_data = fetch_invoiceHistory_data()
    invoiceHistory_list = invoiceHistory_data.to_dict(orient="records")
    return jsonify(invoiceHistory_list)


# ================================================================================================================================================================================================================================================
sql_queries_StaffCalendar = [
    "SELECT * FROM StaffCalendar;",
    "SELECT * FROM StaffCalendar WHERE date_worked = 'YYYYMMDD';",
    "SELECT * FROM StaffCalendar WHERE signin_time > 'HHMM';",
    "SELECT * FROM StaffCalendar WHERE signin_time < 'HHMM';",
    "SELECT * FROM StaffCalendar WHERE signout_time > 'HHMM';",
    "SELECT * FROM StaffCalendar WHERE signout_time < 'HHMM';",
    "SELECT * FROM StaffCalendar WHERE mechanic_id = 'mechanic_id';",
    "SELECT * FROM StaffCalendar WHERE salesperson_id = 'salesperson_id';",
    "SELECT DISTINCT date_worked FROM StaffCalendar;",
    "SELECT COUNT(*) FROM StaffCalendar;"]
def printQueries(list = []):
    x = int(0)
    print("\nList of Example Queries For The Entered Table")
    for data in list:
        print(f"{x+1}. {data}")
        x += 1 
# printQueries(sql_queries_StaffCalendar)
selected_query5 = "SELECT * from StaffCalendar WHERE date_worked = '4172024'" 

def fetch_StaffCalendar_data():
    connection = sqlite3.connect('Official_DB.db')
    data_frame = pandas.read_sql(selected_query5, connection)
    connection.close()
    return data_frame

@views.route("/fetch_StaffCalendar_data", methods=["GET"])
def fetch_StaffCalendar_data_route():
    StaffCalendar_data = fetch_StaffCalendar_data()
    StaffCalendar_list = StaffCalendar_data.to_dict(orient="records")
    return jsonify(StaffCalendar_list)


# ================================================================================================================================================================================================================================================

sql_queries_ServiceSchedule = [
    "SELECT * FROM ServiceSchedule;",
    "SELECT * FROM ServiceSchedule WHERE service_date = 'service_date';",
    "SELECT * FROM ServiceSchedule WHERE services = 'service_name';",
    "SELECT * FROM ServiceSchedule WHERE parts = 'part_name';",
    "SELECT * FROM ServiceSchedule WHERE service_date < 'YYYYMMDD';",
    "SELECT * FROM ServiceSchedule WHERE service_date > 'YYYYMMDD';",
    "SELECT DISTINCT service_date FROM ServiceSchedule;",
    "SELECT COUNT(*) FROM ServiceSchedule;"]
def printQueries(list = []):
    x = int(0)
    print("\nList of Example Queries For The Entered Table")
    for data in list:
        print(f"{x+1}. {data}")
        x += 1 
# printQueries(sql_queries_ServiceSchedule)
selected_query4 = "SELECT * from ServiceSchedule" 

def fetch_ServiceSchedule_data():
    connection = sqlite3.connect('Official_DB.db')
    data_frame = pandas.read_sql(selected_query4, connection)
    connection.close()
    return data_frame

@views.route("/fetch_ServiceSchedule_data", methods=["GET"])
def fetch_ServiceSchedule_data_route():
    ServiceSchedule_data = fetch_ServiceSchedule_data()
    ServiceSchedule_list = ServiceSchedule_data.to_dict(orient="records")
    return jsonify(ServiceSchedule_list)


# ================================================================================================================================================================================================================================================
sql_queries_MechanicInfo = [
    "SELECT * FROM MechanicInfo;",
    "SELECT * FROM MechanicInfo WHERE mechanic_id = 'mechanic_id';",
    "SELECT * FROM MechanicInfo WHERE mech_fname = 'first_name';",
    "SELECT * FROM MechanicInfo WHERE mech_lname = 'last_name';",
    "SELECT * FROM MechanicInfo WHERE date_worked < 'YYYYMMDD';",
    "SELECT * FROM MechanicInfo WHERE date_worked > 'YYYYMMDD';",
    "SELECT DISTINCT mechanic_id FROM MechanicInfo;",
    "SELECT COUNT(*) FROM MechanicInfo;"]
def printQueries(list = []):
    x = int(0)
    print("\nList of Example Queries For The Entered Table")
    for data in list:
        print(f"{x+1}. {data}")
        x += 1 
# printQueries(sql_queries_MechanicInfo)
selected_query = 'SELECT * from MechanicInfo ORDER BY mech_lname' 
def fetch_mechanic_data():
    connection = sqlite3.connect('Official_DB.db')
    data_frame = pandas.read_sql(selected_query, connection)
    connection.close()
    return data_frame

@views.route("/fetch_mechanic_data", methods=["GET"])
def fetch_mechanic_data_route():
    mechanics_data = fetch_mechanic_data()
    mechanics_list = mechanics_data.to_dict(orient="records")
    return jsonify(mechanics_list)
    
# ================================================================================================================================================================================================================================================








sql_queries_Salesperson = [
    "SELECT * FROM Salesperson;",
    "SELECT * from MechanicInfo ORDER BY mech_lname",
    "SELECT salesperson_id, sp_fname, sp_lname FROM Salesperson;",
    "SELECT * FROM Salesperson WHERE sp_fname = 'John';",
    "UPDATE Salesperson SET sp_fname = 'Robert' WHERE salesperson_id = 2;",
    "DELETE FROM Salesperson WHERE salesperson_id = 3;"]

def printQueries(list = []):
    x = int(0)
    print("\nList of Example Queries For The Entered Table")
    for data in list:
        print(f"{x+1}. {data}")
        x += 1 
# printQueries(sql_queries_Salesperson)
selected_query2 = 'SELECT * from Salesperson ORDER BY salesperson_id LIMIT 3' 
def fetch_Salesperson_data():
    connection = sqlite3.connect('Official_DB.db')
    data_frame = pandas.read_sql(selected_query2, connection)
    connection.close()
    return data_frame

@views.route("/fetch_Salesperson_data", methods=["GET"])
def fetch_Salesperson_data_route():
    Salesperson_data = fetch_Salesperson_data()
    Salesperson_list = Salesperson_data.to_dict(orient="records")
    return jsonify(Salesperson_list)









# ================================================================================================================================================================================================================================================
sql_queries_Services_Inventory = [ 
    "SELECT * FROM Services_and_Inventory;",
    "SELECT * FROM Services_and_Inventory WHERE services = 'service_name';",
    "SELECT * FROM Services_and_Inventory WHERE parts_amount > value;",
    "SELECT * FROM Services_and_Inventory WHERE parts LIKE '%keyword%';",
    "SELECT DISTINCT services FROM Services_and_Inventory;",
    "SELECT COUNT(*) FROM Services_and_Inventory;",
    "SELECT SUM(parts_amount) FROM Services_and_Inventory;",
    "SELECT AVG(parts_amount) FROM Services_and_Inventory;",
    "SELECT MAX(parts_amount) FROM Services_and_Inventory;",
    "SELECT MIN(parts_amount) FROM Services_and_Inventory;"]

selected_query3 = "SELECT * from Services_and_Inventory;" 
def fetch_Services_Inventory():
     connection = sqlite3.connect('Official_DB.db')
     data_frame = pandas.read_sql(selected_query3, connection)
     connection.close()
     return data_frame
@views.route("/fetch_Services_Inventory", methods=["GET"])
def fetch_Services_Inventory_data_route():
    Services_Inventory_data = fetch_Services_Inventory()
    Services_Inventory_list = Services_Inventory_data.to_dict(orient="records")
    return jsonify(Services_Inventory_list)
# ================================================================================================================================================================================================================================================
sql_queries_vehicles = [
    "SELECT * FROM Vehicles;",
    "SELECT * FROM Vehicles WHERE vin_number = 'vin_number';",
    "SELECT * FROM Vehicles WHERE car_price = price;",
    "SELECT * FROM Vehicles WHERE vehicle_make = 'make';",
    "SELECT * FROM Vehicles WHERE vehicle_model = 'model';",
    "SELECT * FROM Vehicles WHERE vehicle_year = year;",
    "SELECT * FROM Vehicles WHERE car_price < value;",
    "SELECT * FROM Vehicles WHERE car_price > value;",
    "SELECT DISTINCT vin_number FROM Vehicles;",
    "SELECT COUNT(*) FROM Vehicles;"]
def fetch_vehicle_data():
    connection = sqlite3.connect('Official_DB.db')
    dataframe_example = pandas.read_sql("SELECT * from Vehicles", connection)
    connection.close()
    return dataframe_example
@views.route("/fetch_vehicle_data", methods=["GET"])
def fetch_vehicle_data_route():
    vehicle_data = fetch_vehicle_data()
    vehicle_list = vehicle_data.to_dict(orient="records")
    return jsonify(vehicle_list)
# ================================================================================================================================================================================================================================================

@views.route("/")
def home():
    return render_template("index_work.html")

@views.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
       
        email = request.form.get("email")
        password = request.form.get("password")
        
        
        if email == "mattkilp5@gmail.com" and password == "matt":
            return "Login successful" 
        else:
            return "Invalid email or password"  

    else:
        
        return render_template("login.html")
@views.route("/vechicles")
def vehicles():
    return render_template("Vechicles.html")