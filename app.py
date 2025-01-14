from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the homepage
@app.route("/")
def home():
    return render_template("home.html")

# Route for the services page
@app.route("/services")
def services():
    return render_template("services.html")

# Route for the about page
@app.route("/about")
def about():
    return render_template("about.html")

# Route for the contact page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        # Here, you can save the information or send it via email
        return render_template("thank_you.html", name=name)
    return render_template("contact.html")

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
