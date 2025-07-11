import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { BrowserRouter } from 'react-router-dom'
import Layout from '@/components/layout/Layout'
import { PortfolioEnhanced } from '@/components/visualizations/PortfolioEnhanced'
import { ToastProvider } from '@/contexts/ToastContext'
import { RiskMetricsCards } from '@/components/dashboard/RiskMetricsCards'
import { AIAssistantLayout } from '@/components/ai-assistant'

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
      <ToastProvider>
        <BrowserRouter>
          <Layout>
            <AIAssistantLayout>
              <div className="space-y-6">
                {/* Risk Metrics Cards */}
                <RiskMetricsCards />
                
                {/* Portfolio Overview - Full Width */}
                <div>
                  <h2 className="text-lg font-semibold mb-2">Portfolio Risk View</h2>
                  <PortfolioEnhanced groupId={10006} />
                </div>
              </div>
            </AIAssistantLayout>
          </Layout>
        </BrowserRouter>
      </ToastProvider>
    </QueryClientProvider>
  )
}

export default App
