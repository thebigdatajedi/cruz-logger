from src.utils.buit_ins_helper import BuiltInsHelper


def test_is_built_in_int():
    result = BuiltInsHelper.is_built_in(2)
    assert result


def test_is_built_in_float():
    result = BuiltInsHelper.is_built_in(3.141592653589793238462643383279502884197)
    assert result


def test_is_built_in_str():
    result = BuiltInsHelper.is_built_in('Hello World!')
    assert result


def test_is_built_in_str_two():
    result = BuiltInsHelper.is_built_in("Hello World!")
    assert result


def test_is_built_in_str_three():
    result = BuiltInsHelper.is_built_in('')
    assert result


def test_is_built_in_str_four():
    result = BuiltInsHelper.is_built_in("")
    assert result


def test_is_built_in_str_five():
    something: str = "something good"
    result = BuiltInsHelper.is_built_in(f"{something}")
    assert result


def test_is_built_in_bool():
    result = BuiltInsHelper.is_built_in(True)
    assert result


def test_is_built_in_bool_two():
    result = BuiltInsHelper.is_built_in(False)
    assert result


def test_is_built_in_list():
    quickness = [1, 2, 3]
    result = BuiltInsHelper.is_built_in(quickness)
    assert result


def test_is_built_in_list_two():
    quickness = [1, 2, 3]
    result = BuiltInsHelper.is_built_in(quickness)
    assert result


def test_is_built_in_list_three():
    quickness = []
    result = BuiltInsHelper.is_built_in(quickness)
    assert result


def test_is_built_in_tuple():
    quickness = (1, 2, 3)
    result = BuiltInsHelper.is_built_in(quickness)
    assert result


def test_is_built_in_tuple_two():
    quickness = ('a', 'b', 'c')
    result = BuiltInsHelper.is_built_in(quickness)
    assert result


def test_is_built_in_tuple_three():
    quickness = ()
    result = BuiltInsHelper.is_built_in(quickness)
    assert result


def test_is_built_in_set():
    quickness = {1, 2, 3}
    result = BuiltInsHelper.is_built_in(quickness)
    assert result


def test_is_built_in_set_two():
    quickness = {'a', 'b', 'c'}
    result = BuiltInsHelper.is_built_in(quickness)
    assert result


def test_is_built_in_set_three():
    quickness = set()
    result = BuiltInsHelper.is_built_in(quickness)
    assert result


def test_is_built_in_dict():
    quickness = {1: 'one', 2: 'two', 3: 'three'}
    result = BuiltInsHelper.is_built_in(quickness)
    assert result


def test_is_built_in_dict_two():
    quickness = {'a': 1, 'b': 2, 'c': 3}
    result = BuiltInsHelper.is_built_in(quickness)
    assert result


def test_is_built_in_dict_three():
    quickness = {}
    result = BuiltInsHelper.is_built_in(quickness)
    assert result


def test_is_built_in_none():
    quickness = None
    result = BuiltInsHelper.is_built_in(quickness)
    assert result
