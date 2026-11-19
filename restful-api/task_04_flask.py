#!/usr/bin/python3
"""simple api implementation using flash module"""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """welcome message"""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """list of user names"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """status check - returns ok if working"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """returns user if they exist"""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """adds a new user if receiving valid data"""
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "Invalid JSON"}), 400
    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = payload
    return jsonify({"message": "User added", "user": payload}), 201


if __name__ == "__main__":
    app.run()
