import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 20))
ax.set_xlim(0, 10)
ax.set_ylim(0, 50)
ax.axis('off')

# Define colors for different types of nodes
colors = {
    'start_end': '#90EE90',      # Light green
    'process': '#87CEEB',        # Sky blue
    'decision': '#FFB6C1',       # Light pink
    'data': '#DDA0DD',           # Plum
    'system': '#F0E68C'          # Khaki
}

def create_box(x, y, width, height, text, color, text_size=8):
    """Create a box with text"""
    box = FancyBboxPatch((x, y), width, height, 
                         boxstyle="round,pad=0.1", 
                         facecolor=color, 
                         edgecolor='black', 
                         linewidth=1.5)
    ax.add_patch(box)
    
    # Add text
    ax.text(x + width/2, y + height/2, text, 
            ha='center', va='center', fontsize=text_size, 
            weight='bold', wrap=True)

def create_diamond(x, y, size, text, color):
    """Create a diamond shape for decisions"""
    diamond = mpatches.RegularPolygon((x, y), 4, radius=size, 
                                     orientation=np.pi/4,
                                     facecolor=color, 
                                     edgecolor='black', 
                                     linewidth=1.5)
    ax.add_patch(diamond)
    ax.text(x, y, text, ha='center', va='center', 
            fontsize=7, weight='bold')

def draw_arrow(x1, y1, x2, y2, text=''):
    """Draw arrow between nodes"""
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='black'))
    if text:
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        ax.text(mid_x + 0.2, mid_y, text, fontsize=6, 
                bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

# Title
ax.text(5, 49, 'Consol Educational Assessment System\nComprehensive User Flow', 
        ha='center', va='center', fontsize=14, weight='bold')

# Start node
create_box(4, 47, 2, 1, 'User Accesses\nConsol System', colors['start_end'])

# Authentication Phase
create_box(4, 45, 2, 1, 'Authentication\nVerification', colors['system'])
create_diamond(5, 43, 0.8, 'User\nLogged In?', colors['decision'])
create_box(1, 41, 1.8, 1, 'Display Login\nInterface', colors['process'])
create_diamond(2, 39, 0.8, 'Has\nAccount?', colors['decision'])
create_box(0.2, 37, 1.6, 1, 'User\nRegistration', colors['process'])
create_box(3, 37, 1.5, 1, 'Login Form\nSubmission', colors['process'])

# Main Dashboard
create_box(4, 35, 2, 1, 'Load Main\nDashboard', colors['process'])
create_box(7, 35, 2, 1, 'Fetch User Profile\n& History', colors['data'])

# User Action Selection
create_diamond(5, 33, 1, 'User Action\nSelection', colors['decision'])

# Note Creation Branch (Left side)
create_box(0.5, 31, 1.8, 1, 'Create New\nNote', colors['process'])
create_box(0.5, 29, 1.8, 1, 'Text Input\nInterface', colors['process'])
create_box(0.5, 27, 1.8, 1, 'Text Content\nValidation', colors['data'])
create_diamond(1.4, 25, 0.8, 'Text\nValid?', colors['decision'])
create_box(0.2, 23, 1.3, 1, 'Error\nMessage', colors['process'])
create_box(0.5, 21, 1.8, 1, 'SimCSE Embedding\nGeneration', colors['data'])
create_box(0.5, 19, 1.8, 1, 'Store Note in\nDatabase', colors['data'])

# Practice Session Branch (Right side)
create_box(7.2, 31, 1.8, 1, 'Begin Practice\nSession', colors['process'])
create_box(7.2, 29, 1.8, 1, 'Select Note for\nPractice', colors['process'])
create_box(7.2, 27, 1.8, 1, 'Display Original\nText Prompt', colors['process'])
create_box(7.2, 25, 1.8, 1, 'Start Session\nTimer', colors['system'])
create_box(7.2, 23, 1.8, 1, 'User Recall\nInput', colors['process'])
create_diamond(8.1, 21, 0.8, 'Session\nComplete?', colors['decision'])
create_box(6.5, 19, 1.2, 0.8, 'Hint\nSystem', colors['process'])
create_box(7.2, 17, 1.8, 1, 'Stop Timer &\nCalculate Metrics', colors['data'])
create_box(7.2, 15, 1.8, 1, 'SimCSE Similarity\nCalculation', colors['data'])
create_box(7.2, 13, 1.8, 1, 'Performance\nEvaluation', colors['data'])
create_box(7.2, 11, 1.8, 1, 'Star Rating\nAssignment', colors['data'])
create_box(7.2, 9, 1.8, 1, 'Display Results\n& Feedback', colors['process'])
create_diamond(8.1, 7, 0.8, 'Continue\nPractice?', colors['decision'])

# Note Management Branch (Center)
create_box(4, 31, 2, 1, 'Manage Existing\nNotes', colors['process'])
create_box(4, 29, 2, 1, 'Display Notes\nList', colors['process'])
create_diamond(5, 27, 0.8, 'Note\nAction?', colors['decision'])
create_box(3.2, 25, 1.3, 1, 'Edit\nNote', colors['process'])
create_box(5.5, 25, 1.3, 1, 'Delete\nNote', colors['process'])

# Analytics Branch
create_box(4, 17, 2, 1, 'View Progress\nAnalytics', colors['process'])
create_box(4, 15, 2, 1, 'Load Analytics\nDashboard', colors['process'])
create_box(1.5, 13, 1.8, 1, 'Calculate Learning\nTrends', colors['data'])
create_box(6.7, 13, 1.8, 1, 'Generate Progress\nCharts', colors['data'])
create_box(4, 11, 2, 1, 'Display Detailed\nAnalysis', colors['process'])
create_diamond(5, 9, 0.8, 'Export\nData?', colors['decision'])
create_box(3.2, 7, 1.3, 1, 'Generate PDF\nReport', colors['process'])

# Session Storage and Return
create_box(7.2, 5, 1.8, 1, 'Store Session\nin Database', colors['data'])
create_box(4, 3, 2, 1, 'Return to\nDashboard', colors['process'])

# End
create_box(4, 1, 2, 1, 'Session\nComplete', colors['start_end'])

# Draw arrows for main flow
draw_arrow(5, 47, 5, 46)  # Start to Auth
draw_arrow(5, 45, 5, 43.8)  # Auth to Decision
draw_arrow(4.2, 43, 1.9, 42)  # Decision to Login (No)
draw_arrow(5.8, 43, 5, 36)  # Decision to Dashboard (Yes)
draw_arrow(1.9, 41, 2, 39.8)  # Login to Has Account
draw_arrow(1.2, 39, 1.1, 38)  # Has Account to Register (No)
draw_arrow(2.8, 39, 3.7, 38)  # Has Account to Login Form (Yes)
draw_arrow(1.1, 37, 5, 36)  # Register to Dashboard
draw_arrow(3.8, 37, 5, 36)  # Login Form to Dashboard

# Dashboard to data fetch
draw_arrow(6, 35.5, 7, 35.5)  # Dashboard to Data Fetch
draw_arrow(5, 35, 5, 34)  # Dashboard to User Action

# User Action branches
draw_arrow(4, 33, 1.4, 32)  # To Create Note
draw_arrow(5, 32, 5, 32)  # To Manage Notes
draw_arrow(6, 33, 8.1, 32)  # To Practice

# Note Creation flow
draw_arrow(1.4, 31, 1.4, 30)
draw_arrow(1.4, 29, 1.4, 28)
draw_arrow(1.4, 27, 1.4, 25.8)
draw_arrow(0.6, 25, 0.8, 24)  # Error path
draw_arrow(2.2, 25, 1.4, 22)  # Valid path
draw_arrow(1.4, 21, 1.4, 20)
draw_arrow(1.4, 19, 5, 4)  # Return to dashboard

# Practice Session flow
draw_arrow(8.1, 31, 8.1, 30)
draw_arrow(8.1, 29, 8.1, 28)
draw_arrow(8.1, 27, 8.1, 26)
draw_arrow(8.1, 25, 8.1, 24)
draw_arrow(8.1, 23, 8.1, 21.8)
draw_arrow(7.3, 21, 7.1, 19.8, 'Hint')  # Hint path
draw_arrow(8.9, 21, 8.1, 18)  # Complete path
draw_arrow(8.1, 17, 8.1, 16)
draw_arrow(8.1, 15, 8.1, 14)
draw_arrow(8.1, 13, 8.1, 12)
draw_arrow(8.1, 11, 8.1, 10)
draw_arrow(8.1, 9, 8.1, 7.8)
draw_arrow(7.3, 7, 8.1, 24, 'Yes')  # Continue practice
draw_arrow(8.9, 7, 8.1, 6)  # End session
draw_arrow(8.1, 5, 5, 4)  # Return to dashboard

# Note Management flow
draw_arrow(5, 31, 5, 30)
draw_arrow(5, 29, 5, 27.8)
draw_arrow(4.2, 27, 3.9, 26)  # Edit
draw_arrow(5.8, 27, 6.1, 26)  # Delete
draw_arrow(3.9, 25, 5, 4)  # Edit return
draw_arrow(6.1, 25, 5, 4)  # Delete return

# Analytics flow
draw_arrow(5, 32.2, 5, 18)  # From User Action to Analytics
draw_arrow(5, 17, 5, 16)
draw_arrow(5, 15, 2.4, 14)  # To trends
draw_arrow(5, 15, 7.6, 14)  # To charts
draw_arrow(2.4, 13, 5, 12)  # Trends to analysis
draw_arrow(7.6, 13, 5, 12)  # Charts to analysis
draw_arrow(5, 11, 5, 9.8)
draw_arrow(4.2, 9, 3.9, 8)  # Export Yes
draw_arrow(5.8, 9, 5, 4)  # Export No
draw_arrow(3.9, 7, 5, 4)  # Report return

# Add labels for decision paths
ax.text(3.5, 42.5, 'No', fontsize=8, weight='bold')
ax.text(5.5, 42.5, 'Yes', fontsize=8, weight='bold')
ax.text(1.5, 38.5, 'No', fontsize=8, weight='bold')
ax.text(2.5, 38.5, 'Yes', fontsize=8, weight='bold')
ax.text(3.2, 32.5, 'Create', fontsize=8, weight='bold')
ax.text(5, 32.2, 'Manage', fontsize=8, weight='bold')
ax.text(6.8, 32.5, 'Practice', fontsize=8, weight='bold')

# Create legend
legend_elements = [
    mpatches.Patch(color=colors['start_end'], label='Start/End'),
    mpatches.Patch(color=colors['process'], label='Process'),
    mpatches.Patch(color=colors['decision'], label='Decision'),
    mpatches.Patch(color=colors['data'], label='Data/Storage'),
    mpatches.Patch(color=colors['system'], label='System Action')
]

ax.legend(handles=legend_elements, loc='lower right', bbox_to_anchor=(0.98, 0.02))

plt.tight_layout()
plt.savefig('C:/Users/ASUS LAPTOP/Downloads/Thesis/FinalPaper_Latex/latex_cs_thesis/images/comprehensive_user_flow.png', 
            dpi=300, bbox_inches='tight')
plt.show()

print("Comprehensive user flow diagram has been created and saved!")