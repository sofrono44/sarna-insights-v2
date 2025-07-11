import React from 'react';
import { Alert } from './types';
import { AlertIcon } from './AlertIcon';

interface AlertListProps {
  alerts: Alert[];
  onAcknowledge?: (alertId: number) => void;
  onResolve?: (alertId: number) => void;
}

export const AlertList: React.FC<AlertListProps> = ({ 
  alerts, 
  onAcknowledge,
  onResolve 
}) => {
  const formatTime = (timestamp: string) => {
    const date = new Date(timestamp);
    const now = new Date();
    const diffMs = now.getTime() - date.getTime();
    const diffMins = Math.floor(diffMs / 60000);
    
    if (diffMins < 60) return `${diffMins}m ago`;
    const diffHours = Math.floor(diffMins / 60);
    if (diffHours < 24) return `${diffHours}h ago`;
    const diffDays = Math.floor(diffHours / 24);
    return `${diffDays}d ago`;
  };

  const statusColors = {
    open: 'bg-red-50 border-red-200',
    acknowledged: 'bg-yellow-50 border-yellow-200',
    resolved: 'bg-green-50 border-green-200'
  };

  const statusBadgeColors = {
    open: 'bg-red-100 text-red-800',
    acknowledged: 'bg-yellow-100 text-yellow-800',
    resolved: 'bg-green-100 text-green-800'
  };

  if (alerts.length === 0) {
    return (
      <div className="text-center py-8 text-gray-500">
        <svg className="mx-auto h-12 w-12 text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <p className="mt-2">No active alerts</p>
      </div>
    );
  }

  return (
    <div className="space-y-3">
      {alerts.map((alert) => (
        <div
          key={alert.alert_id}
          className={`
            border rounded-lg p-4 transition-all duration-200
            ${statusColors[alert.status]}
            ${alert.status === 'open' ? 'shadow-sm hover:shadow-md' : ''}
          `}
        >
          <div className="flex items-start justify-between">
            <div className="flex items-start space-x-3">
              <AlertIcon severity={alert.severity} size="md" />
              <div className="flex-1">
                <div className="flex items-center space-x-2">
                  <span className="font-semibold text-gray-900">
                    {alert.account_number}
                  </span>
                  <span className={`
                    inline-flex items-center px-2 py-0.5 rounded text-xs font-medium
                    ${statusBadgeColors[alert.status]}
                  `}>
                    {alert.status.charAt(0).toUpperCase() + alert.status.slice(1)}
                  </span>
                </div>
                <p className="mt-1 text-sm text-gray-700">{alert.message}</p>
                <div className="mt-2 text-xs text-gray-500 space-x-4">
                  <span>Created: {formatTime(alert.created_time)}</span>
                  {alert.current_value && (
                    <span>Current: {alert.current_value.toFixed(1)}%</span>
                  )}
                </div>
              </div>
            </div>
            
            {alert.status === 'open' && (
              <div className="flex flex-col space-y-1">
                {onAcknowledge && (
                  <button
                    onClick={() => onAcknowledge(alert.alert_id)}
                    className="text-xs px-3 py-1 bg-yellow-500 text-white rounded hover:bg-yellow-600 transition-colors"
                  >
                    Acknowledge
                  </button>
                )}
                {onResolve && (
                  <button
                    onClick={() => onResolve(alert.alert_id)}
                    className="text-xs px-3 py-1 bg-green-500 text-white rounded hover:bg-green-600 transition-colors"
                  >
                    Resolve
                  </button>
                )}
              </div>
            )}
          </div>
        </div>
      ))}
    </div>
  );
};
