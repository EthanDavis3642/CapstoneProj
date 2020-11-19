from grid import Grid
import unittest

class TestGrid(unittest.TestCase):
    def test_size(self):
        a = Grid()
        rows = len(a.grid)
        columns = len(a.grid[0])
        tot = rows * columns
        self.assertEqual(tot, 16)   
    def test_init(self):
        a = Grid()
        self.assertFalse(True in a.grid[0])
        self.assertFalse(True in a.grid[1])
        self.assertFalse(True in a.grid[2])
        self.assertFalse(True in a.grid[3])
        
    def test_piece(self):
        a = Grid()
        a.next_piece()
        self.assertTrue(any( True in subl for subl in a.grid))
        
    def test_piece2(self):
        a = Grid()
        a.next_piece()
        counter = 0
        for i in range(4):
            for j in range(4):
                if a.grid[j][i]:
                    counter = counter + 1                  
        self.assertEqual(counter, 4)

    def test_piece3(self):
        a = Grid()
        b = len(a.available_pieces)
        a.next_piece()
        c = len(a.available_pieces)
        self.assertEqual(b, c + 1)
    def test_reset(self):
        a = Grid()
        b = len(a.available_pieces)
        a.next_piece()
        a.reset()
        c = len(a.available_pieces)
        self.assertEqual(b, c)
    def test_clear(self):
        a = Grid()
        a.next_piece()
        a.clear()
        self.assertFalse(True in a.grid[0])
        self.assertFalse(True in a.grid[1])
        self.assertFalse(True in a.grid[2])
        self.assertFalse(True in a.grid[3])
if __name__ == '__main_':
    unittest.main()
   
