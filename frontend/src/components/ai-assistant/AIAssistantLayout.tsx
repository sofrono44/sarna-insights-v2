import React, { useState } from 'react';
import { ChevronLeft, ChevronRight } from 'lucide-react';
import ChatPanel from './ChatPanel';
import VisualizationPanel from './VisualizationPanel';
import { VisualizationData } from './types';

interface AIAssistantLayoutProps {
  children: React.ReactNode;
}

const AIAssistantLayout: React.FC<AIAssistantLayoutProps> = ({ children }) => {
  const [showAssistant, setShowAssistant] = useState(true);
  const [activeVisualization, setActiveVisualization] = useState<VisualizationData | null>(null);
  const [splitPosition, setSplitPosition] = useState(35); // percentage

  const handleVisualizationRequest = (visualization: VisualizationData) => {
    setActiveVisualization(visualization);
    // Ensure the assistant is visible when a visualization is generated
    if (!showAssistant) {
      setShowAssistant(true);
    }
  };

  return (
    <div className="flex flex-col h-full">
      {/* Dashboard content (cards and portfolio table) */}
      <div className="flex-shrink-0">
        {children}
      </div>
      
      {/* AI Assistant Section */}
      <div className="mt-6">
        <div className="bg-white border border-gray-200 rounded-lg shadow-sm overflow-hidden">
          {/* Section Header */}
          <div className="bg-gray-50 border-b border-gray-200 px-4 py-3 flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <h3 className="text-lg font-semibold text-gray-900">AI Risk Assistant</h3>
              <span className="text-sm text-gray-500">
                {activeVisualization ? 'Viewing visualization' : 'Ask questions about your portfolio'}
              </span>
            </div>
            <button
              onClick={() => setShowAssistant(!showAssistant)}
              className="p-1 hover:bg-gray-200 rounded transition-colors"
              aria-label={showAssistant ? 'Hide assistant' : 'Show assistant'}
            >
              {showAssistant ? <ChevronLeft className="w-5 h-5" /> : <ChevronRight className="w-5 h-5" />}
            </button>
          </div>

          {/* Split View Container */}
          <div className="relative flex h-[600px]">
            {/* Chat Panel */}
            <div 
              className={`${showAssistant ? `w-[${splitPosition}%]` : 'w-0'} transition-all duration-300 border-r border-gray-200 overflow-hidden`}
              style={{ width: showAssistant ? `${splitPosition}%` : '0' }}
            >
              <ChatPanel 
                onVisualizationRequest={handleVisualizationRequest}
                isVisible={showAssistant}
              />
            </div>
            
            {/* Resize Handle */}
            {showAssistant && (
              <div 
                className="absolute top-0 bottom-0 w-1 cursor-col-resize hover:bg-blue-500 transition-colors z-10"
                style={{ left: `${splitPosition}%` }}
                onMouseDown={(e) => {
                  const startX = e.clientX;
                  const startSplit = splitPosition;
                  
                  const handleMouseMove = (e: MouseEvent) => {
                    const containerWidth = (e.target as HTMLElement).parentElement?.offsetWidth || 1;
                    const deltaX = e.clientX - startX;
                    const deltaPercent = (deltaX / containerWidth) * 100;
                    const newSplit = Math.max(20, Math.min(50, startSplit + deltaPercent));
                    setSplitPosition(newSplit);
                  };
                  
                  const handleMouseUp = () => {
                    document.removeEventListener('mousemove', handleMouseMove);
                    document.removeEventListener('mouseup', handleMouseUp);
                  };
                  
                  document.addEventListener('mousemove', handleMouseMove);
                  document.addEventListener('mouseup', handleMouseUp);
                }}
              />
            )}
            
            {/* Visualization Panel */}
            <div className={`${showAssistant ? 'flex-1' : 'w-full'} bg-gray-50`}>
              <VisualizationPanel 
                visualization={activeVisualization}
                onClear={() => setActiveVisualization(null)}
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AIAssistantLayout;
