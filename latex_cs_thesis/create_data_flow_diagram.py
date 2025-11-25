from PIL import Image, ImageDraw, ImageFont
import math

def create_data_flow_diagram():
    """Create comprehensive data flow diagram for the educational system"""
    
    width, height = 1800, 1000
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 22)
        header_font = ImageFont.truetype("arial.ttf", 14)
        text_font = ImageFont.truetype("arial.ttf", 11)
        small_font = ImageFont.truetype("arial.ttf", 9)
    except:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Colors for different data types
    colors = {
        'user_data': '#E3F2FD',      # Light blue - user inputs
        'process': '#E8F5E8',        # Light green - processing
        'storage': '#FFF3E0',        # Light orange - databases
        'ai_process': '#FFEBEE',     # Light red - AI/ML
        'output': '#F3E5F5',         # Light purple - results
        'external': '#F5F5F5',       # Gray - external services
        'border': '#666666',
        'arrow': '#2196F3',
        'text': '#000000',
        'data_flow': '#FF6B35',      # Orange for data flow
        'control_flow': '#4ECDC4'    # Teal for control flow
    }
    
    def draw_data_store(x, y, width, height, name, details):
        """Draw a data store (database/file)"""
        # Draw cylinder-like shape for database
        draw.ellipse([x, y, x + width, y + 20], fill=colors['storage'], outline=colors['border'], width=2)
        draw.ellipse([x, y + height - 20, x + width, y + height], fill=colors['storage'], outline=colors['border'], width=2)
        draw.rectangle([x, y + 10, x + width, y + height - 10], fill=colors['storage'], outline=None)
        draw.line([x, y + 10, x, y + height - 10], fill=colors['border'], width=2)
        draw.line([x + width, y + 10, x + width, y + height - 10], fill=colors['border'], width=2)
        
        # Name
        name_bbox = draw.textbbox((0, 0), name, font=header_font)
        name_width = name_bbox[2] - name_bbox[0]
        name_x = x + (width - name_width) // 2
        draw.text((name_x, y + 25), name, fill=colors['text'], font=header_font)
        
        # Details
        detail_y = y + 50
        for detail in details:
            detail_bbox = draw.textbbox((0, 0), detail, font=small_font)
            detail_width = detail_bbox[2] - detail_bbox[0]
            detail_x = x + (width - detail_width) // 2
            draw.text((detail_x, detail_y), detail, fill=colors['text'], font=small_font)
            detail_y += 15
    
    def draw_process_circle(x, y, radius, name, details, color):
        """Draw a process as a circle"""
        draw.ellipse([x - radius, y - radius, x + radius, y + radius], 
                    fill=color, outline=colors['border'], width=2)
        
        # Name
        name_bbox = draw.textbbox((0, 0), name, font=text_font)
        name_width = name_bbox[2] - name_bbox[0]
        name_x = x - name_width // 2
        draw.text((name_x, y - 10), name, fill=colors['text'], font=text_font)
        
        # Details below circle
        detail_y = y + radius + 10
        for detail in details:
            detail_bbox = draw.textbbox((0, 0), detail, font=small_font)
            detail_width = detail_bbox[2] - detail_bbox[0]
            detail_x = x - detail_width // 2
            draw.text((detail_x, detail_y), detail, fill='#666666', font=small_font)
            detail_y += 12
    
    def draw_external_entity(x, y, width, height, name, details):
        """Draw an external entity (user/service)"""
        draw.rectangle([x, y, x + width, y + height], 
                      fill=colors['external'], outline=colors['border'], width=3)
        
        # Name
        name_bbox = draw.textbbox((0, 0), name, font=header_font)
        name_width = name_bbox[2] - name_bbox[0]
        name_x = x + (width - name_width) // 2
        draw.text((name_x, y + 15), name, fill=colors['text'], font=header_font)
        
        # Details
        detail_y = y + 40
        for detail in details:
            detail_bbox = draw.textbbox((0, 0), detail, font=small_font)
            detail_width = detail_bbox[2] - detail_bbox[0]
            detail_x = x + (width - detail_width) // 2
            draw.text((detail_x, detail_y), detail, fill=colors['text'], font=small_font)
            detail_y += 15
    
    def draw_data_flow_arrow(start, end, label, data_type="data"):
        """Draw data flow arrow with label"""
        x1, y1 = start
        x2, y2 = end
        
        arrow_color = colors['data_flow'] if data_type == "data" else colors['control_flow']
        
        # Draw line
        draw.line([(x1, y1), (x2, y2)], fill=arrow_color, width=3)
        
        # Arrowhead
        angle = math.atan2(y2 - y1, x2 - x1)
        arrow_length = 15
        arrow_angle = 0.4
        
        arrow_x1 = x2 - arrow_length * math.cos(angle - arrow_angle)
        arrow_y1 = y2 - arrow_length * math.sin(angle - arrow_angle)
        arrow_x2 = x2 - arrow_length * math.cos(angle + arrow_angle)
        arrow_y2 = y2 - arrow_length * math.sin(angle + arrow_angle)
        
        draw.polygon([(x2, y2), (arrow_x1, arrow_y1), (arrow_x2, arrow_y2)], fill=arrow_color)
        
        # Label with background
        if label:
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2 - 12
            
            label_bbox = draw.textbbox((0, 0), label, font=small_font)
            label_width = label_bbox[2] - label_bbox[0]
            label_height = label_bbox[3] - label_bbox[1]
            
            # Label background
            draw.rectangle([mid_x - label_width//2 - 3, mid_y - label_height//2 - 2,
                          mid_x + label_width//2 + 3, mid_y + label_height//2 + 2],
                         fill='white', outline=arrow_color, width=1)
            
            draw.text((mid_x - label_width//2, mid_y - label_height//2), label, 
                     fill=arrow_color, font=small_font)
    
    # Title
    title = "Comprehensive Data Flow Diagram - Educational Recall Assessment System"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    draw.text((title_x, 20), title, fill=colors['text'], font=title_font)
    
    # External Entities
    # Student User
    draw_external_entity(50, 100, 150, 80, "Student User", 
                        ["Input: Notes", "Input: Recalls", "Output: Scores"])
    
    # Educator User
    draw_external_entity(50, 200, 150, 80, "Educator User", 
                        ["View: Analytics", "Export: Reports", "Manage: Sessions"])
    
    # External Services
    draw_external_entity(width-200, 100, 150, 80, "External Services", 
                        ["Google Drive", "File Upload", "Authentication"])
    
    # Data Stores
    # User Database
    draw_data_store(300, 120, 180, 100, "User Database", 
                   ["PostgreSQL", "Users table", "Sessions table", "Auth tokens"])
    
    # Notes Database  
    draw_data_store(300, 240, 180, 100, "Notes Database", 
                   ["PostgreSQL", "Notes table", "Content BLOB", "Metadata"])
    
    # Results Database
    draw_data_store(300, 360, 180, 100, "Results Database", 
                   ["PostgreSQL", "Scores table", "Similarity data", "Analytics"])
    
    # AI Model Cache
    draw_data_store(600, 480, 180, 100, "AI Model Cache", 
                   ["File System", "SimCSE model", "Embeddings cache", "Temp processing"])
    
    # Process Centers
    # Authentication Process
    draw_process_circle(400, 80, 40, "Authentication", ["NextAuth.js", "JWT tokens"], colors['process'])
    
    # Note Management
    draw_process_circle(550, 180, 50, "Note Management", ["CRUD ops", "File handling"], colors['process'])
    
    # Practice Session
    draw_process_circle(750, 250, 50, "Practice Session", ["Random selection", "Timing control"], colors['process'])
    
    # AI Processing
    draw_process_circle(750, 400, 60, "AI Processing", ["SimCSE model", "Similarity calc"], colors['ai_process'])
    
    # Results Processing
    draw_process_circle(550, 480, 50, "Results Processing", ["Score calculation", "Star rating"], colors['output'])
    
    # Analytics Engine
    draw_process_circle(1050, 350, 55, "Analytics Engine", ["Progress tracking", "Performance stats"], colors['output'])
    
    # Data Flows
    
    # User login flow
    draw_data_flow_arrow((200, 140), (360, 90), "Login Request")
    draw_data_flow_arrow((380, 120), (380, 120), "User Verification")
    draw_data_flow_arrow((440, 90), (500, 140), "Auth Response")
    
    # Note upload/management
    draw_data_flow_arrow((200, 160), (500, 180), "Upload Notes")
    draw_data_flow_arrow((570, 160), (width-200, 140), "External Files")
    draw_data_flow_arrow((520, 210), (420, 240), "Store Notes")
    
    # Practice session initiation
    draw_data_flow_arrow((200, 180), (700, 250), "Start Practice")
    draw_data_flow_arrow((720, 280), (450, 290), "Fetch Notes")
    draw_data_flow_arrow((480, 290), (750, 290), "Selected Notes")
    
    # User recall input
    draw_data_flow_arrow((200, 200), (720, 270), "User Recall")
    draw_data_flow_arrow((750, 300), (750, 340), "Text Pairs")
    
    # AI processing flow
    draw_data_flow_arrow((750, 360), (680, 480), "Processing Request")
    draw_data_flow_arrow((640, 520), (750, 460), "Cached Models")
    draw_data_flow_arrow((690, 450), (600, 450), "Similarity Score")
    
    # Results storage and display
    draw_data_flow_arrow((520, 500), (440, 410), "Store Results")
    draw_data_flow_arrow((500, 470), (200, 220), "Display Scores")
    
    # Analytics and reporting
    draw_data_flow_arrow((480, 410), (995, 350), "Performance Data")
    draw_data_flow_arrow((1000, 380), (200, 240), "Analytics Report")
    
    # Add legend
    legend_x = 50
    legend_y = height - 200
    
    draw.text((legend_x, legend_y), "Data Flow Legend:", fill=colors['text'], font=header_font)
    
    # Legend items
    legend_items = [
        ("User Input/Output", colors['external']),
        ("Data Processing", colors['process']),
        ("Data Storage", colors['storage']),
        ("AI/ML Processing", colors['ai_process']),
        ("Results & Analytics", colors['output'])
    ]
    
    legend_y += 30
    for item_name, item_color in legend_items:
        draw.rectangle([legend_x, legend_y, legend_x + 15, legend_y + 15],
                      fill=item_color, outline=colors['border'])
        draw.text((legend_x + 25, legend_y + 2), item_name, fill=colors['text'], font=small_font)
        legend_y += 20
    
    # Data types legend
    data_legend_x = 300
    data_legend_y = height - 200
    
    draw.text((data_legend_x, data_legend_y), "Data Types:", fill=colors['text'], font=header_font)
    data_legend_y += 30
    
    # Data flow examples
    draw.line([data_legend_x, data_legend_y, data_legend_x + 30, data_legend_y], 
             fill=colors['data_flow'], width=3)
    draw.text((data_legend_x + 35, data_legend_y - 5), "User Data Flow", fill=colors['text'], font=small_font)
    
    data_legend_y += 20
    draw.line([data_legend_x, data_legend_y, data_legend_x + 30, data_legend_y], 
             fill=colors['control_flow'], width=3)
    draw.text((data_legend_x + 35, data_legend_y - 5), "System Control Flow", fill=colors['text'], font=small_font)
    
    # Performance metrics box
    metrics_x = width - 400
    metrics_y = height - 180
    
    draw.rectangle([metrics_x, metrics_y, metrics_x + 350, metrics_y + 150],
                  fill='#F8F9FA', outline='#6C757D', width=2)
    
    draw.text((metrics_x + 10, metrics_y + 10), "System Performance Metrics:", 
             fill=colors['text'], font=header_font)
    
    metrics = [
        "• Data Throughput: 50-100 notes/second",
        "• Average Processing Time: 200ms per comparison",
        "• Database Response Time: <50ms",
        "• Concurrent Users: Up to 100 students",
        "• Data Retention: 12 months user data",
        "• Backup Frequency: Daily automated backups",
        "• Uptime Target: 99.5% availability"
    ]
    
    metric_y = metrics_y + 35
    for metric in metrics:
        draw.text((metrics_x + 15, metric_y), metric, fill=colors['text'], font=small_font)
        metric_y += 18
    
    # Save the diagram
    img.save('data_flow_diagram.png', 'PNG', quality=95)
    print("✅ Data Flow Diagram created and saved as 'data_flow_diagram.png'")

if __name__ == "__main__":
    create_data_flow_diagram()