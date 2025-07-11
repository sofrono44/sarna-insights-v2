# Next Session: Implement RAG for Portfolio Data Access

## 🎯 Primary Goal
Implement a RAG (Retrieval-Augmented Generation) solution using ChromaDB to make portfolio data more accessible to LLMs, replacing the current approach of sending all data in the prompt.

## 🔍 Current Problem
1. **Context Limitations**: Sending entire portfolio data in every prompt hits token limits
2. **Data Discovery**: LLMs struggle to find specific accounts/positions in nested JSON
3. **Scalability**: Current approach won't work with historical data or external sources
4. **Performance**: Large prompts slow down response times

## 📐 Proposed Architecture

### Phase 1: Basic RAG with ChromaDB (Demo)
```
┌─────────────────┐
│   Sarna API     │
└────────┬────────┘
         │
┌────────▼────────┐
│  Data Ingestion │ (Index portfolio snapshots)
└────────┬────────┘
         │
┌────────▼────────┐
│   ChromaDB      │ (Embedded vector store)
│  - Accounts     │
│  - Positions    │
│  - Risk Data    │
└────────┬────────┘
         │
┌────────▼────────┐
│   RAG Chain     │ (LangChain retrieval)
└────────┬────────┘
         │
┌────────▼────────┐
│   LLM + Tools   │
└─────────────────┘
```

### Data to Index
1. **Account Summaries**
   - Account ID, NAV, buying power, margin
   - Risk metrics and utilization
   - Position count and types

2. **Position Details**
   - Symbol, quantity, market value
   - P&L, cost basis, margins
   - Risk scenarios

3. **Aggregated Views**
   - Portfolio totals
   - Top positions by value/risk
   - Account groupings

## 🛠️ Implementation Tasks

### 1. Set Up ChromaDB
```python
# backend/services/vector_store.py
from chromadb import Client
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

class VectorStoreService:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection("portfolio")
```

### 2. Create Ingestion Pipeline
```python
# backend/services/portfolio_indexer.py
async def index_portfolio_data(portfolio_data):
    documents = []
    
    # Index account summaries
    for account in portfolio_data['accounts']:
        documents.append({
            'text': f"Account {account['id']} has NAV ${account['nav']:,.0f}...",
            'metadata': {'type': 'account', 'account_id': account['id']}
        })
    
    # Index positions
    for position in all_positions:
        documents.append({
            'text': f"Position {position['symbol']} in account...",
            'metadata': {'type': 'position', 'symbol': position['symbol']}
        })
```

### 3. Update Chat Endpoint
```python
# backend/routers/chat.py
async def query_portfolio_with_rag(query: ChatQuery):
    # 1. Retrieve relevant context
    relevant_docs = await vector_store.search(query.question, k=10)
    
    # 2. Build focused context
    context = format_retrieved_documents(relevant_docs)
    
    # 3. Query LLM with relevant context only
    response = await llm_service.query(
        prompt=f"Context:\n{context}\n\nQuestion: {query.question}",
        provider=query.provider
    )
```

### 4. Migration-Friendly Design
```python
# backend/services/vector_store_interface.py
class VectorStoreInterface(ABC):
    @abstractmethod
    async def add_documents(self, documents: List[Document])
    
    @abstractmethod
    async def search(self, query: str, k: int) -> List[Document]

# Easy to swap ChromaDB → Pinecone later
```

## 📋 Success Criteria
1. ✅ Portfolio data indexed in ChromaDB
2. ✅ LLM queries use semantic search for context
3. ✅ Reduced prompt sizes (under 2k tokens)
4. ✅ Accurate responses about specific positions/accounts
5. ✅ Faster response times
6. ✅ Architecture ready for Pinecone migration

## 🚀 Quick Start Commands
```bash
# 1. Install new dependencies
cd backend
pip install chromadb langchain langchain-openai

# 2. Update requirements.txt
pip freeze > requirements.txt

# 3. Rebuild backend
docker-compose build backend
docker-compose up -d
```

## 📦 New Dependencies Needed
- chromadb==0.4.24
- langchain==0.1.0
- langchain-openai==0.0.5
- tiktoken==0.5.2 (for token counting)

## 🔄 Migration Path to Pinecone
1. Change VectorStoreInterface implementation
2. Run migration script to copy embeddings
3. Update configuration
4. No changes to business logic needed

## 💡 Key Design Decisions
- Use repository pattern for easy migration
- Index at ingestion time (not query time)
- Cache embeddings to reduce API costs
- Separate collections for different data types
- Include temporal metadata for historical data

Remember: Start simple with ChromaDB, but design for Pinecone scale!