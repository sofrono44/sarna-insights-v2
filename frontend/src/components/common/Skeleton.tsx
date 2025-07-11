import React from 'react';

interface SkeletonProps {
  className?: string;
  variant?: 'text' | 'circular' | 'rectangular';
  width?: string | number;
  height?: string | number;
  animation?: 'pulse' | 'wave';
}

export const Skeleton: React.FC<SkeletonProps> = ({
  className = '',
  variant = 'rectangular',
  width = '100%',
  height = 20,
  animation = 'pulse',
}) => {
  const baseClasses = 'bg-gray-200 rounded';
  
  const variantClasses = {
    text: 'rounded',
    circular: 'rounded-full',
    rectangular: 'rounded',
  };

  const animationClasses = {
    pulse: 'animate-pulse',
    wave: 'animate-shimmer',
  };

  const style: React.CSSProperties = {
    width: typeof width === 'number' ? `${width}px` : width,
    height: typeof height === 'number' ? `${height}px` : height,
  };

  return (
    <div
      className={`${baseClasses} ${variantClasses[variant]} ${animationClasses[animation]} ${className}`}
      style={style}
    />
  );
};

// Loading skeleton for cards
export const CardSkeleton: React.FC = () => {
  return (
    <div className="bg-white rounded-lg shadow p-6 space-y-3">
      <Skeleton height={24} width="60%" />
      <Skeleton height={40} />
      <Skeleton height={16} width="40%" />
    </div>
  );
};

// Loading skeleton for table rows
export const TableRowSkeleton: React.FC<{ columns: number }> = ({ columns }) => {
  return (
    <tr>
      {Array.from({ length: columns }).map((_, index) => (
        <td key={index} className="px-6 py-4">
          <Skeleton height={16} />
        </td>
      ))}
    </tr>
  );
};

// Loading skeleton for chat messages
export const MessageSkeleton: React.FC = () => {
  return (
    <div className="flex gap-3">
      <Skeleton variant="circular" width={32} height={32} />
      <div className="flex-1 space-y-2">
        <Skeleton height={16} width="80%" />
        <Skeleton height={16} width="60%" />
      </div>
    </div>
  );
};