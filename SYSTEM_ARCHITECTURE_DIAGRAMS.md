# SYSTEM ARCHITECTURE & DATA FLOW DIAGRAMS

## 🏗️ MICROSERVICES ARCHITECTURE OVERVIEW

```
┌─────────────────────────────────────────────────────────────────┐
│                        CONSOL SYSTEM ARCHITECTURE               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐ │
│  │   FRONTEND      │    │    BACKEND      │    │  AI SERVICES    │ │
│  │   (Next.js)     │    │  (Next.js API)  │    │ (Flask + SimCSE) │ │
│  │                 │    │                 │    │                 │ │
│  │ • Dashboard     │◄──►│ • User API      │◄──►│ • SimCSE Model  │ │
│  │ • Session UI    │    │ • Notes API     │    │ • Similarity    │ │
│  │ • Analytics     │    │ • Sessions API  │    │   Calculation   │ │
│  │ • Profile Mgmt  │    │ • Auth Layer    │    │ • Batch Process │ │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘ │
│           │                       │                       │         │
│           │                       ▼                       │         │
│           │              ┌─────────────────┐              │         │
│           │              │   DATABASE      │              │         │
│           │              │ (PostgreSQL)    │              │         │
│           │              │                 │              │         │
│           │              │ • Users         │              │         │
│           └──────────────►│ • Notes        │◄─────────────┘         │
│                          │ • Sessions      │                        │
│                          │ • Relationships │                        │
│                          └─────────────────┘                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📊 ENTITY RELATIONSHIP DIAGRAM (ERD)

```
                    ┌─────────────────────────────────┐
                    │            USERS                │
                    ├─────────────────────────────────┤
                    │ 🔑 id (SERIAL PRIMARY KEY)      │
                    │ 📛 username (VARCHAR UNIQUE)    │
                    │ 🖼️ profile_picture_url (VARCHAR) │
                    │ 📅 created_at (TIMESTAMP)       │
                    └─────────────────────────────────┘
                                    │
                                    │ 1:N
                                    │
                    ┌───────────────▼─────────────────┐
                    │            NOTES                │
                    ├─────────────────────────────────┤
                    │ 🔑 id (SERIAL PRIMARY KEY)      │
                    │ 🔗 user_id (FK → users.id)      │
                    │ 📝 title (VARCHAR NOT NULL)     │
                    │ 📄 content (TEXT NOT NULL)      │
                    │ 🔢 word_count (INTEGER)         │
                    │ 📅 created_at (TIMESTAMP)       │
                    └─────────────────────────────────┘
                                    │
                                    │ 1:N
                                    │
                    ┌───────────────▼─────────────────┐
                    │           SESSIONS              │
                    ├─────────────────────────────────┤
                    │ 🔑 id (SERIAL PRIMARY KEY)      │
                    │ 🔗 user_id (FK → users.id)      │
                    │ 🔗 note_id (FK → notes.id)      │
                    │ 🎯 similarity (DECIMAL 5,3)     │
                    │ ⭐ stars (INTEGER 0-3)          │
                    │ 🔢 word_count (INTEGER)         │
                    │ ⏱️ duration_secs (INTEGER)       │
                    │ 🏃 wpm (DECIMAL 6,2)            │
                    │ 💡 hints_used (INTEGER)         │
                    │ 📦 session_group_id (VARCHAR)   │
                    │ 📅 created_at (TIMESTAMP)       │
                    └─────────────────────────────────┘

Relationships:
🔗 users.id ←→ notes.user_id (One-to-Many, CASCADE DELETE)
🔗 users.id ←→ sessions.user_id (One-to-Many, CASCADE DELETE)  
🔗 notes.id ←→ sessions.note_id (One-to-Many, CASCADE DELETE)
```

---

## 🔄 DATA FLOW ARCHITECTURE

### **Session Execution Pipeline**

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   USER      │    │  FRONTEND   │    │  BACKEND    │    │ DATABASE    │
│ INTERACTION │    │  (Next.js)  │    │   API       │    │(PostgreSQL) │
└──────┬──────┘    └──────┬──────┘    └──────┬──────┘    └──────┬──────┘
       │                  │                  │                  │
   1. Select Note         │                  │                  │
       ├─────────────────►│                  │                  │
       │                  │ 2. Fetch Note    │                  │
       │                  ├─────────────────►│                  │
       │                  │                  │ 3. Query Note    │
       │                  │                  ├─────────────────►│
       │                  │                  │◄─────────────────┤
       │                  │◄─────────────────┤ 4. Return Data   │
       │                  │ 5. Display UI    │                  │
       │◄─────────────────┤                  │                  │
   6. Start Session       │                  │                  │
       ├─────────────────►│                  │                  │
       │                  │ 7. Timer Start   │                  │
   8. Type Recall         │                  │                  │
       ├─────────────────►│                  │                  │
       │                  │ 9. Store Input   │                  │
  10. Submit Response     │                  │                  │
       ├─────────────────►│                  │                  │
       │                  │ 11. Send to AI   │                  │
       │                  ├──────────────────┼─────────────────┐│
       │                  │                  │                 ││
       │                  │      ┌─────────────────┐           ││
       │                  │      │  FLASK AI API   │           ││
       │                  │      │   (SimCSE)      │           ││
       │                  │      └─────────┬───────┘           ││
       │                  │                │                   ││
       │                  │ 12. Similarity │                   ││
       │                  │◄───────────────┘                   ││
       │                  │ 13. Calculate  │                   ││
       │                  │     Metrics    │                   ││
       │                  │ 14. Store Session                  ││
       │                  ├─────────────────►                  ││
       │                  │                  │ 15. INSERT      ││
       │                  │                  ├─────────────────►│
       │                  │                  │◄─────────────────┘
       │                  │ 16. Return Results                 │
       │                  │◄─────────────────┤                  │
  17. Display Results     │                  │                  │
       │◄─────────────────┤                  │                  │
       │                  │                  │                  │
```

### **Performance Analytics Flow**

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Dashboard  │    │ Analytics   │    │ Aggregation │
│   Request   │    │    API      │    │   Queries   │
└──────┬──────┘    └──────┬──────┘    └──────┬──────┘
       │                  │                  │
   1. Load Stats          │                  │
       ├─────────────────►│                  │
       │                  │ 2. Multi-table   │
       │                  │    JOIN Query    │
       │                  ├─────────────────►│
       │                  │                  │
       │                  │ ┌─────────────────────────┐
       │                  │ │  Complex Aggregation    │
       │                  │ │                         │
       │                  │ │ SELECT u.username,      │
       │                  │ │   COUNT(n.id) AS notes, │
       │                  │ │   AVG(s.similarity),    │ 
       │                  │ │   AVG(s.wpm),           │
       │                  │ │   AVG(s.stars)          │
       │                  │ │ FROM users u            │
       │                  │ │ LEFT JOIN notes n...    │
       │                  │ │ LEFT JOIN sessions s... │
       │                  │ │ GROUP BY u.id           │
       │                  │ └─────────────────────────┘
       │                  │                  │
       │                  │ 3. Computed Stats│
       │                  │◄─────────────────┤
       │                  │ 4. JSON Response │
       │◄─────────────────┤                  │
   5. Render Charts      │                  │
       │                  │                  │
```

---

## 🔧 COMPONENT INTERACTION DIAGRAM

### **Frontend Component Architecture**

```
┌─────────────────────────────────────────────────────────────────┐
│                     NEXT.JS APPLICATION                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   PAGE COMPONENTS                       │    │
│  │                                                         │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │    │
│  │  │ Dashboard   │  │ Session     │  │ Profile     │      │    │
│  │  │   Page      │  │   Page      │  │   Page      │      │    │
│  │  │  /page.js   │  │/session/    │  │/profile/    │      │    │
│  │  │             │  │ page.js     │  │ page.js     │      │    │
│  │  └─────────────┘  └─────────────┘  └─────────────┘      │    │
│  │         │                 │                 │           │    │
│  └─────────┼─────────────────┼─────────────────┼───────────┘    │
│            │                 │                 │                │
│  ┌─────────▼─────────────────▼─────────────────▼───────────┐    │
│  │               SHARED COMPONENTS                        │    │
│  │                                                        │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │    │
│  │  │ Navbar   │ │LineChart │ │RadarChart│ │HistoryTbl│   │    │
│  │  │.js       │ │.js       │ │.js       │ │.js       │   │    │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘   │    │
│  │       │             │             │             │      │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │    │
│  │  │Calendar  │ │HelpModal │ │Preview   │ │Screenshot│   │    │
│  │  │.js       │ │.js       │ │Panel.js  │ │Slideshow │   │    │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘   │    │
│  └────────────────────────────────────────────────────────┘    │
│                               │                                │
│  ┌───────────────────────────▼─────────────────────────────┐    │
│  │                    API ROUTES                          │    │
│  │                                                        │    │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐       │    │
│  │  │/api/users   │ │/api/notes   │ │/api/sessions│       │    │
│  │  │• GET users  │ │• GET notes  │ │• GET history│       │    │
│  │  │• POST user  │ │• POST note  │ │• POST result│       │    │
│  │  │• GET stats  │ │• PUT note   │ │• PUT session│       │    │
│  │  └─────────────┘ └─────────────┘ └─────────────┘       │    │
│  └────────────────────────────────────────────────────────┘    │
│                               │                                │
└───────────────────────────────┼────────────────────────────────┘
                                ▼
         ┌─────────────────────────────────────┐
         │        EXTERNAL SERVICES            │
         ├─────────────────────────────────────┤
         │  ┌─────────────┐ ┌─────────────┐     │
         │  │ PostgreSQL  │ │ Flask API   │     │
         │  │ Database    │ │(SimCSE AI)  │     │
         │  │             │ │             │     │
         │  │• Users      │ │• Similarity │     │
         │  │• Notes      │ │• Embeddings │     │  
         │  │• Sessions   │ │• Batch Proc │     │
         │  └─────────────┘ └─────────────┘     │
         └─────────────────────────────────────┘
```

---

## 🎯 SESSION WORKFLOW DIAGRAM

```
User Journey: Complete Study Session

┌─────────────┐    Select Study Material
│  Dashboard  ├────────────────────────────┐
└─────────────┘                            │
                                           ▼
┌─────────────┐    Configure Session      ┌─────────────┐
│Note Library ├───────────────────────────►│Session Setup│
└─────────────┘                            └──────┬──────┘
                                                  │
                                                  │ Start Session
                                                  ▼
┌─────────────┐    Active Recall Phase     ┌─────────────┐
│ User Input  │◄──────────────────────────►│Session Page │
│  (Memory)   │         Real-time          │             │
└──────┬──────┘         Feedback           └──────┬──────┘
       │                                          │
       │ Submit Response                          │ Process Input
       ▼                                          ▼
┌─────────────┐    AI Evaluation          ┌─────────────┐
│ Flask API   │                           │Session Data │
│ (SimCSE)    │                           │ Collection  │
│             │                           │             │
│• Embeddings │ Similarity Score          │• Content    │
│• Cosine Sim │◄─────────────────────────►│• Duration   │
│• Batch Proc │                           │• WPM Calc   │
└──────┬──────┘                           └──────┬──────┘
       │                                         │
       │ Return Score                            │ Store Metrics
       ▼                                         ▼
┌─────────────┐    Performance Analysis   ┌─────────────┐
│Results Page │                           │PostgreSQL   │
│             │                           │Database     │
│• Similarity │◄──────────────────────────┤             │
│• Stars      │    Query Analytics        │• Sessions   │
│• WPM        │                           │• History    │
│• Progress   │                           │• Aggregates │
└──────┬──────┘                           └─────────────┘
       │
       │ Continue/Exit
       ▼
┌─────────────┐    Learning Loop
│  Dashboard  │
│  (Updated   │
│  Analytics) │
└─────────────┘
```

---

## 💻 TECHNOLOGY STACK INTEGRATION

### **Frontend Layer (Next.js 14)**
```javascript
// Component Example: Session Page
'use client';

import { useState, useEffect } from 'react';
import { LineChart, RadarChart } from '@/components';

export default function SessionPage({ params }) {
    const [userInput, setUserInput] = useState('');
    const [similarity, setSimilarity] = useState(null);
    const [sessionData, setSessionData] = useState(null);
    
    const handleSubmit = async () => {
        // 1. Collect session metrics
        const metrics = calculateMetrics();
        
        // 2. Send to AI API for evaluation
        const response = await fetch('/api/sessions', {
            method: 'POST',
            body: JSON.stringify({
                noteId: params.noteId,
                content: userInput,
                ...metrics
            })
        });
        
        // 3. Display results
        const result = await response.json();
        setSimilarity(result.similarity);
    };
    
    return (
        <div className="session-interface">
            <textarea 
                value={userInput}
                onChange={(e) => setUserInput(e.target.value)}
                placeholder="Type what you remember..."
            />
            <button onClick={handleSubmit}>Submit</button>
            {similarity && <ScoreDisplay score={similarity} />}
        </div>
    );
}
```

### **Backend Layer (Next.js API + PostgreSQL)**
```javascript
// API Route Example: /api/sessions/route.ts
import { db } from '@/lib/database';

export async function POST(request) {
    const { noteId, content, userId, duration } = await request.json();
    
    // 1. Get original note content
    const note = await db.query(
        'SELECT content FROM notes WHERE id = $1',
        [noteId]
    );
    
    // 2. Send to AI API for similarity
    const aiResponse = await fetch('http://localhost:5000/similarity', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            text1: note.content,
            text2: content
        })
    });
    
    const { similarity } = await aiResponse.json();
    
    // 3. Calculate performance metrics
    const wpm = calculateWPM(content, duration);
    const stars = calculateStars(similarity);
    
    // 4. Store session record
    const session = await db.query(
        'INSERT INTO sessions (user_id, note_id, similarity, stars, wpm, duration_secs) VALUES ($1, $2, $3, $4, $5, $6) RETURNING *',
        [userId, noteId, similarity, stars, wpm, duration]
    );
    
    return Response.json(session);
}
```

### **AI Layer (Flask + SimCSE)**
```python
# Flask API Example: app.py
from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
model = SentenceTransformer('princeton-nlp/unsup-simcse-bert-base-uncased')

@app.route('/similarity', methods=['POST'])
def calculate_similarity():
    data = request.json
    text1 = data['text1']
    text2 = data['text2']
    
    # Generate embeddings
    embeddings = model.encode([text1, text2], normalize_embeddings=True)
    
    # Calculate cosine similarity
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    
    return jsonify({
        'similarity': float(similarity),
        'confidence': 'high',
        'model': 'simcse-bert-base-uncased'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

---

## 🌐 DEPLOYMENT ARCHITECTURE OPTIONS

### **Current Prototype (100% Offline)**

```
Your Computer:
├── Next.js App (localhost:3001)
├── PostgreSQL Database (local)
├── SimCSE API (localhost:5000)
└── SimCSE Model (110MB local)
```

**Offline Advantages**:
- ✅ **No internet required** after initial download
- ✅ **All 110 million parameters** stored locally
- ✅ **Full vocabulary** available offline
- ✅ **Identical performance** to online version
- ✅ **Data privacy** - nothing goes online

### **Production Deployment Options**

**Option A: Fully Hosted (Recommended)**
```
Cloud Infrastructure:
├── Next.js App (Vercel/Netlify)
├── PostgreSQL (AWS RDS/Supabase)  ─┐
├── SimCSE API (AWS/GCP/Azure)      ├─── ALL CLOUD
└── SimCSE Model (stored on server) ─┘
```

**Option B: Hybrid API-only Cloud**
```
User's Computer: Next.js App
Cloud: SimCSE API + Database
Local: Nothing (all API calls)
```

**Option C: Edge Computing**
```
CDN Edge Servers: SimCSE model
Cloud: Database + API
User: Next.js App
```

### **Model Deployment Details**

**SimCSE Model Folder Structure**:
```
simcse-model/
├── config.json                  # Model architecture configuration
├── model.safetensors            # 110MB of trained weights (neural network)
├── tokenizer.json               # Vocabulary and tokenization rules
├── tokenizer_config.json        # Tokenizer settings
├── special_tokens_map.json      # [CLS], [SEP], [MASK] definitions
└── vocab.txt                    # 30,000 word vocabulary
```

**What Goes Online vs Offline**:
- **Database queries**: User data, notes, session history
- **Model inference**: If using cloud GPU for SimCSE
- **File uploads**: If storing files in cloud storage
- **User authentication**: Login/signup API calls

**What Stays Offline**:
- **SimCSE model weights**: Could stay on your servers
- **Core logic**: Your algorithms remain proprietary
- **Vector calculation**: Happens server-side

---

## 🔧 TENSOR & PYTORCH IMPLEMENTATION

### **Understanding Tensors in Your System**

```python
# What are Tensors?
inputs = tokenizer([text1, text2], return_tensors="pt", padding=True, truncation=True)

# Tensors are multi-dimensional arrays optimized for machine learning:
input_ids = torch.tensor([[101, 1996, 4937, 102, 0, 0]])      # Shape: [1, 6]
# IDs: [CLS] [the] [cat] [SEP] [PAD] [PAD]

embeddings = torch.tensor([[0.23, -0.45, 0.78, ...]])         # Shape: [1, 768]
# 768-dimensional vector representing sentence meaning
```

**Why PyTorch ("pt")?**
- **GPU Acceleration**: Tensors can run on GPU for faster computation
- **Automatic Differentiation**: For training (though you're only doing inference)
- **Memory Efficiency**: Optimized storage and computation
- **Batch Processing**: Process multiple texts simultaneously

### **The Embedding Journey**

```python
# Your complete pipeline:
outputs = model(**inputs)
embeddings = outputs.last_hidden_state[:, 0, :]  # Extract [CLS] token embedding

# What's happening:
# 1. Token Embeddings: Each word becomes a 768D vector
# 2. Position Embeddings: Added to know word order
# 3. Transformer Processing: 12 layers refine these vectors
# 4. Final Embedding: The [CLS] token contains the sentence summary
```

### **Padding & Truncation Example**

```python
# The Problem: Neural networks need fixed-size inputs
# Your Code:
inputs = tokenizer([text1, text2], padding=True, truncation=True)

# Padding Example:
original_texts = [
    "The cat sat" → [101, 1996, 4937, 2938, 102],           # 5 tokens
    "Dogs run fast in parks" → [101, 6077, 2448, 3435, 1999, 6009, 102]  # 7 tokens
]

# After padding (to max length 7):
padded = [
    "The cat sat" → [101, 1996, 4937, 2938, 102, 0, 0],     # Padded with 0s
    "Dogs run fast in parks" → [101, 6077, 2448, 3435, 1999, 6009, 102]  # No change
]

# Truncation Example:
long_text = "This is a very long sentence that exceeds the maximum token limit..."
truncated = "This is a very long sentence that exceeds the maximum..." # [CUT AT 512 TOKENS]
```

---

This **comprehensive architecture** demonstrates the **sophisticated integration** of **modern web technologies**, **AI models**, and **educational psychology principles** to create an **innovative active recall learning system**.