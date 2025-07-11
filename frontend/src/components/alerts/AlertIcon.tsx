import React from 'react';

interface AlertIconProps {
  severity: 'warning' | 'critical';
  size?: 'sm' | 'md' | 'lg';
  className?: string;
}

export const AlertIcon: React.FC<AlertIconProps> = ({ 
  severity, 
  size = 'md',
  className = ''
}) => {
  const sizeClasses = {
    sm: 'h-4 w-4',
    md: 'h-5 w-5',
    lg: 'h-6 w-6'
  };

  const severityClasses = {
    warning: 'text-yellow-500',
    critical: 'text-red-600'
  };

  return (
    <svg
      className={`${sizeClasses[size]} ${severityClasses[severity]} ${className}`}
      fill="currentColor"
      viewBox="0 0 20 20"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        fillRule="evenodd"
        d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z"
        clipRule="evenodd"
      />
    </svg>
  );
};
