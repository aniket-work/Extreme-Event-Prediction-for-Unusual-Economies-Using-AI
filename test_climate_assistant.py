"""
Unit tests for the Climate Change Assistant module.
"""

import unittest
from climate_assistant import (
    convert_to_iso8601,
    get_current_datetime,
    analyze_niche_agriculture_impact,
    generate_recommendation
)

class TestClimateAssistant(unittest.TestCase):
    
    def test_convert_to_iso8601(self):
        """Test date conversion function"""
        result = convert_to_iso8601("2023-01-01")
        self.assertEqual(result, "2023-01-01T00:00:00+00:00")
    
    def test_get_current_datetime(self):
        """Test current date function"""
        result = get_current_datetime()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
    
    def test_generate_recommendation(self):
        """Test recommendation generation"""
        # Test truffle recommendation
        rec = generate_recommendation("truffle", {})
        self.assertIn("truffle farming", rec.lower())
        
        # Test ice wine recommendation
        rec = generate_recommendation("ice_wine", {})
        self.assertIn("ice wine", rec.lower())
        
        # Test saffron recommendation
        rec = generate_recommendation("saffron", {})
        self.assertIn("saffron", rec.lower())
    
    def test_analyze_niche_agriculture_impact(self):
        """Test agriculture impact analysis structure"""
        # This test checks the structure without making actual API calls
        # We'll mock the API response in a real test scenario
        result = analyze_niche_agriculture_impact("truffle", "TestRegion", "TestCountry")
        
        self.assertIn("agriculture_type", result)
        self.assertIn("location", result)
        self.assertIn("climate_risks", result)
        self.assertIn("recommendation", result)
        
        self.assertEqual(result["agriculture_type"], "truffle")
        self.assertEqual(result["location"], "TestRegion, TestCountry")

if __name__ == "__main__":
    unittest.main()