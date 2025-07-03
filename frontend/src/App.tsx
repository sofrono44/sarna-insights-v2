import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { BrowserRouter } from 'react-router-dom'
import Layout from '@/components/layout/Layout'
import ChatInterface from '@/components/chat/ChatInterface'
import PortfolioOverview from '@/components/visualizations/PortfolioOverview'

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 30 * 1000, // 30 seconds
      retry: 1,
    },
  },
})

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <Layout>
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 p-6">
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-2xl font-bold mb-4">Portfolio Overview</h2>
              <PortfolioOverview />
            </div>
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-2xl font-bold mb-4">AI Assistant</h2>
              <ChatInterface />
            </div>
          </div>
        </Layout>
      </BrowserRouter>
    </QueryClientProvider>
  )
}

export default App
