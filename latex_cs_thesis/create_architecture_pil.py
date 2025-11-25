from PIL import Image, ImageDraw, ImageFont
import io
import os

def create_architecture_image():
    """Create a simple architecture diagram using PIL"""
    
    # Create a large canvas
    width, height = 1600, 1200
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, fallback to basic if not available
    try:
        title_font = ImageFont.truetype("arial.ttf", 24)
        header_font = ImageFont.truetype("arial.ttf", 16)
        text_font = ImageFont.truetype("arial.ttf", 12)
        small_font = ImageFont.truetype("arial.ttf", 10)
    except:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Colors
    colors = {
        'user': '#E8F4FD',
        'frontend': '#FFF3E0', 
        'api': '#F3E5F5',
        'ai': '#E8F5E8',
        'data': '#FFEBEE',
        'external': '#F5F5F5',
        'border': '#666666',
        'text': '#000000',
        'arrow': '#333333'
    }
    
    # Helper function to draw rounded rectangle
    def draw_rounded_rect(xy, fill, outline, width=2):
        x1, y1, x2, y2 = xy
        draw.rectangle(xy, fill=fill, outline=outline, width=width)
    
    # Helper function to draw text box
    def draw_text_box(xy, text, font, fill_color, text_color='black'):
        x1, y1, x2, y2 = xy
        draw.rectangle(xy, fill=fill_color, outline=colors['border'], width=1)
        # Calculate text position to center it
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        text_x = x1 + (x2 - x1 - text_width) // 2
        text_y = y1 + (y2 - y1 - text_height) // 2
        draw.text((text_x, text_y), text, fill=text_color, font=font)
    
    # Helper function to draw arrow
    def draw_arrow(start, end, color=colors['arrow'], width=3):
        """Draw an arrow from start to end point"""
        x1, y1 = start
        x2, y2 = end
        
        # Draw the line
        draw.line([(x1, y1), (x2, y2)], fill=color, width=width)
        
        # Calculate arrowhead
        import math
        angle = math.atan2(y2 - y1, x2 - x1)
        arrowhead_length = 15
        arrowhead_angle = 0.5
        
        # Arrowhead points
        arrow_x1 = x2 - arrowhead_length * math.cos(angle - arrowhead_angle)
        arrow_y1 = y2 - arrowhead_length * math.sin(angle - arrowhead_angle)
        arrow_x2 = x2 - arrowhead_length * math.cos(angle + arrowhead_angle)
        arrow_y2 = y2 - arrowhead_length * math.sin(angle + arrowhead_angle)
        
        # Draw arrowhead
        draw.polygon([(x2, y2), (arrow_x1, arrow_y1), (arrow_x2, arrow_y2)], fill=color)
    
    # Helper function to draw bidirectional arrow
    def draw_bidirectional_arrow(start, end, color=colors['arrow'], width=3):
        """Draw a bidirectional arrow between two points"""
        x1, y1 = start
        x2, y2 = end
        
        # Draw the line
        draw.line([(x1, y1), (x2, y2)], fill=color, width=width)
        
        import math
        angle = math.atan2(y2 - y1, x2 - x1)
        arrowhead_length = 12
        arrowhead_angle = 0.4
        
        # Arrowhead at end point
        arrow_x1 = x2 - arrowhead_length * math.cos(angle - arrowhead_angle)
        arrow_y1 = y2 - arrowhead_length * math.sin(angle - arrowhead_angle)
        arrow_x2 = x2 - arrowhead_length * math.cos(angle + arrowhead_angle)
        arrow_y2 = y2 - arrowhead_length * math.sin(angle + arrowhead_angle)
        draw.polygon([(x2, y2), (arrow_x1, arrow_y1), (arrow_x2, arrow_y2)], fill=color)
        
        # Arrowhead at start point (reversed)
        arrow_x3 = x1 + arrowhead_length * math.cos(angle - arrowhead_angle)
        arrow_y3 = y1 + arrowhead_length * math.sin(angle - arrowhead_angle)
        arrow_x4 = x1 + arrowhead_length * math.cos(angle + arrowhead_angle)
        arrow_y4 = y1 + arrowhead_length * math.sin(angle + arrowhead_angle)
        draw.polygon([(x1, y1), (arrow_x3, arrow_y3), (arrow_x4, arrow_y4)], fill=color)
        """Draw an arrow from start to end point"""
        x1, y1 = start
        x2, y2 = end
        
        # Draw the line
        draw.line([(x1, y1), (x2, y2)], fill=color, width=width)
        
        # Calculate arrowhead
        import math
        angle = math.atan2(y2 - y1, x2 - x1)
        arrowhead_length = 15
        arrowhead_angle = 0.5
        
        # Arrowhead points
        arrow_x1 = x2 - arrowhead_length * math.cos(angle - arrowhead_angle)
        arrow_y1 = y2 - arrowhead_length * math.sin(angle - arrowhead_angle)
        arrow_x2 = x2 - arrowhead_length * math.cos(angle + arrowhead_angle)
        arrow_y2 = y2 - arrowhead_length * math.sin(angle + arrowhead_angle)
        
        # Draw arrowhead
        draw.polygon([(x2, y2), (arrow_x1, arrow_y1), (arrow_x2, arrow_y2)], fill=color)
    
    # Helper function to draw bidirectional arrow
    def draw_bidirectional_arrow(start, end, color=colors['arrow'], width=3):
        """Draw a bidirectional arrow between two points"""
        x1, y1 = start
        x2, y2 = end
        
        # Draw the line
        draw.line([(x1, y1), (x2, y2)], fill=color, width=width)
        
        import math
        angle = math.atan2(y2 - y1, x2 - x1)
        arrowhead_length = 12
        arrowhead_angle = 0.4
        
        # Arrowhead at end point
        arrow_x1 = x2 - arrowhead_length * math.cos(angle - arrowhead_angle)
        arrow_y1 = y2 - arrowhead_length * math.sin(angle - arrowhead_angle)
        arrow_x2 = x2 - arrowhead_length * math.cos(angle + arrowhead_angle)
        arrow_y2 = y2 - arrowhead_length * math.sin(angle + arrowhead_angle)
        draw.polygon([(x2, y2), (arrow_x1, arrow_y1), (arrow_x2, arrow_y2)], fill=color)
        
        # Arrowhead at start point (reversed)
        arrow_x3 = x1 + arrowhead_length * math.cos(angle - arrowhead_angle)
        arrow_y3 = y1 + arrowhead_length * math.sin(angle - arrowhead_angle)
        arrow_x4 = x1 + arrowhead_length * math.cos(angle + arrowhead_angle)
        arrow_y4 = y1 + arrowhead_length * math.sin(angle + arrowhead_angle)
        draw.polygon([(x1, y1), (arrow_x3, arrow_y3), (arrow_x4, arrow_y4)], fill=color)
    
    
    # Helper function to draw arrow label
    def draw_arrow_label(xy, text, font, bgcolor='white'):
        """Draw a label with background for arrows"""
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x, y = xy
        
        # Draw background rectangle
        padding = 3
        draw.rectangle([x - text_width//2 - padding, y - text_height//2 - padding, 
                       x + text_width//2 + padding, y + text_height//2 + padding], 
                      fill=bgcolor, outline=colors['border'], width=1)
        
        # Draw text
        draw.text((x - text_width//2, y - text_height//2), text, fill='black', font=font)
    
    # Title
    title = "Consol System Architecture"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    draw.text((title_x, 30), title, fill=colors['text'], font=title_font)
    
    # Layer positions
    y_positions = {
        'user': 80,
        'frontend': 180,
        'api': 280, 
        'processing': 380,
        'external': 580
    }
    
    layer_height = 80
    margin = 50
    
    # User Interface Layer
    draw_rounded_rect((margin, y_positions['user'], width-margin, y_positions['user']+layer_height), 
                     fill=colors['user'], outline=colors['border'], width=2)
    draw.text((width//2 - 80, y_positions['user'] + 10), "User Interface Layer", 
             fill=colors['text'], font=header_font)
    
    # User components
    user_components = ["📝 Note Creation", "🎯 Practice Sessions", "📊 Analytics"]
    comp_width = (width - 2*margin - 40) // 3
    for i, comp in enumerate(user_components):
        x = margin + 20 + i * (comp_width + 10)
        draw_text_box((x, y_positions['user']+35, x+comp_width, y_positions['user']+65), 
                     comp, small_font, 'white')
    
    # Frontend Layer
    draw_rounded_rect((margin, y_positions['frontend'], width-margin, y_positions['frontend']+layer_height), 
                     fill=colors['frontend'], outline=colors['border'], width=2)
    draw.text((width//2 - 100, y_positions['frontend'] + 10), "Frontend - React.js/Next.js 15", 
             fill=colors['text'], font=header_font)
    
    # Frontend components
    frontend_components = ["Dashboard", "Note Manager", "Sessions", "Analytics", "Profile"]
    comp_width = (width - 2*margin - 60) // 5
    for i, comp in enumerate(frontend_components):
        x = margin + 20 + i * (comp_width + 5)
        draw_text_box((x, y_positions['frontend']+35, x+comp_width, y_positions['frontend']+65), 
                     comp, small_font, 'white')
    
    # API Layer
    draw_rounded_rect((margin, y_positions['api'], width-margin, y_positions['api']+layer_height), 
                     fill=colors['api'], outline=colors['border'], width=2)
    draw.text((width//2 - 100, y_positions['api'] + 10), "API Layer - Next.js API Routes", 
             fill=colors['text'], font=header_font)
    
    # API components
    api_components = ["/api/users", "/api/notes", "/api/sessions", "/api/similarity", "/api/analytics"]
    comp_width = (width - 2*margin - 60) // 5
    for i, comp in enumerate(api_components):
        x = margin + 20 + i * (comp_width + 5)
        draw_text_box((x, y_positions['api']+35, x+comp_width, y_positions['api']+65), 
                     comp, small_font, 'white')
    
    # Processing and Data Layers (side by side)
    mid_point = width // 2
    
    # AI Processing Layer (Left)
    draw_rounded_rect((margin, y_positions['processing'], mid_point-20, y_positions['processing']+layer_height*2), 
                     fill=colors['ai'], outline=colors['border'], width=2)
    draw.text((margin + 20, y_positions['processing'] + 10), "AI Processing Layer", 
             fill=colors['text'], font=header_font)
    draw.text((margin + 20, y_positions['processing'] + 35), "Flask API Server (Port 5000)", 
             fill=colors['text'], font=text_font)
    
    # AI components
    ai_components = ["SimCSE Model", "BERT Encoder", "Cosine Similarity"]
    ai_comp_height = 25
    for i, comp in enumerate(ai_components):
        y = y_positions['processing'] + 60 + i * (ai_comp_height + 5)
        draw_text_box((margin + 20, y, mid_point - 40, y + ai_comp_height), 
                     comp, small_font, 'white')
    
    # Data Layer (Right)
    draw_rounded_rect((mid_point+20, y_positions['processing'], width-margin, y_positions['processing']+layer_height*2), 
                     fill=colors['data'], outline=colors['border'], width=2)
    draw.text((mid_point + 40, y_positions['processing'] + 10), "Data Persistence Layer", 
             fill=colors['text'], font=header_font)
    draw.text((mid_point + 40, y_positions['processing'] + 35), "PostgreSQL Database (Direct SQL)", 
             fill=colors['text'], font=text_font)
    
    # Database components
    db_components = ["Users Table", "Notes Table", "Sessions Table"]
    for i, comp in enumerate(db_components):
        y = y_positions['processing'] + 60 + i * (ai_comp_height + 5)
        draw_text_box((mid_point + 40, y, width - margin - 20, y + ai_comp_height), 
                     comp, small_font, 'white')
    
    # External Services
    draw_rounded_rect((margin, y_positions['external'], width-margin, y_positions['external']+layer_height), 
                     fill=colors['external'], outline=colors['border'], width=2)
    draw.text((width//2 - 100, y_positions['external'] + 10), "External Services & Deployment", 
             fill=colors['text'], font=header_font)
    
    # External components
    external_components = ["Cloudinary", "Vercel", "Hugging Face", "NextAuth"]
    comp_width = (width - 2*margin - 50) // 4
    for i, comp in enumerate(external_components):
        x = margin + 20 + i * (comp_width + 10)
        draw_text_box((x, y_positions['external']+35, x+comp_width, y_positions['external']+65), 
                     comp, small_font, 'white')
    
    # Draw arrows with labels
    arrow_color = '#2196F3'  # Blue arrows
    ai_arrow_color = '#4CAF50'  # Green for AI
    data_arrow_color = '#F44336'  # Red for data
    
    center_x = width // 2
    
    # 1. User Interface to Frontend
    start_y = y_positions['user'] + layer_height
    end_y = y_positions['frontend']
    draw_bidirectional_arrow((center_x, start_y), (center_x, end_y), color=arrow_color)
    draw_arrow_label((center_x + 30, (start_y + end_y)//2), "User Actions", small_font)
    
    # 2. Frontend to API Layer
    start_y = y_positions['frontend'] + layer_height  
    end_y = y_positions['api']
    draw_bidirectional_arrow((center_x, start_y), (center_x, end_y), color=arrow_color)
    draw_arrow_label((center_x + 30, (start_y + end_y)//2), "HTTP/REST", small_font)
    
    # 3. API to AI Processing (left side)
    api_center_y = y_positions['api'] + layer_height//2
    ai_center_y = y_positions['processing'] + layer_height
    ai_center_x = (margin + mid_point - 20) // 2
    
    # Draw curved connection to AI
    draw_bidirectional_arrow((center_x - 100, y_positions['api'] + layer_height), 
                            (ai_center_x, y_positions['processing']), color=ai_arrow_color)
    draw_arrow_label((ai_center_x - 50, y_positions['api'] + layer_height + 20), 
                    "SimCSE API\n(Port 5000)", small_font)
    
    # 4. API to Data Layer (right side)
    data_center_x = (mid_point + 20 + width - margin) // 2
    draw_bidirectional_arrow((center_x + 100, y_positions['api'] + layer_height),
                            (data_center_x, y_positions['processing']), color=data_arrow_color)
    draw_arrow_label((data_center_x + 50, y_positions['api'] + layer_height + 20), 
                    "Direct SQL\nQueries", small_font)
    
    # 5. API to External Services
    draw_bidirectional_arrow((center_x, y_positions['api'] + layer_height), 
                            (center_x, y_positions['external']), color='#666666')
    
    # Calculate the midpoint for the label
    mid_y = y_positions['api'] + layer_height + (y_positions['external'] - y_positions['api'] - layer_height)//2
    draw_arrow_label((center_x + 40, mid_y), "External APIs", small_font)
    
    # 6. Data flow between AI and Data layers
    draw_bidirectional_arrow((mid_point - 20, y_positions['processing'] + layer_height), 
                            (mid_point + 20, y_positions['processing'] + layer_height), 
                            color='#9C27B0')
    draw_arrow_label((mid_point, y_positions['processing'] + layer_height + 15), 
                    "Similarity\nResults", small_font)
    
    # Add data flow text
    flow_y = y_positions['external'] + layer_height + 20
    draw.text((margin, flow_y), "Data Flow:", fill=colors['text'], font=header_font)
    flow_texts = [
        "1. User creates note → API → PostgreSQL (Direct SQL)",
        "2. User practices → API → Flask (SimCSE) → Similarity score → PostgreSQL", 
        "3. Performance analytics → API → PostgreSQL → Chart.js visualization",
        "4. Media uploads → Cloudinary → URL stored in PostgreSQL"
    ]
    
    for i, text in enumerate(flow_texts):
        draw.text((margin, flow_y + 25 + i*20), text, fill=colors['text'], font=text_font)
    
    # Save the image
    img.save('consol_system_architecture.png', 'PNG', quality=95)
    print("✅ System architecture diagram created and saved as 'consol_system_architecture.png'")
    print("📁 File saved in:", os.path.abspath('consol_system_architecture.png'))

if __name__ == "__main__":
    create_architecture_image()