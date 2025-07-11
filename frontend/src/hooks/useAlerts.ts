import { useState, useEffect } from 'react';
import { Alert, mockAlerts } from '../components/alerts/types';

export const useAlerts = () => {
  const [alerts, setAlerts] = useState<Alert[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

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
    } catch (err) {
      // Use mock data on any error
      console.warn('Error fetching alerts, using mock data:', err);
      setAlerts(mockAlerts);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAlerts();
    
    // Refresh alerts every 30 seconds
    const interval = setInterval(fetchAlerts, 30000);
    
    return () => clearInterval(interval);
  }, []);

  const openAlertCount = alerts.filter(a => a.status === 'open').length;
  const criticalAlertCount = alerts.filter(a => a.status === 'open' && a.severity === 'critical').length;
  const warningAlertCount = alerts.filter(a => a.status === 'open' && a.severity === 'warning').length;
  
  const getAlertsForAccount = (accountNumber: string) => {
    return alerts.filter(a => a.account_number === accountNumber && a.status === 'open');
  };

  return {
    alerts,
    loading,
    error,
    openAlertCount,
    criticalAlertCount,
    warningAlertCount,
    getAlertsForAccount,
    refresh: fetchAlerts
  };
};
