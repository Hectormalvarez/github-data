import pytest
from main import get_github_credentials
import logging
import os

# Fixture to mock environment variables
@pytest.fixture
def mock_env_vars():
    with pytest.MonkeyPatch().context() as mp:
        mp.setenv('GITHUB_USERNAME', 'testuser')
        mp.setenv('GITHUB_REPOSITORY', 'testrepo')
        mp.setenv('GITHUB_TOKEN', 'testtoken')
        yield

# Test cases for get_github_credentials
test_cases = [
    (
        {'GITHUB_USERNAME': 'testuser', 'GITHUB_REPOSITORY': 'testrepo', 'GITHUB_TOKEN': 'testtoken'},
        {"username": "testuser", "repository": "testrepo", "token": "testtoken"},
        None
    ),
    (
        {'GITHUB_USERNAME': 'testuser', 'GITHUB_REPOSITORY': 'testrepo'},
        {"username": "testuser", "repository": "testrepo", "token": None},
        None
    ),
    (
        {'GITHUB_USERNAME': 'testuser'},
        None,
        "Missing environment variables: GITHUB_REPOSITORY"
    ),
    (
        {'GITHUB_REPOSITORY': 'testrepo'},
        None,
        "Missing environment variables: GITHUB_USERNAME"
    ),
    (
        {},
        None,
        "Missing environment variables: GITHUB_USERNAME, GITHUB_REPOSITORY"
    )
]

@pytest.mark.parametrize("env_vars, expected_output, expected_error", test_cases)
def test_get_github_credentials(env_vars, expected_output, expected_error, caplog):
    with pytest.MonkeyPatch().context() as mp:
        for key, value in env_vars.items():
            mp.setenv(key, value)

        if expected_error:
            with pytest.raises(KeyError) as exc_info:
                get_github_credentials()
            assert str(exc_info.value) == expected_error
        else:
            credentials = get_github_credentials()
            assert credentials == expected_output
