import pytest
from main import longest_path

def test_longest_path():
    graph1 = [
        [(1, 3), (2, 2)],
        [(3, 4)],
        [(3, 1)],
        []
    ]
    assert longest_path(graph1) == 7

    graph2 = [
        [(1, 2), (2, 1)],
        [(3, 1)],
        [(3, 5)],
        []
    ]
    assert longest_path(graph2) == 6

    graph3 = [
        [(1, 10)],
        [(2, 10)],
        [(3, 10)],
        []
    ]
    assert longest_path(graph3) == 30

    graph4 = [
        [(1, 1), (2, 1)],
        [(3, 1)],
        [(3, 1)],
        []
    ]
    assert longest_path(graph4) == 2
    # As given in your assignment the answer for "graph4" is "3". But I checked that its correct answer is "2".
    '''                      Proof is this
                    1
                0 -----> 1
                |        |
              1 |        | 1
                |        |
                \/      \/ 
                2 -----> 3  
                    1
    If you want the answer as "3" than the graph changes as.
        graph4 = [
        [(1, 1), (2, 1)],
        [],
        [(3, 1)],
        [(1, 1)]
        ]
        assert longest_path(graph4) == 3

    '''

    print("All test cases pass")

if __name__ == "__main__":
    pytest.main()
