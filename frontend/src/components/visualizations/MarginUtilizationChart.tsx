import React, { useEffect, useState } from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ChartOptions,
  ChartData as ChartJSData
} from 'chart.js';
import { Bar } from 'react-chartjs-2';
import { TrendingUp, AlertCircle } from 'lucide-react';
import { useToast } from '@/contexts/ToastContext';
import { Skeleton } from '@/components/common/Skeleton';

// Register ChartJS components
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

interface ChartData {
  title: string;
  type: string;
  data: {
    labels: string[];
    datasets: {
      label: string;
      data: number[];
      backgroundColor: string;
    }[];
  };
  options: any;
}

export const MarginUtilizationChart: React.FC = () => {
  const [chartData, setChartData] = useState<ChartData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const { addToast } = useToast();

  const fetchChartData = async () => {
    try {
      setLoading(true);
      setError(null);
      
      // Fetch portfolio overview data
      const response = await fetch('/api/viz/portfolio-overview/10006');
      if (!response.ok) {
        throw new Error('Failed to fetch chart data');
      }
      
      const data: ChartData = await response.json();
      
      // Transform the data to show margin utilization percentages
      const marginData = data.data.datasets[0].data;
      const buyingPowerData = data.data.datasets[1].data;
      
      // Calculate utilization percentages
      const utilizationData = marginData.map((margin, index) => {
        const totalAvailable = margin + buyingPowerData[index];
        return totalAvailable > 0 ? (margin / totalAvailable) * 100 : 0;
      });
      
      // Create new chart data for margin utilization
      const utilizationChartData: ChartData = {
        title: 'Margin Utilization by Account',
        type: 'bar',
        data: {
          labels: data.data.labels,
          datasets: [{
            label: 'Margin Utilization %',
            data: utilizationData,
            backgroundColor: utilizationData.map(value => 
              value > 50 ? 'rgba(239, 68, 68, 0.5)' : 
              value > 30 ? 'rgba(251, 191, 36, 0.5)' : 
              'rgba(34, 197, 94, 0.5)'
            ) as any
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            title: {
              display: true,
              text: 'Margin Utilization by Account'
            },
            tooltip: {
              callbacks: {
                label: (context: any) => {
                  return `${context.parsed.y.toFixed(2)}%`;
                }
              }
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              max: 100,
              ticks: {
                callback: function(value: any) {
                  return value + '%';
                }
              }
            }
          }
        }
      };
      
      setChartData(utilizationChartData);
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Failed to load chart data';
      setError(errorMessage);
      addToast({
        type: 'error',
        title: 'Chart Loading Failed',
        message: errorMessage,
      });
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchChartData();
    
    // Auto-refresh every 30 seconds
    const interval = setInterval(fetchChartData, 30000);
    return () => clearInterval(interval);
  }, []);

  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow p-6">
        <div className="flex justify-between items-center mb-4">
          <Skeleton height={24} width="40%" />
          <Skeleton height={20} width="20%" />
        </div>
        <div className="h-64 relative">
          <Skeleton height="100%" className="absolute inset-0" />
        </div>
        <div className="mt-4 flex justify-around">
          {[...Array(3)].map((_, i) => (
            <div key={i} className="flex items-center gap-2">
              <Skeleton width={12} height={12} />
              <Skeleton width={80} height={16} />
            </div>
          ))}
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-white rounded-lg shadow p-6">
        <div className="flex items-center text-red-600 mb-4">
          <AlertCircle className="w-5 h-5 mr-2" />
          <span>Failed to load chart: {error}</span>
        </div>
      </div>
    );
  }

  if (!chartData) {
    return null;
  }

  // Calculate average utilization
  const avgUtilization = chartData.data.datasets[0].data.reduce((a, b) => a + b, 0) / chartData.data.datasets[0].data.length;

  return (
    <div className="bg-gray-50 border border-gray-200 rounded-lg p-6 hover:shadow-md transition-shadow">
      <div className="flex justify-between items-center mb-4">
        <div>
          <h3 className="text-lg font-semibold text-gray-900">{chartData.title}</h3>
          <p className="text-sm text-gray-600 mt-1">By account with risk indicators</p>
        </div>
        <div className="flex items-center gap-4">
          <span className="px-3 py-1 text-xs font-medium rounded bg-green-50 text-green-700">
            AI Generated
          </span>
          <div className="flex items-center text-sm text-gray-600">
            <TrendingUp className="w-4 h-4 mr-1" />
            <span>Avg: {avgUtilization.toFixed(1)}%</span>
          </div>
        </div>
      </div>
      
      <div className="h-64">
        <Bar 
          data={chartData.data as ChartJSData<'bar'>} 
          options={chartData.options as ChartOptions<'bar'>} 
        />
      </div>
      
      <div className="mt-4 flex justify-around text-xs">
        <div className="flex items-center">
          <div className="w-3 h-3 bg-green-500 opacity-50 rounded mr-1"></div>
          <span>Low (&lt;30%)</span>
        </div>
        <div className="flex items-center">
          <div className="w-3 h-3 bg-yellow-500 opacity-50 rounded mr-1"></div>
          <span>Medium (30-50%)</span>
        </div>
        <div className="flex items-center">
          <div className="w-3 h-3 bg-red-500 opacity-50 rounded mr-1"></div>
          <span>High (&gt;50%)</span>
        </div>
      </div>
    </div>
  );
};