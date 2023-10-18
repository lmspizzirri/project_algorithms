from challenges.challenge_encrypt_message import encrypt_message
import pytest

def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("xiraibi", "x")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(25, 2)
    assert encrypt_message("mari", 1) == "m_ira"
    assert encrypt_message("mari", 2) == "ir_am"
    assert encrypt_message("mari", 800) == "iram"