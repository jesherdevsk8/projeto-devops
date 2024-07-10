import pytest

from application import create_app
from tests.seeds import create_users, clear_db_seeds

from faker import Faker
from cpf_generator import CPF


faker = Faker()
cpf = CPF.generate()


@pytest.fixture
def client():
    app = create_app('config.MockConfig')
    return app.test_client()


@pytest.fixture(scope='module', autouse=True)
def setup_module():
    app = create_app('config.MockConfig')
    app.test_client()

    create_users()
    yield
    clear_db_seeds()


@pytest.fixture
def valid_user():
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "cpf": CPF.format(cpf),
        "email": faker.email(),
        "birth_date": faker.date_of_birth(
            tzinfo=None,
            minimum_age=18,
            maximum_age=90
        ).strftime('%Y-%m-%d')
    }


@pytest.fixture
def invalid_user():
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "cpf": CPF.format(cpf)[:-1] + '7',  # invalid CPF
        "email": faker.email(),
        "birth_date": faker.date_of_birth(
            tzinfo=None,
            minimum_age=18,
            maximum_age=90
        ).strftime('%Y-%m-%d')
    }


@pytest.fixture
def user_incorrect_mask():
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "cpf": '11122233344',  # CPF with incorrect mask
        "email": faker.email(),
        "birth_date": faker.date_of_birth(
            tzinfo=None,
            minimum_age=18,
            maximum_age=90
        ).strftime('%Y-%m-%d')
    }


@pytest.fixture
def user_less_digits():
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "cpf": '111.222.333-4',  # CPF with only 10 digits
        "email": faker.email(),
        "birth_date": faker.date_of_birth(
            tzinfo=None,
            minimum_age=18,
            maximum_age=90
        ).strftime('%Y-%m-%d')
    }


@pytest.fixture
def user_same_digits():
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "cpf": '111.111.111-11',  # CPF with same digits
        "email": faker.email(),
        "birth_date": faker.date_of_birth(
            tzinfo=None,
            minimum_age=18,
            maximum_age=90
        ).strftime('%Y-%m-%d')
    }
