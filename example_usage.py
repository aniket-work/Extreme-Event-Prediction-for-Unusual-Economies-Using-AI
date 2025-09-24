"""
Example usage of the Climate Change Assistant for predicting extreme event impacts
on niche agricultural exports and micro-economies.
"""

from climate_assistant import (
    analyze_niche_agriculture_impact,
    predict_extreme_event_impact,
    get_pf_data,
    visualize_climate_impact,
    create_comparative_analysis_chart
)
import json

def main():
    print("Climate Change Impact Analysis with Visualization")
    print("=" * 50)
    
    # Example 1: Truffle farming in Europe with visualization
    print("\n1. Truffle Farming Impact Analysis with Visualization")
    print("-" * 50)
    truffle_result = analyze_niche_agriculture_impact("truffle", "Alba", "Italy")
    print(json.dumps(truffle_result, indent=2))
    
    # Create visualization for truffle farming
    try:
        visualize_climate_impact("truffle", "Alba", "Italy", truffle_result['climate_risks'])
    except Exception as e:
        print(f"Could not create visualization: {e}")
    
    # Example 2: Ice wine production with visualization
    print("\n2. Ice Wine Production Impact Analysis with Visualization")
    print("-" * 50)
    ice_wine_result = analyze_niche_agriculture_impact("ice_wine", "Niagara", "Canada")
    print(json.dumps(ice_wine_result, indent=2))
    
    # Create visualization for ice wine production
    try:
        visualize_climate_impact("ice_wine", "Niagara", "Canada", ice_wine_result['climate_risks'])
    except Exception as e:
        print(f"Could not create visualization: {e}")
    
    # Example 3: Saffron cultivation with visualization
    print("\n3. Saffron Cultivation Impact Analysis with Visualization")
    print("-" * 50)
    saffron_result = analyze_niche_agriculture_impact("saffron", "La Mancha", "Spain")
    print(json.dumps(saffron_result, indent=2))
    
    # Create visualization for saffron cultivation
    try:
        visualize_climate_impact("saffron", "La Mancha", "Spain", saffron_result['climate_risks'])
    except Exception as e:
        print(f"Could not create visualization: {e}")
    
    # Example 4: Comparative analysis chart
    print("\n4. Comparative Analysis Chart")
    print("-" * 30)
    results = [truffle_result, ice_wine_result, saffron_result]
    try:
        create_comparative_analysis_chart(results)
    except Exception as e:
        print(f"Could not create comparative analysis chart: {e}")

if __name__ == "__main__":
    main()