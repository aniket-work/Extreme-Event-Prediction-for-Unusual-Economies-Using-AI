"""
Full demonstration of the Climate Change Assistant
Showcasing both analysis and visualization capabilities
"""

import json
from climate_assistant import (
    analyze_niche_agriculture_impact,
    visualize_climate_impact,
    create_comparative_analysis_chart
)

def run_full_demo():
    print("Climate Change Assistant - Full Demonstration")
    print("=" * 50)
    
    # Analyze multiple niche agriculture types
    print("\n1. Analyzing climate impacts...")
    
    # Truffle farming analysis
    print("   - Analyzing truffle farming in Alba, Italy...")
    truffle_analysis = analyze_niche_agriculture_impact("truffle", "Alba", "Italy")
    
    # Ice wine production analysis
    print("   - Analyzing ice wine production in Niagara, Canada...")
    ice_wine_analysis = analyze_niche_agriculture_impact("ice_wine", "Niagara", "Canada")
    
    # Saffron cultivation analysis
    print("   - Analyzing saffron cultivation in La Mancha, Spain...")
    saffron_analysis = analyze_niche_agriculture_impact("saffron", "La Mancha", "Spain")
    
    # Display sample results (without full data due to API limitations in this environment)
    print("\n2. Sample Analysis Results:")
    print("   Truffle Farming Recommendation:")
    print(f"   {truffle_analysis['recommendation']}")
    
    print("\n   Ice Wine Production Recommendation:")
    print(f"   {ice_wine_analysis['recommendation']}")
    
    print("\n   Saffron Cultivation Recommendation:")
    print(f"   {saffron_analysis['recommendation']}")
    
    # Create visualizations
    print("\n3. Generating visualizations...")
    
    # Create individual visualizations
    try:
        print("   - Creating truffle farming visualization...")
        visualize_climate_impact("truffle", "Alba", "Italy", truffle_analysis['climate_risks'])
        
        print("   - Creating ice wine visualization...")
        visualize_climate_impact("ice_wine", "Niagara", "Canada", ice_wine_analysis['climate_risks'])
        
        print("   - Creating saffron visualization...")
        visualize_climate_impact("saffron", "La Mancha", "Spain", saffron_analysis['climate_risks'])
        
        # Create comparative analysis
        print("   - Creating comparative analysis chart...")
        all_results = [truffle_analysis, ice_wine_analysis, saffron_analysis]
        create_comparative_analysis_chart(all_results)
        
        print("\n✓ All visualizations generated successfully!")
        print("\nGenerated files:")
        print("  - truffle_Alba_Italy_impact.png")
        print("  - ice_wine_Niagara_Canada_impact.png")
        print("  - saffron_La_Mancha_Spain_impact.png")
        print("  - comparative_agriculture_risk_analysis.png")
        
    except Exception as e:
        print(f"\n! Error generating visualizations: {e}")
        print("  Note: Visualizations require proper setup of matplotlib backend.")
    
    print("\n4. For more comprehensive visualizations, run:")
    print("   python climate_visualization_demo.py")
    
    print("\nDemo completed!")

if __name__ == "__main__":
    run_full_demo()