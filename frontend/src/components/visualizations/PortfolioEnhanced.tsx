import React, { useState, useEffect } from 'react';
import { ChevronDown, ChevronRight, Settings, X } from 'lucide-react';
import { Skeleton } from '../common/Skeleton';
import { AlertIcon } from '../alerts';
import { useAlerts } from '@/hooks/useAlerts';

interface PortfolioEnhancedProps {
  groupId: number;
  onRefresh?: () => void;
}

interface RiskScenario {
  scenario_index: number;
  price_shock_percent: number;
  gains_losses: number;
  price_movement: number;
}

interface VolatilityScenario {
  scenario_index: number;
  gains_losses: number;
  shock_percentage: number;
}

interface VolatilityShock {
  scenarios: VolatilityScenario[];
  implied_volatility: number;
  vega: number;
}

interface Position {
  symbol: string;
  underlying_symbol: string;
  quantity: number;
  product_type: string;
  price: number;
  nav: number;
  morning_nav: number;
  requirement: number;
  day_pnl: number;
  is_option: boolean;
  strike?: number;
  expiry?: string;
  call_put?: string;
  risk_scenarios: RiskScenario[];
  volatility_shocks?: {
    up: VolatilityShock | null;
    down: VolatilityShock | null;
  };
}
interface Account {
  account_id: string;
  account_number: string;
  net_liquidity: number;
  cash: number;
  nav: number;
  credit_limit: number;
  credit_utilization: number;
  credit_utilization_percent: number;
  requirement: number;
  excess_liquidity: number;
  day_pnl: number;
  positions: Position[];
  positions_count: number;
}

// Column definitions - Updated to include all 15 scenarios
type ColumnKey = 'account' | 'net_liquidity' | 'cash' | 'nav' | 'credit_limit' | 'credit_percent' | 
                 'requirement' | 'excess' | 'day_pnl' | 
                 's1' | 's2' | 's3' | 's4' | 's5' | 's6' | 's7' | 's8' | 's9' | 's10' | 
                 's11' | 's12' | 's13' | 's14' | 's15';

interface Column {
  key: ColumnKey;
  label: string;
  visible: boolean;
  align?: 'left' | 'right' | 'center';
  format?: (value: any, account?: Account) => string;
  width?: string;
  isRiskMatrix?: boolean;
  description?: string;
}
// Risk scenario descriptions - WITHOUT the S1, S2, etc. labels
const riskScenarioDescriptions = [
  { label: '-15%', description: 'Px -15%, IV +50%/-20%', hasIV: true },
  { label: '-12%', description: 'Px -12%', hasIV: false },
  { label: '-10%', description: 'Px -10%, IV +40%/-15%', hasIV: true },
  { label: '-9%', description: 'Px -9%', hasIV: false },
  { label: '-6%', description: 'Px -6%', hasIV: false },
  { label: '-5%', description: 'Px -5%, IV +30%/-10%', hasIV: true },
  { label: '-3%', description: 'Px -3%', hasIV: false },
  { label: '0%', description: 'Px 0%, IV +10%/-10%', hasIV: true },
  { label: '+3%', description: 'Px +3%', hasIV: false },
  { label: '+5%', description: 'Px +5%, IV +10%/-20%', hasIV: true },
  { label: '+6%', description: 'Px +6%', hasIV: false },
  { label: '+9%', description: 'Px +9%', hasIV: false },
  { label: '+10%', description: 'Px +10%, IV +15%/-25%', hasIV: true },
  { label: '+12%', description: 'Px +12%', hasIV: false },
  { label: '+15%', description: 'Px +15%, IV +20%/-30%', hasIV: true }
];

export const PortfolioEnhanced: React.FC<PortfolioEnhancedProps> = ({
  groupId,
  onRefresh
}) => {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState<{ accounts: Account[] } | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [expandedAccounts, setExpandedAccounts] = useState<Set<string>>(new Set());
  const [showColumnSelector, setShowColumnSelector] = useState(false);
  const { getAlertsForAccount } = useAlerts();  
  // Initialize columns with visibility state - RISK SCENARIOS DEFAULT TO TRUE
  const [columns, setColumns] = useState<Column[]>([
    { key: 'account', label: 'Account', visible: true, align: 'left' },
    { key: 'net_liquidity', label: 'Net Liquidity', visible: true, align: 'right' },
    { key: 'cash', label: 'Cash', visible: true, align: 'right' },
    { key: 'nav', label: 'NAV', visible: true, align: 'right' },
    { key: 'credit_limit', label: 'Credit Limit', visible: true, align: 'right' },
    { key: 'credit_percent', label: 'Credit %', visible: true, align: 'right' },
    { key: 'requirement', label: 'Requirement', visible: true, align: 'right' },
    { key: 'excess', label: 'Excess', visible: true, align: 'right' },
    { key: 'day_pnl', label: 'Day P&L', visible: true, align: 'right' },
    // Risk matrix columns - 15 scenarios - DEFAULT TO VISIBLE (true)
    ...riskScenarioDescriptions.map((scenario, index) => ({
      key: `s${index + 1}` as ColumnKey,
      label: scenario.hasIV ? `${scenario.label} IV` : scenario.label,
      visible: true, // DEFAULT TO VISIBLE
      align: 'right' as const,
      isRiskMatrix: true,
      description: scenario.description
    }))
  ]);

  useEffect(() => {
    console.log('PortfolioEnhanced mounted - Version 3.0 with all UI fixes');
    fetchData();
  }, [groupId]);
  const fetchData = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await fetch(`/api/data/portfolio/${groupId}/risk-matrix?risk_profile_id=10011`);
      if (!response.ok) {
        throw new Error(`Failed to fetch: ${response.status} ${response.statusText}`);
      }
      const data = await response.json();
      setData(data);
    } catch (error: any) {
      console.error('Failed to fetch portfolio data:', error);
      setError(error.message || 'Failed to load portfolio data');
    } finally {
      setLoading(false);
    }
  };

  const toggleAccount = (accountId: string) => {
    const newExpanded = new Set(expandedAccounts);
    if (newExpanded.has(accountId)) {
      newExpanded.delete(accountId);
    } else {
      // Only one account expanded at a time
      newExpanded.clear();
      newExpanded.add(accountId);
    }
    setExpandedAccounts(newExpanded);
  };
  const toggleColumn = (key: ColumnKey) => {
    setColumns(columns.map(col => 
      col.key === key ? { ...col, visible: !col.visible } : col
    ));
  };

  const toggleRiskMatrixColumns = () => {
    const anyRiskVisible = columns.some(col => col.isRiskMatrix && col.visible);
    setColumns(columns.map(col => 
      col.isRiskMatrix ? { ...col, visible: !anyRiskVisible } : col
    ));
  };

  const formatCurrency = (value: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(value);
  };

  const formatPercent = (value: number) => {
    return `${value.toFixed(1)}%`;
  };

  const formatRiskValue = (value: number) => {
    return formatCurrency(value);
  };
  const getRiskMatrixValue = (account: Account, scenarioIndex: number): number => {
    // Aggregate risk scenarios from all positions
    return account.positions.reduce((sum, position) => {
      const scenario = position.risk_scenarios.find(s => s.scenario_index === scenarioIndex);
      // For scenario 8 (0% shock), if gains_losses is 0, use NAV instead
      if (scenarioIndex === 7 && scenario?.gains_losses === 0) {
        return sum + position.nav;
      }
      return sum + (scenario?.gains_losses || 0);
    }, 0);
  };

  const getPositionRiskValue = (position: Position, scenarioIndex: number): number => {
    const scenario = position.risk_scenarios.find(s => s.scenario_index === scenarioIndex);
    // For scenario 8 (0% shock), if gains_losses is 0, use NAV instead
    if (scenarioIndex === 7 && scenario?.gains_losses === 0) {
      return position.nav;
    }
    return scenario?.gains_losses || 0;
  };

  const getRiskMatrixColor = (value: number): string => {
    if (value > 0) return 'text-green-600';
    if (value < 0) return 'text-red-600';
    return 'text-gray-900';
  };

  const visibleColumns = columns.filter(col => col.visible);
  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow p-6">
        <Skeleton className="h-8 w-48 mb-4" />
        <Skeleton className="h-64 w-full" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-white rounded-lg shadow p-6">
        <div className="text-red-600">
          <h3 className="font-semibold">Error Loading Portfolio Data</h3>
          <p className="text-sm mt-1">{error}</p>
          {onRefresh && (
            <button
              onClick={onRefresh}
              className="mt-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
            >
              Retry
            </button>
          )}
        </div>
      </div>
    );
  }

  if (!data || !data.accounts) {
    return <div>No data available</div>;
  }
  // Calculate totals
  const totals = data.accounts.reduce((acc, account) => ({
    net_liquidity: acc.net_liquidity + account.net_liquidity,
    cash: acc.cash + account.cash,
    nav: acc.nav + account.nav,
    credit_limit: acc.credit_limit + account.credit_limit,
    requirement: acc.requirement + account.requirement,
    excess_liquidity: acc.excess_liquidity + account.excess_liquidity,
    day_pnl: acc.day_pnl + account.day_pnl,
    positions_count: acc.positions_count + account.positions_count,
  }), {
    net_liquidity: 0,
    cash: 0,
    nav: 0,
    credit_limit: 0,
    requirement: 0,
    excess_liquidity: 0,
    day_pnl: 0,
    positions_count: 0,
  });

  const totalCreditUtilizationPercent = totals.credit_limit > 0 
    ? (totals.requirement / totals.credit_limit) * 100 
    : 0;
  return (
    <div className="bg-white rounded-lg shadow relative">
      {/* Header */}
      <div className="p-4 border-b flex justify-between items-center">
        <h2 className="text-xl font-semibold">Portfolio Risk View (v3.0)</h2>
        <div className="flex items-center gap-4">
          <span className="text-sm text-gray-600">
            {data.accounts.length} Accounts | {totals.positions_count} Positions
          </span>
          <button
            onClick={() => setShowColumnSelector(!showColumnSelector)}
            className="p-2 hover:bg-gray-100 rounded"
            title="Column Settings"
          >
            <Settings className="w-4 h-4" />
          </button>
          {onRefresh && (
            <button
              onClick={onRefresh}
              className="px-3 py-1 text-sm bg-blue-600 text-white rounded hover:bg-blue-700"
            >
              Refresh
            </button>
          )}
        </div>
      </div>
      {/* Column Selector Dropdown */}
      {showColumnSelector && (
        <div className="absolute right-4 top-16 z-10 bg-white rounded-lg shadow-lg border p-4 w-64">
          <div className="flex justify-between items-center mb-3">
            <h3 className="font-semibold text-sm">Show/Hide Columns</h3>
            <button
              onClick={() => setShowColumnSelector(false)}
              className="p-1 hover:bg-gray-100 rounded"
            >
              <X className="w-4 h-4" />
            </button>
          </div>
          <div className="space-y-2 max-h-96 overflow-y-auto">
            <div className="border-b pb-2 mb-2">
              <button
                onClick={toggleRiskMatrixColumns}
                className="text-sm text-blue-600 hover:text-blue-700"
              >
                Toggle All Risk Scenarios
              </button>
            </div>
            {columns.map(col => (
              <label key={col.key} className="flex items-center space-x-2 cursor-pointer">
                <input
                  type="checkbox"
                  checked={col.visible}
                  onChange={() => toggleColumn(col.key)}
                  className="rounded"
                />
                <span className="text-sm">{col.label}</span>
                {col.isRiskMatrix && <span className="text-xs text-gray-500">(Risk)</span>}
              </label>
            ))}
          </div>
        </div>
      )}
      {/* Table */}
      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              {visibleColumns.map(col => (
                <th
                  key={col.key}
                  className={`px-4 py-3 ${col.align === 'right' ? 'text-right' : 'text-left'} text-xs font-medium text-gray-500 uppercase tracking-wider ${
                    col.isRiskMatrix ? 'bg-blue-50' : ''
                  }`}
                  title={col.description}
                >
                  {col.label}
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {data.accounts.map(account => {
              const isExpanded = expandedAccounts.has(account.account_id);
              
              return (
                <React.Fragment key={account.account_id}>
                  {/* Account Row */}
                  <tr
                    className={`hover:bg-gray-50 ${account.positions_count > 0 ? 'cursor-pointer' : ''}`}
                    onClick={() => account.positions_count > 0 && toggleAccount(account.account_id)}
                  >                    {visibleColumns.map(col => {
                      let content: React.ReactNode;
                      const className = 'px-4 py-3 whitespace-nowrap text-sm';
                      
                      if (col.key === 'account') {
                        const accountAlerts = getAlertsForAccount(account.account_number);
                        const hasCriticalAlert = accountAlerts.some(a => a.severity === 'critical');
                        const hasWarningAlert = accountAlerts.some(a => a.severity === 'warning');
                        
                        content = (
                          <div className="flex items-center">
                            {account.positions_count > 0 && (
                              isExpanded ? (
                                <ChevronDown className="w-4 h-4 mr-2 text-gray-400" />
                              ) : (
                                <ChevronRight className="w-4 h-4 mr-2 text-gray-400" />
                              )
                            )}
                            <span className="font-medium text-gray-900">{account.account_number}</span>
                            {account.positions_count > 0 && (
                              <span className="ml-2 text-xs text-gray-500">({account.positions_count})</span>
                            )}
                            {(hasCriticalAlert || hasWarningAlert) && (
                              <div className="ml-2 flex items-center">
                                <AlertIcon 
                                  severity={hasCriticalAlert ? 'critical' : 'warning'} 
                                  size="sm"
                                  className="animate-pulse"
                                />
                              </div>
                            )}
                          </div>
                        );
                        return <td key={col.key} className={className}>{content}</td>;
                      } else if (col.key === 'net_liquidity') {
                        content = formatCurrency(account.net_liquidity);
                      } else if (col.key === 'cash') {
                        content = formatCurrency(account.cash);
                      } else if (col.key === 'nav') {
                        content = formatCurrency(account.nav);
                      } else if (col.key === 'credit_limit') {
                        content = formatCurrency(account.credit_limit);
                      } else if (col.key === 'credit_percent') {                        const creditClass = account.credit_utilization_percent > 80 ? 'text-red-600' :
                                          account.credit_utilization_percent > 60 ? 'text-yellow-600' :
                                          'text-green-600';
                        content = <span className={`font-medium ${creditClass}`}>{formatPercent(account.credit_utilization_percent)}</span>;
                      } else if (col.key === 'requirement') {
                        content = formatCurrency(account.requirement);
                      } else if (col.key === 'excess') {
                        content = formatCurrency(account.excess_liquidity);
                      } else if (col.key === 'day_pnl') {
                        const pnlClass = account.day_pnl >= 0 ? 'text-green-600' : 'text-red-600';
                        content = <span className={pnlClass}>{formatCurrency(account.day_pnl)}</span>;
                      } else if (col.key.startsWith('s')) {
                        // Risk matrix columns
                        const scenarioIndex = parseInt(col.key.substring(1)) - 1;
                        const riskValue = getRiskMatrixValue(account, scenarioIndex);
                        const riskClass = getRiskMatrixColor(riskValue);
                        const scenarioDesc = riskScenarioDescriptions[scenarioIndex];
                        return (
                          <td 
                            key={col.key} 
                            className={`${className} text-right bg-blue-50`}
                            title={scenarioDesc.description}
                          >
                            <span className={riskClass}>{formatRiskValue(riskValue)}</span>
                          </td>
                        );
                      } else {
                        content = '';
                      }
                      
                      return <td key={col.key} className={`${className} ${col.align === 'right' ? 'text-right' : 'text-left'}`}>{content}</td>;
                    })}
                  </tr>

                  {/* Expanded Position Details - REMOVED "Positions for" header */}
                  {isExpanded && account.positions.length > 0 && (
                    <tr>
                      <td colSpan={visibleColumns.length} className="p-0 bg-gray-50">
                        <div className="p-4">
                          <div className="bg-white rounded-lg overflow-hidden">
                            <table className="min-w-full divide-y divide-gray-200">
                              <thead className="bg-gray-50">
                                <tr>
                                  <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase">Symbol</th>
                                  <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase">Type</th>
                                  <th className="px-4 py-2 text-right text-xs font-medium text-gray-500 uppercase">Qty</th>
                                  <th className="px-4 py-2 text-right text-xs font-medium text-gray-500 uppercase">Price</th>
                                  <th className="px-4 py-2 text-right text-xs font-medium text-gray-500 uppercase">NAV</th>
                                  <th className="px-4 py-2 text-right text-xs font-medium text-gray-500 uppercase">Req</th>
                                  <th className="px-4 py-2 text-right text-xs font-medium text-gray-500 uppercase">Day P&L</th>
                                  {/* Risk scenario columns if visible */}
                                  {visibleColumns.filter(col => col.isRiskMatrix).map(col => (
                                    <th 
                                      key={col.key} 
                                      className="px-4 py-2 text-right text-xs font-medium text-gray-500 uppercase bg-blue-50"
                                      title={col.description}
                                    >
                                      {col.label}
                                    </th>
                                  ))}
                                </tr>
                              </thead>
                              <tbody className="divide-y divide-gray-200">
                                {account.positions.map((position, idx) => {
                                  const showVolatilityShocks = position.is_option && 
                                    position.volatility_shocks?.up && 
                                    position.volatility_shocks?.down &&
                                    visibleColumns.some(col => col.isRiskMatrix);
                                  
                                  return (
                                    <React.Fragment key={idx}>
                                      {/* Main position row */}
                                      <tr className="hover:bg-gray-50">
                                        <td className="px-4 py-2 text-sm">
                                          <div>
                                            <span className="font-medium">{position.symbol}</span>
                                            {position.is_option && (
                                              <div className="text-xs text-gray-500">
                                                {position.call_put === 'C' ? 'Call' : 'Put'} ${position.strike} {position.expiry}
                                              </div>
                                            )}
                                          </div>
                                        </td>
                                        <td className="px-4 py-2 text-sm text-gray-600">
                                          {position.product_type}
                                        </td>
                                        <td className="px-4 py-2 text-sm text-right">
                                          {position.quantity.toLocaleString()}
                                        </td>
                                        <td className="px-4 py-2 text-sm text-right">
                                          ${position.price.toFixed(2)}
                                        </td>
                                        <td className="px-4 py-2 text-sm text-right">
                                          {formatCurrency(position.nav)}
                                        </td>
                                        <td className="px-4 py-2 text-sm text-right">
                                          {formatCurrency(position.requirement)}
                                        </td>
                                        <td className="px-4 py-2 text-sm text-right">
                                          <span className={position.day_pnl >= 0 ? 'text-green-600' : 'text-red-600'}>
                                            {formatCurrency(position.day_pnl)}
                                          </span>
                                        </td>
                                        {/* Risk scenarios for main row with TOOLTIPS */}
                                        {visibleColumns.filter(col => col.isRiskMatrix).map(col => {
                                          const scenarioIndex = parseInt(col.key.substring(1)) - 1;
                                          const value = getPositionRiskValue(position, scenarioIndex);
                                          const colorClass = getRiskMatrixColor(value);
                                          const scenarioDesc = riskScenarioDescriptions[scenarioIndex];
                                          return (
                                            <td 
                                              key={col.key} 
                                              className="px-4 py-2 text-sm text-right bg-blue-50"
                                              title={scenarioDesc.description}
                                            >
                                              <span className={colorClass}>
                                                {formatRiskValue(value)}
                                              </span>
                                            </td>
                                          );
                                        })}
                                      </tr>
                                      
                                      {/* Volatility Up Shock Row (for options) - NO IV INFO IN TYPE COLUMN */}
                                      {showVolatilityShocks && (
                                        <tr className="bg-green-50 hover:bg-green-100">
                                          <td className="px-4 py-2 text-xs text-green-700">
                                            <span className="italic">↑ Vol Up</span>
                                          </td>
                                          <td colSpan={6} className="px-4 py-2 text-xs text-green-700">
                                            {/* Empty cells for non-risk columns */}
                                          </td>
                                          {/* Volatility up scenarios WITH TOOLTIPS */}
                                          {visibleColumns.filter(col => col.isRiskMatrix).map(col => {
                                            const scenarioIndex = parseInt(col.key.substring(1)) - 1;
                                            const scenario = position.volatility_shocks.up.scenarios.find(
                                              s => s.scenario_index === scenarioIndex
                                            );
                                            const value = scenario?.gains_losses || 0;
                                            const scenarioDesc = riskScenarioDescriptions[scenarioIndex];
                                            return (
                                              <td 
                                                key={col.key} 
                                                className="px-4 py-2 text-xs text-right bg-green-50"
                                                title={`${scenarioDesc.description} (Volatility Up)`}
                                              >
                                                <span className="text-green-700">
                                                  {formatRiskValue(value)}
                                                </span>
                                              </td>
                                            );
                                          })}
                                        </tr>
                                      )}
                                      
                                      {/* Volatility Down Shock Row (for options) - NO IV INFO IN TYPE COLUMN */}
                                      {showVolatilityShocks && (
                                        <tr className="bg-red-50 hover:bg-red-100">
                                          <td className="px-4 py-2 text-xs text-red-700">
                                            <span className="italic">↓ Vol Down</span>
                                          </td>
                                          <td colSpan={6} className="px-4 py-2 text-xs text-red-700">
                                            {/* Empty cells for non-risk columns */}
                                          </td>
                                          {/* Volatility down scenarios WITH TOOLTIPS */}
                                          {visibleColumns.filter(col => col.isRiskMatrix).map(col => {
                                            const scenarioIndex = parseInt(col.key.substring(1)) - 1;
                                            const scenario = position.volatility_shocks.down.scenarios.find(
                                              s => s.scenario_index === scenarioIndex
                                            );
                                            const value = scenario?.gains_losses || 0;
                                            const scenarioDesc = riskScenarioDescriptions[scenarioIndex];
                                            return (
                                              <td 
                                                key={col.key} 
                                                className="px-4 py-2 text-xs text-right bg-red-50"
                                                title={`${scenarioDesc.description} (Volatility Down)`}
                                              >
                                                <span className="text-red-700">
                                                  {formatRiskValue(value)}
                                                </span>
                                              </td>
                                            );
                                          })}
                                        </tr>
                                      )}
                                    </React.Fragment>
                                  );
                                })}
                              </tbody>
                            </table>
                          </div>
                        </div>
                      </td>
                    </tr>
                  )}
                </React.Fragment>
              );
            })}
            {/* Totals Row */}
            <tr className="bg-gray-100 font-semibold">
              {visibleColumns.map(col => {
                let content: React.ReactNode;
                const className = 'px-4 py-3 whitespace-nowrap text-sm';
                
                if (col.key === 'account') {
                  content = <span className="text-gray-900">Total ({data.accounts.length} accounts)</span>;
                } else if (col.key === 'net_liquidity') {
                  content = formatCurrency(totals.net_liquidity);
                } else if (col.key === 'cash') {
                  content = formatCurrency(totals.cash);
                } else if (col.key === 'nav') {
                  content = formatCurrency(totals.nav);
                } else if (col.key === 'credit_limit') {
                  content = formatCurrency(totals.credit_limit);
                } else if (col.key === 'credit_percent') {
                  const creditClass = totalCreditUtilizationPercent > 80 ? 'text-red-600' :
                                    totalCreditUtilizationPercent > 60 ? 'text-yellow-600' :
                                    'text-green-600';
                  content = <span className={`font-medium ${creditClass}`}>{formatPercent(totalCreditUtilizationPercent)}</span>;
                } else if (col.key === 'requirement') {
                  content = formatCurrency(totals.requirement);
                } else if (col.key === 'excess') {
                  content = formatCurrency(totals.excess_liquidity);
                } else if (col.key === 'day_pnl') {
                  const pnlClass = totals.day_pnl >= 0 ? 'text-green-600' : 'text-red-600';
                  content = <span className={pnlClass}>{formatCurrency(totals.day_pnl)}</span>;
                } else if (col.key.startsWith('s')) {
                  // Risk matrix columns - aggregate all accounts WITH TOOLTIPS
                  const scenarioIndex = parseInt(col.key.substring(1)) - 1;
                  const totalRiskValue = data.accounts.reduce((sum, acc) => 
                    sum + getRiskMatrixValue(acc, scenarioIndex), 0
                  );
                  const riskClass = getRiskMatrixColor(totalRiskValue);
                  const scenarioDesc = riskScenarioDescriptions[scenarioIndex];
                  return (
                    <td 
                      key={col.key} 
                      className={`${className} text-right bg-blue-50`}
                      title={scenarioDesc.description}
                    >
                      <span className={riskClass}>{formatRiskValue(totalRiskValue)}</span>
                    </td>
                  );
                } else {
                  content = '';
                }
                
                return <td key={col.key} className={`${className} ${col.align === 'right' ? 'text-right' : 'text-left'}`}>{content}</td>;
              })}
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};