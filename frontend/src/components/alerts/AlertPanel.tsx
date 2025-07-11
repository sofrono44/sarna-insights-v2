import React, { useEffect, useState } from 'react';
import { Alert, mockAlerts } from './types';
import { AlertList } from './AlertList';
import { AlertBadge } from './AlertBadge';

interface AlertPanelProps {
  isOpen: boolean;
  onClose: () => void;
}

export const AlertPanel: React.FC<AlertPanelProps> = ({ isOpen, onClose }) => {
  const [alerts, setAlerts] = useState<Alert[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (isOpen) {
      fetchAlerts();
    }
  }, [isOpen]);

  const fetchAlerts = async () => {
    try {
      setLoading(true);
      setError(null);
      
      const response = await fetch('/api/data/alerts?page=1&page_size=50');
      
      if (!response.ok) {
        // Use mock data if backend returns error
        console.warn('Alert service unavailable, using mock data');
        setAlerts(mockAlerts);
      } else {
        const data = await response.json();
        setAlerts(data.alerts);
      }
    } catch (err) {      // Use mock data on any error
      console.warn('Error fetching alerts, using mock data:', err);
      setAlerts(mockAlerts);
    } finally {
      setLoading(false);
    }
  };

  const handleAcknowledge = async (alertId: number) => {
    // In a real app, this would call the API
    setAlerts(prev => prev.map(alert => 
      alert.alert_id === alertId 
        ? { ...alert, status: 'acknowledged' as const, acknowledged_time: new Date().toISOString() }
        : alert
    ));
  };

  const handleResolve = async (alertId: number) => {
    // In a real app, this would call the API
    setAlerts(prev => prev.map(alert => 
      alert.alert_id === alertId 
        ? { ...alert, status: 'resolved' as const, resolved_time: new Date().toISOString() }
        : alert
    ));
  };

  const openAlerts = alerts.filter(a => a.status === 'open');
  const criticalCount = openAlerts.filter(a => a.severity === 'critical').length;
  const warningCount = openAlerts.filter(a => a.severity === 'warning').length;

  if (!isOpen) return null;
  return (
    <>
      {/* Backdrop */}
      <div 
        className="fixed inset-0 bg-black bg-opacity-50 z-40 transition-opacity"
        onClick={onClose}
      />
      
      {/* Panel */}
      <div className="fixed right-0 top-0 h-full w-full sm:w-96 bg-white shadow-xl z-50 transform transition-transform">
        <div className="flex flex-col h-full">
          {/* Header */}
          <div className="px-6 py-4 border-b border-gray-200">
            <div className="flex items-center justify-between">
              <div>
                <h2 className="text-xl font-semibold text-gray-900">Alerts</h2>
                <div className="flex items-center space-x-4 mt-2 text-sm">
                  {criticalCount > 0 && (
                    <span className="flex items-center space-x-1">
                      <span className="h-2 w-2 bg-red-600 rounded-full"></span>
                      <span className="text-gray-600">{criticalCount} Critical</span>
                    </span>
                  )}
                  {warningCount > 0 && (
                    <span className="flex items-center space-x-1">
                      <span className="h-2 w-2 bg-yellow-500 rounded-full"></span>
                      <span className="text-gray-600">{warningCount} Warning</span>
                    </span>
                  )}
                </div>
              </div>              <button
                onClick={onClose}
                className="p-1 rounded-md hover:bg-gray-100 transition-colors"
              >
                <svg className="h-6 w-6 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
          </div>
          
          {/* Content */}
          <div className="flex-1 overflow-y-auto px-6 py-4">
            {loading ? (
              <div className="flex items-center justify-center py-12">
                <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
              </div>
            ) : error ? (
              <div className="text-center py-8 text-red-600">
                <p>{error}</p>
              </div>
            ) : (
              <AlertList 
                alerts={alerts} 
                onAcknowledge={handleAcknowledge}
                onResolve={handleResolve}
              />
            )}
          </div>
        </div>
      </div>
    </>
  );
};