import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def create_multipage_flow():
    """Create multiple separate diagrams for each phase"""
    
    # Define colors
    colors = {
        'start_end': '#90EE90',      # Light green
        'process': '#87CEEB',        # Sky blue
        'decision': '#FFB6C1',       # Light pink
        'data': '#DDA0DD',           # Plum
        'system': '#F0E68C'          # Khaki
    }

    def create_box(ax, x, y, width, height, text, color, text_size=10):
        """Create a box with text"""
        box = FancyBboxPatch((x, y), width, height, 
                             boxstyle="round,pad=0.1", 
                             facecolor=color, 
                             edgecolor='black', 
                             linewidth=1.5)
        ax.add_patch(box)
        ax.text(x + width/2, y + height/2, text, 
                ha='center', va='center', fontsize=text_size, 
                weight='bold', wrap=True)

    def create_diamond(ax, x, y, size, text, color, text_size=9):
        """Create a diamond shape for decisions"""
        diamond = mpatches.RegularPolygon((x, y), 4, radius=size, 
                                         orientation=np.pi/4,
                                         facecolor=color, 
                                         edgecolor='black', 
                                         linewidth=1.5)
        ax.add_patch(diamond)
        ax.text(x, y, text, ha='center', va='center', 
                fontsize=text_size, weight='bold')

    def draw_arrow(ax, x1, y1, x2, y2, text=''):
        """Draw arrow between nodes"""
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', lw=2, color='black'))
        if text:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            ax.text(mid_x + 0.3, mid_y, text, fontsize=9, weight='bold',
                    bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

    # Page 1: Authentication and Dashboard Setup
    fig1, ax1 = plt.subplots(figsize=(10, 12))
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 12)
    ax1.axis('off')
    
    # Title
    ax1.text(5, 11.5, 'Consol User Flow - Phase 1: Authentication & Dashboard Setup', 
            ha='center', va='center', fontsize=14, weight='bold')
    
    # Authentication flow
    create_box(ax1, 4, 10, 2, 0.8, 'User Accesses\nConsol System', colors['start_end'])
    create_box(ax1, 4, 8.8, 2, 0.8, 'Authentication\nVerification', colors['system'])
    create_diamond(ax1, 5, 7.5, 0.6, 'User\nLogged In?', colors['decision'])
    
    # Login branch
    create_box(ax1, 1, 6, 2, 0.8, 'Display Login\nInterface', colors['process'])
    create_diamond(ax1, 2, 4.8, 0.6, 'Has\nAccount?', colors['decision'])
    create_box(ax1, 0.5, 3.5, 1.5, 0.8, 'User\nRegistration', colors['process'])
    create_box(ax1, 2.5, 3.5, 1.5, 0.8, 'Login Form\nSubmission', colors['process'])
    
    # Dashboard
    create_box(ax1, 4, 5.5, 2, 0.8, 'Load Main\nDashboard', colors['process'])
    create_box(ax1, 7, 5.5, 2.5, 0.8, 'Fetch User Profile\n& History Data', colors['data'])
    create_box(ax1, 4, 4, 2, 0.8, 'Display User\nInterface', colors['process'])
    
    # Connector to next page
    create_box(ax1, 4, 2.5, 2, 0.8, 'Continue to\nAction Selection', colors['system'])
    
    # Draw arrows
    draw_arrow(ax1, 5, 10, 5, 9.6)
    draw_arrow(ax1, 5, 8.8, 5, 8.1)
    draw_arrow(ax1, 4.4, 7.5, 2, 6.8, 'No')
    draw_arrow(ax1, 5.6, 7.5, 5, 6.3, 'Yes')
    draw_arrow(ax1, 2, 6, 2, 5.4)
    draw_arrow(ax1, 1.4, 4.8, 1.25, 4.3, 'No')
    draw_arrow(ax1, 2.6, 4.8, 3.25, 4.3, 'Yes')
    draw_arrow(ax1, 1.25, 3.5, 5, 4.8)
    draw_arrow(ax1, 3.25, 3.5, 5, 4.8)
    draw_arrow(ax1, 6, 5.9, 7, 5.9)
    draw_arrow(ax1, 5, 5.5, 5, 4.8)
    draw_arrow(ax1, 5, 4, 5, 3.3)
    
    plt.tight_layout()
    plt.savefig('C:/Users/ASUS LAPTOP/Downloads/Thesis/FinalPaper_Latex/latex_cs_thesis/images/userflow_page1.png', 
                dpi=300, bbox_inches='tight')
    plt.close()

    # Page 2: Note Management
    fig2, ax2 = plt.subplots(figsize=(10, 12))
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 12)
    ax2.axis('off')
    
    ax2.text(5, 11.5, 'Consol User Flow - Phase 2: Note Management', 
            ha='center', va='center', fontsize=14, weight='bold')
    
    # From previous page
    create_box(ax2, 4, 10.5, 2, 0.6, 'From Dashboard', colors['system'])
    
    # Action selection
    create_diamond(ax2, 5, 9.5, 0.8, 'User Action\nSelection', colors['decision'])
    
    # Note creation branch (left)
    create_box(ax2, 0.5, 8, 2, 0.8, 'Create New\nNote', colors['process'])
    create_box(ax2, 0.5, 7, 2, 0.8, 'Text Input\nInterface', colors['process'])
    create_box(ax2, 0.5, 6, 2, 0.8, 'Content\nValidation', colors['data'])
    create_diamond(ax2, 1.5, 4.8, 0.6, 'Text\nValid?', colors['decision'])
    create_box(ax2, 0.2, 3.5, 1.6, 0.8, 'Show Error\nMessage', colors['process'])
    create_box(ax2, 0.5, 2.5, 2, 0.8, 'SimCSE Embedding\nGeneration', colors['data'])
    create_box(ax2, 0.5, 1.5, 2, 0.8, 'Store in\nDatabase', colors['data'])
    
    # Note management branch (right)
    create_box(ax2, 7, 8, 2, 0.8, 'Manage\nNotes', colors['process'])
    create_box(ax2, 7, 7, 2, 0.8, 'Display Notes\nList', colors['process'])
    create_diamond(ax2, 8, 5.8, 0.6, 'Note\nAction?', colors['decision'])
    create_box(ax2, 6.5, 4.5, 1.5, 0.8, 'Edit\nNote', colors['process'])
    create_box(ax2, 8, 4.5, 1.5, 0.8, 'Delete\nNote', colors['process'])
    create_box(ax2, 7, 3, 2, 0.8, 'Update\nDatabase', colors['data'])
    
    # Continue to next phase
    create_box(ax2, 4, 0.5, 2, 0.8, 'Continue to Practice\nor Analytics', colors['system'])
    
    # Draw arrows for note creation
    draw_arrow(ax2, 4.2, 9.5, 1.5, 8.8, 'Create')
    draw_arrow(ax2, 1.5, 8, 1.5, 7.8)
    draw_arrow(ax2, 1.5, 7, 1.5, 6.8)
    draw_arrow(ax2, 1.5, 6, 1.5, 5.4)
    draw_arrow(ax2, 0.9, 4.8, 1, 4.3, 'No')
    draw_arrow(ax2, 2.1, 4.8, 1.5, 3.3, 'Yes')
    draw_arrow(ax2, 1, 3.5, 1.5, 7)  # Error back to input
    draw_arrow(ax2, 1.5, 2.5, 1.5, 2.3)
    draw_arrow(ax2, 1.5, 1.5, 5, 1.3)  # To continue
    
    # Draw arrows for note management
    draw_arrow(ax2, 5.8, 9.5, 8, 8.8, 'Manage')
    draw_arrow(ax2, 8, 8, 8, 7.8)
    draw_arrow(ax2, 8, 7, 8, 6.4)
    draw_arrow(ax2, 7.4, 5.8, 7.25, 5.3, 'Edit')
    draw_arrow(ax2, 8.6, 5.8, 8.75, 5.3, 'Delete')
    draw_arrow(ax2, 7.25, 4.5, 8, 3.8)
    draw_arrow(ax2, 8.75, 4.5, 8, 3.8)
    draw_arrow(ax2, 8, 3, 5, 1.3)  # To continue
    
    plt.tight_layout()
    plt.savefig('C:/Users/ASUS LAPTOP/Downloads/Thesis/FinalPaper_Latex/latex_cs_thesis/images/userflow_page2.png', 
                dpi=300, bbox_inches='tight')
    plt.close()

    # Page 3: Practice Session
    fig3, ax3 = plt.subplots(figsize=(10, 12))
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 12)
    ax3.axis('off')
    
    ax3.text(5, 11.5, 'Consol User Flow - Phase 3: Practice Session', 
            ha='center', va='center', fontsize=14, weight='bold')
    
    # From previous page
    create_box(ax3, 4, 10.5, 2, 0.6, 'Start Practice\nSession', colors['system'])
    
    # Practice flow
    create_box(ax3, 4, 9.5, 2, 0.8, 'Select Note\nfor Practice', colors['process'])
    create_box(ax3, 4, 8.5, 2, 0.8, 'Display Original\nText Prompt', colors['process'])
    create_box(ax3, 4, 7.5, 2, 0.8, 'Start Session\nTimer', colors['system'])
    create_box(ax3, 4, 6.5, 2, 0.8, 'User Types\nRecall Response', colors['process'])
    
    # Session decision
    create_diamond(ax3, 5, 5.3, 0.8, 'Session\nComplete?', colors['decision'])
    
    # Hint system (left branch)
    create_box(ax3, 1, 4.5, 2, 0.8, 'Provide Hint\nto User', colors['process'])
    create_box(ax3, 1, 3.5, 2, 0.8, 'Increment Hint\nCounter', colors['data'])
    
    # Assessment processing (right branch)
    create_box(ax3, 7, 4.5, 2, 0.8, 'Stop Timer &\nCalculate Duration', colors['system'])
    create_box(ax3, 7, 3.5, 2, 0.8, 'SimCSE Similarity\nCalculation', colors['data'])
    create_box(ax3, 7, 2.5, 2, 0.8, 'Performance\nEvaluation', colors['data'])
    create_box(ax3, 7, 1.5, 2, 0.8, 'Generate Star\nRating (0-3)', colors['data'])
    
    # Results and continuation
    create_box(ax3, 4, 0.5, 2, 0.8, 'Display Results\n& Feedback', colors['process'])
    
    # Draw arrows
    draw_arrow(ax3, 5, 10.5, 5, 10.3)
    draw_arrow(ax3, 5, 9.5, 5, 9.3)
    draw_arrow(ax3, 5, 8.5, 5, 8.3)
    draw_arrow(ax3, 5, 7.5, 5, 7.3)
    draw_arrow(ax3, 5, 6.5, 5, 6.1)
    draw_arrow(ax3, 4.2, 5.3, 2, 5.3, 'Need Hint')
    draw_arrow(ax3, 5.8, 5.3, 8, 5.3, 'Complete')
    draw_arrow(ax3, 2, 4.5, 2, 4.3)
    draw_arrow(ax3, 2, 3.5, 5, 6.5)  # Back to input
    draw_arrow(ax3, 8, 4.5, 8, 4.3)
    draw_arrow(ax3, 8, 3.5, 8, 3.3)
    draw_arrow(ax3, 8, 2.5, 8, 2.3)
    draw_arrow(ax3, 8, 1.5, 5, 1.3)
    
    plt.tight_layout()
    plt.savefig('C:/Users/ASUS LAPTOP/Downloads/Thesis/FinalPaper_Latex/latex_cs_thesis/images/userflow_page3.png', 
                dpi=300, bbox_inches='tight')
    plt.close()

    # Page 4: Analytics and Completion
    fig4, ax4 = plt.subplots(figsize=(10, 12))
    ax4.set_xlim(0, 10)
    ax4.set_ylim(0, 12)
    ax4.axis('off')
    
    ax4.text(5, 11.5, 'Consol User Flow - Phase 4: Analytics & Session Management', 
            ha='center', va='center', fontsize=14, weight='bold')
    
    # Session continuation decision
    create_diamond(ax4, 5, 10.5, 0.8, 'Continue\nPractice?', colors['decision'])
    
    # Continue practice branch
    create_box(ax4, 1, 9.5, 2, 0.8, 'Select Different\nNote', colors['process'])
    create_box(ax4, 1, 8.5, 2, 0.8, 'Return to\nPractice Flow', colors['system'])
    
    # Analytics branch
    create_box(ax4, 7, 9.5, 2, 0.8, 'View Progress\nAnalytics', colors['process'])
    create_box(ax4, 7, 8.5, 2, 0.8, 'Load Analytics\nDashboard', colors['process'])
    create_box(ax4, 5.5, 7.5, 1.8, 0.8, 'Calculate Learning\nTrends', colors['data'])
    create_box(ax4, 7.7, 7.5, 1.8, 0.8, 'Generate Progress\nCharts', colors['data'])
    create_box(ax4, 7, 6.5, 2, 0.8, 'Display Detailed\nAnalysis', colors['process'])
    
    # Export functionality
    create_diamond(ax4, 8, 5.3, 0.6, 'Export\nData?', colors['decision'])
    create_box(ax4, 6.5, 4, 1.8, 0.8, 'Generate PDF\nReport', colors['process'])
    
    # Session storage and completion
    create_box(ax4, 4, 3, 2, 0.8, 'Store Session\nin Database', colors['data'])
    create_box(ax4, 4, 2, 2, 0.8, 'Update User\nProgress', colors['data'])
    create_box(ax4, 4, 1, 2, 0.8, 'Return to Main\nDashboard', colors['process'])
    create_box(ax4, 4, 0.2, 2, 0.6, 'Session Complete', colors['start_end'])
    
    # Draw arrows
    draw_arrow(ax4, 4.2, 10.5, 2, 10.3, 'Yes')
    draw_arrow(ax4, 5.8, 10.5, 8, 10.3, 'No')
    draw_arrow(ax4, 2, 9.5, 2, 9.3)
    draw_arrow(ax4, 2, 8.5, 5, 10.5)  # Back to continue decision
    draw_arrow(ax4, 8, 9.5, 8, 9.3)
    draw_arrow(ax4, 8, 8.5, 6.4, 8.3)
    draw_arrow(ax4, 8, 8.5, 8.6, 8.3)
    draw_arrow(ax4, 6.4, 7.5, 8, 7.3)
    draw_arrow(ax4, 8.6, 7.5, 8, 7.3)
    draw_arrow(ax4, 8, 6.5, 8, 5.9)
    draw_arrow(ax4, 7.4, 5.3, 7.4, 4.8, 'Yes')
    draw_arrow(ax4, 8.6, 5.3, 5, 3.8, 'No')
    draw_arrow(ax4, 7.4, 4, 5, 3.8)
    draw_arrow(ax4, 5, 3, 5, 2.8)
    draw_arrow(ax4, 5, 2, 5, 1.8)
    draw_arrow(ax4, 5, 1, 5, 0.8)
    
    plt.tight_layout()
    plt.savefig('C:/Users/ASUS LAPTOP/Downloads/Thesis/FinalPaper_Latex/latex_cs_thesis/images/userflow_page4.png', 
                dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Multi-page user flow diagrams created successfully!")
    print("Created files:")
    print("- userflow_page1.png (Authentication & Dashboard)")
    print("- userflow_page2.png (Note Management)")
    print("- userflow_page3.png (Practice Session)")
    print("- userflow_page4.png (Analytics & Completion)")

if __name__ == "__main__":
    create_multipage_flow()