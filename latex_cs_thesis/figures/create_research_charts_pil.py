from PIL import Image, ImageDraw, ImageFont
import math

def create_research_charts_pil():
    """Create research results charts using PIL"""
    
    # Data from the charts
    participants = ['Elleonae', 'Jeg', 'Seraniah', 'Zinoe', 'Zyrah']
    
    # Mean scores data
    simcse_scores = [78, 76, 77, 76, 79]
    chatgpt_scores = [53, 68, 52, 43, 61]
    teacher_scores = [71, 74, 72, 59, 67]
    
    # Deviation data (absolute difference from teacher)
    simcse_deviation = [9.5, 5.2, 8.5, 16.8, 7.6]
    chatgpt_deviation = [18.1, 8.9, 23.2, 17.1, 14.8]
    
    # Load fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 18)
        label_font = ImageFont.truetype("arial.ttf", 14)
        text_font = ImageFont.truetype("arial.ttf", 12)
        small_font = ImageFont.truetype("arial.ttf", 10)
    except:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Colors
    colors = {
        'simcse': '#FFA500',     # Orange
        'chatgpt': '#4A90E2',    # Blue
        'teacher': '#50C878',    # Green
        'border': '#000000',
        'grid': '#CCCCCC',
        'text': '#000000',
        'background': '#FFFFFF'
    }
    
    def draw_bar_chart(data_sets, labels, colors_list, title, ylabel, filename, max_value=85):
        """Draw a bar chart"""
        width, height = 1200, 800
        img = Image.new('RGB', (width, height), colors['background'])
        draw = ImageDraw.Draw(img)
        
        # Chart area
        margin_left = 100
        margin_right = 100
        margin_top = 100
        margin_bottom = 150
        
        chart_width = width - margin_left - margin_right
        chart_height = height - margin_top - margin_bottom
        
        # Draw title
        title_bbox = draw.textbbox((0, 0), title, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = (width - title_width) // 2
        draw.text((title_x, 30), title, fill=colors['text'], font=title_font)
        
        # Draw grid lines and y-axis labels
        num_grid_lines = 9
        for i in range(num_grid_lines + 1):
            y = margin_top + (i * chart_height // num_grid_lines)
            value = max_value - (i * max_value // num_grid_lines)
            
            # Grid line
            draw.line([(margin_left, y), (margin_left + chart_width, y)], 
                     fill=colors['grid'], width=1)
            
            # Y-axis label
            label_text = str(int(value))
            label_bbox = draw.textbbox((0, 0), label_text, font=small_font)
            label_height = label_bbox[3] - label_bbox[1]
            draw.text((margin_left - 30, y - label_height // 2), label_text, 
                     fill=colors['text'], font=small_font)
        
        # Draw bars
        num_participants = len(participants)
        num_categories = len(data_sets)
        bar_group_width = chart_width // (num_participants + 1)
        bar_width = bar_group_width // (num_categories + 1)
        
        for i, participant in enumerate(participants):
            group_x = margin_left + (i + 1) * bar_group_width - (num_categories * bar_width) // 2
            
            for j, (data, color) in enumerate(zip(data_sets, colors_list)):
                value = data[i]
                bar_height = (value / max_value) * chart_height
                bar_x = group_x + j * bar_width
                bar_y = margin_top + chart_height - bar_height
                
                # Draw bar
                draw.rectangle([bar_x, bar_y, bar_x + bar_width - 5, margin_top + chart_height],
                              fill=color, outline=colors['border'], width=2)
                
                # Draw value label on top of bar
                value_text = str(int(value)) if isinstance(value, int) else f"{value:.1f}"
                value_bbox = draw.textbbox((0, 0), value_text, font=small_font)
                value_width = value_bbox[2] - value_bbox[0]
                value_x = bar_x + (bar_width - 5 - value_width) // 2
                draw.text((value_x, bar_y - 20), value_text, fill=colors['text'], font=small_font)
            
            # Draw participant label
            participant_bbox = draw.textbbox((0, 0), participant, font=text_font)
            participant_width = participant_bbox[2] - participant_bbox[0]
            participant_x = group_x + (num_categories * bar_width - 5 - participant_width) // 2
            draw.text((participant_x, margin_top + chart_height + 20), participant, 
                     fill=colors['text'], font=text_font)
        
        # Draw y-axis label
        ylabel_bbox = draw.textbbox((0, 0), ylabel, font=label_font)
        ylabel_height = ylabel_bbox[3] - ylabel_bbox[1]
        
        # Create rotated text image for y-axis label
        ylabel_img = Image.new('RGBA', (ylabel_height + 20, 200), (255, 255, 255, 0))
        ylabel_draw = ImageDraw.Draw(ylabel_img)
        ylabel_draw.text((10, 10), ylabel, fill=colors['text'], font=label_font)
        ylabel_img = ylabel_img.rotate(90, expand=1)
        
        # Paste rotated label
        ylabel_y = margin_top + (chart_height - ylabel_img.height) // 2
        img.paste(ylabel_img, (20, ylabel_y), ylabel_img)
        
        # Draw legend
        legend_x = margin_left + chart_width - 200
        legend_y = margin_top + 20
        
        for i, (label, color) in enumerate(zip(labels, colors_list)):
            # Legend box
            draw.rectangle([legend_x, legend_y + i * 30, legend_x + 20, legend_y + i * 30 + 15],
                          fill=color, outline=colors['border'], width=1)
            # Legend text
            draw.text((legend_x + 30, legend_y + i * 30), label, fill=colors['text'], font=text_font)
        
        # Save image
        img.save(filename, 'PNG', quality=95)
        return filename
    
    # Create Chart 1: Mean Scores
    chart1_filename = draw_bar_chart(
        data_sets=[simcse_scores, chatgpt_scores, teacher_scores],
        labels=['SimCSE', 'ChatGPT', 'Teacher'],
        colors_list=[colors['simcse'], colors['chatgpt'], colors['teacher']],
        title='Mean Scores per Participant and Scorer',
        ylabel='Mean Score Across All Topics & Days',
        filename='mean_scores_comparison.png',
        max_value=85
    )
    
    # Create Chart 2: Deviation from Teacher
    chart2_filename = draw_bar_chart(
        data_sets=[simcse_deviation, chatgpt_deviation],
        labels=['|SimCSE - Teacher|', '|ChatGPT - Teacher|'],
        colors_list=[colors['simcse'], colors['chatgpt']],
        title='Deviation of AI Scorers from Teacher per Participant',
        ylabel='Mean Absolute Difference (Score Points)',
        filename='ai_deviation_comparison.png',
        max_value=25
    )
    
    print("✅ Research results charts created using PIL:")
    print(f"   - {chart1_filename}")
    print(f"   - {chart2_filename}")

if __name__ == "__main__":
    create_research_charts_pil()