from PIL import Image, ImageDraw, ImageFont
import math

def create_simcse_pipeline():
    """Create SimCSE Processing Pipeline diagram"""
    
    width, height = 1600, 900
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 20)
        header_font = ImageFont.truetype("arial.ttf", 14)
        text_font = ImageFont.truetype("arial.ttf", 11)
        small_font = ImageFont.truetype("arial.ttf", 9)
        math_font = ImageFont.truetype("arial.ttf", 10)
    except:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
        math_font = ImageFont.load_default()
    
    # Colors
    colors = {
        'input': '#E3F2FD',      # Light blue
        'processing': '#E8F5E8',  # Light green
        'ai_model': '#FFF3E0',    # Light orange
        'output': '#FFEBEE',      # Light red
        'border': '#666666',
        'arrow': '#2196F3',
        'text': '#000000'
    }
    
    def draw_process_box(x, y, width, height, title, subtitle, color, details=None):
        """Draw a processing step box"""
        # Main box
        draw.rectangle([x, y, x + width, y + height], 
                      fill=color, outline=colors['border'], width=2)
        
        # Title
        title_bbox = draw.textbbox((0, 0), title, font=header_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = x + (width - title_width) // 2
        draw.text((title_x, y + 10), title, fill=colors['text'], font=header_font)
        
        # Subtitle
        if subtitle:
            sub_bbox = draw.textbbox((0, 0), subtitle, font=text_font)
            sub_width = sub_bbox[2] - sub_bbox[0]
            sub_x = x + (width - sub_width) // 2
            draw.text((sub_x, y + 30), subtitle, fill='#666666', font=text_font)
        
        # Details
        if details:
            detail_y = y + 55
            for detail in details:
                detail_bbox = draw.textbbox((0, 0), detail, font=small_font)
                detail_width = detail_bbox[2] - detail_bbox[0]
                detail_x = x + (width - detail_width) // 2
                draw.text((detail_x, detail_y), detail, fill=colors['text'], font=small_font)
                detail_y += 15
    
    def draw_arrow_with_label(start, end, label, curve=False):
        """Draw arrow between process boxes"""
        x1, y1 = start
        x2, y2 = end
        
        if curve:
            # Draw curved arrow
            mid_x = (x1 + x2) // 2
            mid_y = min(y1, y2) - 30
            
            # Bezier curve approximation with line segments
            points = []
            for t in range(0, 11):
                t = t / 10.0
                bx = (1-t)**2 * x1 + 2*(1-t)*t * mid_x + t**2 * x2
                by = (1-t)**2 * y1 + 2*(1-t)*t * mid_y + t**2 * y2
                points.append((int(bx), int(by)))
            
            for i in range(len(points)-1):
                draw.line([points[i], points[i+1]], fill=colors['arrow'], width=3)
        else:
            # Straight arrow
            draw.line([(x1, y1), (x2, y2)], fill=colors['arrow'], width=3)
        
        # Arrowhead
        angle = math.atan2(y2 - y1, x2 - x1)
        arrow_length = 12
        arrow_angle = 0.4
        
        arrow_x1 = x2 - arrow_length * math.cos(angle - arrow_angle)
        arrow_y1 = y2 - arrow_length * math.sin(angle - arrow_angle)
        arrow_x2 = x2 - arrow_length * math.cos(angle + arrow_angle)
        arrow_y2 = y2 - arrow_length * math.sin(angle + arrow_angle)
        
        draw.polygon([(x2, y2), (arrow_x1, arrow_y1), (arrow_x2, arrow_y2)], fill=colors['arrow'])
        
        # Label
        if label:
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2 - 10
            if curve:
                mid_y -= 20
            
            label_bbox = draw.textbbox((0, 0), label, font=small_font)
            label_width = label_bbox[2] - label_bbox[0]
            label_height = label_bbox[3] - label_bbox[1]
            
            # Label background
            draw.rectangle([mid_x - label_width//2 - 2, mid_y - label_height//2 - 1,
                          mid_x + label_width//2 + 2, mid_y + label_height//2 + 1],
                         fill='white', outline=colors['arrow'], width=1)
            
            draw.text((mid_x - label_width//2, mid_y - label_height//2), label, 
                     fill=colors['arrow'], font=small_font)
    
    # Title
    title = "SimCSE Processing Pipeline - Semantic Similarity Computation"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    draw.text((title_x, 20), title, fill=colors['text'], font=title_font)
    
    # Process boxes dimensions
    box_width = 180
    box_height = 120
    spacing = 40
    
    # Row 1: Input Processing
    y1 = 80
    x1 = 50
    
    # Text Input
    draw_process_box(x1, y1, box_width, box_height, 
                    "Text Input", "Original & Recalled", colors['input'],
                    ["Note Content", "User Recall", "(String Format)"])
    
    x2 = x1 + box_width + spacing
    # Preprocessing
    draw_process_box(x2, y1, box_width, box_height,
                    "Text Preprocessing", "Cleaning & Normalization", colors['processing'],
                    ["Remove extra spaces", "Handle punctuation", "UTF-8 encoding"])
    
    x3 = x2 + box_width + spacing
    # Tokenization
    draw_process_box(x3, y1, box_width, box_height,
                    "BERT Tokenization", "Subword Segmentation", colors['processing'],
                    ["[CLS] token prefix", "WordPiece tokens", "[SEP] token suffix"])
    
    # Row 2: AI Processing
    y2 = y1 + box_height + spacing + 20
    x4 = 150
    
    # SimCSE Model
    draw_process_box(x4, y2, box_width + 50, box_height + 30,
                    "SimCSE Model", "princeton-nlp/unsup-simcse-bert-base-uncased", colors['ai_model'],
                    ["BERT-base encoder", "768-dimensional output", "Contrastive learning", "Dropout augmentation"])
    
    x5 = x4 + box_width + 50 + spacing
    # Embeddings
    draw_process_box(x5, y2, box_width, box_height + 30,
                    "Sentence Embeddings", "Vector Representations", colors['processing'],
                    ["768-dim vectors", "[CLS] token extraction", "Normalized embeddings", "Float32 tensors"])
    
    # Row 3: Output Processing
    y3 = y2 + box_height + 50 + spacing
    x6 = 250
    
    # Similarity Calculation
    draw_process_box(x6, y3, box_width, box_height,
                    "Cosine Similarity", "Vector Comparison", colors['processing'],
                    ["dot(v1, v2)", "||v1|| * ||v2||", "Range: [-1, 1]"])
    
    x7 = x6 + box_width + spacing
    # Final Output
    draw_process_box(x7, y3, box_width, box_height,
                    "Similarity Score", "Educational Assessment", colors['output'],
                    ["DECIMAL(5,3)", "Range: 0.000-1.000", "Star conversion"])
    
    # Draw arrows
    # Row 1 arrows
    draw_arrow_with_label((x1 + box_width, y1 + box_height//2),
                         (x2, y1 + box_height//2), "Raw Text")
    
    draw_arrow_with_label((x2 + box_width, y1 + box_height//2),
                         (x3, y1 + box_height//2), "Clean Text")
    
    # Down to SimCSE
    draw_arrow_with_label((x3 + box_width//2, y1 + box_height),
                         (x4 + (box_width + 50)//2, y2), "Token IDs")
    
    # Row 2 arrows
    draw_arrow_with_label((x4 + box_width + 50, y2 + (box_height + 30)//2),
                         (x5, y2 + (box_height + 30)//2), "Hidden States")
    
    # Down to similarity
    draw_arrow_with_label((x5 + box_width//2, y2 + box_height + 30),
                         (x6 + box_width//2, y3), "Embeddings")
    
    # Final arrow
    draw_arrow_with_label((x6 + box_width, y3 + box_height//2),
                         (x7, y3 + box_height//2), "Similarity")
    
    # Add mathematical formula
    formula_y = height - 180
    formula_text = "Mathematical Foundation:"
    draw.text((50, formula_y), formula_text, fill=colors['text'], font=header_font)
    
    # SimCSE Loss Function
    formula_y += 30
    loss_text = "SimCSE Loss: ℓᵢ = -log(e^(sim(hᵢ,hᵢ⁺)/τ) / Σⱼ₌₁ᴺ e^(sim(hᵢ,hⱼ⁺)/τ))"
    draw.text((50, formula_y), loss_text, fill='#8B4513', font=text_font)
    
    # Cosine Similarity
    formula_y += 25
    cosine_text = "Cosine Similarity: sim(A,B) = (A·B) / (||A|| × ||B||)"
    draw.text((50, formula_y), cosine_text, fill='#8B4513', font=text_font)
    
    # Star Rating System
    formula_y += 25
    star_text = "Star Rating: 3★(≥0.8) | 2★(≥0.6) | 1★(≥0.4) | 0★(<0.4)"
    draw.text((50, formula_y), star_text, fill='#8B4513', font=text_font)
    
    # Add performance note
    perf_box_x = width - 350
    perf_box_y = height - 150
    
    draw.rectangle([perf_box_x, perf_box_y, perf_box_x + 300, perf_box_y + 120],
                  fill='#F0F8FF', outline='#4169E1', width=2)
    
    draw.text((perf_box_x + 10, perf_box_y + 10), "Performance Specifications:", 
             fill=colors['text'], font=header_font)
    
    perf_details = [
        "• Processing Time: 50-200ms per comparison",
        "• Model Size: ~400MB (BERT-base)",
        "• Memory Usage: ~2GB GPU / 4GB CPU",
        "• Precision: 3 decimal places (0.001)",
        "• Input Limit: 512 tokens per text",
        "• Batch Processing: Supported for efficiency"
    ]
    
    detail_y = perf_box_y + 35
    for detail in perf_details:
        draw.text((perf_box_x + 15, detail_y), detail, fill=colors['text'], font=small_font)
        detail_y += 15
    
    # Save the pipeline diagram
    img.save('simcse_pipeline.png', 'PNG', quality=95)
    print("✅ SimCSE Processing Pipeline created and saved as 'simcse_pipeline.png'")

if __name__ == "__main__":
    create_simcse_pipeline()