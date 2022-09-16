from os import name
from tokenize import Number
from flask import Flask,request,jsonify
import json

app = Flask(__name__)
lastMesg = []

TempData = {}

Data = json.load(open('ServerList.json', 'r'))

@app.route("/Servers",methods=["GET","POST"])
def Server():
    if request.method == "GET":
        return json.load(open('ServerList.json', 'r'))
    elif request.method == "POST":
        ServerName = request.form["ServerName"]
        ServerIp = request.form["ServerIp"]
        ServerPort = request.form["ServerPort"]
        Data = json.load(open('ServerList.json', 'r'))
        Data[ServerName] = {}
        Data[ServerName]["ServerName"] = ServerName
        Data[ServerName]["ServerIP"] = ServerIp
        Data[ServerName]["ServerPort"] = ServerPort
        file = open('ServerList.json', "w")
        json.dump(Data,file, indent = 4, sort_keys = False)
        file.close()
        return jsonify(Data)

@app.route("/ServersInfo",methods=["GET","POST"])
def ServersInfo():
    if request.method == "GET":
        return jsonify(TempData)
    elif request.method == "POST":
        ServerID = request.form["ServerID"]
        PlayerAmount = request.form["PlayerAmount"]

        PlayerName = request.form["PlayerName"]
        PlayerSteamID = request.form["PlayerSteamID"]
        Players = {
            "Name":PlayerName,
            "SteamID":PlayerSteamID
        }

        TempData[ServerID] = {
            "PlayerList":{
                "PlayerAmount":PlayerAmount,
                "Players":Players
            }
        }

        return jsonify(TempData)

if __name__ == "__main__":
    app.run(debug=True)
