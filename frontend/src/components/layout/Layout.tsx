import React, { useState } from 'react';
import { useQueryClient } from '@tanstack/react-query';
import { RefreshCw, LayoutDashboard, TrendingUp, Shield, Settings, HelpCircle, Mail } from 'lucide-react';
import { useToast } from '@/contexts/ToastContext';
import { Drawer } from '@/components/common/Drawer';
import { mockMessages } from '@/components/messages/types';

interface LayoutProps {
  children: React.ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  const queryClient = useQueryClient();
  const { addToast } = useToast();
  const [isRefreshing, setIsRefreshing] = React.useState(false);
  const [isMessageDrawerOpen, setIsMessageDrawerOpen] = useState(false);
  const unreadMessages = mockMessages.filter(m => !m.read).length;

  const handleRefresh = async () => {
    setIsRefreshing(true);
    try {
      await queryClient.invalidateQueries();
      addToast({
        type: 'success',
        title: 'Data Refreshed',
        message: 'All portfolio data has been updated',
        duration: 3000,
      });
    } catch (error) {
      addToast({
        type: 'error',
        title: 'Refresh Failed',
        message: 'Unable to refresh data. Please try again.',
      });
    } finally {
      setIsRefreshing(false);
    }
  };

  const navItems = [
    { icon: LayoutDashboard, label: 'Dashboard', active: true },
    { icon: TrendingUp, label: 'Analytics', active: false },
    { icon: Shield, label: 'Risk Management', active: false },
    { icon: Settings, label: 'Settings', active: false },
  ];

  return (
    <div className="flex h-screen w-screen fixed top-0 left-0 bg-white">
      {/* Sidebar */}
      <div className="w-64 bg-sarna-light border-r border-gray-200 flex flex-col">
        {/* Logo */}
        <div className="p-6">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-sarna-blue rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-lg">SI</span>
            </div>
            <span className="text-xl font-semibold text-sarna-dark">Sarna Insights</span>
          </div>
        </div>

        {/* Navigation */}
        <nav className="flex-1 px-4">
          <div className="space-y-1">
            {navItems.map((item, index) => (
              <button
                key={index}
                className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                  item.active
                    ? 'bg-sarna-blue text-white'
                    : 'text-sarna-gray hover:bg-gray-100'
                }`}
              >
                <item.icon className="w-5 h-5" />
                <span className="font-medium">{item.label}</span>
              </button>
            ))}
          </div>
        </nav>

        {/* Help Section */}
        <div className="p-4 border-t border-gray-200">
          <button className="w-full flex items-center gap-3 px-4 py-3 text-sarna-gray hover:bg-gray-100 rounded-lg transition-colors">
            <HelpCircle className="w-5 h-5" />
            <span className="font-medium">Help & Support</span>
          </button>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Header */}
        <header className="bg-white border-b border-gray-200 px-8 py-4">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-2xl font-bold text-sarna-dark">Risk Dashboard</h1>
              <p className="text-sm text-sarna-gray mt-1">Monitor and analyze portfolio risk in real-time</p>
            </div>
            <div className="flex items-center gap-3">
              <button
                onClick={() => setIsMessageDrawerOpen(true)}
                className="relative p-2 rounded-lg border border-gray-300 hover:bg-gray-50 transition-colors"
              >
                <Mail className="w-5 h-5 text-gray-600" />
                {unreadMessages > 0 && (
                  <div className="absolute -top-2 -right-2">
                    <div className="h-5 w-5 bg-blue-600 text-white rounded-full flex items-center justify-center text-xs font-semibold">
                      6
                    </div>
                  </div>
                )}
              </button>
              
              <button
                onClick={handleRefresh}
                disabled={isRefreshing}
                className={`px-4 py-2 flex items-center gap-2 font-medium rounded-lg border transition-colors ${
                  isRefreshing
                    ? 'border-gray-300 text-gray-400 cursor-not-allowed'
                    : 'border-sarna-blue text-sarna-blue hover:bg-sarna-blue hover:text-white'
                }`}
              >
                <RefreshCw className={`w-4 h-4 ${isRefreshing ? 'animate-spin' : ''}`} />
                Refresh Data
              </button>
            </div>
          </div>
        </header>

        {/* Main Content Area */}
        <main className="flex-1 overflow-y-auto bg-gray-50 p-6">
          <div className="max-w-full">
            {children}
          </div>
        </main>
      </div>
      
      {/* Message Drawer */}
      <Drawer 
        isOpen={isMessageDrawerOpen} 
        onClose={() => setIsMessageDrawerOpen(false)}
        title="Messages"
        subtitle={`${unreadMessages} unread messages`}
      >
        <div className="p-4 space-y-3">
          {mockMessages.map(message => (
            <div 
              key={message.message_id}
              className={`p-4 rounded-lg border transition-all ${
                !message.read 
                  ? 'bg-blue-50 border-blue-200 hover:shadow-md' 
                  : 'bg-gray-50 border-gray-200 hover:shadow-sm'
              }`}
            >
              <div className="flex justify-between items-start mb-2">
                <div>
                  <div className="flex items-center gap-2">
                    <span className="font-semibold text-gray-900">{message.from}</span>
                    <span className={`px-2 py-0.5 text-xs font-medium rounded-full ${
                      message.priority === 'high' 
                        ? 'bg-red-100 text-red-700' 
                        : message.priority === 'low' 
                        ? 'bg-gray-100 text-gray-700'
                        : 'bg-blue-100 text-blue-700'
                    }`}>
                      {message.priority}
                    </span>
                  </div>
                  <h4 className="font-medium text-gray-900 mt-1">{message.subject}</h4>
                </div>
                <span className="text-xs text-gray-500">
                  {new Date(message.timestamp).toLocaleTimeString([], { 
                    hour: '2-digit', 
                    minute: '2-digit' 
                  })}
                </span>
              </div>
              <p className="text-sm text-gray-600">{message.preview}</p>
            </div>
          ))}
        </div>
      </Drawer>
    </div>
  );
};

export default Layout;
