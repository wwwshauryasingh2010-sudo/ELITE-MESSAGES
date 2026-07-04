from form import reg
from flask import Flask , flash , render_template , redirect,request ,url_for


app=Flask(__name__)
app.config["SECRET_KEY"]="mysecret"




@app.route("/",methods=["POST","GET"])
def home () :
    form=reg()
    if form.validate_on_submit() :
        name=form.name.data
        email=form.email.data
        password=form.password.data
        flash("you had loged in successfully")
        return redirect(url_for("page"))
    return render_template("main.html",form=form)

@app.route("/page",methods=["POST","GET"])
def page():
    #if request.method=="POST":
        #id=request.form.get("id")
        #message=request.form.get("message")
        #flash("your message has been sent successfully")
        #return redirect(url_for("welcome"))

    return render_template("page.html")

if __name__=="__main__":
    app.run(debug=True)