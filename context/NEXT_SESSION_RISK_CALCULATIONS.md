# Next Session Quick Start - Implement Real Risk Calculations

## 🎯 Primary Goal
Now that positions are loading correctly, implement real risk calculations for the 15 price scenarios instead of using placeholder values.

## ✅ What's Working
- All 33 positions loading correctly
- Expandable rows showing position details
- Risk matrix UI with 15 columns ready
- Column selector for hiding/showing scenarios

## 🔧 What Needs Implementation

### 1. Real Risk Calculations
The risk scenarios data is already being extracted but not used:
```python
# In _extract_position_data:
gains_losses = safe_get_list(product, "GainsAndLossesScenarios", [])
price_movements = safe_get_list(product, "PriceMovementValues", [])
scenario_percentages = safe_get_list(product, "ScenariosPercentages", [])
```

### 2. Fix Credit Utilization
All accounts show 0% credit utilization. Check if:
- Credit limit data exists in the response
- Calculation logic is correct
- Field names match the API response

### 3. Update Frontend Risk Display
- Remove placeholder random values
- Use real risk scenario data from backend
- Color code based on actual P&L values

## Quick Start Commands
```bash
# Start everything
cd C:\Development\sarna-insights-v2
docker-compose up -d

# Check that positions are still loading
curl http://localhost:8000/api/data/portfolio/10006/risk-matrix | jq '.accounts[1].positions[0].risk_scenarios'

# Monitor logs while implementing
docker-compose logs -f backend
```

## Key Files to Modify

### Backend: `/backend/services/portfolio_service.py`
- Line ~140: Fix credit utilization calculation
- Line ~350: Risk scenarios are already extracted, just need to be used

### Frontend: `/frontend/src/components/visualizations/PortfolioEnhanced.tsx`
- Remove random value generation for risk columns
- Use actual risk_scenarios data from API

## Testing Approach
1. Start with one account (e.g., TS4 with 6 positions)
2. Verify risk calculations in API response
3. Update frontend to display real values
4. Test column hiding/showing still works
5. Verify performance with all scenarios

## Expected Outcome
- Risk matrix shows real P&L for each price scenario
- Values change based on position size and price
- Options (if any) show non-linear risk profiles
- Credit utilization shows actual percentages

## Success Metrics
- No more `Math.random()` in risk calculations
- Risk values correlate with position sizes
- Larger positions show proportionally larger risk
- All 15 scenarios have distinct, realistic values