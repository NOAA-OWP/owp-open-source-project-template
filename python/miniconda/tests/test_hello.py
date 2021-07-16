import pytest
from hello.hello import greet

def test_greet():
    # Create a greeting
    greeting = greet("Jo")

    # Check the greeting
    assert greeting == "Hello, Jo!"
