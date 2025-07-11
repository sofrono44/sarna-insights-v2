import React from 'react';

interface RiskMatrixVisualizationProps {
  data: {
    scenarios: string[];
    accounts: Array<{
      id: string;
      name: string;
      values: number[];
    }>;
  };
}

const RiskMatrixVisualization: React.FC<RiskMatrixVisualizationProps> = ({ data }) => {
  const getColorForValue = (value: number) => {
    if (value > 0) return 'text-green-600 bg-green-50';
    if (value < -10000) return 'text-red-600 bg-red-50';
    if (value < -5000) return 'text-orange-600 bg-orange-50';
    return 'text-gray-600 bg-gray-50';
  };

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full">
        <thead>
          <tr className="border-b border-gray-200">
            <th className="sticky left-0 bg-white px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              Account
            </th>
            {data.scenarios.map((scenario, index) => (
              <th key={index} className="px-4 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">
                {scenario}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-200">
          {data.accounts.map((account) => (
            <tr key={account.id} className="hover:bg-gray-50">
              <td className="sticky left-0 bg-white px-4 py-3 whitespace-nowrap text-sm font-medium text-gray-900">
                {account.name}
              </td>
              {account.values.map((value, index) => (
                <td key={index} className="px-4 py-3 text-center">
                  <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${getColorForValue(value)}`}>
                    {value.toLocaleString('en-US', {
                      style: 'currency',
                      currency: 'USD',
                      minimumFractionDigits: 0,
                      maximumFractionDigits: 0,
                    })}
                  </span>
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default RiskMatrixVisualization;
