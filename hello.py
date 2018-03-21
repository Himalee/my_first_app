from flask import Flask, render_template, request

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

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"]) #methods specified as post get vs post. see in terminal - get and post.
                                        #Get- give me the webpage that I am looking for.
                                        #Post- I want to give the server some information to do something with
                                        #needed to be a post because it is receiving form data
                                        #get is the default 
def sign_up():
    form_data = request.form
    print form_data["email"] #must match id in html(input type)
    return "All OK"

app.run(debug=True) #runs application
