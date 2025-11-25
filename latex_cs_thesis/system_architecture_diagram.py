import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch, Arrow, Rectangle
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(16, 12))
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.axis('off')

# Define colors - more professional palette
user_color = '#E8F4FD'      # Light blue for user layer
frontend_color = '#FFF3E0'   # Light orange for frontend
api_color = '#F3E5F5'       # Light purple for API layer  
ai_color = '#E8F5E8'        # Light green for AI processing
data_color = '#FFEBEE'      # Light red for data layer
external_color = '#F5F5F5'  # Light gray for external

# Title
ax.text(8, 11.5, 'Consol System Architecture', fontsize=18, fontweight='bold', ha='center')

# User Layer
user_box = FancyBboxPatch((1, 9.5), 14, 1.2, 
                         boxstyle="round,pad=0.1", 
                         facecolor=user_color, 
                         edgecolor='#1976D2', linewidth=2)
ax.add_patch(user_box)
ax.text(8, 10.1, 'User Interface Layer', fontsize=14, fontweight='bold', ha='center')
ax.text(3, 9.75, '📝 Note Creation', fontsize=10, ha='center')
ax.text(8, 9.75, '🎯 Practice Sessions', fontsize=10, ha='center')
ax.text(13, 9.75, '📊 Performance Analytics', fontsize=10, ha='center')

# Frontend Layer  
frontend_box = FancyBboxPatch((1, 7.8), 14, 1.2, 
                             boxstyle="round,pad=0.1", 
                             facecolor=frontend_color, 
                             edgecolor='#F57C00', linewidth=2)
ax.add_patch(frontend_box)
ax.text(8, 8.6, 'Frontend Layer - React.js/Next.js 15', fontsize=14, fontweight='bold', ha='center')

# Frontend components
frontend_components = [
    ('Dashboard', 2.5, 8.1),
    ('Note Management', 5.5, 8.1),
    ('Session Interface', 8.5, 8.1),
    ('Analytics Dashboard', 11.5, 8.1),
    ('User Profile', 13.5, 8.1)
]

for comp, x, y in frontend_components:
    comp_box = FancyBboxPatch((x-0.8, y-0.15), 1.6, 0.3, 
                             boxstyle="round,pad=0.03", 
                             facecolor='white', 
                             edgecolor='#F57C00', linewidth=1)
    ax.add_patch(comp_box)
    ax.text(x, y, comp, fontsize=8, ha='center')

# API Layer
api_box = FancyBboxPatch((1, 6.1), 14, 1.2, 
                        boxstyle="round,pad=0.1", 
                        facecolor=api_color, 
                        edgecolor='#7B1FA2', linewidth=2)
ax.add_patch(api_box)
ax.text(8, 6.9, 'API Layer - Next.js API Routes', fontsize=14, fontweight='bold', ha='center')

# API endpoints
api_components = [
    ('/api/users', 2.5, 6.4),
    ('/api/notes', 5, 6.4),
    ('/api/sessions', 7.5, 6.4),
    ('/api/similarity', 10, 6.4),
    ('/api/analytics', 12.5, 6.4)
]

for comp, x, y in api_components:
    comp_box = FancyBboxPatch((x-0.7, y-0.15), 1.4, 0.3, 
                             boxstyle="round,pad=0.03", 
                             facecolor='white', 
                             edgecolor='#7B1FA2', linewidth=1)
    ax.add_patch(comp_box)
    ax.text(x, y, comp, fontsize=8, ha='center')

# Split AI and Data layers side by side
# AI Processing Layer (Left)
ai_box = FancyBboxPatch((1, 3.5), 7, 2.2, 
                       boxstyle="round,pad=0.1", 
                       facecolor=ai_color, 
                       edgecolor='#388E3C', linewidth=2)
ax.add_patch(ai_box)
ax.text(4.5, 5.4, 'AI Processing Layer', fontsize=14, fontweight='bold', ha='center')
ax.text(4.5, 5.1, 'Flask API Server (Port 5000)', fontsize=11, ha='center', style='italic')

# AI components
ai_components = [
    ('SimCSE Model\n(princeton-nlp)', 2.5, 4.5),
    ('BERT Encoder\n(base-uncased)', 4.5, 4.5),
    ('Cosine Similarity\nCalculation', 6.5, 4.5),
    ('Embedding\nGeneration', 3.5, 3.9)
]

for comp, x, y in ai_components:
    ai_comp_box = FancyBboxPatch((x-0.7, y-0.25), 1.4, 0.5, 
                                boxstyle="round,pad=0.03", 
                                facecolor='white', 
                                edgecolor='#388E3C', linewidth=1)
    ax.add_patch(ai_comp_box)
    ax.text(x, y, comp, fontsize=8, ha='center')

# Data Layer (Right)
data_box = FancyBboxPatch((8.5, 3.5), 6.5, 2.2, 
                         boxstyle="round,pad=0.1", 
                         facecolor=data_color, 
                         edgecolor='#D32F2F', linewidth=2)
ax.add_patch(data_box)
ax.text(11.75, 5.4, 'Data Persistence Layer', fontsize=14, fontweight='bold', ha='center')
ax.text(11.75, 5.1, 'PostgreSQL Database (Direct SQL)', fontsize=11, ha='center', style='italic')

# Database components
db_components = [
    ('Users Table', 9.5, 4.5),
    ('Notes Table', 11.75, 4.5),
    ('Sessions Table', 14, 4.5),
    ('pg Pool\nConnections', 11.75, 3.9)
]

for comp, x, y in db_components:
    db_comp_box = FancyBboxPatch((x-0.6, y-0.25), 1.2, 0.5, 
                                boxstyle="round,pad=0.03", 
                                facecolor='white', 
                                edgecolor='#D32F2F', linewidth=1)
    ax.add_patch(db_comp_box)
    ax.text(x, y, comp, fontsize=8, ha='center')

# External Services Layer
ext_box = FancyBboxPatch((1, 1.5), 14, 1.2, 
                        boxstyle="round,pad=0.1", 
                        facecolor=external_color, 
                        edgecolor='#424242', linewidth=2)
ax.add_patch(ext_box)
ax.text(8, 2.3, 'External Services & Deployment', fontsize=14, fontweight='bold', ha='center')

# External service components
ext_components = [
    ('Cloudinary\n(Media Storage)', 3, 1.8),
    ('Vercel\n(Hosting)', 6, 1.8),
    ('Hugging Face\n(Model Hub)', 9, 1.8),
    ('NextAuth\n(Authentication)', 12, 1.8)
]

for comp, x, y in ext_components:
    ext_comp_box = FancyBboxPatch((x-0.8, y-0.25), 1.6, 0.5, 
                                 boxstyle="round,pad=0.03", 
                                 facecolor='white', 
                                 edgecolor='#424242', linewidth=1)
    ax.add_patch(ext_comp_box)
    ax.text(x, y, comp, fontsize=8, ha='center')

# Add connections/arrows with labels
# Frontend to API
arrow1 = ConnectionPatch((8, 7.8), (8, 7.3), "data", "data",
                        arrowstyle="<->", shrinkA=5, shrinkB=5, 
                        mutation_scale=20, fc="black", linewidth=2)
ax.add_artist(arrow1)
ax.text(8.5, 7.55, 'HTTP/REST', fontsize=9, rotation=90, ha='center', fontweight='bold')

# API to AI Processing
arrow2 = ConnectionPatch((7, 6.1), (5, 5.7), "data", "data",
                        arrowstyle="<->", shrinkA=5, shrinkB=5, 
                        mutation_scale=20, fc="green", linewidth=2)
ax.add_artist(arrow2)
ax.text(5.8, 5.8, 'Flask API\n(Port 5000)', fontsize=9, ha='center', fontweight='bold', color='green')

# API to Database
arrow3 = ConnectionPatch((9, 6.1), (11, 5.7), "data", "data",
                        arrowstyle="<->", shrinkA=5, shrinkB=5, 
                        mutation_scale=20, fc="red", linewidth=2)
ax.add_artist(arrow3)
ax.text(10.2, 5.8, 'Direct SQL\nQueries', fontsize=9, ha='center', fontweight='bold', color='red')

# API to External Services
arrow4 = ConnectionPatch((8, 6.1), (8, 2.7), "data", "data",
                        arrowstyle="<->", shrinkA=5, shrinkB=5, 
                        mutation_scale=20, fc="gray", linewidth=2)
ax.add_artist(arrow4)
ax.text(8.5, 4.4, 'External\nAPIs', fontsize=9, rotation=90, ha='center', fontweight='bold', color='gray')

# Add data flow indicators
ax.text(1.5, 0.8, '🔄 Data Flow:', fontsize=12, fontweight='bold')
ax.text(1.5, 0.5, '1. User creates note → API → PostgreSQL', fontsize=10)
ax.text(1.5, 0.2, '2. User practices → API → Flask (SimCSE) → Similarity score → PostgreSQL', fontsize=10)
ax.text(9, 0.5, '3. Performance analytics → API → PostgreSQL → Chart.js visualization', fontsize=10)
ax.text(9, 0.2, '4. Media uploads → Cloudinary → URL stored in PostgreSQL', fontsize=10)

# Add technology stack note
tech_box = FancyBboxPatch((1, 0.05), 14, 0.05, 
                         boxstyle="round,pad=0.02", 
                         facecolor='lightblue', 
                         edgecolor='blue', linewidth=1)
ax.add_patch(tech_box)

plt.tight_layout()
plt.savefig('consol_system_architecture.png', dpi=300, bbox_inches='tight')
plt.close()

print("Improved Consol system architecture diagram created and saved as 'consol_system_architecture.png'")