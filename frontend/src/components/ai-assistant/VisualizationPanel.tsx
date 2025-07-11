import React from 'react';
import { X, Download, Maximize2, BarChart2, Table, Grid3X3, HelpCircle } from 'lucide-react';
import { VisualizationData } from './types';
import ChartVisualization from './visualizations/ChartVisualization';
import TableVisualization from './visualizations/TableVisualization';
import RiskMatrixVisualization from './visualizations/RiskMatrixVisualization';

interface VisualizationPanelProps {
  visualization: VisualizationData | null;
  onClear: () => void;
}

const VisualizationPanel: React.FC<VisualizationPanelProps> = ({ visualization, onClear }) => {
  const getIcon = () => {
    if (!visualization) return <HelpCircle className="w-8 h-8" />;
    
    switch (visualization.type) {
      case 'chart':
        return <BarChart2 className="w-8 h-8" />;
      case 'table':
        return <Table className="w-8 h-8" />;
      case 'risk-matrix':
        return <Grid3X3 className="w-8 h-8" />;
      default:
        return <BarChart2 className="w-8 h-8" />;
    }
  };

  const renderVisualization = () => {
    if (!visualization) return null;

    switch (visualization.type) {
      case 'chart':
        return <ChartVisualization data={visualization.data} config={visualization.config} />;
      case 'table':
        return <TableVisualization data={visualization.data} />;
      case 'risk-matrix':
        return <RiskMatrixVisualization data={visualization.data} />;
      default:
        return <div>Unsupported visualization type</div>;
    }
  };

  const handleExport = () => {
    // Implement export functionality
    console.log('Exporting visualization...');
  };

  if (!visualization) {
    return (
      <div className="h-full flex items-center justify-center">
        <div className="text-center">
          <div className="text-gray-400 mb-4">
            {getIcon()}
          </div>
          <h3 className="text-lg font-medium text-gray-700 mb-2">
            No Visualization Selected
          </h3>
          <p className="text-sm text-gray-500 max-w-md">
            Ask the AI assistant to generate charts, tables, or risk matrices based on your portfolio data.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="h-full flex flex-col">
      {/* Header */}
      <div className="flex items-center justify-between p-4 border-b border-gray-200">
        <div>
          <h3 className="text-lg font-semibold text-gray-900">{visualization.title}</h3>
          {visualization.description && (
            <p className="text-sm text-gray-600 mt-1">{visualization.description}</p>
          )}
        </div>
        
        <div className="flex items-center gap-2">
          <button
            onClick={handleExport}
            className="p-2 text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg transition-colors"
            title="Export visualization"
          >
            <Download className="w-5 h-5" />
          </button>
          <button
            onClick={() => {/* Implement fullscreen */}}
            className="p-2 text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg transition-colors"
            title="Fullscreen"
          >
            <Maximize2 className="w-5 h-5" />
          </button>
          <button
            onClick={onClear}
            className="p-2 text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-lg transition-colors"
            title="Close visualization"
          >
            <X className="w-5 h-5" />
          </button>
        </div>
      </div>
      
      {/* Visualization Content */}
      <div className="flex-1 p-4 overflow-auto">
        {renderVisualization()}
      </div>
    </div>
  );
};

export default VisualizationPanel;
