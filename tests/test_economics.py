import unittest
from decimal import Decimal
from economics import annual_net_benefit, break_even_avoided_fraction

class EconomicsTests(unittest.TestCase):
    def test_synthetic_scenario(self):
        r=annual_net_benefit(100,5000,.3,50,800,50000)
        self.assertEqual(r['net_benefit'], Decimal('60000.0'))
    def test_break_even(self):
        self.assertEqual(break_even_avoided_fraction(100,5000,50,800,50000),Decimal('.18'))
    def test_negative_benefit_visible(self):
        self.assertLess(annual_net_benefit(10,1000,.1,50,800,50000)['net_benefit'],0)
    def test_invalid_fraction(self):
        with self.assertRaises(ValueError): annual_net_benefit(100,5000,1.1,50,800,50000)
    def test_no_baseline(self):
        with self.assertRaises(ValueError): break_even_avoided_fraction(0,5000,50,800,50000)

if __name__ == '__main__': unittest.main()
