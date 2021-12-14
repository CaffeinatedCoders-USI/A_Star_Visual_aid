import A_star_pathfinding_helper

def test_h():
    assert A_star_pathfinding_helper.h((10,10),(20,20)) == 20
def test_get_clicked_pos():
    assert A_star_pathfinding_helper.get_clicked_pos((16,16),50,800) == (1,1)