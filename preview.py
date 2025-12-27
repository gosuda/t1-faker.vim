import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_t1_faker_preview():
    # 1. T1 x Faker Palette Definition
    palette = [
        {"name": "SK Red (c1)", "hex": "#EA002C", "role": "Crimson Accent / Statements", "fg": "#FFFFFF"},
        {"name": "Trophy Gold", "hex": "#C8A951", "role": "Champion's Aura / Specials", "fg": "#071019"},
        {"name": "Deep Crimson", "hex": "#B80020", "role": "Mouse Shell / UI Depth", "fg": "#FFFFFF"},
        {"name": "Faker Grey", "hex": "#071019", "role": "Base Void / Midnight", "fg": "#DDDDDF"},
        {"name": "Razor Green", "hex": "#1BE65B", "role": "Gaming Gear / Strings", "fg": "#071019"},
        {"name": "T1 Blue", "hex": "#3453C1", "role": "Technical / Type Systems", "fg": "#FFFFFF"},
        {"name": "T1 White", "hex": "#DDDDDF", "role": "Primary Text / Logic", "fg": "#071019"},
        {"name": "Abyssal Purple", "hex": "#8C6FB9", "role": "Arcane / Constants", "fg": "#FFFFFF"},
    ]

    # 2. Setup Figure
    bg_main = '#071019'
    fig, ax = plt.subplots(figsize=(14, 8), facecolor=bg_main)
    ax.set_facecolor(bg_main)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, len(palette) + 1)
    ax.axis('off')

    # Header: T1 x Faker Brand
    plt.title("T1-FAKER : THE UNKILLABLE DEMON KING", 
              color='#EA002C', fontsize=24, pad=30, fontweight='black', family='sans-serif')
    
    ax.text(5, len(palette) + 0.5, "Vim Colorscheme // Victory through Precision", 
            color='#C8A951', fontsize=12, ha='center', weight='bold', style='italic')

    # 3. Dynamic Slanted Card Rendering
    for i, color in enumerate(reversed(palette)):
        y_pos = i + 0.5
        
        # Draw Slanted Background Card
        # Creating a trapezoid-like shape for a dynamic "gaming" look
        verts = [
            (0.5, y_pos),     # bottom left
            (9.5, y_pos),     # bottom right
            (9.7, y_pos + 0.8), # top right
            (0.7, y_pos + 0.8), # top left
        ]
        poly = patches.Polygon(verts, facecolor=color['hex'], edgecolor='#202332', linewidth=1, alpha=0.9)
        ax.add_patch(poly)

        # Labeling
        # ID & Hex
        ax.text(1.2, y_pos + 0.4, color['name'].upper(), 
                color=color['fg'], fontsize=13, va='center', fontweight='black')
        
        ax.text(4.0, y_pos + 0.4, color['hex'].upper(), 
                color=color['fg'], fontsize=11, va='center', family='monospace', weight='bold')
        
        # Systemic Role
        ax.text(6.0, y_pos + 0.4, f"// {color['role']}", 
                color=color['fg'], fontsize=11, va='center', fontweight='medium', alpha=0.8)

    # 4. Footer Branding
    ax.text(9.5, 0.1, "T1 WIN", color='#EA002C', fontsize=18, ha='right', fontweight='black', alpha=0.5)

    plt.tight_layout()
    
    # Save output
    save_name = 'preview.png'
    plt.savefig(save_name, facecolor=fig.get_facecolor(), dpi=300, bbox_inches='tight')
    print(f"Esports-grade preview exported: {save_name}")
    plt.show()

if __name__ == "__main__":
    draw_t1_faker_preview()
