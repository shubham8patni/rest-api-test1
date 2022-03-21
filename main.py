from flask import Flask, flash, redirect, render_template, url_for,request, jsonify


app = Flask(__name__)

# # All the session data is encrypted on the server, thus a asecret key is needed to encrypt and decrypt that data (key should be unpredictable and secret)
app.secret_key = "andhisnameisjohncena"

@app.route("/")
def home(): 
    return "<h3> You can make 3 different calls :</h3> <br> <h4> get sum of list of numbers : add the following to the URL -> <p>&nbsp;</p> /sum/ls=[list of numbers ',' seperated] <br><br> get average of list of numbers : add the following to the URL -> <p>&nbsp;</p> /avg/ls=[list of numbers ',' seperated] <br><br> Find if given value is a palindrome : add the following to the URL -> <p>&nbsp;</p> /palin/ls=[value to be checked] </h4>"

@app.route("/sum/ls=[<lis2>]")
def addition(lis2):
    lis=[]
    # print(lis2)
    # print(type(lis2))
    lis2 = lis2.split(",")
    # print(lis2)
    # print(type(lis2))
    for i in range((len(lis2))):
        if lis2[i]!='':
            lis.append(int(lis2[i])) 
    # print(type(lis))
    if type(lis)!=list:
        result = {
            "Input" : lis,
            "Output" : "Invalid Input, array/list of numbers accepted"
        }
        return jsonify(result)
    if len(lis)<=1:
        result = {
            "Input" : lis,
            "Output" : "Number of values entered are not sufficient"
        }
        return jsonify(result)
    else:
        def sum(ls):
            add = 0
            for i in ls:
                add += i
            return add
        add = sum(lis)
        result = {
            "Input" : lis,
            "Output" : add
        }
        return jsonify(result)
    
@app.route("/avg/ls=[<lis2>]")
def avg(lis2):
    lis=[]
    
    lis2 = lis2.split(",")
    
    for i in range((len(lis2))):
        if lis2[i]!='':
            lis.append(int(lis2[i])) 
   
    if type(lis)!=list:
        result = {
            "Input" : lis,
            "Output" : "Invalid Input, array/list of numbers accepted"
        }
        return jsonify(result)
    if len(lis)<=1:
        result = {
            "Input" : lis,
            "Output" : "Number of values entered are not sufficient"
        }
        return jsonify(result)
    else:
        def averageg(ls:list):
            add = 0
            for i in ls:
                add += i
            return add/(len(ls))
        avrg = averageg(lis)
        result = {
            "Input" : lis,
            "Output" : avrg
        }
        return jsonify(result)
    

@app.route("/palin/ls=[<lis>]")
def palin(lis):

    # print(lis)
    # print(type(lis))

    if type(lis)!=str:
        result = {
            "Input" : lis,
            "Output" : "Invalid Input, string accepted"
        }
        return jsonify(result)
    if len(lis)<=1:
        result = {
            "Input" : lis,
            "Output" : "Number of values entered are not sufficient"
        }
        return jsonify(result)
    else:
        def palindrome(ls):
            if type(ls)==int:
                ls = str(ls)
            if ls == ls[::-1]:
                return "Palindrome"
            else:
                return "Not a Palindrome"
        rs = palindrome(lis)
        result = {
            "Input" : lis,
            "Output" : rs
        }
        return jsonify(result)
    

# @app.route("/sum/<list : n>", methods=["POST", "GET"])
# def addition():
#     if request.method=="POST":
#         lis=[]
#         lis2 = request.form["usr-list"]
#         lis2 = lis2.split(",")
#         for i in range((len(lis2))):
#             if lis2[i]!='':
#                 lis.append(int(lis2[i])) 
#         if len(lis)<=1:
#             flash("Number of values entered are not sufficient")
#             return render_template("index.html" ,solution = "")
#         else:
#             def sum(ls):
#                 add = 0
#                 for i in ls:
#                     add += i
#                 print(add)
#                 return add
#             add = sum(lis)
#             result = {
#                 "List of Numbers" : lis,
#                 "Sum" : add
#             }
#             solution = jsonify(result)
#             return render_template("index.html" , solution = solution)
#     else:
#         return render_template("index.html", solution = "")

if __name__ == "__main__":
    app.run(debug=True)
