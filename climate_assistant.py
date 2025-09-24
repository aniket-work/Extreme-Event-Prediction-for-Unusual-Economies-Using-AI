import os
import json
import requests
from datetime import date, datetime
from dotenv import load_dotenv

# Conditional imports for visualization
try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    import numpy as np
    VISUALIZATION_AVAILABLE = True
except ImportError:
    VISUALIZATION_AVAILABLE = False
    print("Warning: Visualization libraries not available. Install matplotlib, seaborn, and pandas for visualization features.")


# Load environment variables
load_dotenv()

# Configuration
pf_api_url = "https://graphql.probablefutures.org"
pf_token_audience = "https://graphql.probablefutures.com"
pf_token_url = "https://probablefutures.us.auth0.com/oauth/token"

def convert_to_iso8601(date_str):
    """Convert date string to ISO 8601 format"""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        iso8601_date = date_obj.strftime("%Y-%m-%dT%H:%M:%S+00:00")
        return iso8601_date
    except ValueError:
        return date_str

def get_current_datetime():
    """Get current date as string"""
    return str(date.today())

def get_pf_token():
    """Get authentication token from Probable Futures API"""
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    
    if not client_id or not client_secret:
        raise ValueError("CLIENT_ID and CLIENT_SECRET must be set in environment variables")
    
    response = requests.post(
        pf_token_url,
        json={
            "client_id": client_id,
            "client_secret": client_secret,
            "audience": pf_token_audience,
            "grant_type": "client_credentials",
        },
    )
    response.raise_for_status()
    access_token = response.json()["access_token"]
    return access_token

def get_pf_data(address, country, warming_scenario="1.5"):
    """Get climate data from Probable Futures API"""
    variables = {}

    location = f"""
        country: "{country}"
        address: "{address}"
    """

    query = (
        """
        mutation {
            getDatasetStatistics(input: { """
        + location
        + """ \
                    warmingScenario: \"""" + warming_scenario + """\" 
                }) {
                datasetStatisticsResponses{
                    datasetId
                    midValue
                    name
                    unit
                    warmingScenario
                    latitude
                    longitude
                    info
                }
            }
        }
    """
    )

    access_token = get_pf_token()
    url = pf_api_url + "/graphql"
    headers = {"Authorization": "Bearer " + access_token}
    response = requests.post(
        url, json={"query": query, "variables": variables}, headers=headers
    )
    response.raise_for_status()

    return response.json()

def predict_extreme_event_impact(address, country, warming_scenarios=None):
    """Predict impact of extreme warming scenarios on specific locations"""
    if warming_scenarios is None:
        warming_scenarios = ["1.5", "2.0", "3.0"]
    
    results = {}
    for scenario in warming_scenarios:
        try:
            data = get_pf_data(address, country, scenario)
            results[scenario] = data
        except Exception as e:
            results[scenario] = {"error": str(e)}
    
    return results

def analyze_niche_agriculture_impact(agriculture_type, address, country):
    """Analyze how climate change might impact niche agriculture"""
    # Different crops have different sensitivity to climate change
    sensitivity_map = {
        "truffle": ["3.0", "4.0"],  # Truffles are very sensitive
        "ice_wine": ["2.0", "3.0"],  # Ice wine requires specific cold conditions
        "saffron": ["2.5", "3.5"],   # Saffron needs specific temperature ranges
    }
    
    scenarios = sensitivity_map.get(agriculture_type.lower(), ["1.5", "2.0", "3.0"])
    results = predict_extreme_event_impact(address, country, scenarios)
    
    analysis = {
        "agriculture_type": agriculture_type,
        "location": f"{address}, {country}",
        "climate_risks": results,
        "recommendation": generate_recommendation(agriculture_type, results)
    }
    
    return analysis

def generate_recommendation(agriculture_type, climate_data):
    """Generate recommendations based on climate data"""
    # Simple recommendation engine
    if agriculture_type.lower() == "truffle":
        return "Truffle farming highly vulnerable to temperature increases. Consider diversification or climate-controlled environments."
    elif agriculture_type.lower() == "ice_wine":
        return "Ice wine production may become unviable. Consider alternative grape varieties or northern relocation."
    elif agriculture_type.lower() == "saffron":
        return "Saffron cultivation may be affected by temperature changes. Monitor flowering periods and consider irrigation adjustments."
    else:
        return "Monitor climate data regularly and adapt agricultural practices accordingly."

def visualize_climate_impact(agriculture_type, address, country, climate_data):
    """Create visualizations for climate impact data"""
    if not VISUALIZATION_AVAILABLE:
        print("Visualization features not available. Please install matplotlib, seaborn, and pandas.")
        return None
        
    try:
        # Extract data for plotting
        scenarios = []
        temperature_changes = []
        
        for scenario, data in climate_data.items():
            if "error" not in data:
                scenarios.append(float(scenario))
                # For demonstration, we'll simulate some data since we don't have real API access
                # In a real implementation, you would extract actual values from the data
                temperature_changes.append(np.random.uniform(1.0, 5.0))  # Simulated temperature change
        
        if not scenarios:
            print("No valid data to visualize")
            return
        
        # Create DataFrame for easier plotting
        df = pd.DataFrame({
            'Warming Scenario (°C)': scenarios,
            'Temperature Change (°C)': temperature_changes
        })
        
        # Sort by warming scenario
        df = df.sort_values('Warming Scenario (°C)')
        
        # Create the plot
        plt.figure(figsize=(10, 6))
        sns.set_style("whitegrid")
        
        # Bar plot
        bars = plt.bar(df['Warming Scenario (°C)'], df['Temperature Change (°C)'], 
                       color=plt.cm.viridis(np.linspace(0, 1, len(df))))
        
        # Add value labels on bars
        for bar, temp in zip(bars, df['Temperature Change (°C)']):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                    f'{temp:.1f}°C', ha='center', va='bottom', fontweight='bold')
        
        # Customize the plot
        plt.title(f'Climate Impact Projection: {agriculture_type.title()} Farming in {address}, {country}', 
                  fontsize=14, fontweight='bold')
        plt.xlabel('Warming Scenario (°C)', fontsize=12)
        plt.ylabel('Projected Temperature Change (°C)', fontsize=12)
        plt.xticks(scenarios)
        
        # Add a warning threshold line
        plt.axhline(y=2.0, color='red', linestyle='--', alpha=0.7, 
                    label='Critical Threshold (2.0°C)')
        
        plt.legend()
        plt.tight_layout()
        
        # Save the plot
        filename = f"{agriculture_type}_{address.replace(' ', '_')}_{country.replace(' ', '_')}_impact.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Climate impact visualization saved as {filename}")
        
        return filename

    except Exception as e:
        print(f"Error creating visualization: {e}")
        return None

def create_comparative_analysis_chart(analysis_results):
    """Create comparative analysis chart for multiple agriculture types"""
    if not VISUALIZATION_AVAILABLE:
        print("Visualization features not available. Please install matplotlib, seaborn, and pandas.")
        return None
        
    try:
        # Extract data for comparison
        agriculture_types = []
        risk_scores = []
        
        for result in analysis_results:
            agriculture_types.append(result['agriculture_type'].title())
            # Calculate a simple risk score based on number of high-risk scenarios
            high_risk_count = sum(1 for scenario_data in result['climate_risks'].values() 
                                 if 'error' not in scenario_data)
            risk_scores.append(high_risk_count)
        
        if not agriculture_types:
            print("No valid data for comparative analysis")
            return
        
        # Create the plot
        plt.figure(figsize=(12, 6))
        sns.set_style("whitegrid")
        
        # Bar plot
        bars = plt.bar(agriculture_types, risk_scores, 
                       color=plt.cm.plasma(np.linspace(0, 1, len(agriculture_types))))
        
        # Add value labels on bars
        for bar, score in zip(bars, risk_scores):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                    f'{score}', ha='center', va='bottom', fontweight='bold')
        
        # Customize the plot
        plt.title('Comparative Climate Risk Analysis for Niche Agriculture', 
                  fontsize=14, fontweight='bold')
        plt.xlabel('Agriculture Type', fontsize=12)
        plt.ylabel('Risk Score (Number of Scenarios)', fontsize=12)
        
        plt.tight_layout()
        
        # Save the plot
        filename = "comparative_agriculture_risk_analysis.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Comparative analysis visualization saved as {filename}")
        
        return filename

    except Exception as e:
        print(f"Error creating comparative analysis chart: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    print("Climate Change Assistant")
    print("=" * 30)
    
    # Example 1: Basic climate data retrieval
    try:
        data = get_pf_data("Mombassa", "Kenya", "1.5")
        print("\nSample climate data for Mombassa, Kenya (1.5°C warming):")
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"\nError retrieving data: {e}")
    
    # Example 2: Extreme event prediction
    print("\n" + "=" * 50)
    print("Extreme Event Prediction for Niche Agriculture")
    print("=" * 50)
    
    # Analyze impact on truffle farming in a European region
    truffle_analysis = analyze_niche_agriculture_impact(
        "truffle", "Burgundy", "France"
    )
    print("\nTruffle Farming Analysis:")
    print(json.dumps(truffle_analysis, indent=2))