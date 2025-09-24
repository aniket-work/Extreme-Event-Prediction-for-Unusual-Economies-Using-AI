"""
Test script for climate assistant visualization features.
"""

import json
import traceback
from climate_assistant import visualize_climate_impact, create_comparative_analysis_chart

def test_visualization():
    print("Testing climate assistant visualization features...")
    
    # Mock climate data for testing visualization
    mock_climate_data = {
        "1.5": {"temperature_change": 1.5, "precipitation_change": 2.1},
        "2.0": {"temperature_change": 2.0, "precipitation_change": 3.2},
        "3.0": {"temperature_change": 3.0, "precipitation_change": 4.5},
        "4.0": {"temperature_change": 4.0, "precipitation_change": 5.8}
    }
    
    # Test single visualization
    print("\n1. Testing single climate impact visualization...")
    try:
        filename = visualize_climate_impact("truffle", "Alba", "Italy", mock_climate_data)
        print(f"   Created visualization: {filename}")
    except Exception as e:
        print(f"   Error creating visualization: {e}")
        print(f"   Traceback: {traceback.format_exc()}")
    
    # Test comparative analysis chart
    print("\n2. Testing comparative analysis chart...")
    mock_analysis_results = [
        {
            "agriculture_type": "truffle",
            "climate_risks": mock_climate_data
        },
        {
            "agriculture_type": "ice_wine",
            "climate_risks": mock_climate_data
        },
        {
            "agriculture_type": "saffron",
            "climate_risks": mock_climate_data
        }
    ]
    
    try:
        filename = create_comparative_analysis_chart(mock_analysis_results)
        print(f"   Created comparative chart: {filename}")
    except Exception as e:
        print(f"   Error creating comparative chart: {e}")
        print(f"   Traceback: {traceback.format_exc()}")
    
    print("\nVisualization tests completed!")

if __name__ == "__main__":
    test_visualization()