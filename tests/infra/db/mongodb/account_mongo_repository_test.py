from faker import Faker
import mongomock
import pytest
from unittest.mock import patch

from src.domain.params import AddAccountParams
from src.infra.db.mongodb import AccountMongoRepository, mongohelper

from ....domain.mocks import mock_add_account_params


class TestAccountMongoRepository:
    # SetUp
    faker = Faker()
    params: AddAccountParams = mock_add_account_params()
    mongohelper.connect(mongomock.MongoClient())

    def make_sut(self) -> AccountMongoRepository:
        return AccountMongoRepository()

    @pytest.fixture
    def clear_db(self) -> None:
        collection = mongohelper.get_collection(collection='accounts')
        collection.delete_many({})

    def test_1_should_return_true_on_success(self, clear_db):
        sut = self.make_sut()
        is_valid = sut.add(dict(self.params))

        assert is_valid

    @patch('src.infra.db.mongodb.AccountMongoRepository.add')
    def test_2_should_return_false_on_fail(self, mocker, clear_db):
        mocker.return_value = False

        sut = self.make_sut()
        is_valid = sut.add(dict(self.params))

        assert is_valid is False

    def test_3_should_return_true_if_email_is_valid(self, clear_db):
        sut = self.make_sut()
        collections = mongohelper.get_collection(collection='accounts')
        collections.insert_one(self.params)
        exists = sut.check_by_email(self.params['email'])

        assert exists

    @patch('src.infra.db.mongodb.AccountMongoRepository.check_by_email')
    def test_4_should_return_false_if_email_is_not_valid(self, mocker, clear_db):
        mocker.return_value = False
        sut = self.make_sut()
        collections = mongohelper.get_collection(collection='accounts')
        collections.insert_one(self.params)
        exists = sut.check_by_email(self.params['email'])

        assert exists is False

    def test_5_should_return_an_account_on_success(self, clear_db):
        sut = self.make_sut()
        collections = mongohelper.get_collection(collection='accounts')
        collections.insert_one(self.params)
        account = sut.load_by_email(self.params['email'])

        assert account
        assert account['id']
        assert account['name'] == self.params['name']
        assert account['password'] == self.params['password']

    def test_6_should_return_None_if_load_by_email_fails(self, clear_db):
        sut = self.make_sut()
        account = sut.load_by_email(self.params['email'])

        assert account is None

    def test_7_should_update_account_access_token_on_success(self, clear_db):
        sut = self.make_sut()
        collections = mongohelper.get_collection(collection='accounts')
        inserted_params = collections.insert_one(self.params)
        fake_account = collections.find_one({'_id': inserted_params.inserted_id})

        assert not fake_account.get('access_token')

        access_token = self.faker.uuid4()
        sut.update_access_token(user_id=fake_account['_id'], token=access_token)
        account = collections.find_one({'_id': inserted_params.inserted_id})

        assert account
        assert account['access_token'] == access_token

    def test_8_should_return_an_account_on_load_by_token_without_role(self, clear_db):
        access_token = self.faker.uuid4()
        sut = self.make_sut()
        collections = mongohelper.get_collection(collection='accounts')
        collections.insert_one({**self.params, 'access_token': access_token})
        account = sut.load_by_token(access_token)

        assert account
        assert account['id']

    def test_9_should_return_an_account_on_load_by_token_with_admin_role(self, clear_db):
        access_token = self.faker.uuid4()
        sut = self.make_sut()
        collections = mongohelper.get_collection(collection='accounts')
        collections.insert_one({
            **self.params,
            'access_token': access_token,
            'role': 'admin'
        })
        account = sut.load_by_token(access_token, 'admin')

        assert account
        assert account['id']

    def test_10_should_return_None_on_load_by_token_with_invalid_role(self, clear_db):
        access_token = self.faker.uuid4()
        sut = self.make_sut()
        collections = mongohelper.get_collection(collection='accounts')
        collections.insert_one({
            **self.params,
            'access_token': access_token,
        })
        account = sut.load_by_token(access_token, 'admin')

        assert account is None
