from http import HTTPStatus
from flask import jsonify, request
from flask_restful import Resource, reqparse
from mongoengine import NotUniqueError
from application.models import UserModel
import re

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('last_name',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('cpf',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('birth_date',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )


class Users(Resource):
    def get(self):
        cpf = request.args.get('cpf')
        email = request.args.get('email')

        if not cpf and not email:
            return jsonify(UserModel.objects())

        if cpf and email:
            user = UserModel.objects(cpf=cpf, email=email).first()
        elif cpf:
            user = UserModel.objects(cpf=cpf).first()
        elif email:
            user = UserModel.objects(email=email).first()

        if not user:
            return {"message": "User does not exist!"}, HTTPStatus.NOT_FOUND

        return jsonify(user)


class User(Resource):

    def validate_cpf(self, cpf):

        # Has the correct mask?
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            return False

        # Grab only numbers
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Does it have 11 digits?
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validate first digit after -
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9],
                                                  range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validate second digit after -
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10],
                                                  range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True

    def post(self):
        data = _user_parser.parse_args()

        if not self.validate_cpf(data["cpf"]):
            return {"message": "CPF is not valid!"}, HTTPStatus.BAD_REQUEST

        try:
            response = UserModel(**data).save()
            msg = {"message": "User %s successfully created!" % response.id}
            return msg, HTTPStatus.CREATED
        except NotUniqueError as e:
            return {"message": str(e)}, HTTPStatus.BAD_REQUEST
