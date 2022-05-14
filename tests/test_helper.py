from nmcli._helper import add_wait_option_if_needed, add_fields_option_if_needed


def test_add_wait_option_if_needed():
    assert add_wait_option_if_needed(10) == ['--wait', '10']
    assert add_wait_option_if_needed(11) == ['--wait', '11']
    assert not add_wait_option_if_needed()
    assert not add_wait_option_if_needed(None)

def test_add_fields_option_if_needed():
    assert add_fields_option_if_needed('all') == ['-f', 'all']
    assert add_fields_option_if_needed('common') == ['-f', 'common']
    assert not add_fields_option_if_needed()
    assert not add_fields_option_if_needed(None)
