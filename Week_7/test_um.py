import pytest
from um import count

@pytest.mark.parametrize("strummms, output",[
    ("um", 1),
    ("UM", 1),
    ("um?", 1),
    ("UM,", 1),
    ("Um, thanks for the album", 1),
    ("Um, thanks, um", 2),
    ("Um? Mum? is this that album where, um, umm, the clumsy alums play drums", 2),
    ("mum", 0),
    ("Hello World!", 0),
    ("um, hello, um world!", 2),
    ("um...", 1),
    ("yummy", 0)
])
def test_count(strummms, output):
    assert count(strummms) == output