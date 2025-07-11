import React, { useState, useRef, useEffect } from 'react';
import { useMutation } from '@tanstack/react-query';
import { Send, Bot, User } from 'lucide-react';
import { useToast } from '@/contexts/ToastContext';
import { MessageSkeleton } from '@/components/common/Skeleton';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
}

interface LLMProvider {
  name: string;
  model: string;
  active: boolean;
}

const ChatInterface: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [selectedProvider, setSelectedProvider] = useState('openai');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Hardcode providers for now since there's no providers endpoint
  const providers: LLMProvider[] = [
    { name: 'openai', model: 'gpt-4', active: true },
    { name: 'anthropic', model: 'claude-3.5-sonnet', active: true },
    { name: 'google', model: 'gemini-1.5-flash', active: true },
  ];

  const { addToast } = useToast();

  // Chat mutation
  const chatMutation = useMutation({
    mutationFn: async (question: string) => {
      const response = await fetch('/api/chat/query', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          question,
          provider: selectedProvider,
        }),
      });
      if (!response.ok) {
        const error = await response.text();
        throw new Error(error || 'Failed to send message');
      }
      return response.json();
    },
    onSuccess: (data) => {
      const assistantMessage: Message = {
        id: Date.now().toString(),
        role: 'assistant',
        content: data.answer,
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, assistantMessage]);
    },
    onError: (error: Error) => {
      addToast({
        type: 'error',
        title: 'Failed to get response',
        message: error.message || 'Please try again later',
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
    if (!input.trim()) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: input,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    chatMutation.mutate(input);
    setInput('');
  };

  return (
    <div className="flex flex-col h-[400px]">
      {/* Provider Selector */}
      <div className="mb-4 flex items-center justify-between">
        <label className="text-xs font-medium text-[#718096]">AI Provider</label>
        <select
          value={selectedProvider}
          onChange={(e) => setSelectedProvider(e.target.value)}
          className="px-3 py-1 text-sm border border-gray-200 rounded-md focus:outline-none focus:ring-2 focus:ring-[#28549C] text-[#4A5568]"
        >
          {providers.map((provider) => (
            <option key={provider.name} value={provider.name} disabled={!provider.active}>
              {provider.name.charAt(0).toUpperCase() + provider.name.slice(1)} - {provider.model}
            </option>
          ))}
        </select>
      </div>
      
      {/* Messages Container */}
      <div className="flex-1 overflow-y-auto mb-4">
        {messages.length === 0 ? (
          <div className="bg-[#E6EDFA] text-[#1A1F2E] rounded-lg p-4 text-sm">
            Hello! I'm your AI Risk Assistant. I can help you analyze portfolio risk, understand margin requirements, and identify potential issues. What would you like to know?
          </div>
        ) : (
          <div className="space-y-4">
            {messages.map((message) => (
              <div
                key={message.id}
                className={`${message.role === 'user' ? 'text-right' : 'text-left'}`}
              >
                <div
                  className={`inline-block px-4 py-3 rounded-lg max-w-[70%] text-sm ${
                    message.role === 'user'
                      ? 'bg-[#28549C] text-white'
                      : 'bg-[#E6EDFA] text-[#1A1F2E]'
                  }`}
                >
                  {message.content}
                </div>
              </div>
            ))}
            {chatMutation.isPending && (
              <div className="text-left">
                <div className="inline-block px-4 py-3 rounded-lg bg-[#E6EDFA]">
                  <MessageSkeleton />
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>
        )}
      </div>
      
      {/* Input Form */}
      <form onSubmit={handleSubmit} className="flex gap-3">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your question..."
          className="flex-1 px-4 py-2 border border-gray-200 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-[#28549C] focus:border-transparent"
          disabled={chatMutation.isPending}
        />
        <button
          type="submit"
          disabled={chatMutation.isPending || !input.trim()}
          className="px-6 py-2 bg-[#28549C] text-white rounded-md hover:bg-[#1E3F76] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#28549C] disabled:opacity-50 disabled:cursor-not-allowed transition-colors text-sm font-medium"
        >
          {chatMutation.isPending ? (
            <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></div>
          ) : (
            'Send'
          )}
        </button>
      </form>
    </div>
  );
};

export default ChatInterface;
