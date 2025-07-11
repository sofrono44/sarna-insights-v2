import React from 'react';
import { useQuery } from '@tanstack/react-query';
import { Skeleton } from '@/components/common/Skeleton';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ChartOptions,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

export const CreditUtilizationChart: React.FC = () => {
  const { data: portfolio, isLoading } = useQuery({
    queryKey: ['portfolio-risk-matrix'],
    queryFn: async () => {
      const response = await fetch('/api/data/portfolio/10006/risk-matrix');
      if (!response.ok) throw new Error('Failed to fetch portfolio data');
      return response.json();
    },
  });

  const chartData = React.useMemo(() => {
    if (!portfolio?.accounts) {
      return null;
    }

    const sortedAccounts = [...portfolio.accounts].sort(
      (a, b) => (b.credit_utilization_percent || 0) - (a.credit_utilization_percent || 0)
    );

    return {
      labels: sortedAccounts.map(acc => acc.account_number),
      datasets: [
        {
          label: 'Credit Utilization %',
          data: sortedAccounts.map(acc => acc.credit_utilization_percent || 0),
          backgroundColor: sortedAccounts.map(acc => {
            const util = acc.credit_utilization_percent || 0;
            if (util >= 80) return 'rgba(239, 68, 68, 0.8)'; // red
            if (util >= 60) return 'rgba(251, 191, 36, 0.8)'; // yellow
            return 'rgba(34, 197, 94, 0.8)'; // green
          }),
          borderColor: sortedAccounts.map(acc => {
            const util = acc.credit_utilization_percent || 0;
            if (util >= 80) return 'rgb(239, 68, 68)';
            if (util >= 60) return 'rgb(251, 191, 36)';
            return 'rgb(34, 197, 94)';
          }),
          borderWidth: 1,
        },
      ],
    };
  }, [portfolio]);

  const options: ChartOptions<'bar'> = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: false,
      },
      title: {
        display: true,
        text: 'Credit Utilization by Account',
        font: {
          size: 16,
          weight: '600',
        },
      },
      tooltip: {
        callbacks: {
          label: (context) => {
            const account = portfolio?.accounts[context.dataIndex];
            const value = context.parsed.y;
            return [
              `Credit Utilization: ${value.toFixed(1)}%`,
              `Credit Used: $${(account?.credit_utilization || 0).toLocaleString()}`,
              `Credit Limit: $${(account?.credit_limit || 0).toLocaleString()}`,
            ];
          },
        },
      },
    },
    scales: {
      x: {
        grid: {
          display: false,
        },
      },
      y: {
        beginAtZero: true,
        max: 100,
        ticks: {
          callback: (value) => `${value}%`,
        },
        grid: {
          color: 'rgba(0, 0, 0, 0.05)',
        },
      },
    },
  };

  if (isLoading) {
    return (
      <div className="bg-white rounded-lg shadow p-6">
        <Skeleton className="h-8 w-48 mb-4" />
        <Skeleton className="h-64 w-full" />
      </div>
    );
  }

  if (!chartData) {
    return (
      <div className="bg-white rounded-lg shadow p-6">
        <p className="text-gray-500">No data available</p>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <div className="h-64">
        <Bar data={chartData} options={options} />
      </div>
      <div className="mt-4 flex items-center justify-center space-x-6 text-sm">
        <div className="flex items-center">
          <div className="w-3 h-3 bg-green-500 rounded mr-2" />
          <span className="text-gray-600">Low Risk (&lt;60%)</span>
        </div>
        <div className="flex items-center">
          <div className="w-3 h-3 bg-yellow-500 rounded mr-2" />
          <span className="text-gray-600">Medium Risk (60-80%)</span>
        </div>
        <div className="flex items-center">
          <div className="w-3 h-3 bg-red-500 rounded mr-2" />
          <span className="text-gray-600">High Risk (&gt;80%)</span>
        </div>
      </div>
    </div>
  );
};