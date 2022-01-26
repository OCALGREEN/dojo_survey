from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 

class LogIn:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

# Create
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        result = connectToMySQL("dojos_survey_schema").query_db(query, data)
        return result

    @staticmethod
    def validator(check):
        is_valid = True
        if len(check["name"]) < 1:
            flash("Please enter a name")
            is_valid = False
        if len(check["location"]) < 1:
            flash("Please enter a location")
            is_valid = False
        if len(check["language"]) < 1:
            flash("Please enter a language")
            is_valid = False
        if len(check["comment"]) < 1:
            flash("Please enter a comment")
            is_valid = False
        return is_valid 