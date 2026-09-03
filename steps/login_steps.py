from pytest_bdd import scenario


@scenario("../features/login.feature", "Successful login")
def test_successful_login():
    pass