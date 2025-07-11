import React from 'react';
import { ChevronUp, ChevronDown } from 'lucide-react';

interface TableVisualizationProps {
  data: {
    headers: string[];
    rows: any[][];
    sortable?: boolean;
  };
}

const TableVisualization: React.FC<TableVisualizationProps> = ({ data }) => {
  const [sortConfig, setSortConfig] = React.useState<{
    key: number;
    direction: 'asc' | 'desc';
  } | null>(null);

  const sortedRows = React.useMemo(() => {
    if (!sortConfig || !data.sortable) return data.rows;

    return [...data.rows].sort((a, b) => {
      const aValue = a[sortConfig.key];
      const bValue = b[sortConfig.key];

      if (aValue === null || aValue === undefined) return 1;
      if (bValue === null || bValue === undefined) return -1;

      if (aValue < bValue) {
        return sortConfig.direction === 'asc' ? -1 : 1;
      }
      if (aValue > bValue) {
        return sortConfig.direction === 'asc' ? 1 : -1;
      }
      return 0;
    });
  }, [data.rows, sortConfig, data.sortable]);

  const handleSort = (columnIndex: number) => {
    if (!data.sortable) return;

    setSortConfig((current) => {
      if (!current || current.key !== columnIndex) {
        return { key: columnIndex, direction: 'asc' };
      }
      if (current.direction === 'asc') {
        return { key: columnIndex, direction: 'desc' };
      }
      return null;
    });
  };

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            {data.headers.map((header, index) => (
              <th
                key={index}
                onClick={() => handleSort(index)}
                className={`px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider ${
                  data.sortable ? 'cursor-pointer hover:bg-gray-100' : ''
                }`}
              >
                <div className="flex items-center space-x-1">
                  <span>{header}</span>
                  {data.sortable && sortConfig?.key === index && (
                    <span className="text-gray-400">
                      {sortConfig.direction === 'asc' ? (
                        <ChevronUp className="w-4 h-4" />
                      ) : (
                        <ChevronDown className="w-4 h-4" />
                      )}
                    </span>
                  )}
                </div>
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {sortedRows.map((row, rowIndex) => (
            <tr key={rowIndex} className="hover:bg-gray-50">
              {row.map((cell, cellIndex) => (
                <td key={cellIndex} className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  {cell}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TableVisualization;
