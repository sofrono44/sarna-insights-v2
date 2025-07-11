import React, { useState } from 'react';
import { ChevronLeft, ChevronRight, X } from 'lucide-react';
import { MarginUtilizationChart } from './MarginUtilizationChart';

interface Visualization {
  id: string;
  type: 'margin-utilization' | 'portfolio-trends' | 'risk-analysis' | 'custom';
  title: string;
  data: any;
  timestamp: Date;
  fromChat?: boolean;
}

export const VisualizationContainer: React.FC = () => {
  const [visualizations, setVisualizations] = useState<Visualization[]>([
    {
      id: 'default-margin',
      type: 'margin-utilization',
      title: 'Margin Utilization by Account',
      data: null,
      timestamp: new Date(),
      fromChat: false
    }
  ]);
  const [currentIndex, setCurrentIndex] = useState(0);

  // This would be called from the chat component when a visualization is requested
  const addVisualization = (viz: Omit<Visualization, 'id' | 'timestamp'>) => {
    const newViz: Visualization = {
      ...viz,
      id: `viz-${Date.now()}`,
      timestamp: new Date()
    };
    setVisualizations(prev => [...prev, newViz]);
    setCurrentIndex(visualizations.length); // Navigate to the new visualization
  };

  const navigate = (direction: 'prev' | 'next') => {
    if (direction === 'prev' && currentIndex > 0) {
      setCurrentIndex(currentIndex - 1);
    } else if (direction === 'next' && currentIndex < visualizations.length - 1) {
      setCurrentIndex(currentIndex + 1);
    }
  };

  const removeVisualization = (index: number) => {
    if (visualizations.length === 1) return; // Keep at least one
    
    setVisualizations(prev => prev.filter((_, i) => i !== index));
    if (currentIndex >= index && currentIndex > 0) {
      setCurrentIndex(currentIndex - 1);
    }
  };

  const current = visualizations[currentIndex];

  return (
    <div className="bg-gray-50 border border-gray-200 rounded-lg p-6">
      {/* Header with navigation */}
      <div className="flex justify-between items-center mb-4">
        <div className="flex items-center gap-4">
          <h3 className="text-lg font-semibold text-gray-900">{current.title}</h3>
          {current.fromChat && (
            <span className="px-2 py-1 text-xs font-medium rounded bg-blue-50 text-blue-700">
              From Chat
            </span>
          )}
        </div>
        
        {/* Navigation controls */}
        <div className="flex items-center gap-2">
          <button
            onClick={() => navigate('prev')}
            disabled={currentIndex === 0}
            className={`p-1.5 rounded ${
              currentIndex === 0 
                ? 'text-gray-300 cursor-not-allowed' 
                : 'text-gray-600 hover:bg-gray-100'
            }`}
          >
            <ChevronLeft className="w-4 h-4" />
          </button>
          
          <span className="text-sm text-gray-600">
            {currentIndex + 1} / {visualizations.length}
          </span>
          
          <button
            onClick={() => navigate('next')}
            disabled={currentIndex === visualizations.length - 1}
            className={`p-1.5 rounded ${
              currentIndex === visualizations.length - 1 
                ? 'text-gray-300 cursor-not-allowed' 
                : 'text-gray-600 hover:bg-gray-100'
            }`}
          >
            <ChevronRight className="w-4 h-4" />
          </button>
          
          {visualizations.length > 1 && (
            <button
              onClick={() => removeVisualization(currentIndex)}
              className="p-1.5 rounded text-gray-600 hover:bg-gray-100 ml-2"
              title="Remove this visualization"
            >
              <X className="w-4 h-4" />
            </button>
          )}
        </div>
      </div>

      {/* Visualization content */}
      <div className="h-64">
        {current.type === 'margin-utilization' && <MarginUtilizationChart />}
        {/* Add other visualization types here */}
      </div>

      {/* History dots */}
      {visualizations.length > 1 && (
        <div className="flex justify-center gap-1 mt-4">
          {visualizations.map((_, index) => (
            <button
              key={index}
              onClick={() => setCurrentIndex(index)}
              className={`w-2 h-2 rounded-full transition-colors ${
                index === currentIndex 
                  ? 'bg-blue-600' 
                  : 'bg-gray-300 hover:bg-gray-400'
              }`}
            />
          ))}
        </div>
      )}
    </div>
  );
};
