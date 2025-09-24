"""
Climate Change Visualization Demo
Demonstrates how to create charts and graphs for climate impact analysis
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import json

# Set up the plotting style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def create_temperature_projection_chart():
    """Create a temperature projection chart for different warming scenarios"""
    # Data for the chart
    scenarios = [1.5, 2.0, 3.0, 4.0, 5.0]
    truffle_regions = [1.2, 1.8, 3.2, 5.1, 7.2]  # Impact on truffle farming
    ice_wine_regions = [0.8, 1.5, 2.8, 4.5, 6.8]  # Impact on ice wine production
    saffron_regions = [1.0, 1.7, 3.0, 4.8, 7.0]   # Impact on saffron cultivation
    
    # Create the DataFrame
    df = pd.DataFrame({
        'Warming Scenario (°C)': scenarios,
        'Truffle Farming': truffle_regions,
        'Ice Wine Production': ice_wine_regions,
        'Saffron Cultivation': saffron_regions
    })
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Plot each agriculture type
    plt.plot('Warming Scenario (°C)', 'Truffle Farming', data=df, marker='o', linewidth=2, markersize=8, label='Truffle Farming')
    plt.plot('Warming Scenario (°C)', 'Ice Wine Production', data=df, marker='s', linewidth=2, markersize=8, label='Ice Wine Production')
    plt.plot('Warming Scenario (°C)', 'Saffron Cultivation', data=df, marker='^', linewidth=2, markersize=8, label='Saffron Cultivation')
    
    # Customize the plot
    plt.title('Climate Impact Projections for Niche Agricultural Exports', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Global Warming Scenario (°C)', fontsize=14, fontweight='bold')
    plt.ylabel('Projected Impact Score', fontsize=14, fontweight='bold')
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Add a critical threshold line
    plt.axhline(y=4.0, color='red', linestyle='--', alpha=0.7, label='Critical Impact Threshold')
    
    # Add value labels
    for i, txt in enumerate(truffle_regions):
        plt.annotate(f'{txt}', (scenarios[i], truffle_regions[i]), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.tight_layout()
    plt.savefig('temperature_projection_chart.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Temperature projection chart saved as 'temperature_projection_chart.png'")

def create_regional_impact_heatmap():
    """Create a heatmap showing regional impact of climate change"""
    # Data for heatmap
    regions = ['Burgundy, France', 'Alba, Italy', 'Niagara, Canada', 'La Mancha, Spain', 'Tokaj, Hungary']
    crops = ['Truffles', 'Ice Wine', 'Saffron', 'Champagne', 'Wine']
    
    # Impact scores (higher = more vulnerable)
    impact_data = np.array([
        [8.2, 2.1, 4.3, 6.7, 5.8],  # Burgundy
        [9.1, 1.8, 5.2, 4.3, 6.2],  # Alba
        [3.2, 9.5, 2.1, 7.8, 8.9],  # Niagara
        [6.8, 3.2, 8.7, 5.4, 4.9],  # La Mancha
        [5.9, 7.3, 3.8, 8.2, 7.6]   # Tokaj
    ])
    
    # Create heatmap
    fig, ax = plt.subplots(figsize=(12, 8))
    im = ax.imshow(impact_data, cmap='RdYlGn_r', aspect='auto')
    
    # Set ticks and labels
    ax.set_xticks(np.arange(len(crops)))
    ax.set_yticks(np.arange(len(regions)))
    ax.set_xticklabels(crops, fontsize=12)
    ax.set_yticklabels(regions, fontsize=12)
    
    # Rotate the tick labels and set their alignment
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('Climate Vulnerability Score', fontsize=12, fontweight='bold')
    
    # Add text annotations
    for i in range(len(regions)):
        for j in range(len(crops)):
            text = ax.text(j, i, f'{impact_data[i, j]:.1f}',
                          ha="center", va="center", color="white" if impact_data[i, j] < 5 else "black", fontweight='bold')
    
    # Customize the plot
    plt.title('Regional Climate Impact Vulnerability for Specialty Agricultural Products', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('regional_impact_heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Regional impact heatmap saved as 'regional_impact_heatmap.png'")

def create_risk_comparison_bar_chart():
    """Create a bar chart comparing climate risks across different agriculture types"""
    # Data for the chart
    agriculture_types = ['Truffle Farming', 'Ice Wine Production', 'Saffron Cultivation', 'Champagne', 'Specialty Coffee', 'Artisanal Cheese']
    risk_scores = [9.2, 8.7, 7.8, 6.9, 8.1, 5.4]
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create bar chart with gradient colors
    colors = plt.cm.RdYlGn_r(np.linspace(0, 1, len(agriculture_types)))
    bars = plt.bar(agriculture_types, risk_scores, color=colors)
    
    # Customize the plot
    plt.title('Climate Risk Comparison for Specialty Agricultural Exports', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Agriculture Type', fontsize=14, fontweight='bold')
    plt.ylabel('Climate Risk Score (0-10)', fontsize=14, fontweight='bold')
    
    # Rotate x-axis labels
    plt.xticks(rotation=45, ha='right')
    
    # Add value labels on bars
    for bar, score in zip(bars, risk_scores):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                f'{score}', ha='center', va='bottom', fontweight='bold', fontsize=12)
    
    # Add a critical threshold line
    plt.axhline(y=7.0, color='orange', linestyle='--', alpha=0.7, label='High Risk Threshold')
    plt.axhline(y=5.0, color='green', linestyle='--', alpha=0.7, label='Moderate Risk Threshold')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('risk_comparison_bar_chart.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Risk comparison bar chart saved as 'risk_comparison_bar_chart.png'")

def create_scenario_impact_dashboard():
    """Create a dashboard with multiple charts showing climate impact scenarios"""
    # Create a figure with subplots
    fig = plt.figure(figsize=(20, 15))
    
    # Subplot 1: Line chart of temperature projections
    ax1 = plt.subplot(2, 3, (1, 2))
    scenarios = [1.5, 2.0, 3.0, 4.0, 5.0]
    temp_change = [1.2, 1.8, 3.2, 5.1, 7.2]
    precip_change = [0.8, 1.5, 2.8, 4.5, 6.8]
    
    ax1.plot(scenarios, temp_change, marker='o', linewidth=3, markersize=10, label='Temperature Change')
    ax1.plot(scenarios, precip_change, marker='s', linewidth=3, markersize=10, label='Precipitation Change')
    ax1.set_title('Climate Variable Changes by Warming Scenario', fontsize=16, fontweight='bold')
    ax1.set_xlabel('Warming Scenario (°C)', fontsize=14)
    ax1.set_ylabel('Change Magnitude', fontsize=14)
    ax1.legend(fontsize=12)
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Pie chart of economic impact distribution
    ax2 = plt.subplot(2, 3, 3)
    sectors = ['Direct Crop Loss', 'Supply Chain Disruption', 'Market Price Volatility', 'Labor Impact', 'Infrastructure Damage']
    sizes = [35, 25, 20, 12, 8]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
    
    ax2.pie(sizes, labels=sectors, autopct='%1.1f%%', startangle=90, colors=colors)
    ax2.set_title('Economic Impact Distribution', fontsize=16, fontweight='bold')
    
    # Subplot 3: Bar chart of adaptation readiness
    ax3 = plt.subplot(2, 3, (4, 5))
    regions = ['Europe', 'North America', 'Asia', 'South America', 'Africa']
    readiness_scores = [7.8, 6.9, 5.2, 4.8, 3.9]
    
    bars = ax3.bar(regions, readiness_scores, color=plt.cm.viridis(np.linspace(0, 1, len(regions))))
    ax3.set_title('Regional Climate Adaptation Readiness', fontsize=16, fontweight='bold')
    ax3.set_xlabel('Region', fontsize=14)
    ax3.set_ylabel('Readiness Score (0-10)', fontsize=14)
    
    # Add value labels on bars
    for bar, score in zip(bars, readiness_scores):
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                f'{score}', ha='center', va='bottom', fontweight='bold')
    
    # Subplot 4: Scatter plot of vulnerability vs. adaptive capacity
    ax4 = plt.subplot(2, 3, 6)
    vulnerability = [8.2, 7.5, 6.8, 7.9, 9.1, 6.2, 8.7, 7.3]
    adaptive_capacity = [7.1, 6.8, 5.9, 8.2, 4.3, 7.8, 5.6, 6.9]
    agriculture_types = ['Truffles', 'Ice Wine', 'Saffron', 'Champagne', 'Coffee', 'Cheese', 'Wine', 'Olive Oil']
    
    scatter = ax4.scatter(vulnerability, adaptive_capacity, s=150, alpha=0.7, c=range(len(agriculture_types)), cmap='viridis')
    ax4.set_xlabel('Climate Vulnerability', fontsize=14)
    ax4.set_ylabel('Adaptive Capacity', fontsize=14)
    ax4.set_title('Vulnerability vs. Adaptive Capacity', fontsize=16, fontweight='bold')
    
    # Add labels for each point
    for i, txt in enumerate(agriculture_types):
        ax4.annotate(txt, (vulnerability[i], adaptive_capacity[i]), 
                    xytext=(5, 5), textcoords='offset points', fontsize=10)
    
    # Add diagonal line for reference
    ax4.plot([0, 10], [0, 10], 'k--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('climate_impact_dashboard.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Climate impact dashboard saved as 'climate_impact_dashboard.png'")

def main():
    print("Creating Climate Change Visualization Charts")
    print("=" * 50)
    
    # Create all visualizations
    create_temperature_projection_chart()
    print()
    
    create_regional_impact_heatmap()
    print()
    
    create_risk_comparison_bar_chart()
    print()
    
    create_scenario_impact_dashboard()
    print()
    
    print("All climate visualization charts have been created successfully!")
    print("\nGenerated files:")
    print("- temperature_projection_chart.png")
    print("- regional_impact_heatmap.png")
    print("- risk_comparison_bar_chart.png")
    print("- climate_impact_dashboard.png")

if __name__ == "__main__":
    main()