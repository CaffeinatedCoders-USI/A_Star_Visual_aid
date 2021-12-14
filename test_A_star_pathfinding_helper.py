import A_star_pathfinding_helper

def test_h():
    assert A_star_pathfinding_helper.h((10,10),(20,20)) == 20
