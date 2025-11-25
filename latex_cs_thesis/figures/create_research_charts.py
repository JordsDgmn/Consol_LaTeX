import matplotlib.pyplot as plt
import numpy as np

def create_research_results_charts():
    """Create the research results charts from the thesis data"""
    
    # Set style for academic presentation
    plt.style.use('default')
    plt.rcParams['font.size'] = 12
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['axes.linewidth'] = 1.2
    plt.rcParams['grid.alpha'] = 0.3
    
    # Data from the charts
    participants = ['Elleonae', 'Jeg', 'Seraniah', 'Zinoe', 'Zyrah']
    
    # Mean scores data
    simcse_scores = [78, 76, 77, 76, 79]
    chatgpt_scores = [53, 68, 52, 43, 61]
    teacher_scores = [71, 74, 72, 59, 67]
    
    # Deviation data (absolute difference from teacher)
    simcse_deviation = [9.5, 5.2, 8.5, 16.8, 7.6]
    chatgpt_deviation = [18.1, 8.9, 23.2, 17.1, 14.8]
    
    # Chart 1: Mean Scores per Participant and Scorer
    fig1, ax1 = plt.subplots(figsize=(12, 8))
    
    x = np.arange(len(participants))
    width = 0.25
    
    bars1 = ax1.bar(x - width, simcse_scores, width, label='SimCSE', 
                   color='#FFA500', edgecolor='black', linewidth=0.8)
    bars2 = ax1.bar(x, chatgpt_scores, width, label='ChatGPT', 
                   color='#4A90E2', edgecolor='black', linewidth=0.8)
    bars3 = ax1.bar(x + width, teacher_scores, width, label='Teacher', 
                   color='#50C878', edgecolor='black', linewidth=0.8)
    
    ax1.set_xlabel('Participants', fontweight='bold')
    ax1.set_ylabel('Mean Score Across All Topics & Days', fontweight='bold')
    ax1.set_title('Mean Scores per Participant and Scorer', fontweight='bold', pad=20)
    ax1.set_xticks(x)
    ax1.set_xticklabels(participants)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 85)
    
    # Add value labels on bars
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
                    f'{height:.0f}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('mean_scores_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Chart 2: Deviation of AI Scorers from Teacher
    fig2, ax2 = plt.subplots(figsize=(12, 8))
    
    x = np.arange(len(participants))
    width = 0.35
    
    bars1 = ax2.bar(x - width/2, simcse_deviation, width, 
                   label='|SimCSE - Teacher|', color='#FFA500', 
                   edgecolor='black', linewidth=0.8)
    bars2 = ax2.bar(x + width/2, chatgpt_deviation, width, 
                   label='|ChatGPT - Teacher|', color='#4A90E2', 
                   edgecolor='black', linewidth=0.8)
    
    ax2.set_xlabel('Participants', fontweight='bold')
    ax2.set_ylabel('Mean Absolute Difference (Score Points)', fontweight='bold')
    ax2.set_title('Deviation of AI Scorers from Teacher per Participant', fontweight='bold', pad=20)
    ax2.set_xticks(x)
    ax2.set_xticklabels(participants)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(0, 25)
    
    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                    f'{height:.1f}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('ai_deviation_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("✅ Research results charts created:")
    print("   - mean_scores_comparison.png")
    print("   - ai_deviation_comparison.png")

if __name__ == "__main__":
    create_research_results_charts()