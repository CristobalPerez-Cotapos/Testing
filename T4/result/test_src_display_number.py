# Automatically generated by Pynguin.
import src.display_number as module_0


def test_case_0():
    dict_0 = {}
    str_0 = 'xZ2|9Htp'
    number_display_0 = module_0.NumberDisplay(dict_0, str_0)
    assert number_display_0.value == {}
    assert number_display_0.limit == 'xZ2|9Htp'
    var_0 = number_display_0.reset()
    assert number_display_0.value == 0


def test_case_1():
    float_0 = 512.25
    tuple_0 = float_0,
    list_0 = []
    number_display_0 = None
    number_display_1 = module_0.NumberDisplay(list_0, number_display_0)
    assert number_display_1.value == []
    assert number_display_1.limit is None
    tuple_1 = tuple_0, number_display_1, list_0
    int_0 = 23
    number_display_2 = module_0.NumberDisplay(tuple_1, int_0)
    assert len(number_display_2.value) == 3
    assert number_display_2.limit == 23
    var_0 = number_display_2.clone()
    assert len(var_0.value) == 3
    assert var_0.limit == 23
