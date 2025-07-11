# Next Session: Fix Visualization Parsing

## 🎯 Primary Goal
Complete the visualization parsing implementation so that charts, tables, and matrices render when requested through the AI assistant.

## 🔍 Current Problem
LLMs (especially Google Gemini) return visualization JSON with syntax errors:
```javascript
// What we get:
'backgroundColor': ['rgba(54, 162, 235, 0.6)']  // Single quotes!

// What we need:
"backgroundColor": ["rgba(54, 162, 235, 0.6)"]  // Double quotes
```

## 📍 Where to Start
1. **File**: `/backend/routers/chat.py`
2. **Function**: `parse_llm_response()` (line ~58)
3. **Current partial fix**: Basic regex for single quotes (needs improvement)

## 🛠️ Implementation Tasks

### Task 1: Robust JSON Parsing
```python
def parse_llm_response(response: str) -> tuple[str, Optional[VisualizationData]]:
    # 1. Extract JSON from markdown code blocks
    # 2. Fix quote issues without breaking escaped quotes
    # 3. Handle nested structures properly
    # 4. Validate against expected schema
```

### Task 2: Test Cases
Create test cases for common LLM response patterns:
- JSON in ```json blocks
- Mixed single/double quotes
- Escaped quotes in strings
- Arrays with color values
- Nested visualization configs

### Task 3: Fallback Generation
If parsing fails, generate visualization server-side:
```python
# Detect intent from question
if "chart" in question and parsing_failed:
    return generate_chart_from_portfolio_data()
```

## 🧪 Testing Commands

```powershell
# Test 1: Bar chart request
$q1 = "Create a bar chart showing buying power for each account"

# Test 2: Table request  
$q2 = "Show me a table of accounts with their NAV values"

# Test 3: Risk matrix request
$q3 = "Display a risk matrix for my portfolio"

# Run test
$body = @{question=$q1; provider="google"; include_historical=$false} | ConvertTo-Json
Invoke-WebRequest -Uri http://localhost/api/chat/query -Method POST -Body $body -ContentType "application/json" -UseBasicParsing
```

## 📝 Success Criteria
1. ✅ Visualization object returned in API response (not null)
2. ✅ Charts render in the UI when requested
3. ✅ Tables display with proper formatting
4. ✅ No parsing errors in backend logs
5. ✅ Works with all three LLM providers

## 🚨 Watch Out For
- Don't break regular text responses while fixing visualization parsing
- Ensure escaped quotes in data aren't corrupted
- Handle edge cases (empty data, malformed JSON)
- Test with different LLM providers (they format differently)

## 💡 Quick Fixes to Try
1. **More sophisticated quote replacement**:
```python
# Don't just replace all single quotes
# Be smart about it - only in JSON contexts
```

2. **Use ast.literal_eval as fallback**:
```python
try:
    # Try json.loads first
except:
    # Try ast.literal_eval for Python literals
```

3. **Preprocess response before parsing**:
```python
# Remove markdown formatting
# Standardize whitespace
# Fix common LLM mistakes
```

## 🔄 Development Loop
1. Edit parse_llm_response()
2. Restart backend: `docker-compose restart backend`
3. Test with curl/PowerShell
4. Check logs: `docker-compose logs -f backend`
5. Verify in browser at http://localhost

## 📊 Expected Outcome
When asking "Show me a chart of account balances", the API should return:
```json
{
  "question": "Show me a chart of account balances",
  "answer": "Here's a visualization of account balances...",
  "provider": "google",
  "visualization": {
    "type": "chart",
    "title": "Account Balances",
    "data": { /* Chart.js config */ }
  }
}
```

Remember: The UI components are ready and waiting - we just need clean visualization data!