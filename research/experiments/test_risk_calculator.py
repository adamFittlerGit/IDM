import unittest
from models.risk_calculator import RiskCalculator, DetectedObject, RiskLevel

class TestRiskCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = RiskCalculator(pixel_to_meter_ratio=0.1)  # 10 pixels = 1 meter
        
    def test_height_calculation(self):
        height = self.calculator.calculate_height_from_diameter(5.0)  # 5m diameter
        self.assertGreater(height, 0)
        
    def test_risk_assessment(self):
        parkinsonia = DetectedObject(
            id=1,
            class_name="parkinsonia",
            bbox=(0, 0, 100, 100),  # 10m x 10m in our scale
            diameter=5.0
        )
        
        target = DetectedObject(
            id=2,
            class_name="other_plant",
            bbox=(200, 200, 300, 300)  # 20m away diagonally
        )
        
        risk_level, justification = self.calculator.assess_risk(parkinsonia, target)
        self.assertIsInstance(risk_level, RiskLevel)
        self.assertIsInstance(justification, str)

if __name__ == '__main__':
    unittest.main() 