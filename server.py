from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<page>")
def page(page):
    return render_template(page)

def write_to_file(data):
    with open("database.txt", mode="a") as database:
        database.write(f"{data['email']}, {data['subject']}, {data['message']}\n")

def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database:
        writer = csv.writer(database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([data["email"], data["subject"], data["message"]])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            write_to_csv(request.form.to_dict())
            return redirect("thankyou.html")
        except:
            return "Error! Did not save to database."
    return "Error!"