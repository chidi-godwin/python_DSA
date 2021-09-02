from ..node import Node

def test_node():
    x =  Node(7)

    assert isinstance(x, Node)
    assert x.value == 7
    assert hasattr(x, 'leftChild')
    assert hasattr(x, 'rightChild')

