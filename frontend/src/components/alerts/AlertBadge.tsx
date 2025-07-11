import React from 'react';

interface AlertBadgeProps {
  count: number;
  severity?: 'warning' | 'critical' | 'mixed';
  size?: 'sm' | 'md' | 'lg';
}

export const AlertBadge: React.FC<AlertBadgeProps> = ({ 
  count, 
  severity = 'mixed',
  size = 'md' 
}) => {
  if (count === 0) return null;

  const sizeClasses = {
    sm: 'h-5 w-5 text-xs',
    md: 'h-6 w-6 text-sm',
    lg: 'h-8 w-8 text-base'
  };

  const severityClasses = {
    warning: 'bg-yellow-500 text-white',
    critical: 'bg-red-600 text-white',
    mixed: 'bg-orange-500 text-white'
  };

  return (
    <div className={`
      ${sizeClasses[size]} 
      ${severityClasses[severity]}
      rounded-full flex items-center justify-center font-semibold
      animate-pulse shadow-lg
    `}>
      {count > 99 ? '99+' : count}
    </div>
  );
};
