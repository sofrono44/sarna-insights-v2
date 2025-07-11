import React, { useState, useRef, useEffect } from 'react';
import { useMutation } from '@tanstack/react-query';
import { Send, Sparkles, AlertCircle } from 'lucide-react';
import { useToast } from '@/contexts/ToastContext';
import { Message, VisualizationData, LLMProvider, SUGGESTED_QUERIES } from './types';
import MessageBubble from './MessageBubble';
import SuggestedQueries from './SuggestedQueries';

interface ChatPanelProps {
  onVisualizationRequest: (visualization: VisualizationData) => void;
  isVisible: boolean;
}

const ChatPanel: React.FC<ChatPanelProps> = ({ onVisualizationRequest, isVisible }) => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [selectedProvider, setSelectedProvider] = useState('google');
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const { addToast } = useToast();

  const providers: LLMProvider[] = [
    { name: 'openai', model: 'gpt-4', active: true },
    { name: 'anthropic', model: 'claude-3.5-sonnet', active: true },
    { name: 'google', model: 'gemini-1.5-flash', active: true },
  ];

  // Enhanced chat mutation to handle visualizations
  const chatMutation = useMutation({
    mutationFn: async (question: string) => {
      const response = await fetch('/api/chat/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          question,
          provider: selectedProvider,
          context: {
            hasActiveAlerts: true, // Could be dynamic
            currentView: 'portfolio',
            previousMessages: messages.slice(-5), // Last 5 messages for context
          }
        }),
      });
      if (!response.ok) throw new Error('Failed to send message');
      return response.json();
    },
    onSuccess: (data) => {
      // Backend now returns visualization directly
      const assistantMessage: Message = {
        id: Date.now().toString(),
        role: 'assistant',
        content: data.answer,
        timestamp: new Date(),
        visualization: data.visualization,
      };
      
      setMessages((prev) => [...prev, assistantMessage]);
      
      // If visualization was generated, notify parent
      if (data.visualization) {
        onVisualizationRequest(data.visualization);
      }
    },
    onError: (error: Error) => {
      addToast({
        type: 'error',
        title: 'Failed to get response',
        message: error.message,
      });
    },
  });

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || chatMutation.isPending) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: input,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    chatMutation.mutate(input);
    setInput('');
    
    // Reset textarea height
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
    }
  };

  const handleTextareaChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setInput(e.target.value);
    
    // Auto-resize textarea
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = `${Math.min(textareaRef.current.scrollHeight, 120)}px`;
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  const handleSuggestedQuery = (query: string) => {
    setInput(query);
    // Focus the textarea
    textareaRef.current?.focus();
  };

  if (!isVisible) return null;

  return (
    <div className="flex flex-col h-full">
      {/* Provider Selector */}
      <div className="p-4 border-b border-gray-200">
        <div className="flex items-center justify-between">
          <label className="text-xs font-medium text-gray-600">AI Provider</label>
          <select
            value={selectedProvider}
            onChange={(e) => setSelectedProvider(e.target.value)}
            className="px-3 py-1 text-sm border border-gray-200 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            {providers.map((provider) => (
              <option key={provider.name} value={provider.name}>
                {provider.name.charAt(0).toUpperCase() + provider.name.slice(1)} ({provider.model})
              </option>
            ))}
          </select>
        </div>
      </div>
      
      {/* Messages Container */}
      <div className="flex-1 overflow-y-auto p-4">
        {messages.length === 0 ? (
          <div>
            <div className="bg-blue-50 text-blue-900 rounded-lg p-4 mb-4">
              <div className="flex items-start space-x-2">
                <Sparkles className="w-5 h-5 flex-shrink-0 mt-0.5" />
                <div>
                  <p className="font-medium">Welcome to AI Risk Assistant!</p>
                  <p className="text-sm mt-1">
                    I can help you analyze portfolio risk, visualize data, and identify issues. 
                    Try asking me to create charts or analyze specific metrics.
                  </p>
                </div>
              </div>
            </div>
            
            <SuggestedQueries onQuerySelect={handleSuggestedQuery} />
          </div>
        ) : (
          <div className="space-y-4">
            {messages.map((message) => (
              <MessageBubble key={message.id} message={message} />
            ))}
            
            {chatMutation.isPending && (
              <div className="flex items-center space-x-2 text-gray-500">
                <div className="animate-pulse">Thinking...</div>
              </div>
            )}
            
            <div ref={messagesEndRef} />
          </div>
        )}
      </div>      
      
      {/* Input Form */}
      <form onSubmit={handleSubmit} className="p-4 border-t border-gray-200">
        <div className="flex gap-2">
          <div className="flex-1 relative">
            <textarea
              ref={textareaRef}
              value={input}
              onChange={handleTextareaChange}
              onKeyDown={handleKeyDown}
              placeholder="Ask about risk, margins, P&L, or request visualizations..."
              className="w-full px-3 py-2 border border-gray-300 rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm"
              disabled={chatMutation.isPending}
              rows={1}
              style={{ minHeight: '40px', maxHeight: '120px' }}
            />
            {input.length > 0 && (
              <div className="absolute bottom-1 right-1 text-xs text-gray-400">
                {input.length}/500
              </div>
            )}
          </div>
          <button
            type="submit"
            disabled={chatMutation.isPending || !input.trim()}
            className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            {chatMutation.isPending ? (
              <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
            ) : (
              <Send className="w-5 h-5" />
            )}
          </button>
        </div>
        <div className="mt-2 text-xs text-gray-500">
          Press Enter to send, Shift+Enter for new line
        </div>
      </form>
    </div>
  );
};

export default ChatPanel;