from unittest import TestCase
from neighborLogic import num_of_neighbors
__author__ = 'Kyle'


class TestNeighborLogic(TestCase):

    def test_num_of_neighbors_with_empty_grid(self):
        assert num_of_neighbors([]) == []

    def test_num_of_neighbors_with_1x1_1_grid(self):
        assert num_of_neighbors([[1]]) == [[0]]

    def test_num_of_neighbors_with_1x1_0_grid(self):
        assert num_of_neighbors([[0]]) == [[0]]

    def test_num_of_neighbors_with_2x1_grid(self):
        assert num_of_neighbors([[1,0]]) == [[0,1]]

    def test_num_of_neighbors_with_2x2_grid(self):
        assert num_of_neighbors([[1,0], [0,1]]) == [[1,2], [2,1]]