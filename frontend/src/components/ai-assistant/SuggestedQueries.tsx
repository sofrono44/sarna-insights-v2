import React from 'react';
import { Lightbulb } from 'lucide-react';
import { SUGGESTED_QUERIES } from './types';

interface SuggestedQueriesProps {
  onQuerySelect: (query: string) => void;
}

const SuggestedQueries: React.FC<SuggestedQueriesProps> = ({ onQuerySelect }) => {
  return (
    <div className="mt-4">
      <div className="flex items-center gap-2 text-sm text-gray-600 mb-3">
        <Lightbulb className="w-4 h-4" />
        <span>Suggested queries:</span>
      </div>
      
      <div className="grid grid-cols-1 gap-2">
        {SUGGESTED_QUERIES.slice(0, 5).map((query, index) => (
          <button
            key={index}
            onClick={() => onQuerySelect(query)}
            className="text-left px-3 py-2 text-sm border border-gray-200 rounded-lg hover:bg-gray-50 hover:border-gray-300 transition-colors"
          >
            {query}
          </button>
        ))}
      </div>
      
      <div className="mt-3 text-xs text-gray-500">
        Click any suggestion or type your own question
      </div>
    </div>
  );
};

export default SuggestedQueries;
