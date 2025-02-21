import numpy as np
from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple, Optional

class RiskLevel(Enum):
    NO_RISK = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

@dataclass
class DetectedObject:
    """Class for storing detected object information"""
    id: int
    class_name: str
    bbox: Tuple[float, float, float, float]  # x1, y1, x2, y2
    diameter: Optional[float] = None  # canopy diameter in meters
    confidence: float = 1.0

class RiskCalculator:
    def __init__(self, pixel_to_meter_ratio: float):
        self.pixel_to_meter_ratio = pixel_to_meter_ratio
        
    def calculate_height_from_diameter(self, diameter: float) -> float:
        """
        Calculate Parkinsonia height from canopy diameter using the formula:
        H = ((0.091D)^3.04/0.025)^(1/4.47)
        
        Args:
            diameter: Canopy diameter in meters
        Returns:
            height: Tree height in meters
        """
        W = 0.091 * (diameter ** 3.04)
        height = (W / 0.025) ** (1 / 4.47)
        return height

    def calculate_risk_radius(self, height: float) -> float:
        """Calculate maximum risk radius as 5 times the tree height"""
        return 5 * height

    def calculate_distance(self, obj1: DetectedObject, obj2: DetectedObject) -> float:
        """Calculate center-to-center distance between two objects in meters"""
        # Calculate centers
        x1 = (obj1.bbox[0] + obj1.bbox[2]) / 2
        y1 = (obj1.bbox[1] + obj1.bbox[3]) / 2
        x2 = (obj2.bbox[0] + obj2.bbox[2]) / 2
        y2 = (obj2.bbox[1] + obj2.bbox[3]) / 2
        
        # Calculate pixel distance
        pixel_distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        # Convert to meters
        return pixel_distance * self.pixel_to_meter_ratio

    def assess_risk(self, parkinsonia: DetectedObject, target: DetectedObject) -> Tuple[RiskLevel, str]:
        """
        Assess risk level based on distance relative to Parkinsonia height
        
        Returns:
            Tuple of (RiskLevel, justification)
        """
        if parkinsonia.diameter is None:
            raise ValueError("Parkinsonia diameter must be provided")

        height = self.calculate_height_from_diameter(parkinsonia.diameter)
        max_radius = self.calculate_risk_radius(height)
        distance = self.calculate_distance(parkinsonia, target)
        
        # Calculate risk based on percentage of max radius
        distance_percentage = (distance / max_radius) * 100
        
        if distance_percentage > 100:
            return RiskLevel.NO_RISK, f"Target is beyond the maximum spread distance ({distance:.1f}m > {max_radius:.1f}m)"
        elif distance_percentage > 75:
            return RiskLevel.LOW, f"Target is at {distance:.1f}m, which is {distance_percentage:.1f}% of maximum spread distance"
        elif distance_percentage > 50:
            return RiskLevel.MEDIUM, f"Target is at {distance:.1f}m, within 50-75% of maximum spread distance"
        elif distance_percentage > 25:
            return RiskLevel.HIGH, f"Target is at {distance:.1f}m, within 25-50% of maximum spread distance"
        else:
            return RiskLevel.CRITICAL, f"Target is very close at {distance:.1f}m, within 25% of maximum spread distance"

    def calculate_normal_distribution_risk(self, distance: float, max_radius: float) -> float:
        """
        Calculate risk probability using a normal distribution
        
        Args:
            distance: Distance between objects in meters
            max_radius: Maximum risk radius in meters
        Returns:
            probability: Risk probability between 0 and 1
        """
        # Use max_radius/3 as standard deviation (99.7% of values within max radius)
        std_dev = max_radius / 3
        return np.exp(-0.5 * (distance / std_dev)**2) 