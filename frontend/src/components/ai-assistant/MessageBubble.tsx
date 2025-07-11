import React from 'react';
import { format } from 'date-fns';
import { User, Bot, BarChart2, Copy, Check } from 'lucide-react';
import { Message } from './types';

interface MessageBubbleProps {
  message: Message;
}

const MessageBubble: React.FC<MessageBubbleProps> = ({ message }) => {
  const [copied, setCopied] = React.useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(message.content);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const isUser = message.role === 'user';

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div className={`flex max-w-[80%] ${isUser ? 'flex-row-reverse' : 'flex-row'} gap-2`}>
        {/* Avatar */}
        <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${
          isUser ? 'bg-blue-600' : 'bg-gray-600'
        }`}>
          {isUser ? <User className="w-4 h-4 text-white" /> : <Bot className="w-4 h-4 text-white" />}
        </div>
        
        {/* Message Content */}
        <div className="flex flex-col">
          <div className={`rounded-lg px-4 py-2 ${
            isUser 
              ? 'bg-blue-600 text-white' 
              : 'bg-gray-100 text-gray-900'
          }`}>
            <p className="text-sm whitespace-pre-wrap">{message.content}</p>
            
            {/* Visualization Indicator */}
            {message.visualization && (
              <div className={`mt-2 flex items-center gap-1 text-xs ${
                isUser ? 'text-blue-200' : 'text-gray-600'
              }`}>
                <BarChart2 className="w-3 h-3" />
                <span>Visualization generated</span>
              </div>
            )}
          </div>
          
          {/* Timestamp and Actions */}
          <div className={`mt-1 flex items-center gap-2 text-xs text-gray-500 ${
            isUser ? 'justify-end' : 'justify-start'
          }`}>
            <span>{format(message.timestamp, 'HH:mm')}</span>
            
            {!isUser && (
              <button
                onClick={handleCopy}
                className="flex items-center gap-1 hover:text-gray-700 transition-colors"
                title="Copy message"
              >
                {copied ? (
                  <>
                    <Check className="w-3 h-3" />
                    <span>Copied</span>
                  </>
                ) : (
                  <>
                    <Copy className="w-3 h-3" />
                    <span>Copy</span>
                  </>
                )}
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default MessageBubble;
