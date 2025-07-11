# UI Fixes Summary

## Fixed Issues:

### 1. ✅ S8 Column (0% Scenario) Value Fix
- Added logic to use position NAV value when gains_losses is 0 for scenario 8
- This is a workaround for the backend issue where 0% scenario returns $0
- Applied to both position-level and account-level displays

### 2. ✅ Removed IV Info from Type Column
- Volatility shock rows now just show "↑ Vol Up" and "↓ Vol Down"
- Removed the IV percentage display that was confusing

### 3. ✅ Simplified Column Headers
- Removed "S1:", "S2:", etc. prefixes
- Headers now show just the percentage values: "-15%", "-12%", "0%", "+15%", etc.
- Column tooltips still show full descriptions with IV shock info

### 4. ✅ Removed "Positions for [Account]" Headers
- Expanded sections now directly show the position table
- Saves vertical space and reduces clutter

### 5. ✅ Default Risk Scenarios to Visible
- Changed `visible: false` to `visible: true` for all risk scenario columns
- Users will see the full risk matrix by default

### 6. ✅ Added Tooltips to All Scenario Cells
- All risk scenario cells now have tooltips showing:
  - Main rows: "Px -15%, IV +50%/-20%" (example)
  - Volatility Up rows: "Px -15%, IV +50%/-20% (Volatility Up)"
  - Volatility Down rows: "Px -15%, IV +50%/-20% (Volatility Down)"
- Tooltips appear on hover for all cells in risk columns

## Test the Changes:
1. Navigate to http://localhost
2. The risk scenarios should be visible by default
3. Hover over any value in the risk columns to see the tooltip
4. Check the 0% column - it should show actual values, not $0
5. Expand an account with options to verify the 3-row display

## Note on Backend Issue:
The 0% scenario returning $0 is a backend bug. The frontend now works around this by using the NAV value when gains_losses is 0 for scenario index 7.