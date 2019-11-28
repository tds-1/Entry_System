import os
import smtplib
from flask_mail import Mail, Message
from flask import Flask, render_template, request, redirect, jsonify, make_response
import flask
import random
import sqlite3 as sql
from twilio.rest import Client
app = Flask(__name__, static_folder="static_dir")

# debug mode on
client = Client('AC63723ce152ee2dac596879db1440f45e', '1ef774ac3e2fd39789355e3fe36fa64d')
if __name__ == "__main__":
	app.run(debug=True)
	
def resetdb():
	with sql.connect("hack.db") as con:
		cur=con.cursor()
		cur.execute("delete from host")
	con.close()

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'innovaccercheckout@gmail.com',
    MAIL_PASSWORD = 'innovaccer123',
))

mymail = Mail(app)


@app.route("/", methods=["GET"])
def first_page():
	return render_template("main.html")

@app.route("/host", methods=["GET"])
def fun_get():
	return render_template("host.html")

@app.route("/host", methods=["POST"])
def fun_get_post():
	name=request.form["name"]
	Phone_Number=request.form["Phone_Number"]
	email=request.form["email"]
	flag=0
	with sql.connect("innovaccer.db") as con:
		cur=con.cursor()
		if(len(cur.execute("select * from host where name=(?) and phone_number=(?) and email=(?) ",[name,Phone_Number,email]).fetchall())==0):
			cur.execute("INSERT INTO host (name,phone_number,email) Values (?,?,?)",[name,Phone_Number,email])
			print ("new host added")
			flag="new host added"
			#toast new host added
		else:
			print ("host already exists")
			flag="host already exists"
			#toast host already exists
	con.close()
	return render_template("toast.html",toas=flag)


@app.route("/visitor", methods=["GET"])
def visit_get():
	id=request.args.get('id')
	if id is None:
		cid=[]
		with sql.connect("innovaccer.db") as con:
			cur=con.cursor()
			cid=cur.execute("select hostid, name, phone_number, email from host").fetchall()
		con.close()
		
		return render_template("visitor.html",msg=cid)
	else:
		cid=[]
		xyz=[]
		with sql.connect("innovaccer.db") as con:
			cur=con.cursor()
			cid=cur.execute("select distinct name, email, phone_number,visitorid from visitor where hostid=(?)",[id]).fetchall()
			xyz=cur.execute("select distinct name from host where hostid=(?)",[id]).fetchone()
			print ("**************************",cid)
		con.close()
		print (cid)
		return render_template("specific_person.html",msg=cid,hostid=id,name=xyz[0])


@app.route("/visitor", methods=["POST"])
def visitor_delete():
	id=request.args.get('id')
	cid=[]
	with sql.connect("innovaccer.db") as con:
		cur=con.cursor()
		cur.execute("delete from host where hostid=(?)",[id])
		cur.execute("delete from visitor where hostid=(?)",[id])
		cid=cur.execute("select hostid, name, phone_number, email from host").fetchall()
	con.close()
	return render_template("visitor.html",msg=cid)

@app.route("/visitor/addnewvisitor", methods=["GET"])
def addnewvisitor():
	id=request.args.get('id')
	print("id=="+id)
	return render_template("addnewvisitor.html",hostid=id)



@app.route("/visitor/addnewvisitor", methods=["POST"])
def addnewvisitor_post():
	
	id=request.args.get('id')
	name=request.form["name"]
	Phone_Number=request.form["Phone_Number"]
	email=request.form["email"]
	print (name,Phone_Number,email)
	cid=[]
	query=[]
	xyz=[]
	hostmail=""
	with sql.connect("innovaccer.db") as con:
		cur=con.cursor()
		cur.execute("INSERT INTO visitor (name,phone_number,email,hostid,check_in) Values (?,?,?,?,datetime('now', 'localtime') )",[name,Phone_Number,email,id])
		cid=cur.execute("select distinct name,email,phone_number,visitorid,hostid from visitor where hostid=(?)",[id]).fetchall()
		xyz=cur.execute("select email,phone_number,name from host where hostid=(?)",[id]).fetchone()
		hostmail=xyz[0]
		print ("cid+++++++",cid)
	con.close()
	message=("New Visitor details: \n1. Name: "+name+
		"\n2. Phone: "+ Phone_Number+
		"\n3. Email: "+email
		)
	# print (message)
	
	client.messages.create(from_='+13202798033', to='+919799968212', body=message)
	

	return render_template("specific_person.html",msg=cid,hostid=id,name=xyz[2])




@app.route("/visitor/checkout", methods=["GET","POST"])
def checkout():
	id=request.args.get('id')
	print ("YES! we are here"+str(id))
	with sql.connect("innovaccer.db") as con:
		cur=con.cursor()
		cur.execute("UPDATE visitor SET check_out=datetime('now', 'localtime') where visitorid=(?)",[id])
	con.close()
	query=[]
	qu=[]
	with sql.connect("innovaccer.db") as con:
		cur=con.cursor()
		query=cur.execute("select * from visitor where visitorid=(?)",[id]).fetchone()
		print (query)
		qu=cur.execute("select * from host where hostid=(?)",[query[1]]).fetchone()
		print (qu)

	con.close()
	visitormail=query[3]
	# print (query[0][6])
	message=("Meeting Details:\n1. Name: "+query[2]+
		"\n2. Phone: "+ query[4]+
		"\n3. Check-in time: "+query[5]+
		"\n4. Check-out time: "+query[6]+
		"\n5. Host name: "+qu[1]+
		"\n6. Host email: "+qu[3]
		)
	# print (message)

	msg = Message("User Info",#subject
		sender=("Admin", "innovaccercheckout@gmail.com"), 
		recipients=[visitormail],
		body=message)
	mymail.send(msg)

	client.messages.create(from_='+13202798033', to='+919799968212', body=message)
 
	with sql.connect("innovaccer.db") as con:
		cur=con.cursor()
		cur.execute("delete from visitor where visitorid=(?)",[id])

	con.close()

	return render_template("checkout.html",hostid=id)

@app.route("/about", methods=["GET","POST"])
def about():
	return redirect("https://www.linkedin.com/in/tanmay-deep-sharma-696124148/")
