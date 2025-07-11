import React, { useEffect, useRef } from 'react';
import { Chart as ChartJS, registerables } from 'chart.js';

ChartJS.register(...registerables);

interface ChartVisualizationProps {
  data: any;
  config?: any;
}

const ChartVisualization: React.FC<ChartVisualizationProps> = ({ data, config }) => {
  const chartRef = useRef<HTMLCanvasElement>(null);
  const chartInstance = useRef<ChartJS | null>(null);

  useEffect(() => {
    if (!chartRef.current) return;

    // Destroy previous chart instance
    if (chartInstance.current) {
      chartInstance.current.destroy();
    }

    // Create new chart
    const ctx = chartRef.current.getContext('2d');
    if (!ctx) return;

    const defaultConfig = {
      type: 'bar',
      data: data,
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'top' as const,
          },
          title: {
            display: false,
          },
        },
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              callback: function(value: any) {
                if (typeof value === 'number') {
                  return value.toLocaleString('en-US', {
                    style: 'currency',
                    currency: 'USD',
                    minimumFractionDigits: 0,
                    maximumFractionDigits: 0,
                  });
                }
                return value;
              },
            },
          },
        },
      },
    };

    chartInstance.current = new ChartJS(ctx, config || defaultConfig);

    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
    };
  }, [data, config]);

  return (
    <div className="w-full h-full min-h-[400px]">
      <canvas ref={chartRef} />
    </div>
  );
};

export default ChartVisualization;
