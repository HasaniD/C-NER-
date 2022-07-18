import spacy
from spacy import displacy
from pathlib import Path
from flask import Flask, redirect, url_for, render_template, request

#Define flask app
app= Flask(__name__)

#routing
@app.route('/')
def home():
    return render_template("index.html")

#routing
@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

#routing
@app.route('/help')
def cerhelp():
    return render_template("help.html")


#routing
#Creating method for post requests
@app.route('/cner', methods=["POST"])
def cner():
    if request.method == "POST": #check weather the request is post
        txt = request.form["name"] #get the http post request parameter & assign it to a variable
        nlp_ner = spacy.load("model-best") #load ner model
        new = str(txt) #convert txt variable value to string and assign to the 'new' variable
        doc = nlp_ner(new) #pass input valu to the model and assign the prediction to new variable
        html = displacy.render(doc, style="ent",jupyter=False) #visualize the output
        return render_template("index.html", content=html) # send 
    else:
        return "Error! http "

if __name__ == "__main__":
    app.run(host='0.0.0.0')#run flask app