# Next Session TODO - AI Assistant Improvements

## Current State
The AI Risk Assistant is functional but needs UI/UX improvements. It currently appears as a card in the main view below the portfolio table.

## Priority Tasks

### 1. Redesign AI Assistant UI
Consider these options:
- **Option A**: Floating chat bubble (bottom-right corner)
- **Option B**: Dedicated drawer (like other notifications)
- **Option C**: Modal dialog
- **Option D**: Collapsible panel in main view

### 2. Enhance Chat Interface
```typescript
// Suggested improvements:
- Message bubbles (user vs assistant)
- Timestamps on messages
- Loading animation while thinking
- Error states with retry
- Copy response button
- Clear conversation button
```

### 3. Add Conversation History
- Store messages in component state
- Show full conversation thread
- Allow scrolling through history
- Persist recent conversations (localStorage)

### 4. Improve Input Area
- Multi-line text input
- Send on Enter (Shift+Enter for new line)
- Character count indicator
- Disable while processing
- Clear button

### 5. Suggested Queries
Add quick-action buttons for common queries:
- "What are my biggest risks?"
- "Show me accounts with margin calls"
- "Explain my portfolio volatility"
- "Which positions need attention?"
- "Summarize today's P&L"

### 6. Context Integration
Make the assistant aware of:
- Current portfolio state
- Active alerts and notifications
- Selected accounts or positions
- Risk scenarios being viewed

### 7. Response Formatting
- Markdown support
- Tables for data
- Highlight important numbers
- Action buttons (e.g., "View Account")
- Charts/visualizations in responses

### 8. Provider Improvements
- Show response time
- Cost indicator
- Model capabilities hint
- Quick switch between providers

## Technical Considerations

### State Management
```typescript
interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
  provider?: string;
  error?: boolean;
}

interface ChatState {
  messages: ChatMessage[];
  isLoading: boolean;
  currentProvider: string;
}
```

### API Integration
- Stream responses for better UX
- Handle timeouts gracefully
- Retry failed requests
- Cache frequent queries

### Component Structure
```
ChatAssistant/
├── ChatContainer.tsx      // Main container
├── ChatHeader.tsx        // Title, provider selector
├── ChatMessages.tsx      // Message history
├── ChatInput.tsx         // Input area
├── ChatMessage.tsx       // Individual message
├── SuggestedQueries.tsx  // Quick actions
└── types.ts             // TypeScript types
```

## Testing Checklist
- [ ] Chat opens/closes smoothly
- [ ] Messages display correctly
- [ ] Provider switching works
- [ ] Error handling is graceful
- [ ] Loading states are clear
- [ ] Keyboard shortcuts work
- [ ] Mobile responsive
- [ ] Accessibility compliant

## Design Mockup Ideas
1. **Floating Bubble**: Minimizes to icon, expands to chat
2. **Side Drawer**: Full height, slides from right
3. **Bottom Panel**: Collapsible, takes bottom 1/3 of screen
4. **Modal**: Centered, with backdrop, focused experience

## Performance Goals
- Initial load: < 100ms
- First response: < 2s (Gemini)
- Smooth animations: 60fps
- Memory efficient: < 50MB