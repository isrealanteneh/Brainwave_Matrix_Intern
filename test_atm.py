from unittest import mock
from atm import auth , deposite 


def main():
    test_non_numeric_input_deposit()
    test_non_numeric_pin_auth()

# test auth function if it return None for non numeric inputs
def test_non_numeric_pin_auth(): 
    with mock.patch('builtins.input', return_value="non_numeric_input"):
        assert auth() == None

# test deposite function if it return None for non numeric inputs
def test_non_numeric_input_deposit():
    with mock.patch('builtins.input', return_value="$50"):
        assert deposite("invalid data") == None


if __name__ == "__main__":
    main()