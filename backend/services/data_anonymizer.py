"""Data anonymization service to protect PII."""
import re
from typing import Dict, Any, List
import hashlib
import json


class DataAnonymizer:
    """Service to strip PII before sending data to LLMs."""
    
    def __init__(self):
        self.account_mapping = {}
        self.reverse_mapping = {}
        self._counter = 0
    
    def anonymize_account_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Anonymize account data by replacing identifiers."""
        anonymized = data.copy()
        
        # Replace account numbers
        if 'account_number' in anonymized:
            anon_id = self._get_anonymous_id(anonymized['account_number'])
            anonymized['account_number'] = anon_id
        
        # Replace account IDs
        if 'account_id' in anonymized:
            anon_id = self._get_anonymous_id(anonymized['account_id'])
            anonymized['account_id'] = anon_id
            
        # Remove any personal information fields
        pii_fields = ['name', 'email', 'phone', 'address', 'ssn', 'tax_id']
        for field in pii_fields:
            if field in anonymized:
                del anonymized[field]
        
        return anonymized
    
    def anonymize_portfolio_data(self, portfolio: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Anonymize a list of account data."""
        return [self.anonymize_account_data(account) for account in portfolio]
    
    def _get_anonymous_id(self, original_id: str) -> str:
        """Get or create anonymous ID for an account."""
        if original_id not in self.account_mapping:
            self._counter += 1
            anon_id = f"ACCOUNT_{self._counter}"
            self.account_mapping[original_id] = anon_id
            self.reverse_mapping[anon_id] = original_id
        return self.account_mapping[original_id]
    
    def restore_identifiers(self, text: str) -> str:
        """Restore original identifiers in LLM response."""
        result = text
        for anon_id, original_id in self.reverse_mapping.items():
            result = result.replace(anon_id, original_id)
        return result
    
    def get_context_for_llm(self, data: Any) -> str:
        """Create anonymized context string for LLM."""
        if isinstance(data, list):
            anonymized = self.anonymize_portfolio_data(data)
        elif isinstance(data, dict):
            anonymized = self.anonymize_account_data(data)
        else:
            anonymized = data
        
        return json.dumps(anonymized, indent=2)
