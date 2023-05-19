import pytest
from rcpch_nhs_numbers.nhs_number_validator import validate_nhs_number
from rcpch_nhs_numbers.nhs_number_generator import (
    generate_nhs_numbers,
    generate_nhs_number,
)

# thanks to Dan Bayley for providing the gold standards
test_nhs_numbers = [
    7219208987,
    6023056105,
    6499348333,
    8622085937,
    8855413465,
    3876061172,
    7019824153,
    3403811735,
    5198697451,
    5155090784,
    1348060298,
    7960811202,
    7304865075,
    6330269564,
    5352037886,
    9647299494,
    5670034597,
    5526797627,
    2235993982,
    1715364112,
    4831805769,
    9483312078,
    6567229071,
    7322045645,
    9150002023,
    6936542476,
    2661183736,
    4743776392,
    2555520821,
    8826558299,
    9503873851,
    8359369895,
    8600256887,
    4310116523,
    7109962636,
    4892756237,
    9925708958,
    3724283164,
    8873862292,
    8166387751,
    8467609117,
    4069273557,
    6619845657,
    2857741731,
    5647080170,
    9551028481,
    5952295622,
    5621753798,
    1963876512,
    1907223630,
]


@pytest.mark.parametrize("n", test_nhs_numbers)
def test_nhs_number_validation(n):
    """
    Tests validation function against 50 gold standards
    """
    assert validate_nhs_number(n)


def test_generate_nhs_number():
    """
    Generates an NHS numbers and then tests its validity
    """
    generated_number = generate_nhs_number()
    assert validate_nhs_number(generated_number)


def test_generate_nhs_numbers():
    """
    Generates 50 NHS numbers and then tests their validity
    """
    generated_number_list = generate_nhs_numbers(50)
    fail = False
    for i in generated_number_list:
        if validate_nhs_number(i):
            pass
        else:
            fail = True

    assert fail == False
