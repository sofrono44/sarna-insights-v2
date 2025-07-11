import React from 'react';
import { useQuery } from '@tanstack/react-query';
import { useToast } from '@/contexts/ToastContext';
import { TableRowSkeleton } from '@/components/common/Skeleton';

interface AccountData {
  account_id: string;
  margin: number;
  buying_power: number;
  excess_liquidity: number;
  margin_utilization: number;
  unrealized_pl: number;
  realized_pl: number;
  positions_count: number;
}

interface PortfolioData {
  group_id: number;
  accounts: AccountData[];
  timestamp: string;
  total_margin: number;
  total_buying_power: number | null;
  total_pl: number | null;
}

const PortfolioOverview: React.FC = () => {
  console.log('PortfolioOverview component loaded - UPDATED VERSION WITHOUT STATS CARDS');
  const { addToast } = useToast();
  
  const { data: portfolio, isLoading, error } = useQuery<PortfolioData>({
    queryKey: ['portfolio-current'],
    queryFn: async () => {
      const response = await fetch('/api/data/portfolio/10006');
      if (!response.ok) throw new Error('Failed to fetch portfolio data');
      return response.json();
    },
    refetchInterval: 30000, // Refresh every 30 seconds
  });

  // Show error toast when fetch fails
  React.useEffect(() => {
    if (error) {
      addToast({
        type: 'error',
        title: 'Failed to load portfolio data',
        message: error.message,
      });
    }
  }, [error, addToast]);

  if (isLoading) {
    return (
      <div className="overflow-hidden shadow ring-1 ring-black ring-opacity-5 md:rounded-lg">
        <table className="min-w-full divide-y divide-gray-300">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Account
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Margin
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Buying Power
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Excess Liquidity
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Utilization
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Unrealized P&L
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Realized P&L
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Positions
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {[...Array(5)].map((_, i) => (
              <TableRowSkeleton key={i} columns={8} />
            ))}
          </tbody>
        </table>
      </div>
    );
  }

  if (error || !portfolio) {
    return (
      <div className="text-center text-red-600 py-8">
        <p>Failed to load portfolio data</p>
        <p className="text-sm mt-2">Please check your connection and try again</p>
      </div>
    );
  }

  const formatCurrency = (value: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(value);
  };

  return (
    <div>
      {/* UPDATED VERSION - NO STATS CARDS */}
      {/* Account List */}
      <div className="overflow-x-auto">
        <table className="min-w-full">
          <thead>
            <tr className="bg-gray-50">
              <th className="text-left px-4 py-3 text-xs font-semibold text-gray-700 uppercase tracking-wider">
                Account
              </th>
              <th className="text-left px-4 py-3 text-xs font-semibold text-gray-700 uppercase tracking-wider">
                Margin
              </th>
              <th className="text-left px-4 py-3 text-xs font-semibold text-gray-700 uppercase tracking-wider">
                Buying Power
              </th>
              <th className="text-left px-4 py-3 text-xs font-semibold text-gray-700 uppercase tracking-wider">
                Excess Liquidity
              </th>
              <th className="text-left px-4 py-3 text-xs font-semibold text-gray-700 uppercase tracking-wider">
                Utilization
              </th>
              <th className="text-left px-4 py-3 text-xs font-semibold text-gray-700 uppercase tracking-wider">
                Unrealized P&L
              </th>
              <th className="text-left px-4 py-3 text-xs font-semibold text-gray-700 uppercase tracking-wider">
                Realized P&L
              </th>
              <th className="text-left px-4 py-3 text-xs font-semibold text-gray-700 uppercase tracking-wider">
                Positions
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {portfolio.accounts.map((account) => (
              <tr key={account.account_id} className="hover:bg-gray-50 transition-colors">
                <td className="px-4 py-3 text-sm font-medium text-gray-900">
                  {account.account_id}
                </td>
                <td className="px-4 py-3 text-sm text-gray-600">
                  {formatCurrency(account.margin)}
                </td>
                <td className="px-4 py-3 text-sm text-gray-600">
                  {formatCurrency(account.buying_power)}
                </td>
                <td className="px-4 py-3 text-sm text-gray-600">
                  {formatCurrency(account.excess_liquidity)}
                </td>
                <td className="px-4 py-3">
                  <span className={`inline-flex items-center text-sm font-medium ${
                    account.margin_utilization > 50 ? 'text-red-600' : 
                    account.margin_utilization > 30 ? 'text-yellow-600' : 'text-green-600'
                  }`}>
                    <span className={`w-2 h-2 rounded-full mr-2 ${
                      account.margin_utilization > 50 ? 'bg-red-600' : 
                      account.margin_utilization > 30 ? 'bg-yellow-600' : 'bg-green-600'
                    }`}></span>
                    {account.margin_utilization.toFixed(1)}%
                  </span>
                </td>
                <td className={`px-4 py-3 text-sm font-medium ${
                  account.unrealized_pl >= 0 ? 'text-green-600' : 'text-red-600'
                }`}>
                  {formatCurrency(account.unrealized_pl)}
                </td>
                <td className={`px-4 py-3 text-sm font-medium ${
                  account.realized_pl >= 0 ? 'text-green-600' : 'text-red-600'
                }`}>
                  {formatCurrency(account.realized_pl)}
                </td>
                <td className="px-4 py-3 text-sm text-gray-600">
                  {account.positions_count}
                </td>
              </tr>
            ))}
          </tbody>
          <tfoot className="bg-gray-50">
            <tr>
              <td className="px-4 py-3 text-sm font-semibold text-gray-900">
                Total
              </td>
              <td className="px-4 py-3 text-sm font-semibold text-gray-900">
                {formatCurrency(portfolio.total_margin)}
              </td>
              <td className="px-4 py-3 text-sm font-semibold text-gray-900">
                {formatCurrency(portfolio.total_buying_power || 0)}
              </td>
              <td className="px-4 py-3 text-sm font-semibold text-gray-900">
                {formatCurrency(portfolio.accounts.reduce((sum, acc) => sum + acc.excess_liquidity, 0))}
              </td>
              <td className="px-4 py-3 text-sm font-semibold text-gray-900">
                {(portfolio.accounts.reduce((sum, acc) => sum + acc.margin_utilization, 0) / portfolio.accounts.length).toFixed(1)}%
              </td>
              <td className={`px-4 py-3 text-sm font-semibold ${
                portfolio.accounts.reduce((sum, acc) => sum + acc.unrealized_pl, 0) >= 0 ? 'text-green-600' : 'text-red-600'
              }`}>
                {formatCurrency(portfolio.accounts.reduce((sum, acc) => sum + acc.unrealized_pl, 0))}
              </td>
              <td className={`px-4 py-3 text-sm font-semibold ${
                portfolio.accounts.reduce((sum, acc) => sum + acc.realized_pl, 0) >= 0 ? 'text-green-600' : 'text-red-600'
              }`}>
                {formatCurrency(portfolio.accounts.reduce((sum, acc) => sum + acc.realized_pl, 0))}
              </td>
              <td className="px-4 py-3 text-sm font-semibold text-gray-900">
                {portfolio.accounts.reduce((sum, acc) => sum + acc.positions_count, 0)}
              </td>
            </tr>
          </tfoot>
        </table>
      </div>

      {/* Last Updated */}
      <p className="text-xs text-gray-500 mt-4 text-center">
        Last updated: {new Date(portfolio.timestamp).toLocaleString()}
      </p>
    </div>
  );
};

export default PortfolioOverview;
