# DATABASE SCHEMA & ERD DOCUMENTATION

## 📊 COMPLETE POSTGRESQL SCHEMA

Based on your codebase analysis, here is the **complete database schema** that I found:

```sql
-- ═══════════════════════════════════════════════════════════════
-- CONSOL DATABASE SCHEMA (PostgreSQL)
-- ═══════════════════════════════════════════════════════════════

-- Users Table: Core user management
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    profile_picture_url VARCHAR(500) DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Notes Table: User-created study content  
CREATE TABLE notes (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    word_count INTEGER DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Sessions Table: Study session records with performance metrics
CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    note_id INTEGER REFERENCES notes(id) ON DELETE CASCADE,
    similarity DECIMAL(5,3) NOT NULL,
    stars INTEGER NOT NULL CHECK (stars >= 0 AND stars <= 3),
    word_count INTEGER DEFAULT NULL,
    duration_secs INTEGER DEFAULT NULL,
    wpm DECIMAL(6,2) DEFAULT NULL,
    hints_used INTEGER DEFAULT 0,
    session_group_id VARCHAR(100) DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for Performance Optimization
CREATE INDEX idx_notes_user_id ON notes(user_id);
CREATE INDEX idx_sessions_user_id ON sessions(user_id);
CREATE INDEX idx_sessions_note_id ON sessions(note_id);
CREATE INDEX idx_sessions_created_at ON sessions(created_at DESC);
CREATE INDEX idx_sessions_similarity ON sessions(similarity);
```

---

## 🔗 ENTITY RELATIONSHIPS

### **Primary Relationships**

1. **One-to-Many: Users → Notes**
   - One user can have multiple notes
   - Cascade delete: When user deleted, all their notes are removed
   - Foreign Key: `notes.user_id → users.id`

2. **One-to-Many: Users → Sessions**
   - One user can have multiple study sessions
   - Cascade delete: When user deleted, all their sessions are removed
   - Foreign Key: `sessions.user_id → users.id`

3. **One-to-Many: Notes → Sessions**
   - One note can have multiple study sessions
   - Cascade delete: When note deleted, all sessions for that note are removed
   - Foreign Key: `sessions.note_id → notes.id`

### **Key Constraints**

- **Username Uniqueness**: `UNIQUE` constraint on `users.username`
- **Star Rating Validation**: `CHECK (stars >= 0 AND stars <= 3)`
- **Referential Integrity**: All foreign keys with `CASCADE DELETE`
- **Similarity Precision**: `DECIMAL(5,3)` allows values like 0.851

---

## 📋 TABLE ANALYSIS

### **Users Table**
```sql
Field                 | Type                | Purpose
----------------------|-------------------- |---------------------------
id                    | SERIAL PRIMARY KEY  | Unique user identifier
username              | VARCHAR(255) UNIQUE | User display name 
profile_picture_url   | VARCHAR(500)        | Cloudinary image URL
created_at           | TIMESTAMP           | Account creation tracking
```

**Business Logic**: Simple user management with profile pictures stored via Cloudinary integration.

### **Notes Table**  
```sql
Field       | Type                | Purpose
------------|-------------------- |---------------------------
id          | SERIAL PRIMARY KEY  | Unique note identifier
user_id     | INTEGER FK          | Owner relationship
title       | VARCHAR(255)        | Note display name
content     | TEXT                | Full note content (ground truth)
word_count  | INTEGER             | Calculated content length
created_at  | TIMESTAMP           | Note creation tracking
```

**Business Logic**: User-generated study content serving as "ground truth" for similarity comparison.

### **Sessions Table**
```sql
Field             | Type                | Purpose
------------------|-------------------- |---------------------------
id                | SERIAL PRIMARY KEY  | Unique session identifier
user_id           | INTEGER FK          | Session owner
note_id           | INTEGER FK          | Associated study content
similarity        | DECIMAL(5,3)        | AI-calculated similarity score
stars             | INTEGER             | Performance rating (0-3)
word_count        | INTEGER             | User recall length
duration_secs     | INTEGER             | Session completion time
wpm               | DECIMAL(6,2)        | Words per minute calculation
hints_used        | INTEGER             | Help requests during session
session_group_id  | VARCHAR(100)        | Grouped session tracking
created_at        | TIMESTAMP           | Session completion time
```

**Business Logic**: Comprehensive performance tracking with AI-generated metrics and user behavior analytics.

---

## 🎯 KEY QUERIES FROM YOUR API

Based on your codebase, here are the critical database operations:

### **User Statistics Query** (from `/api/users/route.ts`)
```sql
SELECT 
  u.id,
  u.username,
  u.profile_picture_url,
  u.created_at,
  COUNT(DISTINCT n.id) AS notes,
  ROUND(AVG(s.wpm)::numeric, 1) AS speed,
  ROUND(AVG(s.stars)::numeric, 1) AS mastery,
  ROUND(AVG(s.similarity)::numeric, 2) AS comprehension,
  MAX(s.created_at) AS last_active
FROM users u
LEFT JOIN notes n ON u.id = n.user_id
LEFT JOIN sessions s ON u.id = s.user_id
GROUP BY u.id
ORDER BY u.id ASC;
```

**Purpose**: Dashboard overview with computed performance metrics.

### **Session History Query** (from `/api/sessions/route.ts`)
```sql
SELECT sessions.*, notes.title
FROM sessions
JOIN notes ON sessions.note_id = notes.id
WHERE sessions.user_id = $1 AND sessions.note_id = $2
ORDER BY sessions.created_at ASC;
```

**Purpose**: Performance tracking and progress visualization.

### **Session Recording Query** (from `/api/sessions/route.ts`)
```sql
INSERT INTO sessions (user_id, note_id, similarity, stars, word_count, duration_secs, wpm, hints_used, session_group_id)
VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
RETURNING *;
```

**Purpose**: Persist performance data after AI evaluation.

---

## 🔍 DATA FLOW ANALYSIS

### **Session Execution Pipeline**

1. **User Selection**: Query `notes` table for user's content
2. **Active Recall**: User types from memory (frontend state)
3. **AI Processing**: Send to Flask API for SimCSE evaluation  
4. **Score Calculation**: Receive similarity score from AI model
5. **Performance Metrics**: Calculate WPM, stars, duration
6. **Data Persistence**: Insert into `sessions` table
7. **Analytics Update**: Refresh dashboard with new statistics

### **User Experience Flow**
```
Dashboard → Select Note → Configure Session → Start
    ↓
Session Page → User Input → SimCSE API → Similarity Score
    ↓  
Results → Database Storage → Analytics Update
```

---

## 💾 SAMPLE DATA STRUCTURE

### **Example Records**

**Users Table**:
```sql
INSERT INTO users (username, profile_picture_url) VALUES 
('student1', 'https://res.cloudinary.com/demo/image/upload/v1234567890/profiles/user1.jpg'),
('teacher2', NULL),
('researcher3', 'https://res.cloudinary.com/demo/image/upload/v1234567890/profiles/user3.jpg');
```

**Notes Table**:
```sql  
INSERT INTO notes (user_id, title, content, word_count) VALUES
(1, 'Biology Chapter 3', 'Photosynthesis is the process by which plants convert sunlight into energy...', 45),
(1, 'History Notes', 'World War II began in 1939 when Germany invaded Poland...', 32),
(2, 'Math Formulas', 'The quadratic formula is x = (-b ± √(b²-4ac)) / 2a...', 28);
```

**Sessions Table**:
```sql
INSERT INTO sessions (user_id, note_id, similarity, stars, word_count, duration_secs, wpm, hints_used) VALUES
(1, 1, 0.876, 3, 42, 180, 14.0, 0),
(1, 1, 0.654, 2, 38, 150, 15.2, 1),  
(1, 2, 0.423, 1, 25, 120, 12.5, 2);
```

---

## 🚀 PERFORMANCE OPTIMIZATIONS

### **Indexing Strategy**
- **User-based queries**: `idx_notes_user_id`, `idx_sessions_user_id`
- **Note performance**: `idx_sessions_note_id`  
- **Temporal analysis**: `idx_sessions_created_at DESC`
- **Score filtering**: `idx_sessions_similarity`

### **Query Optimization**
- **Left joins** for optional relationships (user stats)
- **Aggregated calculations** in single query (avoid N+1 problems)
- **Ordered results** for consistent pagination
- **Selective columns** to reduce data transfer

---

## 🛡️ DATA INTEGRITY MEASURES

### **Referential Integrity**
- **CASCADE DELETE**: Orphaned records automatically removed
- **NOT NULL constraints**: Essential fields always populated
- **UNIQUE constraints**: Username uniqueness enforced
- **CHECK constraints**: Star ratings within valid range (0-3)

### **Data Validation**  
- **Frontend validation**: Input sanitization and length limits
- **Backend validation**: Type checking and business rule enforcement
- **Database constraints**: Final data integrity enforcement layer

---

## 🚀 DEPLOYMENT CONSIDERATIONS

### **Inference Optimization Questions**

Based on your technical notes, key considerations for production deployment:

1. **Vector Storage vs. Recalculation**:
   - **Current approach**: Recalculate embeddings each time (50-200ms)
   - **Alternative**: Store vectors (3KB per note, 4KB per recollection)
   - **Recommendation**: Keep recalculation for consistency and simplicity

2. **SimCSE Vectorization Timing**:
   - **Question**: When does SimCSE vectorize? During comparison or pre-stored?
   - **Answer**: Real-time during comparison for fresh, consistent results
   - **Benefit**: Always uses current model state, no storage overhead

3. **Computational Intensity**:
   - **Current**: Every similarity check requires full model inference
   - **Performance**: 50-200ms acceptable for educational use case
   - **Scaling**: Linear with number of comparisons

### **Performance Optimization Strategies**

```sql
-- Optimized session query with performance metrics
SELECT 
  s.id,
  s.similarity,
  s.stars,
  s.wpm,
  s.duration_secs,
  s.hints_used,
  s.created_at,
  n.title,
  n.word_count as original_word_count,
  s.word_count as recall_word_count,
  ROUND((s.word_count::float / n.word_count), 3) as completeness_ratio
FROM sessions s
JOIN notes n ON s.note_id = n.id
WHERE s.user_id = $1
ORDER BY s.created_at DESC
LIMIT 50;
```

### **Educational Analytics Queries**

```sql
-- Learning progression analysis
SELECT 
  note_id,
  COUNT(*) as attempt_count,
  AVG(similarity) as avg_similarity,
  MAX(similarity) as best_similarity,
  AVG(wpm) as avg_speed,
  AVG(stars) as avg_mastery,
  DATE_TRUNC('week', created_at) as week
FROM sessions
WHERE user_id = $1
GROUP BY note_id, week
ORDER BY week, note_id;
```

```sql
-- Difficulty analysis by content type
SELECT 
  n.title,
  n.word_count,
  COUNT(s.id) as session_count,
  AVG(s.similarity) as avg_difficulty_score,
  AVG(s.duration_secs) as avg_time_required,
  CASE 
    WHEN AVG(s.similarity) >= 0.7 THEN 'Easy'
    WHEN AVG(s.similarity) >= 0.5 THEN 'Medium'
    ELSE 'Difficult'
  END as difficulty_category
FROM notes n
LEFT JOIN sessions s ON n.id = s.note_id
WHERE n.user_id = $1
GROUP BY n.id, n.title, n.word_count
ORDER BY avg_difficulty_score DESC;
```

This schema design supports **scalable performance tracking** with **referential integrity** and **efficient querying** for your AI-powered learning system.