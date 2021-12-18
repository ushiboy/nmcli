from nmcli._helper import add_wait_option_if_needed

def test_add_wait_option_if_needed():
    assert add_wait_option_if_needed(10) == ['--wait', '10']
    assert add_wait_option_if_needed(11) == ['--wait', '11']
    assert add_wait_option_if_needed() == []
    assert add_wait_option_if_needed(None) == []
