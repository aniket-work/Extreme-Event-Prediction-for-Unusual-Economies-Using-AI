# Climate Change Assistant - Simplified Version

A streamlined Python application for predicting how extreme warming scenarios could impact niche agricultural exports and micro-economies.

## Features

- Retrieve climate data from Probable Futures API
- Predict impact of extreme warming scenarios on specific locations
- Analyze climate risks for niche agriculture (truffles, ice wine, saffron)
- Generate recommendations for adaptation strategies

## Installation

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Set up your environment variables:
   - Copy `.env.example` to `.env`
   - Fill in your Probable Futures API credentials

## Usage

```python
from climate_assistant import analyze_niche_agriculture_impact

# Analyze impact on truffle farming in France
result = analyze_niche_agriculture_impact("truffle", "Burgundy", "France")
print(result)
```

## Example Applications

### Extreme Event Prediction for Unusual Economies

This tool can forecast how rare or extreme warming scenarios could impact:
- Truffle farming
- Ice wine production
- Saffron cultivation
- Other micro-economies dependent on specific climate patterns

## API Reference

### `predict_extreme_event_impact(address, country, warming_scenarios)`
Predict impact of extreme warming scenarios on specific locations.

### `analyze_niche_agriculture_impact(agriculture_type, address, country)`
Analyze how climate change might impact niche agriculture.

### `get_pf_data(address, country, warming_scenario)`
Direct access to Probable Futures climate data.