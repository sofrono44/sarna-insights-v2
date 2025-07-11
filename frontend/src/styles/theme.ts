// Sarna Brand Colors and Design System
export const theme = {
  colors: {
    // Primary Scale
    primary: {
      50: '#EEF2FF',
      100: '#E6EDFA',
      200: '#C7D7F0',
      300: '#94B3E0',
      400: '#5B84C4',
      500: '#28549C',
      600: '#1E3F76',
      700: '#152D57',
      800: '#0F1F3A',
      900: '#0A1425',
    },
    // Brand Colors
    brand: {
      primary: '#28549C',
      surface: '#FFFFFF',
      card: '#F8F9FB',
    },
    // Text Colors
    text: {
      primary: '#1A1F2E',
      secondary: '#4A5568',
      light: '#718096',
    },
    // Semantic Colors
    success: '#48BB78',
    warning: '#ED8936',
    error: '#E53E3E',
    info: '#4299E1',
  },
  spacing: {
    1: '0.25rem',
    2: '0.5rem',
    3: '0.75rem',
    4: '1rem',
    5: '1.25rem',
    6: '1.5rem',
    8: '2rem',
    10: '2.5rem',
    12: '3rem',
  },
  fontSize: {
    xs: '0.75rem',
    sm: '0.875rem',
    base: '1rem',
    lg: '1.125rem',
    xl: '1.25rem',
    '2xl': '1.5rem',
    '3xl': '1.875rem',
    '4xl': '2.25rem',
  },
  fontWeight: {
    normal: 400,
    medium: 500,
    semibold: 600,
    bold: 700,
  },
  borderRadius: {
    sm: '0.25rem',
    md: '0.375rem',
    lg: '0.5rem',
    xl: '0.75rem',
  },
};

// Tailwind CSS class mappings for easy use
export const tailwindConfig = {
  primary: 'bg-[#28549C] hover:bg-[#1E3F76]',
  primaryText: 'text-[#28549C]',
  cardBg: 'bg-[#F8F9FB]',
  textPrimary: 'text-[#1A1F2E]',
  textSecondary: 'text-[#4A5568]',
  textLight: 'text-[#718096]',
};