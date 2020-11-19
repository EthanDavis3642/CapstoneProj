import unittest
from TrackVolumeLogic import pollgpio
#from TrackVolumeLogic import set_volume
from TrackVolumeLogic import mainloop_tester

class TestVolume(unittest.TestCase):
    
    def test_max(self):
        a = mainloop_tester(True)
        self.assertEqual(1, a[0])
        
    def test_min(self):
        a = mainloop_tester(False)
        self.assertEqual(0, a[0])
if __name__ == '__main_':
    unittest.main()
   
