import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ArrowStyle

output_dir = r"E:\Google-AntiGravity-Projects\1.PPTs-Lecture-Notes\LASERS-BSc.Physics\digitized-diagrams"
os.makedirs(output_dir, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# 1. SPONTANEOUS VS STIMULATED EMISSION
def create_emission_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), dpi=300, facecolor='white')
    
    # Left: Spontaneous Emission
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 7)
    ax1.axis('off')
    ax1.set_title("SPONTANEOUS EMISSION", fontsize=18, fontweight='bold', color='#1A237E', pad=20)
    
    # State lines for Before & After
    # (a) Before
    ax1.text(2.5, 6.2, "(a) Before Emission", fontsize=14, fontweight='bold', ha='center', color='#0D47A1')
    ax1.hlines(y=[5.2, 2.0], xmin=0.5, xmax=4.5, colors=['#E53935', '#1E88E5'], linewidth=3.5)
    ax1.text(0.3, 5.2, r"$E_2$", fontsize=15, fontweight='bold', va='center', ha='right', color='#D32F2F')
    ax1.text(4.7, 5.2, "Excited state", fontsize=12, fontweight='bold', va='center', color='#C62828')
    ax1.text(0.3, 2.0, r"$E_1$", fontsize=15, fontweight='bold', va='center', ha='right', color='#1565C0')
    ax1.text(4.7, 2.0, "Ground state", fontsize=12, fontweight='bold', va='center', color='#1565C0')
    # Electron at E2
    circle1 = plt.Circle((2.5, 5.2), 0.22, color='#E53935', ec='#B71C1C', lw=2, zorder=5)
    ax1.add_patch(circle1)
    ax1.text(2.5, 5.6, "Excited Atom", fontsize=11, ha='center', color='#B71C1C', fontweight='bold')
    
    # (b) After
    ax1.text(7.5, 6.2, "(b) After Emission", fontsize=14, fontweight='bold', ha='center', color='#0D47A1')
    ax1.hlines(y=[5.2, 2.0], xmin=5.5, xmax=9.5, colors=['#E53935', '#1E88E5'], linewidth=3.5)
    ax1.text(5.3, 5.2, r"$E_2$", fontsize=15, fontweight='bold', va='center', ha='right', color='#D32F2F')
    ax1.text(9.7, 5.2, "Excited state", fontsize=12, fontweight='bold', va='center', color='#C62828')
    ax1.text(5.3, 2.0, r"$E_1$", fontsize=15, fontweight='bold', va='center', ha='right', color='#1565C0')
    ax1.text(9.7, 2.0, "Ground state", fontsize=12, fontweight='bold', va='center', color='#1565C0')
    # Transition arrow
    ax1.annotate('', xy=(7.2, 2.15), xytext=(7.2, 5.15),
                 arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", lw=2.5, color='#D81B60', ls='--'))
    ax1.text(6.8, 3.6, "Spontaneous\njump\n(random time)", fontsize=10, ha='right', va='center', color='#880E4F', fontweight='bold')
    # Electron at E1
    circle2 = plt.Circle((7.2, 2.0), 0.22, color='#1E88E5', ec='#0D47A1', lw=2, zorder=5)
    ax1.add_patch(circle2)
    # Emitted photon wave
    x_wave = np.linspace(7.6, 9.4, 150)
    y_wave = 3.6 + 0.3 * np.sin(2 * np.pi * 3.5 * (x_wave - 7.6) / 1.8)
    ax1.plot(x_wave, y_wave, color='#FF6F00', lw=3)
    ax1.annotate('', xy=(9.5, 3.6), xytext=(9.2, 3.6),
                 arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", lw=3, color='#FF6F00'))
    ax1.text(8.5, 4.2, r"$h\nu = E_2 - E_1$", fontsize=12, fontweight='bold', color='#E65100', ha='center')
    ax1.text(8.5, 3.0, "Emitted Photon\n(Random Phase & Dir)", fontsize=10, fontweight='bold', color='#E65100', ha='center')
    
    # Info badge at bottom
    ax1.text(5.0, 0.7, "* Occurs naturally without external trigger\n* Life time ~ 10⁻⁸ s | Incoherent & Broad spectrum (Like a lamp)", 
             fontsize=12, ha='center', va='center', color='#37474F',
             bbox=dict(boxstyle="round,pad=0.6", fc="#ECEFF1", ec="#90A4AE", lw=1.5))

    # Right: Stimulated Emission
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 7)
    ax2.axis('off')
    ax2.set_title("STIMULATED (INDUCED) EMISSION", fontsize=18, fontweight='bold', color='#B71C1C', pad=20)
    
    # (a) Before
    ax2.text(2.5, 6.2, "(a) Before Stimulated Emission", fontsize=14, fontweight='bold', ha='center', color='#B71C1C')
    ax2.hlines(y=[5.2, 2.0], xmin=0.5, xmax=4.5, colors=['#E53935', '#1E88E5'], linewidth=3.5)
    ax2.text(0.3, 5.2, r"$E_2$", fontsize=15, fontweight='bold', va='center', ha='right', color='#D32F2F')
    ax2.text(0.3, 2.0, r"$E_1$", fontsize=15, fontweight='bold', va='center', ha='right', color='#1565C0')
    # Electron at E2
    circle3 = plt.Circle((2.8, 5.2), 0.22, color='#E53935', ec='#B71C1C', lw=2, zorder=5)
    ax2.add_patch(circle3)
    # Incident photon wave
    x_in = np.linspace(0.6, 2.2, 100)
    y_in = 4.2 + 0.25 * np.sin(2 * np.pi * 3 * (x_in - 0.6) / 1.6)
    ax2.plot(x_in, y_in, color='#00897B', lw=3)
    ax2.annotate('', xy=(2.3, 4.2), xytext=(2.0, 4.2),
                 arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", lw=3, color='#00897B'))
    ax2.text(1.4, 4.7, "Incident Photon", fontsize=11, fontweight='bold', color='#00695C', ha='center')
    ax2.text(1.4, 3.7, r"$h\nu = E_2 - E_1$", fontsize=12, fontweight='bold', color='#00695C', ha='center')
    
    # (b) After
    ax2.text(7.5, 6.2, "(b) After Stimulated Emission", fontsize=14, fontweight='bold', ha='center', color='#B71C1C')
    ax2.hlines(y=[5.2, 2.0], xmin=5.5, xmax=9.5, colors=['#E53935', '#1E88E5'], linewidth=3.5)
    ax2.text(5.3, 5.2, r"$E_2$", fontsize=15, fontweight='bold', va='center', ha='right', color='#D32F2F')
    ax2.text(5.3, 2.0, r"$E_1$", fontsize=15, fontweight='bold', va='center', ha='right', color='#1565C0')
    # Transition arrow
    ax2.annotate('', xy=(6.8, 2.15), xytext=(6.8, 5.15),
                 arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", lw=2.5, color='#D81B60', ls='--'))
    # Electron at E1
    circle4 = plt.Circle((6.8, 2.0), 0.22, color='#1E88E5', ec='#0D47A1', lw=2, zorder=5)
    ax2.add_patch(circle4)
    # Two coherent emitted photons
    x_out1 = np.linspace(7.2, 9.4, 120)
    y_out1 = 4.4 + 0.25 * np.sin(2 * np.pi * 3.5 * (x_out1 - 7.2) / 2.2)
    ax2.plot(x_out1, y_out1, color='#D81B60', lw=3)
    ax2.annotate('', xy=(9.5, 4.4), xytext=(9.2, 4.4),
                 arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", lw=3, color='#D81B60'))
    
    y_out2 = 3.2 + 0.25 * np.sin(2 * np.pi * 3.5 * (x_out1 - 7.2) / 2.2)
    ax2.plot(x_out1, y_out2, color='#D81B60', lw=3)
    ax2.annotate('', xy=(9.5, 3.2), xytext=(9.2, 3.2),
                 arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", lw=3, color='#D81B60'))
    
    ax2.text(8.3, 5.0, "2 Photons In-Phase!", fontsize=12, fontweight='bold', color='#C2185B', ha='center')
    ax2.text(8.3, 2.6, "Identical Frequency, Phase,\nPolarization & Direction", fontsize=10, fontweight='bold', color='#880E4F', ha='center')

    # Info badge at bottom
    ax2.text(5.0, 0.7, "* Induced by external photon (Einstein 1917)\n* Foundation of LASER amplification | Highly Coherent & Monochromatic", 
             fontsize=12, ha='center', va='center', color='#880E4F',
             bbox=dict(boxstyle="round,pad=0.6", fc="#FCE4EC", ec="#F48FB1", lw=1.5))
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "spontaneous_vs_stimulated_emission.png"), dpi=300)
    plt.close()
    print("Created spontaneous_vs_stimulated_emission.png")

create_emission_diagram()
