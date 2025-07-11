export interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
  visualization?: VisualizationData;
}

export interface VisualizationData {
  type: 'chart' | 'table' | 'risk-matrix' | 'custom';
  title: string;
  description?: string;
  data: any;
  config?: any;
}

export type ChatResponse = 
  | { type: 'text'; content: string }
  | { type: 'visualization'; content: string; data: VisualizationData }
  | { type: 'hybrid'; text: string; visualization: VisualizationData };

export interface AIAssistantState {
  messages: Message[];
  visualizations: VisualizationData[];
  activeVisualizationId: string | null;
  isGenerating: boolean;
  splitPosition: number;
}

export interface LLMProvider {
  name: string;
  model: string;
  active: boolean;
}

export const SUGGESTED_QUERIES = [
  "What are my biggest risks?",
  "Show me accounts with margin calls",
  "Explain my portfolio volatility",
  "Which positions need attention?",
  "Summarize today's P&L",
  "Compare performance across all scenarios",
  "Show top 5 riskiest positions",
  "List accounts approaching PDT limits",
  "Visualize portfolio concentration",
  "What's my overall margin utilization?"
];
