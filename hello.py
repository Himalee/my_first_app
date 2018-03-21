from flask import Flask, render_template

app = Flask("MyApp")

#relative route:

@app.route("/") #decorator, route path?
def hello():
    return "Hello Himalee!"

@app.route("/idontexist") #new route for different urls
def hello2():
    return "I exist now"

@app.route("/himalee")
def desert():
    return "I love tiramisu!"

app.run(debug=True) #runs application
