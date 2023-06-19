from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    DB = 'email_schema'
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_email(cls, data):
        query = """
        INSERT INTO emails (email)
        VALUES (%(email)s);
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        return results
    
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM emails
        """

        results = connectToMySQL(cls.DB).query_db(query)

        all_emails = []

        for email in results:
            all_emails.append(cls(email))

        return all_emails

    @staticmethod
    def validate_email(new_email):
        is_valid = True

        if not EMAIL_REGEX.match(new_email['email']):
            flash('Invalid email address')
            is_valid = False
        return is_valid