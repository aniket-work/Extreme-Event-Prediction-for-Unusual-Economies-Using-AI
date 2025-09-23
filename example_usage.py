"""
Example usage of the Climate Change Assistant for predicting extreme event impacts
on niche agricultural exports and micro-economies.
"""

from climate_assistant import (
    analyze_niche_agriculture_impact,
    predict_extreme_event_impact,
    get_pf_data
)
import json

def main():
    print("Climate Change Impact Analysis")
    print("=" * 40)
    
    # Example 1: Truffle farming in Europe
    print("\n1. Truffle Farming Impact Analysis")
    print("-" * 30)
    truffle_result = analyze_niche_agriculture_impact("truffle", "Alba", "Italy")
    print(json.dumps(truffle_result, indent=2))
    
    # Example 2: Ice wine production
    print("\n2. Ice Wine Production Impact Analysis")
    print("-" * 30)
    ice_wine_result = analyze_niche_agriculture_impact("ice_wine", "Niagara", "Canada")
    print(json.dumps(ice_wine_result, indent=2))
    
    # Example 3: Saffron cultivation
    print("\n3. Saffron Cultivation Impact Analysis")
    print("-" * 30)
    saffron_result = analyze_niche_agriculture_impact("saffron", "La Mancha", "Spain")
    print(json.dumps(saffron_result, indent=2))
    
    # Example 4: Custom warming scenarios
    print("\n4. Custom Warming Scenarios for Micro-Economies")
    print("-" * 30)
    custom_scenarios = ["1.5", "2.0", "3.0", "4.0", "5.0"]
    custom_result = predict_extreme_event_impact("Small Island", "Nation", custom_scenarios)
    print("Climate projections for Small Island Nation:")
    print(json.dumps(custom_result, indent=2))

if __name__ == "__main__":
    main()