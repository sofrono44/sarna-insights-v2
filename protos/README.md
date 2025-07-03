# Proto Files Directory

Place your risk system's `.proto` files in this directory.

## Structure

```
proto/
├── risk_service.proto      # Main risk service definitions
├── common.proto           # Common message types
├── portfolio.proto        # Portfolio-related messages
└── margin.proto          # Margin calculation messages
```

## Generating Python Code

Run the generation script after adding proto files:

```bash
python scripts/generate_proto.py
```

This will generate Python code in `app/grpc_generated/`

## Example Proto File

```protobuf
syntax = "proto3";

package risk;

service RiskService {
  rpc GetPortfolioRisk (PortfolioRequest) returns (PortfolioRiskResponse);
  rpc StreamRiskUpdates (StreamRequest) returns (stream RiskUpdate);
}

message PortfolioRequest {
  string account_id = 1;
  string as_of_date = 2;
}

message PortfolioRiskResponse {
  string account_id = 1;
  double total_margin = 2;
  repeated Position positions = 3;
}
```