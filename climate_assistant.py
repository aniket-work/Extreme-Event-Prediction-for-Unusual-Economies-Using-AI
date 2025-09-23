import os
import json
import requests
from datetime import date, datetime
from dotenv import load_dotenv

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