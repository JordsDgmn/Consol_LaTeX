import sys

def create_ascii_architecture():
    """Create a text-based system architecture diagram"""
    
    diagram = """
CONSOL SYSTEM ARCHITECTURE
==========================

┌─────────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE LAYER                       │
│     📝 Note Creation     🎯 Practice Sessions     📊 Analytics      │
└─────────────────────────────┬───────────────────────────────────────┘
                              │ HTTP/HTTPS Requests
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    FRONTEND LAYER - React.js/Next.js 15            │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐    │
│  │  Dashboard  │ │Note Manager │ │ Sessions    │ │ Analytics   │    │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘    │
└─────────────────────────────┬───────────────────────────────────────┘
                              │ REST API Calls
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    API LAYER - Next.js API Routes                  │
│  /api/users  │  /api/notes  │  /api/sessions  │  /api/analytics    │
└──────┬──────────────┬─────────────────┬─────────────────────────────┘
       │              │                 │
       ▼              ▼                 ▼
┌─────────────┐  ┌─────────────────────────────────────────┐
│ AI PROCESSING │  │           DATA PERSISTENCE LAYER        │
│    LAYER      │  │         PostgreSQL Database             │
│               │  │                                         │
│ Flask API     │  │  ┌─────────────┐ ┌─────────────┐        │
│ (Port 5000)   │  │  │ Users Table │ │ Notes Table │        │
│               │  │  └─────────────┘ └─────────────┘        │
│ ┌───────────┐ │  │  ┌─────────────┐ ┌─────────────┐        │
│ │SimCSE     │ │  │  │Sessions Tbl │ │pg Pool Conn │        │
│ │Model      │ │  │  └─────────────┘ └─────────────┘        │
│ └───────────┘ │  │          (Direct SQL Queries)           │
│ ┌───────────┐ │  └─────────────────────────────────────────┘
│ │BERT Base  │ │
│ │Encoder    │ │
│ └───────────┘ │
│ ┌───────────┐ │
│ │Cosine     │ │
│ │Similarity │ │
│ └───────────┘ │
└─────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     EXTERNAL SERVICES                              │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐    │
│  │ Cloudinary  │ │   Vercel    │ │Hugging Face │ │  NextAuth   │    │
│  │   (Media)   │ │  (Hosting)  │ │(Model Hub)  │ │   (Auth)    │    │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘    │
└─────────────────────────────────────────────────────────────────────┘

DATA FLOW:
==========
1. User creates note → API → PostgreSQL (Direct SQL)
2. User practices → API → Flask (SimCSE) → Similarity score → PostgreSQL
3. Performance analytics → API → PostgreSQL → Chart.js visualization  
4. Media uploads → Cloudinary → URL stored in PostgreSQL

KEY TECHNICAL DETAILS:
=====================
• No Prisma ORM - Direct SQL via pg Pool for performance
• Flask API server hosts SimCSE model (princeton-nlp/unsup-simcse-bert-base-uncased)
• Real-time similarity computation (50-200ms processing time)
• PostgreSQL ACID compliance for educational data integrity
• Next.js 15 API routes for backend business logic
"""
    
    return diagram

def save_architecture_diagram():
    """Save the architecture diagram to a text file"""
    diagram = create_ascii_architecture()
    
    with open('consol_system_architecture.txt', 'w', encoding='utf-8') as f:
        f.write(diagram)
    
    print("✅ System architecture diagram saved as 'consol_system_architecture.txt'")
    print("\nTo view the diagram:")
    print("1. Open 'consol_system_architecture.txt' in any text editor")
    print("2. Use a monospace font for proper alignment")
    print("\nDiagram preview:")
    print("=" * 50)
    print(diagram[:500] + "...")

if __name__ == "__main__":
    save_architecture_diagram()