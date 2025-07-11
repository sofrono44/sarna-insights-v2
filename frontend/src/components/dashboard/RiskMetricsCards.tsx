import React, { useState } from 'react';
import { TrendingUp, TrendingDown, AlertCircle, Shield, Phone, Gavel, AlertTriangle } from 'lucide-react';
import { useQuery } from '@tanstack/react-query';
import { CardSkeleton } from '@/components/common/Skeleton';
import { useAlerts } from '@/hooks/useAlerts';
import { AlertPanel } from '@/components/alerts';
import { Drawer } from '@/components/common/Drawer';
import { mockCalls } from '@/components/calls/types';
import { mockPDTAlerts } from '@/components/pdt/types';
import { mockLiquidationAlerts } from '@/components/liquidation/types';

interface MetricCard {
  id: string;
  title: string;
  subtitle: string;
  value: string | number;
  change?: {
    value: number;
    label: string;
    positive: boolean;
  };
  badge?: {
    text: string;
    type: 'ai' | 'info' | 'live' | 'alert' | 'warning' | 'critical';
  };
  icon?: React.ReactNode;
  onClick?: () => void;
}

export const RiskMetricsCards: React.FC = () => {
  const { data: portfolio, isLoading: portfolioLoading } = useQuery({
    queryKey: ['portfolio-risk-matrix'],
    queryFn: async () => {
      const response = await fetch('/api/data/portfolio/10006/risk-matrix');
      if (!response.ok) throw new Error('Failed to fetch portfolio data');
      return response.json();
    },
  });
  const { openAlertCount, criticalAlertCount, warningAlertCount, loading: alertsLoading } = useAlerts();
  
  // Drawer states
  const [isAlertPanelOpen, setIsAlertPanelOpen] = useState(false);
  const [isCallsDrawerOpen, setIsCallsDrawerOpen] = useState(false);
  const [isPDTDrawerOpen, setIsPDTDrawerOpen] = useState(false);
  const [isLiquidationDrawerOpen, setIsLiquidationDrawerOpen] = useState(false);

  // Calculate metrics from mock data
  const fedCalls = mockCalls.filter(c => c.call_type === 'fed').length;
  const houseCalls = mockCalls.filter(c => c.call_type === 'house').length;
  const pdtAlerts = mockPDTAlerts.length;
  const liquidationAlerts = mockLiquidationAlerts.length;

  // Calculate metrics from portfolio data
  const metrics: MetricCard[] = React.useMemo(() => {
    return [
      {
        id: 'alerts',
        title: 'Active Alerts',
        subtitle: `${criticalAlertCount} critical, ${warningAlertCount} warning`,
        value: openAlertCount,
        badge: { 
          text: criticalAlertCount > 0 ? 'Critical' : warningAlertCount > 0 ? 'Warning' : 'Clear', 
          type: criticalAlertCount > 0 ? 'critical' : warningAlertCount > 0 ? 'warning' : 'info'
        },
        icon: <AlertCircle className="w-5 h-5" />,
        onClick: () => setIsAlertPanelOpen(true)
      },
      {
        id: 'calls',
        title: 'Calls',
        subtitle: `${fedCalls} Fed, ${houseCalls} House`,
        value: fedCalls + houseCalls,        badge: { text: 'Urgent', type: 'critical' },
        icon: <Phone className="w-5 h-5" />,
        onClick: () => setIsCallsDrawerOpen(true)
      },
      {
        id: 'pdt',
        title: 'Pattern Day Trader',
        subtitle: `${pdtAlerts} accounts flagged`,
        value: pdtAlerts,
        change: {
          value: 2,
          label: 'from yesterday',
          positive: false,
        },
        icon: <Gavel className="w-5 h-5" />,
        onClick: () => setIsPDTDrawerOpen(true)
      },
      {
        id: 'liquidation',
        title: 'Liquidation Alerts',
        subtitle: 'End of day liquidations',
        value: liquidationAlerts,
        badge: { text: 'EOD', type: 'warning' },
        icon: <AlertTriangle className="w-5 h-5" />,
        onClick: () => setIsLiquidationDrawerOpen(true)
      },
    ];
  }, [openAlertCount, criticalAlertCount, warningAlertCount, fedCalls, houseCalls, pdtAlerts, liquidationAlerts]);

  const getBadgeStyles = (type: string) => {
    switch (type) {
      case 'ai':
        return 'bg-green-50 text-green-700';
      case 'info':
        return 'bg-blue-50 text-blue-700';
      case 'live':
        return 'bg-blue-50 text-blue-700';
      case 'warning':
        return 'bg-yellow-50 text-yellow-700';
      case 'critical':
        return 'bg-red-50 text-red-700';
      default:
        return 'bg-gray-50 text-gray-700';
    }
  };

  const getIconColor = (metric: MetricCard) => {
    switch(metric.id) {
      case 'alerts':
        if (criticalAlertCount > 0) return 'text-red-600';
        if (warningAlertCount > 0) return 'text-yellow-600';
        return 'text-green-600';
      case 'calls':
        return 'text-red-600';
      case 'pdt':
        return 'text-yellow-600';
      case 'liquidation':
        return 'text-orange-600';
      default:
        return 'text-blue-600';
    }
  };

  if (portfolioLoading || alertsLoading) {
    return (
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        {[...Array(4)].map((_, i) => (
          <CardSkeleton key={i} />
        ))}
      </div>
    );
  }
  return (
    <>
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        {metrics.map((metric) => (
          <div
            key={metric.id}
            className={`bg-white border border-gray-200 rounded-lg p-4 transition-all duration-200 ${
              metric.onClick ? 'cursor-pointer hover:shadow-lg hover:border-gray-300' : 'hover:shadow-lg'
            }`}
            onClick={metric.onClick}
          >
            <div className="flex justify-between items-start mb-2">
              <div className="flex-1">
                <div className="flex items-center gap-2">
                  {metric.icon && (
                    <div className={getIconColor(metric)}>
                      {metric.icon}
                    </div>
                  )}
                  <h3 className="text-sm font-semibold text-gray-900">{metric.title}</h3>
                </div>
                <p className="text-xs text-gray-600 mt-0.5">{metric.subtitle}</p>
              </div>
              {metric.badge && (
                <span
                  className={`px-2 py-0.5 text-xs font-medium rounded-full ${getBadgeStyles(
                    metric.badge.type
                  )}`}
                >
                  {metric.badge.text}
                </span>
              )}
            </div>
            
            <div className="mt-3">
              <div className="text-2xl font-bold text-gray-900">
                {metric.value}
              </div>
              
              {metric.change && (
                <div
                  className={`flex items-center gap-1 text-xs font-medium mt-1 ${
                    metric.change.positive ? 'text-green-600' : 'text-red-600'
                  }`}
                >
                  {metric.change.positive ? (
                    <TrendingUp className="w-3 h-3" />
                  ) : (
                    <TrendingDown className="w-3 h-3" />
                  )}
                  <span>{Math.abs(metric.change.value)}% {metric.change.label}</span>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
      {/* Alert Panel */}
      <AlertPanel 
        isOpen={isAlertPanelOpen} 
        onClose={() => setIsAlertPanelOpen(false)} 
      />

      {/* Calls Drawer */}
      <Drawer
        isOpen={isCallsDrawerOpen}
        onClose={() => setIsCallsDrawerOpen(false)}
        title="Margin Calls"
        subtitle={`${fedCalls} Federal, ${houseCalls} House calls`}
      >
        <div className="p-4 space-y-3">
          {mockCalls.map(call => (
            <div 
              key={call.call_id}
              className={`p-4 rounded-lg border ${
                call.status === 'overdue' 
                  ? 'bg-red-50 border-red-200' 
                  : 'bg-yellow-50 border-yellow-200'
              }`}
            >
              <div className="flex justify-between items-start mb-2">
                <div>
                  <span className="font-semibold text-gray-900">{call.account_number}</span>
                  <span className={`ml-2 px-2 py-0.5 text-xs font-medium rounded-full ${
                    call.call_type === 'fed' 
                      ? 'bg-red-100 text-red-700' 
                      : 'bg-orange-100 text-orange-700'
                  }`}>
                    {call.call_type === 'fed' ? 'Federal' : 'House'}
                  </span>
                  {call.status === 'overdue' && (
                    <span className="ml-2 px-2 py-0.5 text-xs font-medium rounded-full bg-red-600 text-white">
                      OVERDUE
                    </span>
                  )}
                </div>
                <span className="text-lg font-bold text-gray-900">
                  ${(call.amount / 1000).toFixed(0)}k
                </span>
              </div>
              <p className="text-sm text-gray-700 mb-2">{call.description}</p>
              <div className="text-xs text-gray-600">
                Due: {new Date(call.due_date).toLocaleDateString()}
              </div>
            </div>
          ))}
        </div>
      </Drawer>
      {/* PDT Drawer */}
      <Drawer
        isOpen={isPDTDrawerOpen}
        onClose={() => setIsPDTDrawerOpen(false)}
        title="Pattern Day Trader Alerts"
        subtitle={`${pdtAlerts} accounts affected`}
      >
        <div className="p-4 space-y-3">
          {mockPDTAlerts.map(alert => (
            <div 
              key={alert.alert_id}
              className={`p-4 rounded-lg border ${
                alert.status === 'restricted' 
                  ? 'bg-red-50 border-red-200' 
                  : alert.status === 'flagged'
                  ? 'bg-orange-50 border-orange-200'
                  : 'bg-yellow-50 border-yellow-200'
              }`}
            >
              <div className="flex justify-between items-start mb-2">
                <div>
                  <span className="font-semibold text-gray-900">{alert.account_number}</span>
                  <span className={`ml-2 px-2 py-0.5 text-xs font-medium rounded-full ${
                    alert.status === 'restricted' 
                      ? 'bg-red-100 text-red-700' 
                      : alert.status === 'flagged'
                      ? 'bg-orange-100 text-orange-700'
                      : 'bg-yellow-100 text-yellow-700'
                  }`}>
                    {alert.status.toUpperCase()}
                  </span>
                </div>
              </div>
              <div className="grid grid-cols-2 gap-2 text-sm">
                <div>
                  <span className="text-gray-600">Day Trades:</span>
                  <span className="ml-1 font-medium">{alert.day_trades_count}/4</span>
                </div>
                <div>
                  <span className="text-gray-600">5-Day Count:</span>
                  <span className="ml-1 font-medium">{alert.rolling_5_day_count}</span>
                </div>
                <div>
                  <span className="text-gray-600">Equity:</span>
                  <span className={`ml-1 font-medium ${
                    alert.equity < alert.minimum_equity_required ? 'text-red-600' : 'text-green-600'
                  }`}>
                    ${(alert.equity / 1000).toFixed(0)}k
                  </span>
                </div>
                <div>
                  <span className="text-gray-600">Required:</span>
                  <span className="ml-1 font-medium">${(alert.minimum_equity_required / 1000).toFixed(0)}k</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </Drawer>
      {/* Liquidation Drawer */}
      <Drawer
        isOpen={isLiquidationDrawerOpen}
        onClose={() => setIsLiquidationDrawerOpen(false)}
        title="Liquidation Alerts"
        subtitle="Positions requiring liquidation"
      >
        <div className="p-4 space-y-3">
          {mockLiquidationAlerts.map(alert => (
            <div 
              key={alert.alert_id}
              className={`p-4 rounded-lg border ${
                alert.priority === 'immediate' 
                  ? 'bg-red-50 border-red-200 animate-pulse' 
                  : alert.priority === 'eod'
                  ? 'bg-orange-50 border-orange-200'
                  : 'bg-yellow-50 border-yellow-200'
              }`}
            >
              <div className="flex justify-between items-start mb-2">
                <div>
                  <span className="font-semibold text-gray-900">{alert.account_number}</span>
                  <span className={`ml-2 px-2 py-0.5 text-xs font-medium rounded-full ${
                    alert.priority === 'immediate' 
                      ? 'bg-red-600 text-white' 
                      : alert.priority === 'eod'
                      ? 'bg-orange-100 text-orange-700'
                      : 'bg-yellow-100 text-yellow-700'
                  }`}>
                    {alert.priority === 'immediate' ? 'IMMEDIATE' : alert.priority === 'eod' ? 'EOD' : 'WARNING'}
                  </span>
                </div>
                <span className="text-xs font-medium text-gray-600">
                  {alert.liquidation_time}
                </span>
              </div>
              <div className="mb-2">
                <div className="flex justify-between items-center">
                  <span className="font-medium text-gray-900">{alert.position_symbol}</span>
                  <span className="text-sm text-gray-600">Qty: {alert.quantity}</span>
                </div>
                <div className="text-lg font-bold text-gray-900">
                  ${(alert.current_value / 1000).toFixed(0)}k
                </div>
              </div>
              <p className="text-sm text-gray-700">{alert.reason}</p>
            </div>
          ))}
        </div>
      </Drawer>
    </>
  );
};