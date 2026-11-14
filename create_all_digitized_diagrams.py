# Digitized, High-Resolution Diagram Generator for LASERS (B.Sc. Physics)
# Generates 300 DPI publication-quality diagrams with zero overlapping text, glossy modern aesthetics, and clear physical rigor.

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

output_dir = r"E:\Google-AntiGravity-Projects\1.PPTs-Lecture-Notes\LASERS-BSc.Physics\digitized-diagrams"
os.makedirs(output_dir, exist_ok=True)

plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['mathtext.fontset'] = 'dejavusans'

# ==============================================================================
# 1. SPONTANEOUS VS STIMULATED EMISSION
# ==============================================================================
def create_emission_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8.5), dpi=300, facecolor='white')
    
    # ------------------ Left: Spontaneous Emission ------------------
    ax1.set_xlim(0, 11)
    ax1.set_ylim(0, 8.5)
    ax1.axis('off')
    ax1.set_title("SPONTANEOUS EMISSION", fontsize=20, fontweight='bold', color='#1A237E', pad=25)
    
    # (a) Before
    ax1.text(2.6, 7.6, "(a) Before", fontsize=16, fontweight='bold', ha='center', color='#0D47A1', zorder=10)
    ax1.hlines(y=[5.8, 2.6], xmin=0.8, xmax=4.4, colors=['#E53935', '#1E88E5'], linewidth=4)
    ax1.text(0.5, 5.8, r"$E_2$", fontsize=18, fontweight='bold', va='center', ha='right', color='#D32F2F', zorder=10)
    ax1.text(2.6, 6.25, "Excited state", fontsize=13, fontweight='bold', ha='center', color='#C62828', zorder=10)
    ax1.text(0.5, 2.6, r"$E_1$", fontsize=18, fontweight='bold', va='center', ha='right', color='#1565C0', zorder=10)
    ax1.text(2.6, 2.15, "Ground state", fontsize=13, fontweight='bold', ha='center', color='#1565C0', zorder=10)
    
    # Electron at E2
    circle1 = plt.Circle((2.6, 5.8), 0.22, color='#E53935', ec='#B71C1C', lw=2.5, zorder=5)
    ax1.add_patch(circle1)
    
    # (b) After
    ax1.text(8.2, 7.6, "(b) After", fontsize=16, fontweight='bold', ha='center', color='#0D47A1', zorder=10)
    ax1.hlines(y=[5.8, 2.6], xmin=6.4, xmax=10.0, colors=['#E53935', '#1E88E5'], linewidth=4)
    ax1.text(6.1, 5.8, r"$E_2$", fontsize=18, fontweight='bold', va='center', ha='right', color='#D32F2F', zorder=10)
    ax1.text(8.2, 6.25, "Excited state", fontsize=13, fontweight='bold', ha='center', color='#C62828', zorder=10)
    ax1.text(6.1, 2.6, r"$E_1$", fontsize=18, fontweight='bold', va='center', ha='right', color='#1565C0', zorder=10)
    ax1.text(8.2, 2.15, "Ground state", fontsize=13, fontweight='bold', ha='center', color='#1565C0', zorder=10)
    
    # Downward transition arrow
    ax1.annotate('', xy=(7.2, 2.75), xytext=(7.2, 5.65),
                 arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.6", lw=2.8, color='#880E4F', ls='--'))
    ax1.text(7.0, 4.2, "Natural\nJump\n(~10⁻⁸ s)", fontsize=11, ha='right', va='center', color='#880E4F', fontweight='bold', zorder=10)
    
    # Electron at E1
    circle2 = plt.Circle((7.2, 2.6), 0.22, color='#1E88E5', ec='#0D47A1', lw=2.5, zorder=5)
    ax1.add_patch(circle2)
    
    # Emitted photon wave (offset to the right, separate from text)
    x_wave = np.linspace(8.0, 10.4, 150)
    y_wave = 4.2 + 0.3 * np.sin(2 * np.pi * 3.5 * (x_wave - 8.0) / 2.4)
    ax1.plot(x_wave, y_wave, color='#FF6F00', lw=3.2)
    ax1.annotate('', xy=(10.5, 4.2), xytext=(10.2, 4.2),
                 arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.55", lw=3.2, color='#FF6F00'))
    ax1.text(9.2, 5.0, r"$h\nu = E_2 - E_1$", fontsize=14, fontweight='bold', color='#E65100', ha='center', zorder=10)
    ax1.text(9.2, 3.4, "Emitted photon\n(Random direction & phase)", fontsize=11, fontweight='bold', color='#E65100', ha='center', zorder=10)
    
    # Bottom Summary
    ax1.text(5.5, 0.8, "• Spontaneous decay without external stimulus\n• Photons emitted in random directions & random phases\n• Incoherent, broad spectrum (Ordinary light, e.g., light bulb)", 
             fontsize=12, ha='center', va='center', color='#263238', fontweight='medium', zorder=10,
             bbox=dict(boxstyle="round,pad=0.7", fc="#ECEFF1", ec="#90A4AE", lw=1.8))

    # ------------------ Right: Stimulated Emission ------------------
    ax2.set_xlim(0, 11)
    ax2.set_ylim(0, 8.5)
    ax2.axis('off')
    ax2.set_title("STIMULATED (INDUCED) EMISSION", fontsize=20, fontweight='bold', color='#B71C1C', pad=25)
    
    # (a) Before
    ax2.text(2.6, 7.6, "(a) Before", fontsize=16, fontweight='bold', ha='center', color='#B71C1C', zorder=10)
    ax2.hlines(y=[5.8, 2.6], xmin=0.8, xmax=4.4, colors=['#E53935', '#1E88E5'], linewidth=4)
    ax2.text(0.5, 5.8, r"$E_2$", fontsize=18, fontweight='bold', va='center', ha='right', color='#D32F2F', zorder=10)
    ax2.text(2.6, 6.25, "Excited state", fontsize=13, fontweight='bold', ha='center', color='#C62828', zorder=10)
    ax2.text(0.5, 2.6, r"$E_1$", fontsize=18, fontweight='bold', va='center', ha='right', color='#1565C0', zorder=10)
    ax2.text(2.6, 2.15, "Ground state", fontsize=13, fontweight='bold', ha='center', color='#1565C0', zorder=10)
    
    # Electron at E2
    circle3 = plt.Circle((3.4, 5.8), 0.22, color='#E53935', ec='#B71C1C', lw=2.5, zorder=5)
    ax2.add_patch(circle3)
    
    # Incoming photon
    x_in = np.linspace(0.8, 2.4, 100)
    y_in = 4.2 + 0.28 * np.sin(2 * np.pi * 3 * (x_in - 0.8) / 1.6)
    ax2.plot(x_in, y_in, color='#00897B', lw=3.2)
    ax2.annotate('', xy=(2.5, 4.2), xytext=(2.2, 4.2),
                 arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.55", lw=3.2, color='#00897B'))
    ax2.text(1.6, 5.0, "Incident photon", fontsize=12, fontweight='bold', color='#00695C', ha='center', zorder=10)
    ax2.text(1.6, 3.4, r"$h\nu = E_2 - E_1$", fontsize=12, fontweight='bold', color='#00695C', ha='center', zorder=10)
    
    # (b) After
    ax2.text(8.2, 7.6, "(b) After", fontsize=16, fontweight='bold', ha='center', color='#B71C1C', zorder=10)
    ax2.hlines(y=[5.8, 2.6], xmin=6.4, xmax=10.0, colors=['#E53935', '#1E88E5'], linewidth=4)
    ax2.text(6.1, 5.8, r"$E_2$", fontsize=18, fontweight='bold', va='center', ha='right', color='#D32F2F', zorder=10)
    ax2.text(8.2, 6.25, "Excited state", fontsize=13, fontweight='bold', ha='center', color='#C62828', zorder=10)
    ax2.text(6.1, 2.6, r"$E_1$", fontsize=18, fontweight='bold', va='center', ha='right', color='#1565C0', zorder=10)
    ax2.text(8.2, 2.15, "Ground state", fontsize=13, fontweight='bold', ha='center', color='#1565C0', zorder=10)
    
    # Induced transition arrow
    ax2.annotate('', xy=(7.2, 2.75), xytext=(7.2, 5.65),
                 arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.6", lw=2.8, color='#D81B60', ls='--'))
    ax2.text(7.0, 4.2, "Triggered\nTransition", fontsize=11, ha='right', va='center', color='#AD1457', fontweight='bold', zorder=10)
    
    # Electron at E1
    circle4 = plt.Circle((7.2, 2.6), 0.22, color='#1E88E5', ec='#0D47A1', lw=2.5, zorder=5)
    ax2.add_patch(circle4)
    
    # Two identical photons emitted together
    x_out = np.linspace(8.0, 10.3, 120)
    y_out1 = 4.8 + 0.28 * np.sin(2 * np.pi * 3.5 * (x_out - 8.0) / 2.3)
    y_out2 = 3.4 + 0.28 * np.sin(2 * np.pi * 3.5 * (x_out - 8.0) / 2.3)
    ax2.plot(x_out, y_out1, color='#D81B60', lw=3.2)
    ax2.annotate('', xy=(10.4, 4.8), xytext=(10.1, 4.8),
                 arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.55", lw=3.2, color='#D81B60'))
    ax2.text(10.5, 4.8, r"$h\nu$", fontsize=13, fontweight='bold', color='#D81B60', va='center', zorder=10)
    
    ax2.plot(x_out, y_out2, color='#D81B60', lw=3.2)
    ax2.annotate('', xy=(10.4, 3.4), xytext=(10.1, 3.4),
                 arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.55", lw=3.2, color='#D81B60'))
    ax2.text(10.5, 3.4, r"$h\nu$", fontsize=13, fontweight='bold', color='#D81B60', va='center', zorder=10)
    
    ax2.text(9.2, 5.65, "2 Identical Coherent Photons!", fontsize=12, fontweight='bold', color='#C2185B', ha='center', zorder=10)
    ax2.text(9.2, 2.6, "Exact same phase, frequency,\ndirection & polarization", fontsize=11, fontweight='bold', color='#880E4F', ha='center', zorder=10)

    # Bottom Summary
    ax2.text(5.5, 0.8, "• Induced by an external stimulating photon (hν = E₂ - E₁)\n• 1 incoming photon triggers emission of a 2nd identical photon (Amplification)\n• Highly Coherent, Monochromatic & Directional (Principle of LASER)", 
             fontsize=12, ha='center', va='center', color='#880E4F', fontweight='medium', zorder=10,
             bbox=dict(boxstyle="round,pad=0.7", fc="#FCE4EC", ec="#F48FB1", lw=1.8))
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "spontaneous_vs_stimulated_emission.png"), dpi=300)
    plt.close()
    print("Saved spontaneous_vs_stimulated_emission.png")


# ==============================================================================
# 2. METASTABLE STATES & POPULATION INVERSION (COMPLETELY DE-CLUTTERED)
# ==============================================================================
def create_population_inversion_diagram():
    fig, ax = plt.subplots(figsize=(16, 9.5), dpi=300, facecolor='white')
    ax.set_xlim(0, 16.5)
    ax.set_ylim(0, 9.5)
    ax.axis('off')
    ax.set_title("POPULATION INVERSION & METASTABLE STATE", fontsize=22, fontweight='bold', color='#0D47A1', pad=25)
    
    # 3 Energy Levels
    y_E3 = 7.5
    y_E2 = 4.8
    y_E1 = 2.0
    
    # Level lines
    ax.hlines(y=y_E3, xmin=1.5, xmax=12.8, colors='#E53935', linewidth=4.5)
    ax.text(1.2, y_E3, r"$E_3$", fontsize=22, fontweight='bold', va='center', ha='right', color='#D32F2F', zorder=10)
    ax.text(13.1, y_E3, "Excited State (Short lifetime ~ 10⁻⁸ s)", fontsize=13, fontweight='bold', va='center', color='#C62828', zorder=10)
    
    ax.hlines(y=y_E2, xmin=3.5, xmax=12.8, colors='#8E24AA', linewidth=4.5)
    ax.text(3.2, y_E2, r"$E_2$", fontsize=22, fontweight='bold', va='center', ha='right', color='#7B1FA2', zorder=10)
    ax.text(13.1, y_E2, "Metastable State (Long lifetime ~ 10⁻³ s)", fontsize=13, fontweight='bold', va='center', color='#6A1B9A', zorder=10)
    
    ax.hlines(y=y_E1, xmin=1.5, xmax=12.8, colors='#1E88E5', linewidth=4.5)
    ax.text(1.2, y_E1, r"$E_1$", fontsize=22, fontweight='bold', va='center', ha='right', color='#1565C0', zorder=10)
    ax.text(13.1, y_E1, "Ground State (Normal minimum energy)", fontsize=13, fontweight='bold', va='center', color='#0D47A1', zorder=10)
    
    # Atoms in Ground State E1 (Few atoms: N1 is depleted)
    n1_x = [2.2, 3.0, 5.0, 6.2, 11.5, 12.3]
    for x in n1_x:
        ax.add_patch(plt.Circle((x, y_E1), 0.18, color='#1E88E5', ec='#0D47A1', lw=2, zorder=5))
    ax.text(4.0, y_E1 - 0.45, r"$N_1\ \text{(Depleted lower population)}$", fontsize=13, fontweight='bold', color='#1565C0', zorder=10)
    
    # Atoms in E3 (transient, very few)
    n3_x = [2.6, 3.8, 5.0]
    for x in n3_x:
        ax.add_patch(plt.Circle((x, y_E3), 0.18, color='#D32F2F', ec='#B71C1C', lw=2, zorder=5))
        
    # Atoms in Metastable state E2 (Dense accumulation: N2 > N1)
    n2_x = [4.0, 4.7, 5.4, 6.1, 6.8, 7.5, 8.2, 8.9, 9.6, 10.3, 11.0, 11.7, 12.4]
    for x in n2_x:
        ax.add_patch(plt.Circle((x, y_E2), 0.18, color='#8E24AA', ec='#4A148C', lw=2, zorder=5))
    ax.text(4.0, y_E2 + 0.45, r"$N_2\ \text{(Dense accumulation)}$", fontsize=13, fontweight='bold', color='#6A1B9A', zorder=10)
    
    # Pumping arrow from E1 to E3
    ax.annotate('', xy=(2.0, y_E3 - 0.1), xytext=(2.0, y_E1 + 0.1),
                arrowprops=dict(arrowstyle="->,head_width=0.5,head_length=0.7", lw=3.5, color='#43A047'))
    ax.text(1.7, (y_E1 + y_E3)/2, "PUMPING\nTransition\n(Optical / Electrical)", 
            fontsize=12, fontweight='bold', color='#2E7D32', ha='right', va='center', zorder=10)
    
    # Fast Radiationless transition from E3 to E2
    # Arrow line starts at (4.5, y_E3 - 0.15) and ends at (6.8, y_E2 + 0.15)
    ax.annotate('', xy=(6.8, y_E2 + 0.15), xytext=(4.5, y_E3 - 0.15),
                arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.65", lw=3.0, color='#FF8F00', ls='-.'))
    # Label placed safely ABOVE the diagonal arrow, completely clear
    ax.text(5.6, 6.6, "Fast Radiationless Transition\n(~ 10⁻⁸ s, heat to crystal lattice)", 
            fontsize=11.5, fontweight='bold', color='#E65100', ha='center', va='bottom', zorder=10)
    
    # Population Inversion Badge (Placed prominently at x=8.8, y=6.2)
    ax.text(8.8, 6.1, "POPULATION INVERSION\nAchieved:  N₂ > N₁", 
            fontsize=15, fontweight='bold', color='#D81B60', ha='center', va='center', zorder=10,
            bbox=dict(boxstyle="round,pad=0.6", fc="#FFF0F5", ec="#E91E63", lw=2.2))
    
    # Stimulated Laser Transition from E2 to E1
    ax.annotate('', xy=(9.8, y_E1 + 0.15), xytext=(9.8, y_E2 - 0.15),
                arrowprops=dict(arrowstyle="->,head_width=0.5,head_length=0.7", lw=3.5, color='#D81B60'))
    ax.text(9.4, (y_E1 + y_E2)/2, "STIMULATED\nTRANSITION\n(Laser Action)", 
            fontsize=12, fontweight='bold', color='#C2185B', ha='right', va='center', zorder=10)
    
    # Wave of laser photon (offset cleanly to the right of the vertical arrow)
    x_las = np.linspace(10.2, 12.6, 120)
    y_las = (y_E1 + y_E2)/2 + 0.28 * np.sin(2 * np.pi * 3.5 * (x_las - 10.2) / 2.4)
    ax.plot(x_las, y_las, color='#D81B60', lw=3.2)
    ax.annotate('', xy=(12.7, (y_E1 + y_E2)/2), xytext=(12.4, (y_E1 + y_E2)/2),
                arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.55", lw=3.2, color='#D81B60'))
    ax.text(11.4, (y_E1 + y_E2)/2 + 0.55, r"Coherent Laser Light ($h\nu = E_2 - E_1$)", fontsize=11.5, fontweight='bold', color='#D81B60', ha='center', zorder=10)

    # Explanatory card at bottom
    ax.text(8.25, 0.65, 
            "Metastable State: Excited state with ~10⁵ times longer lifetime (~10⁻³ s). Atoms 'wait' here instead of dropping immediately.\n"
            "Population Inversion: A non-equilibrium state where the higher state has more atoms than lower state (N₂ > N₁), essential for optical amplification.",
            fontsize=12, ha='center', va='center', color='#37474F', fontweight='medium', zorder=10,
            bbox=dict(boxstyle="round,pad=0.7", fc="#F3E5F5", ec="#AB47BC", lw=1.6))
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "metastable_population_inversion.png"), dpi=300)
    plt.close()
    print("Saved metastable_population_inversion.png")


# ==============================================================================
# 3. PRINCIPLE OF LASER (3 KEY STEPS)
# ==============================================================================
def create_laser_principle_diagram():
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300, facecolor='white')
    ax.set_xlim(0, 16.5)
    ax.set_ylim(0, 9.2)
    ax.axis('off')
    ax.set_title("PRINCIPLE OF LASER ACTION (3 KEY STEPS)", fontsize=22, fontweight='bold', color='#B71C1C', pad=25)
    
    y_E2 = 7.2
    y_E1 = 4.4
    y_E0 = 1.8
    
    # Levels
    ax.hlines(y=y_E2, xmin=1.5, xmax=12.5, colors='#D32F2F', linewidth=4)
    ax.text(1.2, y_E2, r"$E_2$", fontsize=22, fontweight='bold', va='center', ha='right', color='#D32F2F', zorder=10)
    ax.text(12.8, y_E2, "Upper Excited Level", fontsize=13, fontweight='bold', va='center', color='#D32F2F', zorder=10)
    
    ax.hlines(y=y_E1, xmin=5.0, xmax=12.5, colors='#7B1FA2', linewidth=4)
    ax.text(4.7, y_E1, r"$E_1$", fontsize=22, fontweight='bold', va='center', ha='right', color='#7B1FA2', zorder=10)
    ax.text(12.8, y_E1, "Metastable Level (Long life)", fontsize=13, fontweight='bold', va='center', color='#7B1FA2', zorder=10)
    
    ax.hlines(y=y_E0, xmin=1.5, xmax=12.5, colors='#1565C0', linewidth=4)
    ax.text(1.2, y_E0, r"$E_0$", fontsize=22, fontweight='bold', va='center', ha='right', color='#1565C0', zorder=10)
    ax.text(12.8, y_E0, "Ground Level", fontsize=13, fontweight='bold', va='center', color='#1565C0', zorder=10)
    
    # Step 1: Pumping
    ax.annotate('', xy=(3.0, y_E2 - 0.1), xytext=(3.0, y_E0 + 0.1),
                arrowprops=dict(arrowstyle="->,head_width=0.55,head_length=0.75", lw=4, color='#2E7D32'))
    
    circle_p1 = plt.Circle((3.0, 4.5), 0.45, color='#E8F5E9', ec='#2E7D32', lw=2.5, zorder=6)
    ax.add_patch(circle_p1)
    ax.text(3.0, 4.5, "1", fontsize=16, fontweight='bold', ha='center', va='center', color='#1B5E20', zorder=10)
    
    ax.text(2.6, 5.8, "Step 1: Pumping", fontsize=14, fontweight='bold', color='#1B5E20', ha='right', zorder=10)
    
    # Incoming pumping photon wave (placed safely below title text)
    x_p = np.linspace(1.2, 2.5, 70)
    y_p = 3.2 + 0.25 * np.sin(2 * np.pi * 3.5 * (x_p - 1.2) / 1.3)
    ax.plot(x_p, y_p, color='#43A047', lw=2.8)
    ax.annotate('', xy=(2.6, 3.2), xytext=(2.4, 3.2),
                arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", lw=2.8, color='#43A047'))
    ax.text(1.8, 3.7, r"$h\nu_0 = E_2 - E_0$", fontsize=12, fontweight='bold', color='#1B5E20', ha='center', zorder=10)
    
    # Step 2: Spontaneous transition to Metastable state E1
    ax.annotate('', xy=(7.0, y_E1 + 0.1), xytext=(7.0, y_E2 - 0.1),
                arrowprops=dict(arrowstyle="->,head_width=0.5,head_length=0.7", lw=3.5, color='#F57C00'))
    
    circle_p2 = plt.Circle((7.0, 5.8), 0.45, color='#FFF3E0', ec='#F57C00', lw=2.5, zorder=6)
    ax.add_patch(circle_p2)
    ax.text(7.0, 5.8, "2", fontsize=16, fontweight='bold', ha='center', va='center', color='#E65100', zorder=10)
    
    ax.text(7.5, 6.1, "Step 2: Spontaneous / Radiationless\nTransition to Metastable State", 
            fontsize=13, fontweight='bold', color='#E65100', va='center', zorder=10)
    ax.text(7.5, 5.0, "Atoms rapidly accumulate here\ncreating Population Inversion (N₁ > N₀)", 
            fontsize=11.5, fontweight='bold', color='#BF360C', va='center', zorder=10)
    
    # Step 3: Stimulated Emission
    ax.annotate('', xy=(10.2, y_E0 + 0.1), xytext=(10.2, y_E1 - 0.1),
                arrowprops=dict(arrowstyle="->,head_width=0.55,head_length=0.75", lw=4, color='#D81B60'))
    
    circle_p3 = plt.Circle((10.2, 3.1), 0.45, color='#FCE4EC', ec='#D81B60', lw=2.5, zorder=6)
    ax.add_patch(circle_p3)
    ax.text(10.2, 3.1, "3", fontsize=16, fontweight='bold', ha='center', va='center', color='#880E4F', zorder=10)
    
    ax.text(10.7, 3.6, "Step 3: Stimulated Emission", fontsize=13.5, fontweight='bold', color='#C2185B', va='center', zorder=10)
    ax.text(10.7, 2.8, r"$h\nu = E_1 - E_0$", fontsize=12.5, fontweight='bold', color='#880E4F', va='center', zorder=10)
    ax.text(10.7, 2.1, "Triggered by passing photon;\nreleases identical coherent photon", 
            fontsize=11, fontweight='bold', color='#880E4F', va='center', zorder=10)
    
    # Bottom Summary
    ax.text(8.0, 0.65, 
            "The 3 Pillars of Laser Operation:\n"
            "1. Pumping elevates atoms to excited state  |  2. Rapid decay creates Population Inversion at Metastable level\n"
            "3. Stimulated emission triggers a chain reaction of coherent photons reflected repeatedly in optical resonator",
            fontsize=12, ha='center', va='center', color='#37474F', fontweight='medium', zorder=10,
            bbox=dict(boxstyle="round,pad=0.7", fc="#FFFDE7", ec="#FBC02D", lw=1.8))
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "laser_principle_action.png"), dpi=300)
    plt.close()
    print("Saved laser_principle_action.png")


# ==============================================================================
# 4. COMPONENTS OF A LASER
# ==============================================================================
def create_laser_components_diagram():
    fig, ax = plt.subplots(figsize=(16, 8.5), dpi=300, facecolor='white')
    ax.set_xlim(0, 16.5)
    ax.set_ylim(0, 8.8)
    ax.axis('off')
    ax.set_title("MAIN COMPONENTS OF A LASER SYSTEM", fontsize=22, fontweight='bold', color='#1A237E', pad=25)
    
    # 1. Energy Source Box (Top)
    p_energy = FancyBboxPatch((4.5, 6.2), 6.0, 1.4, boxstyle="round,pad=0.2",
                              fc="#FFE082", ec="#FFA000", lw=2.5, zorder=3)
    ax.add_patch(p_energy)
    ax.text(7.5, 6.9, "1. ENERGY SOURCE\n(Pumping System)", fontsize=14, fontweight='bold', ha='center', va='center', color='#E65100', zorder=10)
    
    # Pumping arrows downwards
    for x_arr in [5.5, 6.5, 7.5, 8.5, 9.5]:
        ax.annotate('', xy=(x_arr, 4.7), xytext=(x_arr, 6.1),
                    arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", lw=2.8, color='#E65100'))
    ax.text(7.5, 5.4, "Pumping Energy (Optical / Electrical / Chemical)", fontsize=11.5, fontweight='bold', ha='center', color='#BF360C', zorder=10,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#FFA000", lw=1.2))

    # 2. Active Medium (Center Bar)
    p_med = FancyBboxPatch((2.2, 2.7), 10.6, 1.7, boxstyle="square,pad=0.0",
                           fc="#E1F5FE", ec="#0288D1", lw=3.0, zorder=2)
    ax.add_patch(p_med)
    ax.text(7.5, 3.7, "2. ACTIVE MEDIUM (Laser Material)\n(Ruby Crystal / He-Ne Gas / Semiconductor)", 
            fontsize=14, fontweight='bold', ha='center', va='center', color='#01579B', zorder=10)
    ax.text(7.5, 3.1, "Provides atoms with metastable state to achieve Population Inversion", 
            fontsize=11.5, ha='center', va='center', color='#0277BD', style='italic', zorder=10)

    # 3. Mirrors (Optical Resonator Cavity)
    # Fully reflective mirror (Left)
    ax.fill_between([1.8, 2.2], [2.4, 2.4], [4.7, 4.7], color='#37474F', zorder=4)
    for y_h in np.linspace(2.5, 4.6, 8):
        ax.plot([1.5, 1.8], [y_h - 0.2, y_h], color='#455A64', lw=2.5)
    ax.text(1.3, 1.6, "3(a). Fully Reflective\nMirror (100% R)", fontsize=12, fontweight='bold', ha='center', color='#263238', zorder=10)
    ax.annotate('', xy=(2.0, 2.4), xytext=(1.5, 1.9),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.4", lw=2, color='#37474F'))

    # Partially reflective mirror (Right)
    ax.fill_between([12.8, 13.2], [2.4, 2.4], [4.7, 4.7], color='#78909C', alpha=0.9, zorder=4)
    for y_h in np.linspace(2.5, 4.6, 8):
        ax.plot([13.2, 13.5], [y_h, y_h + 0.2], color='#90A4AE', lw=2.5)
    ax.text(13.4, 1.6, "3(b). Partially Reflective\nMirror (~90-99% R)", fontsize=12, fontweight='bold', ha='center', color='#37474F', zorder=10)
    ax.annotate('', xy=(13.0, 2.4), xytext=(13.3, 1.9),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.4", lw=2, color='#37474F'))

    # Output Laser Beam escaping to the right
    for y_beam in [3.2, 3.55, 3.9]:
        ax.annotate('', xy=(15.8, y_beam), xytext=(13.25, y_beam),
                    arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.55", lw=3.2, color='#D50000', ls='--'))
    ax.text(14.8, 4.6, "Coherent Output\nLASER BEAM", fontsize=13, fontweight='bold', color='#D50000', ha='center', zorder=10)

    # Explanatory card at bottom
    ax.text(8.0, 0.6, 
            "The Three Essential Components:\n"
            "• Active Medium: Solid, liquid, or gas that amplifies light by stimulated emission.\n"
            "• Energy Source (Pump): Delivers external energy to excite atoms and maintain population inversion.\n"
            "• Optical Resonator: Pair of facing mirrors that traps photons for multiple passes to build maximum beam intensity.",
            fontsize=12, ha='center', va='center', color='#37474F', zorder=10,
            bbox=dict(boxstyle="round,pad=0.7", fc="#ECEFF1", ec="#B0BEC5", lw=1.5))
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "laser_components.png"), dpi=300)
    plt.close()
    print("Saved laser_components.png")


# ==============================================================================
# 5. RUBY LASER CONSTRUCTION DIAGRAM
# ==============================================================================
def create_ruby_laser_construction_diagram():
    fig, ax = plt.subplots(figsize=(16.5, 9.2), dpi=300, facecolor='white')
    ax.set_xlim(0, 16.5)
    ax.set_ylim(0, 9.5)
    ax.axis('off')
    ax.set_title("CONSTRUCTION OF RUBY LASER", fontsize=22, fontweight='bold', color='#C2185B', pad=25)
    
    # Outer Cooling Glass Jacket
    outer_tube = FancyBboxPatch((2.2, 3.0), 10.0, 3.4, boxstyle="round,pad=0.3",
                                 fc="#E0F7FA", ec="#00838F", lw=3.0, alpha=0.6, zorder=1)
    ax.add_patch(outer_tube)
    ax.text(1.5, 6.4, "Glass Tube\n(Cooling Jacket)", fontsize=13, fontweight='bold', color='#006064', ha='center', zorder=10)
    ax.annotate('', xy=(2.4, 5.8), xytext=(1.7, 6.2),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.4", lw=2, color='#006064'))
    
    # Water in / out arrows
    ax.annotate('', xy=(3.9, 2.7), xytext=(3.9, 1.5),
                arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", lw=3, color='#0288D1'))
    ax.text(3.9, 1.1, "Cooling\nWater In", fontsize=12, fontweight='bold', color='#0277BD', ha='center', zorder=10)
    
    ax.annotate('', xy=(10.5, 1.5), xytext=(10.5, 2.7),
                arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", lw=3, color='#0288D1'))
    ax.text(10.5, 1.1, "Cooling\nWater Out", fontsize=12, fontweight='bold', color='#0277BD', ha='center', zorder=10)
    
    # Ruby Crystal Rod
    ruby_rod = FancyBboxPatch((3.8, 4.2), 6.8, 1.0, boxstyle="square,pad=0.0",
                             fc="#FF80AB", ec="#C2185B", lw=3.0, zorder=3)
    ax.add_patch(ruby_rod)
    
    # 100% Silvered Left Face
    ax.fill_between([3.5, 3.8], [4.0, 4.0], [5.4, 5.4], color='#212121', zorder=5)
    ax.text(3.6, 8.2, "Fully Reflecting\nEnd Face (100% Silvered)", fontsize=12, fontweight='bold', ha='center', color='#212121', zorder=10)
    ax.annotate('', xy=(3.65, 5.45), xytext=(3.65, 7.5),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.45", lw=2, color='#212121'))

    # Partially Silvered Right Face
    ax.fill_between([10.6, 10.9], [4.0, 4.0], [5.4, 5.4], color='#757575', zorder=5)
    ax.text(10.8, 8.2, "Partially Reflecting\nEnd Face (~90% Silvered)", fontsize=12, fontweight='bold', ha='center', color='#424242', zorder=10)
    ax.annotate('', xy=(10.75, 5.45), xytext=(10.75, 7.5),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.45", lw=2, color='#424242'))

    # Helical Xenon Flash Tube around Ruby Rod
    for cx in np.linspace(4.4, 10.0, 7):
        arc_top = patches.Arc((cx, 4.7), 0.9, 2.2, angle=0, theta1=0, theta2=180, color='#FF8F00', lw=5.0, zorder=4)
        arc_bot = patches.Arc((cx, 4.7), 0.9, 2.2, angle=0, theta1=180, theta2=360, color='#FFA000', lw=5.0, zorder=2)
        ax.add_patch(arc_top)
        ax.add_patch(arc_bot)
        
    ax.text(7.2, 7.8, "Ruby rod\n(Al₂O₃ + 0.05% Cr³⁺, L ~ 4 cm, D ~ 0.5 cm)", fontsize=12.5, fontweight='bold', ha='center', color='#880E4F', zorder=10)
    ax.annotate('', xy=(7.2, 5.25), xytext=(7.2, 7.1),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.45", lw=2, color='#880E4F'))
        
    # Power Source Box
    p_power = FancyBboxPatch((6.0, 1.4), 2.4, 1.3, boxstyle="round,pad=0.15",
                             fc="#FFCCBC", ec="#D84315", lw=2.5, zorder=5)
    ax.add_patch(p_power)
    ax.text(7.2, 2.05, "Power\nSource", fontsize=13, fontweight='bold', ha='center', va='center', color='#BF360C', zorder=10)
    
    ax.text(12.6, 2.2, "Xenon discharge tube\n(Optical pump: emits 5500 Å)", fontsize=11.5, fontweight='bold', color='#E65100', ha='center', zorder=10)
    ax.annotate('', xy=(9.8, 3.8), xytext=(11.2, 2.6),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.45", lw=2, color='#E65100'))

    # Laser Beam escaping right
    for yb in [4.4, 4.7, 5.0]:
        ax.annotate('', xy=(15.6, yb), xytext=(11.0, yb),
                    arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.55", lw=3.5, color='#D50000', ls='--'))
    ax.text(14.2, 5.7, "Laser beam\n(λ = 6943 Å / 694.3 nm,\nPulsed Red Light)", 
            fontsize=12, fontweight='bold', color='#D50000', ha='center', zorder=10)

    # Summary box
    ax.text(8.0, 0.45, 
            "Key Elements: (1) Pink Ruby Rod (Al₂O₃ doped with 0.05% Cr³⁺)  (2) Helical Xenon flash lamp for optical pumping (5500 Å)\n"
            "(3) Resonator Cavity: 100% silvered flat left face and 90% partially silvered right face  (4) Output: 694.3 nm pulsed intense red laser",
            fontsize=11.5, ha='center', va='center', color='#37474F', zorder=10,
            bbox=dict(boxstyle="round,pad=0.6", fc="#FFEBEE", ec="#EF9A9A", lw=1.6))
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "ruby_laser_construction.png"), dpi=300)
    plt.close()
    print("Saved ruby_laser_construction.png")


# ==============================================================================
# 6. RUBY LASER ENERGY LEVEL DIAGRAM (3-LEVEL LASER)
# ==============================================================================
def create_ruby_laser_energy_level_diagram():
    fig, ax = plt.subplots(figsize=(16, 9.2), dpi=300, facecolor='white')
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9.2)
    ax.axis('off')
    ax.set_title("ENERGY LEVEL DIAGRAM & WORKING OF RUBY LASER", fontsize=22, fontweight='bold', color='#C2185B', pad=25)
    
    y_E3 = 7.0
    y_E2 = 4.8
    y_E1 = 1.8
    
    # E3 Band
    ax.fill_between([1.5, 12.5], [6.7, 6.7], [7.3, 7.3], color='#FFCDD2', ec='#E53935', lw=2.5, zorder=2)
    ax.text(1.2, y_E3, r"$E_3$", fontsize=22, fontweight='bold', va='center', ha='right', color='#D32F2F', zorder=10)
    ax.text(7.0, y_E3 + 0.65, "Excited State Band (Short life ~ 10⁻⁸ s)", fontsize=13, fontweight='bold', ha='center', color='#C62828', zorder=10)
    
    # E2 Metastable state
    ax.hlines(y=y_E2, xmin=4.2, xmax=12.5, colors='#8E24AA', linewidth=4.5)
    ax.text(3.9, y_E2, r"$E_2$", fontsize=22, fontweight='bold', va='center', ha='right', color='#7B1FA2', zorder=10)
    ax.text(8.5, y_E2 + 0.45, "Metastable State (Long life ~ 10⁻³ s)", fontsize=13, fontweight='bold', ha='center', color='#6A1B9A', zorder=10)
    
    # E1 Ground state
    ax.hlines(y=y_E1, xmin=1.5, xmax=12.5, colors='#1E88E5', linewidth=4.5)
    ax.text(1.2, y_E1, r"$E_1$", fontsize=22, fontweight='bold', va='center', ha='right', color='#1565C0', zorder=10)
    ax.text(7.0, y_E1 - 0.45, "Ground Level (Cr³⁺ ions in normal unexcited state)", fontsize=13, fontweight='bold', ha='center', color='#0D47A1', zorder=10)
    
    # 1. Pumping Transition
    ax.annotate('', xy=(2.7, y_E3 - 0.35), xytext=(2.7, y_E1 + 0.1),
                arrowprops=dict(arrowstyle="->,head_width=0.5,head_length=0.7", lw=3.8, color='#2E7D32'))
    
    circle_1 = plt.Circle((2.7, 4.4), 0.42, color='#E8F5E9', ec='#2E7D32', lw=2.5, zorder=6)
    ax.add_patch(circle_1)
    ax.text(2.7, 4.4, "1", fontsize=15, fontweight='bold', ha='center', va='center', color='#1B5E20', zorder=10)
    
    # Green light pumping wave (safely to the left of the arrow)
    x_green = np.linspace(1.2, 2.5, 60)
    y_green = 5.6 + 0.22 * np.sin(2 * np.pi * 3.5 * (x_green - 1.2) / 1.3)
    ax.plot(x_green, y_green, color='#2E7D32', lw=2.8)
    ax.annotate('', xy=(2.6, 5.6), xytext=(2.4, 5.6),
                arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", lw=2.8, color='#2E7D32'))
    ax.text(1.8, 6.2, "5500 Å\n(Green light)", fontsize=11.5, fontweight='bold', color='#1B5E20', ha='center', zorder=10)
    ax.text(2.7, 3.2, "Pumping\ntransition", fontsize=12.5, fontweight='bold', color='#1B5E20', ha='center', zorder=10)
    
    # 2. Radiationless Fast Decay
    ax.annotate('', xy=(6.2, y_E2 + 0.1), xytext=(6.2, y_E3 - 0.35),
                arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.65", lw=3.2, color='#F57C00', ls='-.'))
    
    circle_2 = plt.Circle((5.4, 5.9), 0.42, color='#FFF3E0', ec='#F57C00', lw=2.5, zorder=6)
    ax.add_patch(circle_2)
    ax.text(5.4, 5.9, "2", fontsize=15, fontweight='bold', ha='center', va='center', color='#E65100', zorder=10)
    
    ax.text(6.5, 5.9, "Radiationless\ntransition\n(Energy to\ncrystal lattice)", 
            fontsize=11.5, fontweight='bold', color='#E65100', va='center', zorder=10)
    
    # 3. Spontaneous Trigger Photon
    ax.annotate('', xy=(8.0, y_E1 + 0.1), xytext=(8.0, y_E2 - 0.1),
                arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.65", lw=3.2, color='#C2185B', ls=':'))
    
    circle_3 = plt.Circle((7.2, 3.2), 0.42, color='#FCE4EC', ec='#D81B60', lw=2.5, zorder=6)
    ax.add_patch(circle_3)
    ax.text(7.2, 3.2, "3", fontsize=15, fontweight='bold', ha='center', va='center', color='#880E4F', zorder=10)
    
    ax.text(8.0, 2.3, "Spontaneous\ntrigger", fontsize=11, fontweight='bold', color='#880E4F', ha='center', zorder=10)
    
    # 4. Stimulated Laser Transition
    ax.annotate('', xy=(10.5, y_E1 + 0.1), xytext=(10.5, y_E2 - 0.1),
                arrowprops=dict(arrowstyle="->,head_width=0.55,head_length=0.75", lw=4.2, color='#D50000'))
    
    circle_4 = plt.Circle((9.7, 3.2), 0.42, color='#FFEBEE', ec='#C62828', lw=2.5, zorder=6)
    ax.add_patch(circle_4)
    ax.text(9.7, 3.2, "4", fontsize=15, fontweight='bold', ha='center', va='center', color='#B71C1C', zorder=10)
    
    # Emitted Coherent Red Photons (Cleanly offset to the right)
    x_wave2 = np.linspace(10.8, 13.5, 120)
    y_w2a = 3.6 + 0.25 * np.sin(2 * np.pi * 3.5 * (x_wave2 - 10.8) / 2.7)
    y_w2b = 2.7 + 0.25 * np.sin(2 * np.pi * 3.5 * (x_wave2 - 10.8) / 2.7)
    ax.plot(x_wave2, y_w2a, color='#D50000', lw=3.2)
    ax.plot(x_wave2, y_w2b, color='#D50000', lw=3.2)
    ax.annotate('', xy=(13.6, 3.6), xytext=(13.4, 3.6),
                arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", lw=3.2, color='#D50000'))
    ax.annotate('', xy=(13.6, 2.7), xytext=(13.4, 2.7),
                arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", lw=3.2, color='#D50000'))
    
    # Text cleanly above the waves, no overlap!
    ax.text(12.2, 4.4, "6943 Å (694.3 nm)\nLaser Transition", fontsize=12.5, fontweight='bold', color='#B71C1C', ha='center', zorder=10)
    ax.text(12.2, 2.1, "(In-Phase Coherent Red Light)", fontsize=11, fontweight='bold', color='#B71C1C', ha='center', zorder=10)

    # Bottom summary card
    ax.text(7.5, 0.55, 
            "Working Cycle: (1) Cr³⁺ ions absorbed 5500 Å pump photons → excited to E₃ band\n"
            "(2) Rapid non-radiative decay (~10⁻⁸ s) drops ions into Metastable state E₂\n"
            "(3) Population Inversion achieved: N(E₂) > N(E₁)  (4) Stimulated emission yields 6943 Å coherent red laser pulses",
            fontsize=11.5, ha='center', va='center', color='#37474F', zorder=10,
            bbox=dict(boxstyle="round,pad=0.7", fc="#FFEBEE", ec="#E57373", lw=1.6))
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "ruby_laser_energy_levels.png"), dpi=300)
    plt.close()
    print("Saved ruby_laser_energy_levels.png")


# ==============================================================================
# 7. HE-NE LASER CONSTRUCTION DIAGRAM (PROMINENT RF GENERATOR & NO OVERLAPS)
# ==============================================================================
def create_hene_laser_construction_diagram():
    fig, ax = plt.subplots(figsize=(16.5, 9.2), dpi=300, facecolor='white')
    ax.set_xlim(0, 16.5)
    ax.set_ylim(0, 9.2)
    ax.axis('off')
    ax.set_title("CONSTRUCTION OF HELIUM-NEON (He-Ne) GAS LASER", fontsize=22, fontweight='bold', color='#0D47A1', pad=25)
    
    # Fused Quartz Discharge Tube
    quartz_body = FancyBboxPatch((2.2, 3.6), 10.6, 1.8, boxstyle="round,pad=0.3",
                                 fc="#E8EAF6", ec="#3F51B5", lw=3.5, alpha=0.9, zorder=2)
    ax.add_patch(quartz_body)
    
    # Bulbous ends
    circle_left = plt.Circle((2.5, 4.5), 1.0, color='#E8EAF6', ec='#3F51B5', lw=3.5, zorder=1)
    circle_right = plt.Circle((12.5, 4.5), 1.0, color='#E8EAF6', ec='#3F51B5', lw=3.5, zorder=1)
    ax.add_patch(circle_left)
    ax.add_patch(circle_right)
    
    ax.text(7.5, 6.7, "Fused quartz tube (Length ~ 80 cm, Diameter ~ 1.5 cm)", 
            fontsize=13.5, fontweight='bold', color='#1A237E', ha='center', zorder=10)
    ax.text(7.5, 4.7, "He-Ne mixture (Ratio 10 : 1)", fontsize=15, fontweight='bold', color='#283593', ha='center', zorder=10)
    ax.text(7.5, 4.1, "(Helium at ~ 1 mm of Hg  |  Neon at ~ 0.1 mm of Hg)", fontsize=12, fontweight='bold', color='#3949AB', ha='center', zorder=10)
    
    # Perfect Reflector Mirror (Left)
    ax.fill_between([1.4, 1.7], [3.2, 3.2], [5.8, 5.8], color='#263238', zorder=4)
    for yh in np.linspace(3.4, 5.6, 9):
        ax.plot([1.1, 1.4], [yh - 0.2, yh], color='#455A64', lw=2.5)
    ax.text(1.2, 2.2, "Perfect\nreflector\n(100% R)", fontsize=12.5, fontweight='bold', color='#263238', ha='center', zorder=10)
    ax.annotate('', xy=(1.55, 3.15), xytext=(1.3, 2.7),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.4", lw=2, color='#263238'))

    # Partial Reflector Mirror (Right)
    ax.fill_between([13.3, 13.6], [3.2, 3.2], [5.8, 5.8], color='#78909C', zorder=4)
    for yh in np.linspace(3.4, 5.6, 9):
        ax.plot([13.6, 13.9], [yh, yh + 0.2], color='#90A4AE', lw=2.5)
    ax.text(13.6, 2.2, "Partial\nreflector\n(~99% R, 1% T)", fontsize=12.5, fontweight='bold', color='#37474F', ha='center', zorder=10)
    ax.annotate('', xy=(13.45, 3.15), xytext=(13.6, 2.7),
                arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.4", lw=2, color='#37474F'))

    # Electrodes for RF Discharge
    ax.plot([4.5, 4.5], [2.7, 3.6], color='#212121', lw=3.5)
    ax.plot([10.5, 10.5], [2.7, 3.6], color='#212121', lw=3.5)
    
    # Curly wires to RF generator
    w_x1 = np.linspace(4.5, 6.2, 50)
    w_y1 = 2.4 + 0.15 * np.sin(2 * np.pi * 3 * (w_x1 - 4.5) / 1.7)
    ax.plot(w_x1, w_y1, color='#D84315', lw=2.5)
    
    w_x2 = np.linspace(10.5, 8.8, 50)
    w_y2 = 2.4 + 0.15 * np.sin(2 * np.pi * 3 * (w_x2 - 8.8) / 1.7)
    ax.plot(w_x2, w_y2, color='#D84315', lw=2.5)
    
    ax.text(7.5, 2.7, "Electrodes", fontsize=13, fontweight='bold', color='#212121', ha='center', zorder=10)
    ax.annotate('', xy=(4.55, 3.0), xytext=(6.8, 2.7),
                arrowprops=dict(arrowstyle="->,head_width=0.25,head_length=0.35", lw=1.8, color='#424242'))
    ax.annotate('', xy=(10.45, 3.0), xytext=(8.2, 2.7),
                arrowprops=dict(arrowstyle="->,head_width=0.25,head_length=0.35", lw=1.8, color='#424242'))
    
    # RF Generator Box (PROMINENT WITH HIGH Z-ORDER TEXT)
    p_rf = FancyBboxPatch((6.1, 1.25), 2.8, 1.2, boxstyle="round,pad=0.15",
                          fc="#FFE0B2", ec="#E65100", lw=2.5, zorder=4)
    ax.add_patch(p_rf)
    ax.text(7.5, 1.85, "R.F. Generator\n(27.12 MHz, ~50 W)", fontsize=12, fontweight='bold', ha='center', va='center', color='#BF360C', zorder=10)
    ax.plot([6.2, 6.2], [2.4, 2.1], color='#D84315', lw=2.5)
    ax.plot([8.8, 8.8], [2.4, 2.1], color='#D84315', lw=2.5)

    # Continuous Laser Output Beam (Red, 632.8 nm)
    for yb in [4.1, 4.5, 4.9]:
        ax.annotate('', xy=(15.8, yb), xytext=(13.65, yb),
                    arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.55", lw=3.2, color='#D50000', ls='--'))
    
    # Laser Beam label positioned cleanly to the right and above, ZERO overlap with mirrors!
    ax.text(14.8, 5.8, "Laser Beam\n(Continuous Red\nλ = 632.8 nm)", fontsize=12, fontweight='bold', color='#D50000', ha='center', zorder=10)

    # Summary Card at bottom
    ax.text(7.5, 0.45,
            "Key Construction Elements: (1) Fused Quartz tube filled with 10:1 He:Ne gas  (2) RF generator creates electrical discharge\n"
            "(3) Parallel mirrors (100% and ~99%) form optical cavity  (4) Output is Continuous Wave (CW) high-purity red laser (632.8 nm)",
            fontsize=11.5, ha='center', va='center', color='#37474F', zorder=10,
            bbox=dict(boxstyle="round,pad=0.7", fc="#E8EAF6", ec="#9FA8DA", lw=1.6))
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "hene_laser_construction.png"), dpi=300)
    plt.close()
    print("Saved hene_laser_construction.png")


# ==============================================================================
# 8. HE-NE LASER ENERGY LEVEL DIAGRAM (4-LEVEL RESONANT ENERGY TRANSFER)
# ==============================================================================
def create_hene_laser_energy_level_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 9), dpi=300, facecolor='white', gridspec_kw={'width_ratios': [1, 1.4]})
    
    # ------------------ Helium (He) Energy Levels ------------------
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 9.5)
    ax1.axis('off')
    ax1.set_title("HELIUM (He) ATOM LEVELS\n(Excitation & Resonant Pumping)", fontsize=17, fontweight='bold', color='#0277BD', pad=20)
    
    y_He_E3 = 8.0 # 20.61 eV
    y_He_E2 = 7.1 # 19.81 eV
    y_He_E1 = 1.8 # Ground state
    
    ax1.hlines(y=y_He_E3, xmin=1.5, xmax=9.5, colors='#0288D1', linewidth=4.5)
    ax1.text(1.2, y_He_E3, r"$E_3$", fontsize=20, fontweight='bold', va='center', ha='right', color='#0277BD', zorder=10)
    ax1.text(5.5, y_He_E3 + 0.45, "Metastable state (20.61 eV)", fontsize=12.5, fontweight='bold', ha='center', color='#01579B', zorder=10)
    
    ax1.hlines(y=y_He_E2, xmin=3.5, xmax=9.5, colors='#0288D1', linewidth=4.5)
    ax1.text(3.2, y_He_E2, r"$E_2$", fontsize=20, fontweight='bold', va='center', ha='right', color='#0277BD', zorder=10)
    ax1.text(6.5, y_He_E2 + 0.45, "Metastable state (19.81 eV)", fontsize=12.5, fontweight='bold', ha='center', color='#01579B', zorder=10)
    
    ax1.hlines(y=y_He_E1, xmin=1.5, xmax=9.5, colors='#263238', linewidth=4.5)
    ax1.text(1.2, y_He_E1, r"$E_1$", fontsize=20, fontweight='bold', va='center', ha='right', color='#263238', zorder=10)
    ax1.text(5.5, y_He_E1 - 0.45, "Ground state (He-atom)", fontsize=13, fontweight='bold', ha='center', color='#263238', zorder=10)
    
    # Discharge collision arrows
    ax1.annotate('', xy=(2.2, y_He_E3 - 0.1), xytext=(2.2, y_He_E1 + 0.1),
                 arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.65", lw=3.2, color='#D84315'))
    ax1.text(1.9, 4.8, "Collision by\naccelerated\nelectrons", fontsize=11.5, fontweight='bold', color='#BF360C', ha='right', va='center', zorder=10)
    
    ax1.annotate('', xy=(4.2, y_He_E2 - 0.1), xytext=(4.2, y_He_E1 + 0.1),
                 arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.65", lw=3.2, color='#D84315'))
    ax1.text(4.5, 4.5, "Pumping\nDischarge", fontsize=11.5, fontweight='bold', color='#BF360C', va='center', zorder=10)
    
    ax1.text(5.5, 0.7, "• Electrons collide with He atoms: e⁻ + He → He* + e⁻\n• He atoms accumulate in long-lived metastable states (E₂ & E₃)", 
             fontsize=11.5, ha='center', va='center', color='#37474F', zorder=10,
             bbox=dict(boxstyle="round,pad=0.6", fc="#E1F5FE", ec="#81D4FA", lw=1.5))

    # ------------------ Neon (Ne) Energy Levels ------------------
    ax2.set_xlim(0, 14)
    ax2.set_ylim(0, 9.5)
    ax2.axis('off')
    ax2.set_title("NEON (Ne) ATOM LEVELS\n(Laser Transitions & Lasing Action)", fontsize=17, fontweight='bold', color='#C2185B', pad=20)
    
    y_Ne_E5 = 8.1  # 20.66 eV (Close match to He 20.61 eV)
    y_Ne_E4 = 7.15 # 19.82 eV (Close match to He 19.81 eV)
    y_Ne_E3 = 5.4  # 18.70 eV
    y_Ne_E2 = 3.8  # ~16.7 eV
    y_Ne_E1 = 1.8  # Ground state
    
    # Resonant transfer indicator at the left of Ne
    ax2.annotate('', xy=(1.8, y_Ne_E5), xytext=(0.2, y_Ne_E5),
                 arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.6", lw=3.5, color='#00897B', ls='--'))
    ax2.text(0.9, y_Ne_E5 + 0.45, "Resonant Transfer\n(from He 20.61 eV)", fontsize=10, fontweight='bold', color='#00695C', ha='center', zorder=10)
    
    ax2.annotate('', xy=(1.8, y_Ne_E4), xytext=(0.2, y_Ne_E4),
                 arrowprops=dict(arrowstyle="->,head_width=0.45,head_length=0.6", lw=3.5, color='#00897B', ls='--'))
    
    # Ne levels
    ax2.hlines(y=y_Ne_E5, xmin=2.0, xmax=11.5, colors='#7B1FA2', linewidth=4.5)
    ax2.text(1.7, y_Ne_E5, r"$E_5'$", fontsize=20, fontweight='bold', va='center', ha='right', color='#7B1FA2', zorder=10)
    ax2.text(6.8, y_Ne_E5 + 0.45, "Metastable state (20.66 eV) - Population Inversion", fontsize=11.5, fontweight='bold', ha='center', color='#6A1B9A', zorder=10)
    
    ax2.hlines(y=y_Ne_E4, xmin=2.0, xmax=11.5, colors='#7B1FA2', linewidth=4.5)
    ax2.text(1.7, y_Ne_E4, r"$E_4'$", fontsize=20, fontweight='bold', va='center', ha='right', color='#7B1FA2', zorder=10)
    ax2.text(6.0, y_Ne_E4 + 0.45, "Metastable state (19.82 eV)", fontsize=11, fontweight='bold', ha='center', color='#6A1B9A', zorder=10)
    
    ax2.hlines(y=y_Ne_E3, xmin=3.5, xmax=11.5, colors='#D32F2F', linewidth=4.5)
    ax2.text(3.2, y_Ne_E3, r"$E_3'$", fontsize=20, fontweight='bold', va='center', ha='right', color='#D32F2F', zorder=10)
    ax2.text(7.5, y_Ne_E3 - 0.45, "Lower laser level (18.70 eV)", fontsize=11.5, fontweight='bold', ha='center', color='#C62828', zorder=10)
    
    ax2.hlines(y=y_Ne_E2, xmin=3.5, xmax=11.5, colors='#FB8C00', linewidth=4.5)
    ax2.text(3.2, y_Ne_E2, r"$E_2'$", fontsize=20, fontweight='bold', va='center', ha='right', color='#E65100', zorder=10)
    
    ax2.hlines(y=y_Ne_E1, xmin=1.5, xmax=11.5, colors='#263238', linewidth=4.5)
    ax2.text(1.2, y_Ne_E1, r"$E_1'$", fontsize=20, fontweight='bold', va='center', ha='right', color='#263238', zorder=10)
    ax2.text(6.5, y_Ne_E1 - 0.45, "Ground state (Ne-atom)", fontsize=13, fontweight='bold', ha='center', color='#263238', zorder=10)
    
    # 632.8 nm Laser Transition (E5' -> E3')
    ax2.annotate('', xy=(10.0, y_Ne_E3 + 0.1), xytext=(10.0, y_Ne_E5 - 0.1),
                 arrowprops=dict(arrowstyle="->,head_width=0.55,head_length=0.75", lw=4.2, color='#D50000'))
    
    # Laser Waves
    x_w_ne = np.linspace(10.3, 13.0, 120)
    y_w_ne1 = 6.8 + 0.22 * np.sin(2 * np.pi * 3.5 * (x_w_ne - 10.3) / 2.7)
    y_w_ne2 = 6.2 + 0.22 * np.sin(2 * np.pi * 3.5 * (x_w_ne - 10.3) / 2.7)
    ax2.plot(x_w_ne, y_w_ne1, color='#D50000', lw=3.0)
    ax2.plot(x_w_ne, y_w_ne2, color='#D50000', lw=3.0)
    ax2.annotate('', xy=(13.1, 6.8), xytext=(12.9, 6.8),
                 arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", lw=3.0, color='#D50000'))
    ax2.annotate('', xy=(13.1, 6.2), xytext=(12.9, 6.2),
                 arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", lw=3.0, color='#D50000'))
    
    # Text cleanly above waves
    ax2.text(11.6, 7.6, "LASER TRANSITION\nλ = 632.8 nm (Red Light)", fontsize=11.5, fontweight='bold', color='#D50000', ha='center', zorder=10)
    
    # Infrared 1.15 um transition (E4' -> E3')
    ax2.annotate('', xy=(5.5, y_Ne_E3 + 0.1), xytext=(5.5, y_Ne_E4 - 0.1),
                 arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.55", lw=2.8, color='#C2185B'))
    ax2.text(5.8, 6.3, "Laser: 1.15 μm\n(Infrared)", fontsize=10.5, fontweight='bold', color='#C2185B', va='center', zorder=10)
    
    # Spontaneous decay (E3' -> E2')
    ax2.annotate('', xy=(7.0, y_Ne_E2 + 0.1), xytext=(7.0, y_Ne_E3 - 0.1),
                 arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.55", lw=2.8, color='#E65100'))
    ax2.text(7.3, 4.6, "Spontaneous\nemission (Rapid decay)", fontsize=10.5, fontweight='bold', color='#E65100', va='center', zorder=10)
    
    # De-excitation (E2' -> E1')
    ax2.annotate('', xy=(6.0, y_Ne_E1 + 0.1), xytext=(6.0, y_Ne_E2 - 0.1),
                 arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.55", lw=2.8, color='#37474F', ls=':'))
    ax2.text(6.3, 2.8, "De-excitation (Collisions\nwith tube walls)", fontsize=10.5, fontweight='bold', color='#37474F', va='center', zorder=10)

    # Bottom summary card
    ax2.text(7.0, 0.7, "• Resonant Transfer: Excited He atoms transfer energy to Ne atoms by collision\n• Lasing occurs between E₅' and E₃' emitting 632.8 nm red light\n• Narrow tube walls ensure rapid de-excitation of E₂' to prevent bottleneck",
             fontsize=11, ha='center', va='center', color='#37474F', zorder=10,
             bbox=dict(boxstyle="round,pad=0.6", fc="#FCE4EC", ec="#F48FB1", lw=1.5))
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "hene_laser_energy_levels.png"), dpi=300)
    plt.close()
    print("Saved hene_laser_energy_levels.png")


# ==============================================================================
# 9. PROPERTIES OF LASER COMPARISON
# ==============================================================================
def create_properties_diagram():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), dpi=300, facecolor='white')
    
    # Left: Ordinary Light
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 8.5)
    ax1.axis('off')
    ax1.set_title("ORDINARY LIGHT (e.g. Light Bulb)", fontsize=18, fontweight='bold', color='#E65100', pad=20)
    
    circle_b = plt.Circle((2.0, 4.5), 0.8, color='#FFF59D', ec='#FBC02D', lw=3, zorder=3)
    ax1.add_patch(circle_b)
    ax1.text(2.0, 4.5, "Lamp", fontsize=13, fontweight='bold', ha='center', va='center', color='#F57F17', zorder=10)
    
    colors = ['#E53935', '#FB8C00', '#FDD835', '#43A047', '#1E88E5', '#8E24AA']
    angles = np.linspace(-60, 60, 7)
    for i, ang in enumerate(angles):
        rad = np.radians(ang)
        x_end = 2.0 + 6.5 * np.cos(rad)
        y_end = 4.5 + 6.5 * np.sin(rad)
        ax1.annotate('', xy=(x_end, y_end), xytext=(2.8, 4.5),
                     arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", lw=2.8, color=colors[i % len(colors)]))
        
    ax1.text(5.0, 0.8, 
             "• Divergent: Spreads rapidly in all directions\n"
             "• Incoherent: Out of step (random phases)\n"
             "• Polychromatic: Mixture of many wavelengths\n"
             "• Low Intensity: Energy spreads thin",
             fontsize=12, ha='center', va='center', color='#37474F', fontweight='medium', zorder=10,
             bbox=dict(boxstyle="round,pad=0.7", fc="#FFF9C4", ec="#FBC02D", lw=1.6))
    
    # Right: Laser Light
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 8.5)
    ax2.axis('off')
    ax2.set_title("LASER LIGHT (Coherent Beam)", fontsize=18, fontweight='bold', color='#B71C1C', pad=20)
    
    p_las = FancyBboxPatch((0.8, 3.7), 1.6, 1.6, boxstyle="round,pad=0.1",
                           fc="#FFCDD2", ec="#D32F2F", lw=3, zorder=3)
    ax2.add_patch(p_las)
    ax2.text(1.6, 4.5, "Laser\nSource", fontsize=12, fontweight='bold', ha='center', va='center', color='#B71C1C', zorder=10)
    
    y_rays = [3.9, 4.3, 4.7, 5.1]
    for yr in y_rays:
        x_w = np.linspace(2.5, 8.5, 120)
        y_w = yr + 0.15 * np.sin(2 * np.pi * 3.5 * (x_w - 2.5) / 2.0)
        ax2.plot(x_w, y_w, color='#D50000', lw=3.0)
        ax2.annotate('', xy=(9.2, yr), xytext=(8.5, yr),
                     arrowprops=dict(arrowstyle="->,head_width=0.35,head_length=0.5", lw=3.0, color='#D50000'))
        
    ax2.text(5.0, 0.8, 
             "• Highly Directional: Razor-thin parallel beam, zero spread\n"
             "• High Coherence: All waves march in perfect phase sync\n"
             "• Extraordinary Monochromatic: Pure single wavelength\n"
             "• Extreme Intensity: Immense energy concentrated in tiny area",
             fontsize=12, ha='center', va='center', color='#880E4F', fontweight='medium', zorder=10,
             bbox=dict(boxstyle="round,pad=0.7", fc="#FFEBEE", ec="#EF9A9A", lw=1.6))
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "laser_properties_comparison.png"), dpi=300)
    plt.close()
    print("Saved laser_properties_comparison.png")


# ==============================================================================
# 10. APPLICATIONS OF LASERS INFOGRAPHIC
# ==============================================================================
def create_applications_diagram():
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300, facecolor='white')
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9.5)
    ax.axis('off')
    ax.set_title("PRACTICAL & INDUSTRIAL APPLICATIONS OF LASERS", fontsize=22, fontweight='bold', color='#1A237E', pad=25)
    
    p_center = FancyBboxPatch((6.2, 3.8), 3.6, 2.0, boxstyle="round,pad=0.3",
                              fc="#FFCDD2", ec="#D32F2F", lw=3.5, zorder=5)
    ax.add_patch(p_center)
    ax.text(8.0, 4.8, "APPLICATIONS\nOF LASERS", fontsize=15, fontweight='heavy', ha='center', va='center', color='#B71C1C', zorder=10)
    
    apps = [
        ("1. Medicine & Surgery", 
         "• Bloodless surgery (photocoagulation)\n• LASIK eye vision correction\n• Cancer tumor removal & endoscopy", 
         "#E8F5E9", "#2E7D32", 3.0, 7.6),
        ("2. Industry & Manufacturing", 
         "• Precision cutting, drilling & welding\n• Laser engraving & 3D sintering\n• Semiconductor micro-machining", 
         "#FFF3E0", "#E65100", 13.0, 7.6),
        ("3. Fiber Optic Communications", 
         "• High-speed fiber optic internet\n• Transcontinental undersea cables\n• Huge bandwidth & zero interference", 
         "#E1F5FE", "#0288D1", 3.0, 2.0),
        ("4. Scientific & Defence", 
         "• Holography (3D photography)\n• LiDAR terrain mapping & LIDAR radars\n• Laser range finders & fusion research", 
         "#F3E5F5", "#7B1FA2", 13.0, 2.0)
    ]
    
    for title, text, bg_col, brd_col, x, y in apps:
        p_card = FancyBboxPatch((x - 2.5, y - 1.2), 5.0, 2.3, boxstyle="round,pad=0.25",
                                fc=bg_col, ec=brd_col, lw=2.5, zorder=4)
        ax.add_patch(p_card)
        ax.text(x, y + 0.6, title, fontsize=13.5, fontweight='bold', ha='center', va='center', color=brd_col, zorder=10)
        ax.text(x, y - 0.25, text, fontsize=11, fontweight='medium', ha='center', va='center', color='#263238', zorder=10)
        
        ax.annotate('', xy=(x, y - 1.2 if y > 5 else y + 1.1), xytext=(8.0, 4.8),
                    arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", lw=2.5, color=brd_col, ls='--'))

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "laser_applications_overview.png"), dpi=300)
    plt.close()
    print("Saved laser_applications_overview.png")


if __name__ == "__main__":
    print("Generating all digitized diagrams...")
    create_emission_diagram()
    create_population_inversion_diagram()
    create_laser_principle_diagram()
    create_laser_components_diagram()
    create_ruby_laser_construction_diagram()
    create_ruby_laser_energy_level_diagram()
    create_hene_laser_construction_diagram()
    create_hene_laser_energy_level_diagram()
    create_properties_diagram()
    create_applications_diagram()
    print("All 10 High-Res Digitized diagrams created successfully!")
