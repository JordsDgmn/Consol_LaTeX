from PIL import Image, ImageDraw, ImageFont

def create_database_erd():
    """Create a professional Database ERD for the Consol system"""
    
    # Create canvas
    width, height = 1400, 1000
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 20)
        header_font = ImageFont.truetype("arial.ttf", 14)
        text_font = ImageFont.truetype("arial.ttf", 11)
        small_font = ImageFont.truetype("arial.ttf", 9)
    except:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    # Colors
    colors = {
        'entity_fill': '#F0F8FF',  # Light blue
        'entity_border': '#4169E1',  # Royal blue
        'primary_key': '#FFD700',  # Gold
        'foreign_key': '#FF6B6B',  # Light red
        'relationship': '#32CD32',  # Lime green
        'text': '#000000',
        'constraint': '#8A2BE2'  # Purple
    }
    
    def draw_entity(x, y, width, height, title, attributes):
        """Draw an entity box with attributes"""
        # Main entity box
        draw.rectangle([x, y, x + width, y + height], 
                      fill=colors['entity_fill'], 
                      outline=colors['entity_border'], 
                      width=2)
        
        # Title section
        title_height = 30
        draw.rectangle([x, y, x + width, y + title_height], 
                      fill=colors['entity_border'], 
                      outline=colors['entity_border'])
        
        # Entity title
        title_bbox = draw.textbbox((0, 0), title, font=header_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = x + (width - title_width) // 2
        draw.text((title_x, y + 5), title, fill='white', font=header_font)
        
        # Attributes
        attr_y = y + title_height + 10
        for i, (attr_name, attr_type, is_pk, is_fk) in enumerate(attributes):
            # Background color for special keys
            if is_pk:
                draw.rectangle([x + 5, attr_y - 2, x + width - 5, attr_y + 15], 
                             fill=colors['primary_key'], outline=colors['primary_key'])
            elif is_fk:
                draw.rectangle([x + 5, attr_y - 2, x + width - 5, attr_y + 15], 
                             fill=colors['foreign_key'], outline=colors['foreign_key'])
            
            # Attribute text
            key_symbol = "🔑 " if is_pk else "🔗 " if is_fk else "📄 "
            attr_text = f"{key_symbol}{attr_name}"
            draw.text((x + 10, attr_y), attr_text, fill=colors['text'], font=text_font)
            
            # Data type (right aligned)
            type_bbox = draw.textbbox((0, 0), attr_type, font=small_font)
            type_width = type_bbox[2] - type_bbox[0]
            draw.text((x + width - type_width - 10, attr_y + 2), attr_type, 
                     fill='#666666', font=small_font)
            
            attr_y += 18
    
    def draw_relationship_line(start_x, start_y, end_x, end_y, label, cardinality):
        """Draw relationship line with cardinality"""
        # Draw line
        draw.line([(start_x, start_y), (end_x, end_y)], 
                 fill=colors['relationship'], width=3)
        
        # Draw cardinality labels
        mid_x, mid_y = (start_x + end_x) // 2, (start_y + end_y) // 2
        
        # Label background
        label_bbox = draw.textbbox((0, 0), label, font=small_font)
        label_width = label_bbox[2] - label_bbox[0]
        label_height = label_bbox[3] - label_bbox[1]
        
        draw.rectangle([mid_x - label_width//2 - 3, mid_y - label_height//2 - 2,
                       mid_x + label_width//2 + 3, mid_y + label_height//2 + 2],
                      fill='white', outline=colors['relationship'], width=1)
        
        draw.text((mid_x - label_width//2, mid_y - label_height//2), label, 
                 fill=colors['relationship'], font=small_font)
        
        # Cardinality indicators
        draw.text((start_x + 10, start_y - 15), cardinality[0], 
                 fill=colors['constraint'], font=small_font)
        draw.text((end_x - 30, end_y - 15), cardinality[1], 
                 fill=colors['constraint'], font=small_font)
    
    # Title
    title = "Consol Database Schema - Entity Relationship Diagram"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    draw.text((title_x, 20), title, fill=colors['text'], font=title_font)
    
    # Entity definitions
    users_attrs = [
        ("id", "SERIAL PRIMARY KEY", True, False),
        ("username", "VARCHAR(255) UNIQUE", False, False),
        ("profile_picture_url", "VARCHAR(500)", False, False),
        ("created_at", "TIMESTAMP", False, False)
    ]
    
    notes_attrs = [
        ("id", "SERIAL PRIMARY KEY", True, False),
        ("user_id", "INTEGER", False, True),
        ("title", "VARCHAR(255)", False, False),
        ("content", "TEXT", False, False),
        ("word_count", "INTEGER", False, False),
        ("created_at", "TIMESTAMP", False, False)
    ]
    
    sessions_attrs = [
        ("id", "SERIAL PRIMARY KEY", True, False),
        ("user_id", "INTEGER", False, True),
        ("note_id", "INTEGER", False, True),
        ("similarity", "DECIMAL(5,3)", False, False),
        ("stars", "INTEGER", False, False),
        ("word_count", "INTEGER", False, False),
        ("duration_secs", "INTEGER", False, False),
        ("wpm", "DECIMAL(6,2)", False, False),
        ("created_at", "TIMESTAMP", False, False)
    ]
    
    # Entity positions
    users_x, users_y = 100, 100
    notes_x, notes_y = 500, 100
    sessions_x, sessions_y = 300, 400
    
    entity_width, entity_height = 250, 140
    sessions_height = 200
    
    # Draw entities
    draw_entity(users_x, users_y, entity_width, entity_height, "USERS", users_attrs)
    draw_entity(notes_x, notes_y, entity_width, entity_height, "NOTES", notes_attrs)
    draw_entity(sessions_x, sessions_y, entity_width, sessions_height, "SESSIONS", sessions_attrs)
    
    # Draw relationships
    # Users to Notes (1:N)
    draw_relationship_line(
        users_x + entity_width, users_y + entity_height//2,
        notes_x, notes_y + entity_height//2,
        "creates", ("1", "N")
    )
    
    # Users to Sessions (1:N)
    draw_relationship_line(
        users_x + entity_width//2, users_y + entity_height,
        sessions_x + entity_width//2, sessions_y,
        "performs", ("1", "N")
    )
    
    # Notes to Sessions (1:N)
    draw_relationship_line(
        notes_x + entity_width//2, notes_y + entity_height,
        sessions_x + entity_width//2, sessions_y,
        "generates", ("1", "N")
    )
    
    # Add constraints legend
    legend_x = 50
    legend_y = height - 200
    
    # Legend box
    draw.rectangle([legend_x, legend_y, legend_x + 300, legend_y + 150], 
                  fill='#F9F9F9', outline='#CCCCCC', width=1)
    
    draw.text((legend_x + 10, legend_y + 10), "Legend:", fill=colors['text'], font=header_font)
    
    # Legend items
    legend_items = [
        ("🔑 Primary Key", colors['primary_key']),
        ("🔗 Foreign Key", colors['foreign_key']),
        ("📄 Regular Attribute", 'white'),
        ("─── Relationship (1:N)", colors['relationship'])
    ]
    
    item_y = legend_y + 35
    for item, color in legend_items:
        if color != 'white':
            draw.rectangle([legend_x + 15, item_y - 2, legend_x + 280, item_y + 12], 
                         fill=color, outline=color)
        draw.text((legend_x + 20, item_y), item, fill=colors['text'], font=small_font)
        item_y += 20
    
    # Add constraints information
    constraints_x = 450
    constraints_y = height - 200
    
    draw.rectangle([constraints_x, constraints_y, constraints_x + 400, constraints_y + 150], 
                  fill='#F9F9F9', outline='#CCCCCC', width=1)
    
    draw.text((constraints_x + 10, constraints_y + 10), "Key Constraints:", 
             fill=colors['text'], font=header_font)
    
    constraint_text = [
        "• users.username: UNIQUE constraint",
        "• sessions.stars: CHECK (stars >= 0 AND stars <= 3)",
        "• Foreign Keys: CASCADE DELETE enabled",
        "• sessions.similarity: DECIMAL(5,3) precision",
        "• All entities: AUTO_INCREMENT primary keys",
        "• Temporal tracking: created_at timestamps"
    ]
    
    item_y = constraints_y + 35
    for text in constraint_text:
        draw.text((constraints_x + 15, item_y), text, fill=colors['text'], font=small_font)
        item_y += 15
    
    # Save the ERD
    img.save('database_erd.png', 'PNG', quality=95)
    print("✅ Database ERD created and saved as 'database_erd.png'")

if __name__ == "__main__":
    create_database_erd()