#!/usr/bin/python3
"""API security & Authentication"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt, jwt_required)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "change-this-to-a-long-random-secret-key-123"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"}
}


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """confirm access message"""
    return "Basic Auth: Access Granted"


@auth.verify_password
def verify_password(username, password):
    """confirm valid credentials by returning user name"""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route("/login", methods=["POST"])
def login():
    """returns access token on validation of credentials"""
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    password = payload.get("password")
    user = users.get(username) if isinstance(username, str) else None

    if (user is None or not isinstance(password, str) or
            not check_password_hash(user["password"], password)):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=username,
                                additional_claims={"role": user["role"]})
    return jsonify({"access_token": token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Indicates JWT authorisation is granted"""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """special message for admin login"""
    if get_jwt().get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """error message for missing / invalid token"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """specific invalid token error message"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_data):
    """specific expired token error message"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_data):
    """specific revoked token error message"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_data):
    """specific new token required error message"""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
