import A_star_pathfinding

def test_make_grid():
    assert A_star_pathfinding.make_grid(50,800).count == 50
