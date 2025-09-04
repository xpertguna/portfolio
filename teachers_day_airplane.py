#!/usr/bin/env python3
"""
Teachers Day Image Generator with Airplane Theme
Creates a beautiful Teachers Day image featuring a passenger airplane
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import io

def create_teachers_day_airplane_image():
    # Create figure and axis
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    
    # Create sky gradient background
    y = np.linspace(0, 100, 256).reshape(-1, 1)
    x = np.linspace(0, 100, 256).reshape(1, -1)
    
    # Sky gradient from light blue to deeper blue
    sky_gradient = np.zeros((256, 256, 3))
    sky_gradient[:, :, 0] = 0.5 + 0.3 * (1 - y/100)  # Red component
    sky_gradient[:, :, 1] = 0.7 + 0.2 * (1 - y/100)  # Green component
    sky_gradient[:, :, 2] = 0.9 + 0.1 * (1 - y/100)  # Blue component
    
    ax.imshow(sky_gradient, extent=[0, 100, 0, 100], aspect='auto', alpha=0.8)
    
    # Add some clouds
    cloud_positions = [(20, 75), (60, 80), (85, 70), (15, 85), (45, 90)]
    for x_pos, y_pos in cloud_positions:
        # Create fluffy clouds using multiple circles
        for i, (dx, dy, size) in enumerate([(-2, 0, 4), (0, 0, 5), (2, 0, 4), (0, 2, 3)]):
            cloud = patches.Circle((x_pos + dx, y_pos + dy), size, 
                                 facecolor='white', alpha=0.8, zorder=1)
            ax.add_patch(cloud)
    
    # Draw airplane
    airplane_x, airplane_y = 50, 45
    
    # Airplane body (fuselage)
    fuselage = patches.Rectangle((airplane_x - 15, airplane_y - 2), 30, 4, 
                               facecolor='#E8E8E8', edgecolor='#B0B0B0', linewidth=2, zorder=5)
    ax.add_patch(fuselage)
    
    # Airplane nose
    nose_points = [[airplane_x + 15, airplane_y], [airplane_x + 20, airplane_y], [airplane_x + 15, airplane_y + 2], [airplane_x + 15, airplane_y - 2]]
    nose = patches.Polygon(nose_points, facecolor='#D0D0D0', edgecolor='#B0B0B0', linewidth=2, zorder=5)
    ax.add_patch(nose)
    
    # Wings
    # Main wing
    wing_main = patches.Rectangle((airplane_x - 5, airplane_y - 8), 20, 16, 
                                facecolor='#C0C0C0', edgecolor='#A0A0A0', linewidth=2, zorder=4)
    ax.add_patch(wing_main)
    
    # Tail wing
    tail_wing = patches.Rectangle((airplane_x - 12, airplane_y + 6), 8, 6, 
                                facecolor='#C0C0C0', edgecolor='#A0A0A0', linewidth=2, zorder=4)
    ax.add_patch(tail_wing)
    
    # Vertical stabilizer
    vert_stab_points = [[airplane_x - 15, airplane_y + 2], [airplane_x - 15, airplane_y + 12], 
                       [airplane_x - 8, airplane_y + 8], [airplane_x - 8, airplane_y + 2]]
    vert_stab = patches.Polygon(vert_stab_points, facecolor='#C0C0C0', edgecolor='#A0A0A0', linewidth=2, zorder=4)
    ax.add_patch(vert_stab)
    
    # Windows
    window_positions = [airplane_x - 10, airplane_x - 5, airplane_x, airplane_x + 5, airplane_x + 10]
    for win_x in window_positions:
        window = patches.Circle((win_x, airplane_y + 1), 1.2, 
                              facecolor='#87CEEB', edgecolor='#4682B4', linewidth=1, zorder=6)
        ax.add_patch(window)
    
    # Engines
    engine1 = patches.Circle((airplane_x - 2, airplane_y - 6), 2.5, 
                           facecolor='#A0A0A0', edgecolor='#808080', linewidth=2, zorder=4)
    engine2 = patches.Circle((airplane_x + 8, airplane_y - 6), 2.5, 
                           facecolor='#A0A0A0', edgecolor='#808080', linewidth=2, zorder=4)
    ax.add_patch(engine1)
    ax.add_patch(engine2)
    
    # Propellers/Engine intakes
    prop1 = patches.Circle((airplane_x - 2, airplane_y - 6), 1, 
                         facecolor='#606060', zorder=5)
    prop2 = patches.Circle((airplane_x + 8, airplane_y - 6), 1, 
                         facecolor='#606060', zorder=5)
    ax.add_patch(prop1)
    ax.add_patch(prop2)
    
    # Add some motion lines behind the airplane
    for i in range(5):
        y_offset = airplane_y + (i - 2) * 2
        motion_line = patches.Rectangle((airplane_x - 25 - i*2, y_offset - 0.3), 8 - i, 0.6, 
                                      facecolor='white', alpha=0.6 - i*0.1, zorder=2)
        ax.add_patch(motion_line)
    
    # Add Teachers Day text
    ax.text(50, 25, "Happy Teachers' Day!", 
           fontsize=28, fontweight='bold', ha='center', va='center',
           color='#2E4057', zorder=10)
    
    # Add subtitle
    ax.text(50, 18, "Soaring to New Heights with Great Teachers", 
           fontsize=16, ha='center', va='center',
           color='#34495E', style='italic', zorder=10)
    
    # Add decorative elements
    # School/education symbols floating around
    symbols = ['📚', '✏️', '🎓', '📝', '🍎']
    symbol_positions = [(25, 30), (75, 35), (20, 60), (80, 25), (85, 55)]
    
    for symbol, (sx, sy) in zip(symbols, symbol_positions):
        ax.text(sx, sy, symbol, fontsize=20, ha='center', va='center', zorder=8)
    
    # Add a banner trailing from the airplane
    banner_points = [[airplane_x - 20, airplane_y + 15], [airplane_x - 45, airplane_y + 20],
                    [airplane_x - 45, airplane_y + 25], [airplane_x - 20, airplane_y + 20]]
    banner = patches.Polygon(banner_points, facecolor='#FF6B6B', edgecolor='#E74C3C', 
                           linewidth=2, alpha=0.9, zorder=3)
    ax.add_patch(banner)
    
    # Banner text
    ax.text(airplane_x - 32.5, airplane_y + 22.5, "Thank You\nTeachers!", 
           fontsize=10, fontweight='bold', ha='center', va='center',
           color='white', zorder=7)
    
    # Remove axes
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    plt.tight_layout()
    
    # Save the image
    plt.savefig('/workspace/teachers_day_airplane.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.savefig('/workspace/teachers_day_airplane.jpg', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    
    print("Teachers Day airplane image created successfully!")
    print("Files saved as:")
    print("- teachers_day_airplane.png")
    print("- teachers_day_airplane.jpg")
    
    # plt.show()  # Commented out for headless environment

if __name__ == "__main__":
    create_teachers_day_airplane_image()