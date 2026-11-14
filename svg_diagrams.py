# Reusable animated interactive SVG diagrams for LASERS (B.Sc. Physics)
# Features rich GPU-accelerated CSS animations, full physical labels, and instant complete diagram state.

def get_ordinary_vs_laser_svg():
    return """
<svg id="svg-prop" class="interactive-svg" viewBox="0 0 960 520" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="glow-red-prop" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="bulb-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .prop-ray { stroke-dasharray: 8 6; animation: rayDash 2s linear infinite; }
    .laser-wave-path { stroke-dasharray: 200; animation: waveDraw 2s ease-in-out infinite; }
    .laser-photon-dot { animation: travelLaserPhoton 2s linear infinite; }
    @keyframes rayDash { to { stroke-dashoffset: -28; } }
    @keyframes waveDraw { 0% { stroke-dashoffset: 200; } 100% { stroke-dashoffset: 0; } }
    @keyframes travelLaserPhoton { 0% { transform: translateX(0); opacity: 0; } 20% { opacity: 1; } 90% { opacity: 1; } 100% { transform: translateX(310px); opacity: 0; } }
    .title-txt { font-family: system-ui, sans-serif; font-size: 16px; font-weight: 800; }
  </style>

  <!-- Dividing line -->
  <line x1="480" y1="20" x2="480" y2="480" stroke="#E2E8F0" stroke-width="2.5" stroke-dasharray="6 6"/>

  <!-- LEFT: ORDINARY LIGHT -->
  <text x="240" y="45" text-anchor="middle" class="title-txt" fill="#E65100">ORDINARY LIGHT (e.g. Incandescent Lamp)</text>
  
  <!-- Bulb graphic -->
  <g transform="translate(100, 230)">
    <circle cx="0" cy="0" r="35" fill="#FFF9C4" stroke="#FBC02D" stroke-width="3" filter="url(#bulb-glow)"/>
    <path d="M -12 25 L 12 25 L 8 40 L -8 40 Z" fill="#94A3B8"/>
    <path d="M -15 -10 Q 0 -30 15 -10" fill="none" stroke="#F57F17" stroke-width="2.5"/>
    <text x="0" y="5" text-anchor="middle" font-size="12" font-weight="bold" fill="#E65100">LAMP</text>
  </g>

  <!-- Diverging multi-color chaotic rays -->
  <g class="prop-ray">
    <line x1="140" y1="220" x2="430" y2="90" stroke="#E53935" stroke-width="3.5"/>
    <line x1="140" y1="225" x2="445" y2="145" stroke="#FB8C00" stroke-width="3.5"/>
    <line x1="140" y1="230" x2="455" y2="210" stroke="#FDD835" stroke-width="3.5"/>
    <line x1="140" y1="235" x2="455" y2="275" stroke="#43A047" stroke-width="3.5"/>
    <line x1="140" y1="240" x2="440" y2="345" stroke="#1E88E5" stroke-width="3.5"/>
    <line x1="140" y1="245" x2="420" y2="400" stroke="#8E24AA" stroke-width="3.5"/>
  </g>

  <!-- Left Characteristics Badge -->
  <g transform="translate(60, 420)">
    <rect width="360" height="70" rx="10" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5"/>
    <text x="180" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400E">
      CHAOTIC: Many Colors | Random Phases
    </text>
    <text x="180" y="50" text-anchor="middle" font-size="13" font-weight="bold" fill="#B45309">
      DIVERGENT: Rapid Beam Spread &amp; Low Intensity
    </text>
  </g>

  <!-- RIGHT: LASER LIGHT -->
  <text x="720" y="45" text-anchor="middle" class="title-txt" fill="#D50000">LASER LIGHT (Coherent &amp; Monochromatic)</text>

  <!-- Laser Cavity Source Box -->
  <g transform="translate(520, 200)">
    <rect x="0" y="0" width="80" height="65" rx="8" fill="#FFEBEE" stroke="#D32F2F" stroke-width="3"/>
    <text x="40" y="30" text-anchor="middle" font-size="12" font-weight="bold" fill="#C62828">LASER</text>
    <text x="40" y="48" text-anchor="middle" font-size="11" font-weight="bold" fill="#C62828">CAVITY</text>
  </g>

  <!-- Perfectly Parallel, In-Phase Laser Waves -->
  <g id="laser-waves" filter="url(#glow-red-prop)">
    <path class="laser-wave-path" d="M 605 210 Q 625 198 645 210 T 685 210 T 725 210 T 765 210 T 805 210 T 845 210 T 885 210 L 920 210" 
          fill="none" stroke="#D50000" stroke-width="4"/>
    <polygon points="925,210 913,204 913,216" fill="#D50000"/>

    <path class="laser-wave-path" d="M 605 232 Q 625 220 645 232 T 685 232 T 725 232 T 765 232 T 805 232 T 845 232 T 885 232 L 920 232" 
          fill="none" stroke="#D50000" stroke-width="4"/>
    <polygon points="925,232 913,226 913,238" fill="#D50000"/>

    <path class="laser-wave-path" d="M 605 254 Q 625 242 645 254 T 685 254 T 725 254 T 765 254 T 805 254 T 845 254 T 885 254 L 920 254" 
          fill="none" stroke="#D50000" stroke-width="4"/>
    <polygon points="925,254 913,248 913,260" fill="#D50000"/>

    <!-- Marching photon particles -->
    <circle cx="610" cy="210" r="5" fill="#FFEB3B" stroke="#D50000" stroke-width="1.5" class="laser-photon-dot"/>
    <circle cx="610" cy="232" r="5" fill="#FFEB3B" stroke="#D50000" stroke-width="1.5" class="laser-photon-dot"/>
    <circle cx="610" cy="254" r="5" fill="#FFEB3B" stroke="#D50000" stroke-width="1.5" class="laser-photon-dot"/>
  </g>

  <!-- Annotations -->
  <line x1="750" y1="170" x2="750" y2="198" stroke="#1565C0" stroke-width="2"/>
  <rect x="670" y="140" width="160" height="28" rx="6" fill="#E3F2FD" stroke="#90CAF9"/>
  <text x="750" y="159" text-anchor="middle" font-size="12" font-weight="bold" fill="#0D47A1">Identical Wavelength (λ)</text>

  <line x1="840" y1="285" x2="840" y2="265" stroke="#1565C0" stroke-width="2"/>
  <rect x="760" y="290" width="160" height="28" rx="6" fill="#E3F2FD" stroke="#90CAF9"/>
  <text x="840" y="309" text-anchor="middle" font-size="12" font-weight="bold" fill="#0D47A1">In-Phase Crests (Coherent)</text>

  <!-- Right Characteristics Badge -->
  <g transform="translate(540, 420)">
    <rect width="360" height="70" rx="10" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
    <text x="180" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#991B1B">
      COHERENT: All Waves in Lockstep Unison
    </text>
    <text x="180" y="50" text-anchor="middle" font-size="13" font-weight="bold" fill="#B91C1C">
      DIRECTIONAL: Razor-Sharp Beam (Zero Spread)
    </text>
  </g>
</svg>
"""

def get_spontaneous_vs_stimulated_svg():
    return """
<svg id="svg-emission" class="interactive-svg" viewBox="0 0 960 520" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="glow-atom-em" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .energy-line { stroke-width: 4.5; stroke-linecap: round; }
    .photon-w { stroke-width: 3.5; fill: none; }
    
    /* Dynamic Spontaneous Animation */
    .spont-atom-moving {
      animation: animSpontDrop 4s ease-in-out infinite;
    }
    @keyframes animSpontDrop {
      0%, 20% { transform: translateY(-200px); }
      35%, 85% { transform: translateY(0px); }
      95%, 100% { transform: translateY(-200px); }
    }
    .spont-photon-moving {
      animation: animSpontPhotonFly 4s ease-in-out infinite;
    }
    @keyframes animSpontPhotonFly {
      0%, 25% { opacity: 0; transform: translate(220px, 320px) rotate(-25deg) scale(0.3); }
      40% { opacity: 1; transform: translate(240px, 300px) rotate(-25deg) scale(1); }
      85% { opacity: 1; transform: translate(320px, 240px) rotate(-25deg) scale(1); }
      100% { opacity: 0; transform: translate(360px, 210px) rotate(-25deg) scale(1); }
    }

    /* Dynamic Stimulated Animation */
    .stim-in-photon-moving {
      animation: animStimInPhoton 4s linear infinite;
    }
    @keyframes animStimInPhoton {
      0% { opacity: 0; transform: translate(490px, 240px); }
      15% { opacity: 1; transform: translate(530px, 240px); }
      40% { opacity: 1; transform: translate(680px, 240px); }
      45%, 100% { opacity: 0; transform: translate(720px, 240px); }
    }
    .stim-atom-moving {
      animation: animStimDrop 4s ease-in-out infinite;
    }
    @keyframes animStimDrop {
      0%, 35% { transform: translateY(-200px); }
      50%, 85% { transform: translateY(0px); }
      95%, 100% { transform: translateY(-200px); }
    }
    .stim-out-photons-moving {
      animation: animStimOutPhotons 4s ease-in-out infinite;
    }
    @keyframes animStimOutPhotons {
      0%, 45% { opacity: 0; transform: translate(710px, 210px) scale(0.5); }
      55% { opacity: 1; transform: translate(740px, 210px) scale(1); }
      85% { opacity: 1; transform: translate(800px, 210px) scale(1); }
      100% { opacity: 0; transform: translate(840px, 210px) scale(1); }
    }
  </style>

  <!-- Dividing line -->
  <line x1="480" y1="20" x2="480" y2="480" stroke="#E2E8F0" stroke-width="2.5" stroke-dasharray="6 6"/>

  <!-- LEFT: SPONTANEOUS EMISSION -->
  <text x="240" y="40" text-anchor="middle" font-family="system-ui" font-size="18" font-weight="900" fill="#0D47A1">
    1. SPONTANEOUS EMISSION
  </text>
  <text x="240" y="65" text-anchor="middle" font-family="system-ui" font-size="13" font-weight="bold" fill="#475569">
    Atom drops spontaneously after lifetime ~ 10⁻⁸ s
  </text>

  <!-- Levels Left -->
  <line x1="60" y1="160" x2="420" y2="160" stroke="#D32F2F" class="energy-line"/>
  <rect x="30" y="145" width="40" height="30" rx="6" fill="#FFEBEE" stroke="#EF5350"/>
  <text x="50" y="166" text-anchor="middle" font-size="16" font-weight="bold" fill="#C62828">E₂</text>
  <text x="240" y="148" text-anchor="middle" font-size="13" font-weight="bold" fill="#C62828">Excited State (Short Life)</text>

  <line x1="60" y1="360" x2="420" y2="360" stroke="#1565C0" class="energy-line"/>
  <rect x="30" y="345" width="40" height="30" rx="6" fill="#E3F2FD" stroke="#42A5F5"/>
  <text x="50" y="366" text-anchor="middle" font-size="16" font-weight="bold" fill="#1565C0">E₁</text>
  <text x="240" y="390" text-anchor="middle" font-size="13" font-weight="bold" fill="#1565C0">Ground State (Normal Level)</text>

  <!-- Spontaneous Jump Arrow -->
  <line x1="200" y1="175" x2="200" y2="345" stroke="#880E4F" stroke-width="3" stroke-dasharray="6 4"/>
  <polygon points="200,350 193,338 207,338" fill="#880E4F"/>
  <rect x="110" y="245" width="80" height="35" rx="6" fill="#FCE4EC" stroke="#F48FB1"/>
  <text x="150" y="267" text-anchor="middle" font-size="11" font-weight="bold" fill="#880E4F">Natural Drop</text>

  <!-- Animated Atom in Left Chamber -->
  <circle id="spont-atom" cx="200" cy="360" r="16" fill="#1E88E5" stroke="#0D47A1" stroke-width="3" filter="url(#glow-atom-em)" class="spont-atom-moving"/>

  <!-- Animated Emitted Photon Wave -->
  <g id="spont-photon" class="spont-photon-moving">
    <path class="photon-w" stroke="#FF6F00" d="M 0 0 Q 15 -12 30 0 T 60 0 T 90 0 T 120 0 L 145 0"/>
    <polygon points="152,0 140,-6 140,6" fill="#FF6F00"/>
    <text x="75" y="-14" text-anchor="middle" font-size="12" font-weight="bold" fill="#E65100">hν = E₂ - E₁</text>
    <text x="75" y="22" text-anchor="middle" font-size="10" font-weight="bold" fill="#BF360C">(Random Phase &amp; Direction)</text>
  </g>

  <!-- Bottom Left Summary Box -->
  <g transform="translate(60, 420)">
    <rect width="360" height="60" rx="8" fill="#F1F5F9" stroke="#CBD5E1"/>
    <text x="180" y="24" text-anchor="middle" font-size="12" font-weight="bold" fill="#334155">• Spontaneous decay without external stimulus</text>
    <text x="180" y="46" text-anchor="middle" font-size="12" font-weight="bold" fill="#334155">• Incoherent, broad spectrum (Ordinary light)</text>
  </g>

  <!-- RIGHT: STIMULATED EMISSION -->
  <text x="720" y="40" text-anchor="middle" font-family="system-ui" font-size="18" font-weight="900" fill="#B71C1C">
    2. STIMULATED EMISSION
  </text>
  <text x="720" y="65" text-anchor="middle" font-family="system-ui" font-size="13" font-weight="bold" fill="#475569">
    Triggered by incoming photon: 1 photon in → 2 identical photons out!
  </text>

  <!-- Levels Right -->
  <line x1="540" y1="160" x2="900" y2="160" stroke="#D32F2F" class="energy-line"/>
  <rect x="510" y="145" width="40" height="30" rx="6" fill="#FFEBEE" stroke="#EF5350"/>
  <text x="530" y="166" text-anchor="middle" font-size="16" font-weight="bold" fill="#C62828">E₂</text>

  <line x1="540" y1="360" x2="900" y2="360" stroke="#1565C0" class="energy-line"/>
  <rect x="510" y="345" width="40" height="30" rx="6" fill="#E3F2FD" stroke="#42A5F5"/>
  <text x="530" y="366" text-anchor="middle" font-size="16" font-weight="bold" fill="#1565C0">E₁</text>

  <!-- Animated Incoming stimulating photon -->
  <g id="stim-in-photon" class="stim-in-photon-moving">
    <path class="photon-w" stroke="#00897B" d="M 0 0 Q 15 -12 30 0 T 60 0 T 90 0 T 120 0 L 140 0"/>
    <polygon points="148,0 136,-6 136,6" fill="#00897B"/>
    <text x="70" y="-12" text-anchor="middle" font-size="12" font-weight="bold" fill="#00695C">Incoming Photon (hν)</text>
  </g>

  <!-- Forced Drop Transition Arrow -->
  <line x1="720" y1="175" x2="720" y2="345" stroke="#C2185B" stroke-width="3.5" stroke-dasharray="6 4"/>
  <polygon points="720,350 713,338 727,338" fill="#C2185B"/>
  <rect x="735" y="245" width="85" height="35" rx="6" fill="#FCE4EC" stroke="#F48FB1"/>
  <text x="777" y="267" text-anchor="middle" font-size="11" font-weight="bold" fill="#AD1457">Forced Jump</text>

  <!-- Animated Atom in Right Chamber -->
  <circle id="stim-atom" cx="720" cy="360" r="16" fill="#1E88E5" stroke="#0D47A1" stroke-width="3" filter="url(#glow-atom-em)" class="stim-atom-moving"/>

  <!-- Animated Two Coherent Emitted Photons -->
  <g id="stim-out-photons" class="stim-out-photons-moving">
    <!-- Photon 1 -->
    <path class="photon-w" stroke="#D50000" d="M 0 15 Q 15 3 30 15 T 60 15 T 90 15 T 120 15 L 145 15"/>
    <polygon points="152,15 140,9 140,21" fill="#D50000"/>
    <text x="165" y="19" font-size="12" font-weight="bold" fill="#D50000">hν</text>

    <!-- Photon 2 -->
    <path class="photon-w" stroke="#D50000" d="M 0 55 Q 15 43 30 55 T 60 55 T 90 55 T 120 55 L 145 55"/>
    <polygon points="152,55 140,49 140,61" fill="#D50000"/>
    <text x="165" y="59" font-size="12" font-weight="bold" fill="#D50000">hν</text>

    <text x="80" y="-5" text-anchor="middle" font-size="12" font-weight="bold" fill="#B71C1C">2 IDENTICAL COHERENT PHOTONS</text>
    <text x="80" y="85" text-anchor="middle" font-size="10" font-weight="bold" fill="#880E4F">Same Phase, Frequency &amp; Direction!</text>
  </g>

  <!-- Bottom Right Summary Box -->
  <g transform="translate(540, 420)">
    <rect width="360" height="60" rx="8" fill="#FEF2F2" stroke="#FECACA"/>
    <text x="180" y="24" text-anchor="middle" font-size="12" font-weight="bold" fill="#991B1B">• Stimulated by incoming photon (hν = E₂ - E₁)</text>
    <text x="180" y="46" text-anchor="middle" font-size="12" font-weight="bold" fill="#991B1B">• High Coherence &amp; Amplification (Basis of Laser)</text>
  </g>
</svg>
"""

def get_population_inversion_svg():
    return """
<svg id="svg-pop-inv" class="interactive-svg" viewBox="0 0 960 520" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="atom-glow-p" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    .level-line { stroke-width: 4.5; stroke-linecap: round; }
    
    /* Dynamic Inversion Cycle */
    .pump-atom-moving {
      animation: animPumpCycle 5s ease-in-out infinite;
    }
    @keyframes animPumpCycle {
      0%, 5% { transform: translateY(0); opacity: 1; }
      20% { transform: translateY(-240px); opacity: 1; } /* Leap to E3 */
      35%, 75% { transform: translate(160px, -120px); opacity: 1; } /* Sits in Metastable E2 */
      88%, 95% { transform: translate(160px, 0); opacity: 1; } /* Stimulated drop to E1 */
      100% { transform: translateY(0); opacity: 0; }
    }
    
    .pop-badge-pulse {
      animation: animBadgeGlow 5s ease-in-out infinite;
      transform-origin: 660px 200px;
    }
    @keyframes animBadgeGlow {
      0%, 30% { transform: scale(1); filter: none; }
      40%, 75% { transform: scale(1.06); filter: drop-shadow(0 0 10px #E91E63); }
      85%, 100% { transform: scale(1); filter: none; }
    }

    .laser-burst-moving {
      animation: animLaserBurst 5s ease-in-out infinite;
    }
    @keyframes animLaserBurst {
      0%, 75% { opacity: 0; transform: translate(680px, 310px); }
      82% { opacity: 1; transform: translate(710px, 310px); }
      92% { opacity: 1; transform: translate(780px, 310px); }
      100% { opacity: 0; transform: translate(820px, 310px); }
    }
  </style>

  <text x="480" y="38" text-anchor="middle" font-family="system-ui" font-size="20" font-weight="900" fill="#0D47A1">
    POPULATION INVERSION IN A 3-LEVEL QUANTUM SYSTEM
  </text>
  <text x="480" y="62" text-anchor="middle" font-family="system-ui" font-size="13" font-weight="bold" fill="#475569">
    Atoms accumulate in the Metastable State (E₂) because its lifetime is 100,000× longer (~10⁻³ s)!
  </text>

  <!-- 3 Levels -->
  <!-- E3 Level -->
  <line x1="120" y1="140" x2="840" y2="140" stroke="#E53935" class="level-line"/>
  <rect x="75" y="125" width="40" height="30" rx="6" fill="#FFEBEE" stroke="#EF5350"/>
  <text x="95" y="146" text-anchor="middle" font-size="16" font-weight="bold" fill="#C62828">E₃</text>
  <text x="860" y="145" font-size="13" font-weight="bold" fill="#C62828">Excited State (Short life ~ 10⁻⁸ s)</text>

  <!-- E2 Level (Metastable) -->
  <line x1="280" y1="260" x2="840" y2="260" stroke="#8E24AA" class="level-line"/>
  <rect x="235" y="245" width="40" height="30" rx="6" fill="#F3E5F5" stroke="#BA68C8"/>
  <text x="255" y="266" text-anchor="middle" font-size="16" font-weight="bold" fill="#7B1FA2">E₂</text>
  <text x="860" y="265" font-size="13" font-weight="bold" fill="#7B1FA2">Metastable State (Long life ~ 10⁻³ s)</text>

  <!-- E1 Level (Ground) -->
  <line x1="120" y1="380" x2="840" y2="380" stroke="#1E88E5" class="level-line"/>
  <rect x="75" y="365" width="40" height="30" rx="6" fill="#E3F2FD" stroke="#42A5F5"/>
  <text x="95" y="386" text-anchor="middle" font-size="16" font-weight="bold" fill="#1565C0">E₁</text>
  <text x="860" y="385" font-size="13" font-weight="bold" fill="#1565C0">Ground State (Normal energy)</text>

  <!-- Pumping Arrow (E1 -> E3) -->
  <line x1="180" y1="365" x2="180" y2="155" stroke="#2E7D32" stroke-width="4"/>
  <polygon points="180,145 172,160 188,160" fill="#2E7D32"/>
  <rect x="110" y="235" width="100" height="42" rx="6" fill="#E8F5E9" stroke="#81C784"/>
  <text x="160" y="253" text-anchor="middle" font-size="11" font-weight="bold" fill="#1B5E20">PUMPING</text>
  <text x="160" y="268" text-anchor="middle" font-size="10" font-weight="bold" fill="#2E7D32">hν₀ = E₃ - E₁</text>

  <!-- Fast Radiationless Arrow (E3 -> E2) -->
  <line x1="320" y1="150" x2="480" y2="250" stroke="#F57C00" stroke-width="3.5" stroke-dasharray="6 4"/>
  <polygon points="485,253 470,248 478,238" fill="#F57C00"/>
  <rect x="330" y="180" width="165" height="32" rx="6" fill="#FFF3E0" stroke="#FFB74D"/>
  <text x="412" y="200" text-anchor="middle" font-size="11" font-weight="bold" fill="#E65100">Fast Radiationless Drop (~10⁻⁸ s)</text>

  <!-- Accumulated Atoms on E2 (Metastable) -->
  <g id="metastable-atoms">
    <circle cx="340" cy="260" r="12" fill="#8E24AA" stroke="#4A148C" stroke-width="2" filter="url(#atom-glow-p)"/>
    <circle cx="380" cy="260" r="12" fill="#8E24AA" stroke="#4A148C" stroke-width="2" filter="url(#atom-glow-p)"/>
    <circle cx="420" cy="260" r="12" fill="#8E24AA" stroke="#4A148C" stroke-width="2" filter="url(#atom-glow-p)"/>
    <circle cx="460" cy="260" r="12" fill="#8E24AA" stroke="#4A148C" stroke-width="2" filter="url(#atom-glow-p)"/>
    <circle cx="500" cy="260" r="12" fill="#8E24AA" stroke="#4A148C" stroke-width="2" filter="url(#atom-glow-p)"/>
    <circle cx="540" cy="260" r="12" fill="#8E24AA" stroke="#4A148C" stroke-width="2" filter="url(#atom-glow-p)"/>
    <circle cx="580" cy="260" r="12" fill="#8E24AA" stroke="#4A148C" stroke-width="2" filter="url(#atom-glow-p)"/>
    <circle cx="620" cy="260" r="12" fill="#8E24AA" stroke="#4A148C" stroke-width="2" filter="url(#atom-glow-p)"/>
  </g>

  <!-- Few Ground State Atoms (N1 is depleted) -->
  <circle cx="240" cy="380" r="12" fill="#1E88E5" stroke="#0D47A1" stroke-width="2" filter="url(#atom-glow-p)"/>
  <circle cx="760" cy="380" r="12" fill="#1E88E5" stroke="#0D47A1" stroke-width="2" filter="url(#atom-glow-p)"/>

  <!-- Animated Active Cycling Atom -->
  <circle cx="180" cy="380" r="13" fill="#FF5252" stroke="#B71C1C" stroke-width="2.5" filter="url(#atom-glow-p)" class="pump-atom-moving"/>

  <!-- Population Inversion Badge (Glowing and pulsing) -->
  <g class="pop-badge-pulse">
    <rect x="540" y="175" width="240" height="50" rx="10" fill="#FFF0F5" stroke="#E91E63" stroke-width="2.5"/>
    <text x="660" y="196" text-anchor="middle" font-size="13" font-weight="bold" fill="#D81B60">POPULATION INVERSION</text>
    <text x="660" y="214" text-anchor="middle" font-size="12" font-weight="bold" fill="#C2185B">Achieved: N₂ &gt; N₁</text>
  </g>

  <!-- Stimulated Emission Arrow (E2 -> E1) -->
  <line x1="680" y1="275" x2="680" y2="365" stroke="#D81B60" stroke-width="4"/>
  <polygon points="680,375 672,360 688,360" fill="#D81B60"/>
  <text x="660" y="325" text-anchor="end" font-size="11" font-weight="bold" fill="#C2185B">Stimulated Drop</text>

  <!-- Emitted Coherent Laser Light Waves -->
  <g id="laser-burst" class="laser-burst-moving">
    <path stroke="#D81B60" stroke-width="3.5" fill="none" d="M 0 0 Q 15 -10 30 0 T 60 0 T 90 0 T 120 0 L 140 0"/>
    <polygon points="146,0 134,-6 134,6" fill="#D81B60"/>
    <text x="70" y="-12" text-anchor="middle" font-size="11" font-weight="bold" fill="#D81B60">Laser Emission (hν)</text>
  </g>

  <!-- Bottom Explanatory Card -->
  <g transform="translate(120, 440)">
    <rect width="720" height="55" rx="10" fill="#F8FAFC" stroke="#CBD5E1"/>
    <text x="360" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0F172A">
      • Normal Condition: N₁ &gt; N₂ (Boltzmann Distribution)  |  • Inversion Condition: N₂ &gt; N₁ (Non-equilibrium)
    </text>
    <text x="360" y="44" text-anchor="middle" font-size="12" font-weight="bold" fill="#475569">
      Essential prerequisite for amplification: Stimulated emission rate exceeds absorption rate!
    </text>
  </g>
</svg>
"""

def get_laser_principle_svg():
    return """
<svg id="svg-principle" class="interactive-svg" viewBox="0 0 960 520" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cavityGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E1F5FE"/>
      <stop offset="50%" stop-color="#B3E5FC"/>
      <stop offset="100%" stop-color="#E1F5FE"/>
    </linearGradient>
    <filter id="laserBeamGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    /* Forward Traveling Photons (Left to Right: strictly inside cavity) */
    .photons-forward {
      animation: animForwardPass 3s ease-in-out infinite;
    }
    @keyframes animForwardPass {
      0% { transform: translateX(0px); opacity: 0; }
      5% { opacity: 1; }
      46% { opacity: 1; transform: translateX(525px); }
      48%, 100% { opacity: 0; transform: translateX(525px); }
    }

    /* Reflected Traveling Photons (Right to Left: strictly inside cavity) */
    .photons-backward {
      animation: animBackwardPass 3s ease-in-out infinite;
    }
    @keyframes animBackwardPass {
      0%, 48% { opacity: 0; transform: translateX(0px); }
      52% { opacity: 1; transform: translateX(0px); }
      95% { opacity: 1; transform: translateX(-525px); }
      98%, 100% { opacity: 0; transform: translateX(-525px); }
    }
    
    .cavity-wave-stream {
      stroke-dasharray: 20 10;
      animation: animCavityStream 1.5s linear infinite;
    }
    @keyframes animCavityStream {
      to { stroke-dashoffset: -60; }
    }

    .output-laser-pulse {
      animation: animOutputPulse 2s ease-in-out infinite;
    }
    @keyframes animOutputPulse {
      0%, 100% { opacity: 0.8; filter: drop-shadow(0 0 4px #D50000); }
      50% { opacity: 1; filter: drop-shadow(0 0 12px #FF1744); }
    }
  </style>

  <text x="480" y="36" text-anchor="middle" font-family="system-ui" font-size="20" font-weight="900" fill="#B71C1C">
    PRINCIPLE OF LASER: OPTICAL RESONATOR &amp; AVALANCHE AMPLIFICATION
  </text>
  <text x="480" y="60" text-anchor="middle" font-family="system-ui" font-size="13" font-weight="bold" fill="#475569">
    Photons reflect repeatedly between mirrors, stimulating identical photons with each pass!
  </text>

  <!-- Active Medium Cylinder -->
  <rect x="200" y="150" width="560" height="180" rx="12" fill="url(#cavityGrad)" stroke="#0288D1" stroke-width="3"/>
  <text x="480" y="180" text-anchor="middle" font-size="15" font-weight="bold" fill="#01579B">
    ACTIVE MEDIUM (Population Inversion Maintained by Pump)
  </text>

  <!-- Left Mirror: 100% Perfect Reflector -->
  <rect x="175" y="130" width="22" height="220" rx="4" fill="#263238" stroke="#000000" stroke-width="2"/>
  <g stroke="#90A4AE" stroke-width="2.5">
    <line x1="165" y1="150" x2="175" y2="160"/>
    <line x1="165" y1="190" x2="175" y2="200"/>
    <line x1="165" y1="230" x2="175" y2="240"/>
    <line x1="165" y1="270" x2="175" y2="280"/>
    <line x1="165" y1="310" x2="175" y2="320"/>
  </g>
  <rect x="80" y="215" width="85" height="50" rx="6" fill="#ECEFF1" stroke="#90A4AE"/>
  <text x="122" y="236" text-anchor="middle" font-size="11" font-weight="bold" fill="#263238">Full Mirror</text>
  <text x="122" y="254" text-anchor="middle" font-size="11" font-weight="bold" fill="#D32F2F">100% R</text>

  <!-- Right Mirror: Partial Reflector (99% R, 1% T) -->
  <rect x="760" y="130" width="22" height="220" rx="4" fill="#78909C" stroke="#37474F" stroke-width="2"/>
  <g stroke="#B0BEC5" stroke-width="2.5">
    <line x1="782" y1="150" x2="792" y2="160"/>
    <line x1="782" y1="190" x2="792" y2="200"/>
    <line x1="782" y1="230" x2="792" y2="240"/>
    <line x1="782" y1="270" x2="792" y2="280"/>
    <line x1="782" y1="310" x2="792" y2="320"/>
  </g>
  <rect x="795" y="215" width="95" height="50" rx="6" fill="#ECEFF1" stroke="#90A4AE"/>
  <text x="842" y="236" text-anchor="middle" font-size="11" font-weight="bold" fill="#37474F">Partial Mirror</text>
  <text x="842" y="254" text-anchor="middle" font-size="11" font-weight="bold" fill="#D32F2F">99% R, 1% T</text>

  <!-- Stimulated Avalanche in Cavity -->
  <g class="cavity-wave-stream">
    <line x1="210" y1="220" x2="750" y2="220" stroke="#E53935" stroke-width="4"/>
    <line x1="210" y1="260" x2="750" y2="260" stroke="#D50000" stroke-width="4.5"/>
  </g>

  <!-- Stationary Active Atoms in the Cavity Medium (Resting, Excited State N2 > N1) -->
  <g id="cavity-stationary-atoms" opacity="0.9">
    <circle cx="280" cy="205" r="7" fill="#8E24AA" stroke="#4A148C" stroke-width="1.5"/>
    <circle cx="360" cy="205" r="7" fill="#8E24AA" stroke="#4A148C" stroke-width="1.5"/>
    <circle cx="440" cy="205" r="7" fill="#8E24AA" stroke="#4A148C" stroke-width="1.5"/>
    <circle cx="520" cy="205" r="7" fill="#8E24AA" stroke="#4A148C" stroke-width="1.5"/>
    <circle cx="600" cy="205" r="7" fill="#8E24AA" stroke="#4A148C" stroke-width="1.5"/>
    <circle cx="680" cy="205" r="7" fill="#8E24AA" stroke="#4A148C" stroke-width="1.5"/>

    <circle cx="320" cy="275" r="7" fill="#8E24AA" stroke="#4A148C" stroke-width="1.5"/>
    <circle cx="400" cy="275" r="7" fill="#8E24AA" stroke="#4A148C" stroke-width="1.5"/>
    <circle cx="480" cy="275" r="7" fill="#8E24AA" stroke="#4A148C" stroke-width="1.5"/>
    <circle cx="560" cy="275" r="7" fill="#8E24AA" stroke="#4A148C" stroke-width="1.5"/>
    <circle cx="640" cy="275" r="7" fill="#8E24AA" stroke="#4A148C" stroke-width="1.5"/>
  </g>

  <!-- Photons Bouncing Strictly Between Mirrors (x = 215 to 740) -->
  <!-- 1. Forward Pass: Left to Right (x = 215 -> 740) -->
  <g class="photons-forward">
    <circle cx="215" cy="225" r="8" fill="#FFEB3B" stroke="#D50000" stroke-width="2"/>
    <circle cx="225" cy="240" r="8" fill="#FFEB3B" stroke="#D50000" stroke-width="2"/>
    <circle cx="215" cy="255" r="8" fill="#FFEB3B" stroke="#D50000" stroke-width="2"/>
    <polygon points="237,240 227,234 227,246" fill="#D50000"/>
  </g>

  <!-- 2. Reflected Pass: Right to Left (x = 740 -> 215) -->
  <g class="photons-backward">
    <circle cx="740" cy="225" r="8" fill="#FFEB3B" stroke="#D50000" stroke-width="2"/>
    <circle cx="730" cy="240" r="8" fill="#FFEB3B" stroke="#D50000" stroke-width="2"/>
    <circle cx="740" cy="255" r="8" fill="#FFEB3B" stroke="#D50000" stroke-width="2"/>
    <polygon points="718,240 728,234 728,246" fill="#D50000"/>
  </g>

  <text x="480" y="305" text-anchor="middle" font-size="12" font-weight="bold" fill="#B71C1C">
    ← Resonance Amplification (Standing Wave Sustained: L = n · λ/2) →
  </text>

  <!-- Output Laser Beam -->
  <g class="output-laser-pulse" filter="url(#laserBeamGlow)">
    <line x1="785" y1="230" x2="940" y2="230" stroke="#FF1744" stroke-width="6"/>
    <line x1="785" y1="240" x2="940" y2="240" stroke="#D50000" stroke-width="7"/>
    <line x1="785" y1="250" x2="940" y2="250" stroke="#FF1744" stroke-width="6"/>
    <polygon points="948,240 934,230 934,250" fill="#D50000"/>
  </g>

  <rect x="800" y="160" width="145" height="40" rx="6" fill="#FFEBEE" stroke="#EF9A9A"/>
  <text x="872" y="177" text-anchor="middle" font-size="11" font-weight="bold" fill="#C62828">OUTPUT BEAM</text>
  <text x="872" y="193" text-anchor="middle" font-size="10" font-weight="bold" fill="#B71C1C">Intense &amp; Parallel</text>

  <!-- Bottom Explanatory Steps Card -->
  <g transform="translate(80, 390)">
    <rect width="800" height="95" rx="10" fill="#FFFDE7" stroke="#FFF59D" stroke-width="2"/>
    <text x="400" y="26" text-anchor="middle" font-size="14" font-weight="bold" fill="#F57F17">
      THE 3 STAGES OF LASER ACTION:
    </text>
    <text x="400" y="48" text-anchor="middle" font-size="12" font-weight="bold" fill="#37474F">
      1. Pumping energy creates Population Inversion (more atoms in higher metastable state than ground state)
    </text>
    <text x="400" y="68" text-anchor="middle" font-size="12" font-weight="bold" fill="#37474F">
      2. Spontaneous photon triggers stimulated emission: 1 incoming photon induces 2 identical in-phase photons
    </text>
    <text x="400" y="88" text-anchor="middle" font-size="12" font-weight="bold" fill="#37474F">
      3. Optical resonator traps axial photons, producing an avalanche cascade that escapes as an intense coherent beam
    </text>
  </g>
</svg>
"""

def get_ruby_laser_construction_svg():
    return """
<svg id="svg-ruby-const" class="interactive-svg" viewBox="0 0 960 520" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rubyRodGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FF4081"/>
      <stop offset="50%" stop-color="#E91E63"/>
      <stop offset="100%" stop-color="#C2185B"/>
    </linearGradient>
    <linearGradient id="coolGlassGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#E0F7FA" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#B2EBF2" stop-opacity="0.5"/>
    </linearGradient>
    <filter id="rubyBeamGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="7" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    /* Xenon flash pulse */
    .xenon-flash-anim {
      animation: animXenonFlash 3.5s ease-in-out infinite;
    }
    @keyframes animXenonFlash {
      0%, 15% { opacity: 0.35; stroke: #FFA000; filter: none; }
      25%, 45% { opacity: 1; stroke: #FFEE58; filter: drop-shadow(0 0 12px #FFEB3B); }
      55%, 100% { opacity: 0.35; stroke: #FFA000; filter: none; }
    }

    /* Ruby laser pulsed emission */
    .ruby-laser-pulse {
      animation: animRubyBeam 3.5s ease-in-out infinite;
    }
    @keyframes animRubyBeam {
      0%, 45% { opacity: 0; transform: scaleX(0); transform-origin: 740px 240px; }
      52%, 75% { opacity: 1; transform: scaleX(1); transform-origin: 740px 240px; }
      85%, 100% { opacity: 0; transform: scaleX(1); transform-origin: 740px 240px; }
    }

    /* Water flow dash animation */
    .water-flow {
      stroke-dasharray: 8 6;
      animation: animWaterFlow 2s linear infinite;
    }
    @keyframes animWaterFlow {
      to { stroke-dashoffset: -28; }
    }
  </style>

  <text x="480" y="36" text-anchor="middle" font-family="system-ui" font-size="20" font-weight="900" fill="#B71C1C">
    CONSTRUCTION OF RUBY LASER (Maiman, 1960)
  </text>
  <text x="480" y="60" text-anchor="middle" font-family="system-ui" font-size="13" font-weight="bold" fill="#475569">
    Solid-State 3-Level Laser: Synthetic Ruby Crystal (Al₂O₃ + 0.05% Cr³⁺) pumped by Helical Xenon Flash Lamp
  </text>

  <!-- Outer Glass Cooling Jacket -->
  <rect x="180" y="140" width="580" height="200" rx="20" fill="url(#coolGlassGrad)" stroke="#00838F" stroke-width="3"/>
  <text x="210" y="165" font-size="12" font-weight="bold" fill="#006064">Glass Cooling Jacket</text>

  <!-- Cooling Water Circulation -->
  <g class="water-flow">
    <!-- Water In -->
    <line x1="280" y1="380" x2="280" y2="340" stroke="#0288D1" stroke-width="4"/>
    <!-- Water Out -->
    <line x1="680" y1="340" x2="680" y2="380" stroke="#0288D1" stroke-width="4"/>
  </g>
  <polygon points="280,335 273,348 287,348" fill="#0288D1"/>
  <polygon points="680,385 673,372 687,372" fill="#0288D1"/>
  <text x="280" y="405" text-anchor="middle" font-size="12" font-weight="bold" fill="#0277BD">Cooling Water In</text>
  <text x="680" y="405" text-anchor="middle" font-size="12" font-weight="bold" fill="#0277BD">Cooling Water Out</text>

  <!-- Central Pink Ruby Rod -->
  <rect x="250" y="210" width="460" height="60" rx="4" fill="url(#rubyRodGrad)" stroke="#880E4F" stroke-width="3"/>
  <text x="480" y="246" text-anchor="middle" font-size="14" font-weight="900" fill="#FFFFFF">
    RUBY CRYSTAL ROD (Al₂O₃ + 0.05% Cr³⁺)  L ~ 4 cm, D ~ 0.5 cm
  </text>

  <!-- 100% Silvered Left Face -->
  <rect x="235" y="200" width="18" height="80" rx="3" fill="#212121" stroke="#000000" stroke-width="2"/>
  <text x="244" y="130" text-anchor="middle" font-size="11" font-weight="bold" fill="#212121">100% Silvered</text>
  <text x="244" y="145" text-anchor="middle" font-size="10" font-weight="bold" fill="#424242">(Full Reflector)</text>
  <line x1="244" y1="152" x2="244" y2="195" stroke="#212121" stroke-width="1.8"/>

  <!-- ~90% Partially Silvered Right Face -->
  <rect x="707" y="200" width="18" height="80" rx="3" fill="#757575" stroke="#424242" stroke-width="2"/>
  <text x="716" y="130" text-anchor="middle" font-size="11" font-weight="bold" fill="#424242">90% Silvered</text>
  <text x="716" y="145" text-anchor="middle" font-size="10" font-weight="bold" fill="#616161">(Partial Output)</text>
  <line x1="716" y1="152" x2="716" y2="195" stroke="#424242" stroke-width="1.8"/>

  <!-- Helical Xenon Flash Tube Wrapped Around Ruby Rod -->
  <g class="xenon-flash-anim">
    <!-- Helical coils -->
    <path d="M 300 170 Q 330 200 330 240 Q 330 280 300 310" fill="none" stroke="#FFA000" stroke-width="7" stroke-linecap="round"/>
    <path d="M 370 170 Q 400 200 400 240 Q 400 280 370 310" fill="none" stroke="#FFA000" stroke-width="7" stroke-linecap="round"/>
    <path d="M 440 170 Q 470 200 470 240 Q 470 280 440 310" fill="none" stroke="#FFA000" stroke-width="7" stroke-linecap="round"/>
    <path d="M 510 170 Q 540 200 540 240 Q 540 280 510 310" fill="none" stroke="#FFA000" stroke-width="7" stroke-linecap="round"/>
    <path d="M 580 170 Q 610 200 610 240 Q 610 280 580 310" fill="none" stroke="#FFA000" stroke-width="7" stroke-linecap="round"/>
    <path d="M 650 170 Q 680 200 680 240 Q 680 280 650 310" fill="none" stroke="#FFA000" stroke-width="7" stroke-linecap="round"/>
  </g>

  <!-- Flash Lamp Power Source -->
  <rect x="420" y="380" width="120" height="50" rx="8" fill="#FFE082" stroke="#FFA000" stroke-width="2.5"/>
  <text x="480" y="402" text-anchor="middle" font-size="12" font-weight="bold" fill="#E65100">Power Source</text>
  <text x="480" y="418" text-anchor="middle" font-size="10" font-weight="bold" fill="#BF360C">(Xenon Flash Lamp)</text>

  <!-- Pulsed Laser Output Beam -->
  <g class="ruby-laser-pulse" filter="url(#rubyBeamGlow)">
    <line x1="730" y1="230" x2="940" y2="230" stroke="#FF1744" stroke-width="5"/>
    <line x1="730" y1="240" x2="940" y2="240" stroke="#D50000" stroke-width="7"/>
    <line x1="730" y1="250" x2="940" y2="250" stroke="#FF1744" stroke-width="5"/>
    <polygon points="948,240 934,230 934,250" fill="#D50000"/>
  </g>

  <rect x="760" y="160" width="180" height="42" rx="6" fill="#FFEBEE" stroke="#EF9A9A"/>
  <text x="850" y="178" text-anchor="middle" font-size="11" font-weight="bold" fill="#C62828">PULSED RED LASER</text>
  <text x="850" y="194" text-anchor="middle" font-size="11" font-weight="bold" fill="#B71C1C">λ = 6943 Å (694.3 nm)</text>

  <!-- Bottom Explanatory Card -->
  <g transform="translate(60, 445)">
    <rect width="840" height="55" rx="10" fill="#FFF1F2" stroke="#FECDD3"/>
    <text x="420" y="24" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#9F1239">
      • Optical Pumping: Xenon flash lamp emits green light (5500 Å) absorbed strongly by Cr³⁺ ions
    </text>
    <text x="420" y="44" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#881337">
      • Output Characteristic: Pulsed red light (duration ~ 1 millisecond, immense peak optical power)
    </text>
  </g>
</svg>
"""

def get_ruby_laser_energy_level_svg():
    return """
<svg id="svg-ruby-energy" class="interactive-svg" viewBox="0 0 960 520" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="rubyPhotonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    /* Step 1: Pumping transition */
    .ruby-step1-atom {
      animation: animRubyPump 5s ease-in-out infinite;
    }
    @keyframes animRubyPump {
      0%, 5% { transform: translateY(0); opacity: 1; }
      20%, 30% { transform: translateY(-240px); opacity: 1; }
      40%, 100% { transform: translateY(-240px); opacity: 0; }
    }

    /* Step 2: Radiationless transition */
    .ruby-step2-atom {
      animation: animRubyDecay 5s ease-in-out infinite;
    }
    @keyframes animRubyDecay {
      0%, 20% { opacity: 0; transform: translateY(-240px); }
      25% { opacity: 1; transform: translateY(-240px); }
      38%, 75% { opacity: 1; transform: translateY(-120px); }
      90%, 100% { opacity: 0; transform: translateY(-120px); }
    }

    /* Step 4: Stimulated laser emission */
    .ruby-step4-laser {
      animation: animRubyEmit 5s ease-in-out infinite;
    }
    @keyframes animRubyEmit {
      0%, 65% { opacity: 0; transform: translate(720px, 300px); }
      75% { opacity: 1; transform: translate(750px, 300px); }
      88% { opacity: 1; transform: translate(820px, 300px); }
      100% { opacity: 0; transform: translate(860px, 300px); }
    }
  </style>

  <text x="480" y="36" text-anchor="middle" font-family="system-ui" font-size="20" font-weight="900" fill="#B71C1C">
    WORKING OF RUBY LASER: 3-LEVEL ENERGY SYSTEM
  </text>
  <text x="480" y="60" text-anchor="middle" font-family="system-ui" font-size="13" font-weight="bold" fill="#475569">
    Energy levels of Chromium ions (Cr³⁺): Optical Pumping → Radiationless Drop → Stimulated Laser Emission
  </text>

  <!-- 3 Levels -->
  <!-- E3 Level (Band) -->
  <rect x="120" y="105" width="740" height="30" rx="4" fill="#FFCDD2" stroke="#E53935" stroke-width="2.5"/>
  <rect x="75" y="105" width="40" height="30" rx="6" fill="#FFEBEE" stroke="#EF5350"/>
  <text x="95" y="126" text-anchor="middle" font-size="16" font-weight="bold" fill="#C62828">E₃</text>
  <text x="875" y="125" font-size="13" font-weight="bold" fill="#C62828">Pump Band (Short life ~ 10⁻⁸ s)</text>

  <!-- E2 Level (Metastable) -->
  <line x1="340" y1="240" x2="860" y2="240" stroke="#8E24AA" stroke-width="4.5" stroke-linecap="round"/>
  <rect x="295" y="225" width="40" height="30" rx="6" fill="#F3E5F5" stroke="#BA68C8"/>
  <text x="315" y="246" text-anchor="middle" font-size="16" font-weight="bold" fill="#7B1FA2">E₂</text>
  <text x="875" y="245" font-size="13" font-weight="bold" fill="#7B1FA2">Metastable Level (Long life ~ 10⁻³ s)</text>

  <!-- E1 Level (Ground) -->
  <line x1="120" y1="360" x2="860" y2="360" stroke="#1565C0" stroke-width="4.5" stroke-linecap="round"/>
  <rect x="75" y="345" width="40" height="30" rx="6" fill="#E3F2FD" stroke="#42A5F5"/>
  <text x="95" y="366" text-anchor="middle" font-size="16" font-weight="bold" fill="#1565C0">E₁</text>
  <text x="875" y="365" font-size="13" font-weight="bold" fill="#1565C0">Ground State (Cr³⁺ in normal state)</text>

  <!-- STEP 1: OPTICAL PUMPING -->
  <line x1="200" y1="345" x2="200" y2="145" stroke="#2E7D32" stroke-width="4"/>
  <polygon points="200,135 192,150 208,150" fill="#2E7D32"/>
  <rect x="130" y="215" width="65" height="42" rx="6" fill="#E8F5E9" stroke="#81C784"/>
  <text x="162" y="233" text-anchor="middle" font-size="11" font-weight="bold" fill="#1B5E20">STEP 1</text>
  <text x="162" y="248" text-anchor="middle" font-size="10" font-weight="bold" fill="#2E7D32">5500 Å</text>

  <!-- STEP 2: FAST RADIATIONLESS DECAY -->
  <line x1="420" y1="140" x2="420" y2="230" stroke="#F57C00" stroke-width="3.5" stroke-dasharray="6 4"/>
  <polygon points="420,238 413,225 427,225" fill="#F57C00"/>
  <rect x="430" y="165" width="130" height="42" rx="6" fill="#FFF3E0" stroke="#FFB74D"/>
  <text x="495" y="183" text-anchor="middle" font-size="11" font-weight="bold" fill="#E65100">STEP 2: Fast Decay</text>
  <text x="495" y="198" text-anchor="middle" font-size="10" font-weight="bold" fill="#BF360C">(Energy to lattice)</text>

  <!-- STEP 3: SPONTANEOUS TRIGGER -->
  <line x1="580" y1="250" x2="580" y2="345" stroke="#C2185B" stroke-width="3.5" stroke-dasharray="6 4"/>
  <polygon points="580,352 573,340 587,340" fill="#C2185B"/>
  <rect x="590" y="280" width="115" height="32" rx="6" fill="#FCE4EC" stroke="#F48FB1"/>
  <text x="647" y="300" text-anchor="middle" font-size="10" font-weight="bold" fill="#AD1457">STEP 3: Trigger</text>

  <!-- STEP 4: STIMULATED LASER EMISSION -->
  <line x1="720" y1="250" x2="720" y2="345" stroke="#D50000" stroke-width="4.5"/>
  <polygon points="720,355 711,338 729,338" fill="#D50000"/>
  <rect x="730" y="280" width="130" height="32" rx="6" fill="#FFEBEE" stroke="#EF9A9A"/>
  <text x="795" y="300" text-anchor="middle" font-size="10" font-weight="bold" fill="#B71C1C">STEP 4: Laser Action</text>

  <!-- Moving Atoms -->
  <circle cx="200" cy="360" r="12" fill="#2E7D32" stroke="#1B5E20" stroke-width="2" class="ruby-step1-atom"/>
  <circle cx="420" cy="360" r="12" fill="#F57C00" stroke="#E65100" stroke-width="2" class="ruby-step2-atom"/>

  <!-- Emitted Laser Waves -->
  <g class="ruby-step4-laser" filter="url(#rubyPhotonGlow)">
    <path d="M 0 0 Q 15 -10 30 0 T 60 0 T 90 0 T 120 0 L 140 0" fill="none" stroke="#D50000" stroke-width="3.5"/>
    <polygon points="146,0 134,-6 134,6" fill="#D50000"/>
    <text x="70" y="-12" text-anchor="middle" font-size="11" font-weight="bold" fill="#D50000">6943 Å (Laser Light)</text>
  </g>

  <!-- Bottom Explanatory Card -->
  <g transform="translate(80, 420)">
    <rect width="800" height="65" rx="10" fill="#F8FAFC" stroke="#CBD5E1"/>
    <text x="400" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#0F172A">
      • E₂ is a Metastable level with lifetime ~ 3 ms (100,000× longer than normal excited state)
    </text>
    <text x="400" y="44" text-anchor="middle" font-size="12" font-weight="bold" fill="#334155">
      • Pumping transfers ions to E₃; they quickly fall to E₂, creating population inversion: N(E₂) &gt; N(E₁)
    </text>
  </g>
</svg>
"""

def get_hene_laser_construction_svg():
    return """
<svg id="svg-hene-const" class="interactive-svg" viewBox="0 0 960 520" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="quartzGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#EDE7F6" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#D1C4E9" stop-opacity="0.4"/>
    </linearGradient>
    <filter id="heneBeamGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="7" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    /* RF Discharge Pulse */
    .rf-discharge-pulse {
      animation: animRfDischarge 2.5s ease-in-out infinite;
    }
    @keyframes animRfDischarge {
      0%, 100% { opacity: 0.45; }
      50% { opacity: 0.9; filter: drop-shadow(0 0 10px #7C4DFF); }
    }

    /* Plasma Discharge Glow */
    .hene-plasma-glow {
      animation: animHenePlasma 2.5s ease-in-out infinite;
    }
    @keyframes animHenePlasma {
      0%, 100% { fill-opacity: 0.35; }
      50% { fill-opacity: 0.7; filter: drop-shadow(0 0 12px #FF5252); }
    }

    /* Continuous Laser Beam */
    .hene-cw-beam {
      stroke-dasharray: 20 10;
      animation: animHeneCw 1.2s linear infinite;
    }
    @keyframes animHeneCw {
      to { stroke-dashoffset: -60; }
    }
  </style>

  <text x="480" y="36" text-anchor="middle" font-family="system-ui" font-size="20" font-weight="900" fill="#0D47A1">
    CONSTRUCTION OF HELIUM-NEON (He-Ne) GAS LASER
  </text>
  <text x="480" y="60" text-anchor="middle" font-family="system-ui" font-size="13" font-weight="bold" fill="#475569">
    Continuous Wave (CW) Gas Laser: Fused Quartz Tube (80 cm × 1.5 cm) with He:Ne Gas Mixture (10:1)
  </text>

  <!-- Fused Quartz Discharge Tube Body -->
  <rect x="180" y="190" width="600" height="100" rx="14" fill="url(#quartzGrad)" stroke="#3F51B5" stroke-width="3.5"/>
  
  <!-- Bulbous Ends (as shown in textbook notes) -->
  <circle cx="210" cy="240" r="50" fill="#EDE7F6" stroke="#3F51B5" stroke-width="3.5"/>
  <circle cx="750" cy="240" r="50" fill="#EDE7F6" stroke="#3F51B5" stroke-width="3.5"/>

  <!-- Glowing Pinkish-Red He-Ne Plasma Core -->
  <rect x="220" y="215" width="520" height="50" rx="8" fill="#FF8A80" class="hene-plasma-glow"/>
  <text x="480" y="245" text-anchor="middle" font-size="14" font-weight="900" fill="#FFFFFF">
    He-Ne Gas Mixture (Ratio 10 : 1 | He at ~ 1 mm Hg, Ne at ~ 0.1 mm Hg)
  </text>

  <!-- Left Perfect Reflector (100% R) -->
  <rect x="135" y="170" width="20" height="140" rx="4" fill="#263238" stroke="#000000" stroke-width="2"/>
  <g stroke="#90A4AE" stroke-width="2.5">
    <line x1="125" y1="185" x2="135" y2="195"/>
    <line x1="125" y1="215" x2="135" y2="225"/>
    <line x1="125" y1="245" x2="135" y2="255"/>
    <line x1="125" y1="275" x2="135" y2="285"/>
  </g>
  <rect x="50" y="215" width="80" height="50" rx="6" fill="#ECEFF1" stroke="#90A4AE"/>
  <text x="90" y="236" text-anchor="middle" font-size="11" font-weight="bold" fill="#263238">Full Mirror</text>
  <text x="90" y="254" text-anchor="middle" font-size="11" font-weight="bold" fill="#D32F2F">100% R</text>

  <!-- Right Partial Reflector (~99% R) -->
  <rect x="805" y="170" width="20" height="140" rx="4" fill="#78909C" stroke="#37474F" stroke-width="2"/>
  <g stroke="#B0BEC5" stroke-width="2.5">
    <line x1="825" y1="185" x2="835" y2="195"/>
    <line x1="825" y1="215" x2="835" y2="225"/>
    <line x1="825" y1="245" x2="835" y2="255"/>
    <line x1="825" y1="275" x2="835" y2="285"/>
  </g>
  <rect x="835" y="215" width="95" height="50" rx="6" fill="#ECEFF1" stroke="#90A4AE"/>
  <text x="882" y="236" text-anchor="middle" font-size="11" font-weight="bold" fill="#37474F">Partial Mirror</text>
  <text x="882" y="254" text-anchor="middle" font-size="11" font-weight="bold" fill="#D32F2F">99% R, 1% T</text>

  <!-- Electrodes -->
  <rect x="320" y="150" width="18" height="40" fill="#212121"/>
  <rect x="620" y="150" width="18" height="40" fill="#212121"/>
  <text x="470" y="135" text-anchor="middle" font-size="13" font-weight="bold" fill="#212121">Electrodes</text>
  <line x1="338" y1="135" x2="425" y2="135" stroke="#424242" stroke-width="1.8"/>
  <line x1="515" y1="135" x2="620" y2="135" stroke="#424242" stroke-width="1.8"/>

  <!-- R.F. Generator Box -->
  <g class="rf-discharge-pulse">
    <rect x="400" y="360" width="160" height="55" rx="8" fill="#FFE0B2" stroke="#E65100" stroke-width="2.5"/>
    <text x="480" y="384" text-anchor="middle" font-size="13" font-weight="bold" fill="#BF360C">R.F. Generator</text>
    <text x="480" y="402" text-anchor="middle" font-size="11" font-weight="bold" fill="#E65100">(27.12 MHz, ~50 W)</text>
  </g>

  <!-- Curly Connecting Leads -->
  <path d="M 329 150 Q 300 280 400 380" fill="none" stroke="#D84315" stroke-width="2.5"/>
  <path d="M 629 150 Q 660 280 560 380" fill="none" stroke="#D84315" stroke-width="2.5"/>

  <!-- Continuous Laser Beam Output -->
  <g filter="url(#heneBeamGlow)">
    <line x1="825" y1="235" x2="950" y2="235" stroke="#FF1744" stroke-width="5" class="hene-cw-beam"/>
    <line x1="825" y1="245" x2="950" y2="245" stroke="#D50000" stroke-width="6" class="hene-cw-beam"/>
    <polygon points="958,240 944,232 944,248" fill="#D50000"/>
  </g>

  <rect x="800" y="110" width="150" height="42" rx="6" fill="#FFEBEE" stroke="#EF9A9A"/>
  <text x="875" y="128" text-anchor="middle" font-size="11" font-weight="bold" fill="#C62828">CONTINUOUS LASER</text>
  <text x="875" y="144" text-anchor="middle" font-size="11" font-weight="bold" fill="#B71C1C">λ = 632.8 nm (Red)</text>

  <!-- Bottom Explanatory Card -->
  <g transform="translate(60, 445)">
    <rect width="840" height="55" rx="10" fill="#EEF2FF" stroke="#C7D2FE"/>
    <text x="420" y="24" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#3730A3">
      • Gas Mixture: 10 parts Helium to 1 part Neon. Helium acts as the excitation pump agent via electric discharge
    </text>
    <text x="420" y="44" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#4338CA">
      • CW Operation: Emits unbroken Continuous Wave high-purity laser light (unlike pulsed Ruby laser)
    </text>
  </g>
</svg>
"""

def get_hene_laser_energy_level_svg():
    return """
<svg id="svg-hene-energy" class="interactive-svg" viewBox="0 0 960 520" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="heneLaserGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    /* Resonant collision transfer animation */
    .resonant-transfer-pulse {
      stroke-dasharray: 8 6;
      animation: animResonantTransfer 3s linear infinite;
    }
    @keyframes animResonantTransfer {
      to { stroke-dashoffset: -28; }
    }

    /* Laser transition wave animation */
    .hene-red-wave {
      animation: animHeneWave 3s ease-in-out infinite;
    }
    @keyframes animHeneWave {
      0%, 45% { opacity: 0; transform: translate(720px, 200px); }
      55% { opacity: 1; transform: translate(740px, 200px); }
      85% { opacity: 1; transform: translate(800px, 200px); }
      100% { opacity: 0; transform: translate(840px, 200px); }
    }
  </style>

  <text x="480" y="34" text-anchor="middle" font-family="system-ui" font-size="20" font-weight="900" fill="#0D47A1">
    ENERGY LEVEL DIAGRAM &amp; WORKING OF He-Ne LASER
  </text>
  <text x="480" y="58" text-anchor="middle" font-family="system-ui" font-size="13" font-weight="bold" fill="#475569">
    Electron Collision excites Helium → Resonant Inelastic Collisions pump Neon → 632.8 nm Continuous Laser Emission
  </text>

  <!-- Vertical Divider separating Helium and Neon sides -->
  <line x1="410" y1="80" x2="410" y2="470" stroke="#CBD5E1" stroke-width="2" stroke-dasharray="6 4"/>

  <!-- ================= HELIUM (He) SIDE ================= -->
  <text x="210" y="95" text-anchor="middle" font-size="16" font-weight="900" fill="#0277BD">
    HELIUM (He) ATOMS
  </text>
  <text x="210" y="115" text-anchor="middle" font-size="12" font-weight="bold" fill="#0288D1">
    (Excitation Pump Agent)
  </text>

  <!-- He 20.61 eV Level (E3) -->
  <line x1="60" y1="160" x2="380" y2="160" stroke="#0288D1" stroke-width="4.5" stroke-linecap="round"/>
  <rect x="20" y="145" width="38" height="30" rx="6" fill="#E1F5FE" stroke="#81D4FA"/>
  <text x="39" y="165" text-anchor="middle" font-size="14" font-weight="bold" fill="#01579B">E₃</text>
  <text x="220" y="152" text-anchor="middle" font-size="12" font-weight="bold" fill="#01579B">2¹S (Metastable: 20.61 eV)</text>

  <!-- He 19.81 eV Level (E2) -->
  <line x1="120" y1="210" x2="380" y2="210" stroke="#0288D1" stroke-width="4.5" stroke-linecap="round"/>
  <rect x="75" y="195" width="38" height="30" rx="6" fill="#E1F5FE" stroke="#81D4FA"/>
  <text x="94" y="215" text-anchor="middle" font-size="14" font-weight="bold" fill="#01579B">E₂</text>
  <text x="240" y="202" text-anchor="middle" font-size="12" font-weight="bold" fill="#01579B">2³S (Metastable: 19.81 eV)</text>

  <!-- He Ground Level (E1) -->
  <line x1="60" y1="410" x2="380" y2="410" stroke="#263238" stroke-width="4.5" stroke-linecap="round"/>
  <rect x="20" y="395" width="38" height="30" rx="6" fill="#ECEFF1" stroke="#90A4AE"/>
  <text x="39" y="415" text-anchor="middle" font-size="14" font-weight="bold" fill="#263238">E₁</text>
  <text x="220" y="430" text-anchor="middle" font-size="12" font-weight="bold" fill="#263238">1¹S (Ground State: 0 eV)</text>

  <!-- Electron Impact Discharge Arrows -->
  <line x1="120" y1="395" x2="120" y2="175" stroke="#D84315" stroke-width="3.5"/>
  <polygon points="120,165 113,180 127,180" fill="#D84315"/>
  <rect x="65" y="260" width="110" height="42" rx="6" fill="#FBE9E7" stroke="#FFAB91"/>
  <text x="120" y="278" text-anchor="middle" font-size="10" font-weight="bold" fill="#BF360C">Electric Discharge</text>
  <text x="120" y="293" text-anchor="middle" font-size="9" font-weight="bold" fill="#D84315">e⁻ + He → He* + e⁻</text>

  <!-- ================= NEON (Ne) SIDE ================= -->
  <text x="680" y="95" text-anchor="middle" font-size="16" font-weight="900" fill="#C2185B">
    NEON (Ne) ATOMS
  </text>
  <text x="680" y="115" text-anchor="middle" font-size="12" font-weight="bold" fill="#D81B60">
    (Laser Active Lasing Medium)
  </text>

  <!-- Resonant Energy Transfer from He to Ne -->
  <g class="resonant-transfer-pulse">
    <line x1="380" y1="160" x2="495" y2="155" stroke="#00897B" stroke-width="3.5"/>
    <line x1="380" y1="210" x2="495" y2="205" stroke="#00897B" stroke-width="3.5"/>
  </g>
  <polygon points="502,155 490,149 490,161" fill="#00897B"/>
  <polygon points="502,205 490,199 490,211" fill="#00897B"/>
  <rect x="375" y="115" width="130" height="26" rx="5" fill="#E0F2F1" stroke="#80CBC4"/>
  <text x="440" y="132" text-anchor="middle" font-size="10" font-weight="bold" fill="#004D40">Resonant Collisions</text>

  <!-- Ne 20.66 eV Level (E5') -->
  <line x1="505" y1="155" x2="890" y2="155" stroke="#7B1FA2" stroke-width="4.5" stroke-linecap="round"/>
  <rect x="895" y="140" width="40" height="30" rx="6" fill="#F3E5F5" stroke="#BA68C8"/>
  <text x="915" y="160" text-anchor="middle" font-size="14" font-weight="bold" fill="#6A1B9A">E₅′</text>
  <text x="650" y="148" text-anchor="middle" font-size="12" font-weight="bold" fill="#6A1B9A">3s (Metastable: 20.66 eV)</text>

  <!-- Ne 19.82 eV Level (E4') -->
  <line x1="505" y1="205" x2="890" y2="205" stroke="#7B1FA2" stroke-width="4.5" stroke-linecap="round"/>
  <rect x="895" y="190" width="40" height="30" rx="6" fill="#F3E5F5" stroke="#BA68C8"/>
  <text x="915" y="210" text-anchor="middle" font-size="14" font-weight="bold" fill="#6A1B9A">E₄′</text>
  <text x="650" y="198" text-anchor="middle" font-size="12" font-weight="bold" fill="#6A1B9A">2s (Metastable: 19.82 eV)</text>

  <!-- Ne 18.70 eV Level (E3') -->
  <line x1="550" y1="280" x2="890" y2="280" stroke="#D32F2F" stroke-width="4.5" stroke-linecap="round"/>
  <rect x="895" y="265" width="40" height="30" rx="6" fill="#FFEBEE" stroke="#EF5350"/>
  <text x="915" y="285" text-anchor="middle" font-size="14" font-weight="bold" fill="#C62828">E₃′</text>
  <text x="720" y="272" text-anchor="middle" font-size="12" font-weight="bold" fill="#C62828">2p (Lower Laser Level: 18.70 eV)</text>

  <!-- Ne 16.7 eV Level (E2') -->
  <line x1="550" y1="350" x2="890" y2="350" stroke="#FB8C00" stroke-width="4.5" stroke-linecap="round"/>
  <rect x="895" y="335" width="40" height="30" rx="6" fill="#FFF3E0" stroke="#FFB74D"/>
  <text x="915" y="355" text-anchor="middle" font-size="14" font-weight="bold" fill="#E65100">E₂′</text>
  <text x="720" y="342" text-anchor="middle" font-size="12" font-weight="bold" fill="#E65100">1s (~ 16.7 eV)</text>

  <!-- Ne Ground Level (E1') -->
  <line x1="505" y1="410" x2="890" y2="410" stroke="#263238" stroke-width="4.5" stroke-linecap="round"/>
  <rect x="895" y="395" width="40" height="30" rx="6" fill="#ECEFF1" stroke="#90A4AE"/>
  <text x="915" y="415" text-anchor="middle" font-size="14" font-weight="bold" fill="#263238">E₁′</text>
  <text x="700" y="430" text-anchor="middle" font-size="12" font-weight="bold" fill="#263238">Ground State (0 eV)</text>

  <!-- 632.8 nm Laser Transition Arrow (E5' -> E3') -->
  <line x1="720" y1="165" x2="720" y2="265" stroke="#D50000" stroke-width="4.5"/>
  <polygon points="720,273 711,258 729,258" fill="#D50000"/>
  <rect x="735" y="195" width="135" height="42" rx="6" fill="#FFEBEE" stroke="#EF9A9A"/>
  <text x="802" y="213" text-anchor="middle" font-size="11" font-weight="bold" fill="#C62828">LASER TRANSITION</text>
  <text x="802" y="228" text-anchor="middle" font-size="11" font-weight="bold" fill="#B71C1C">λ = 632.8 nm (Red)</text>

  <!-- Spontaneous Decay (E3' -> E2') -->
  <line x1="650" y1="288" x2="650" y2="340" stroke="#E65100" stroke-width="3" stroke-dasharray="5 3"/>
  <polygon points="650,345 644,334 656,334" fill="#E65100"/>
  <text x="590" y="315" font-size="10" font-weight="bold" fill="#E65100">Spontaneous Drop</text>

  <!-- Wall De-excitation (E2' -> E1') -->
  <line x1="600" y1="358" x2="600" y2="402" stroke="#37474F" stroke-width="3" stroke-dasharray="5 3"/>
  <polygon points="600,406 594,395 606,395" fill="#37474F"/>
  <text x="525" y="380" font-size="10" font-weight="bold" fill="#37474F">Tube Wall Collisions</text>

  <!-- Animated Laser Waves -->
  <g class="hene-red-wave" filter="url(#heneLaserGlow)">
    <path d="M 0 0 Q 15 -10 30 0 T 60 0 T 90 0 T 120 0 L 140 0" fill="none" stroke="#D50000" stroke-width="3.5"/>
    <polygon points="146,0 134,-6 134,6" fill="#D50000"/>
    <text x="70" y="-10" text-anchor="middle" font-size="11" font-weight="bold" fill="#D50000">632.8 nm Red Photon</text>
  </g>

  <!-- Bottom Explanatory Card -->
  <g transform="translate(60, 448)">
    <rect width="840" height="55" rx="10" fill="#F8FAFC" stroke="#CBD5E1"/>
    <text x="420" y="24" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#0F172A">
      • Resonant Transfer: Energy gap between He (20.61 eV) and Ne (20.66 eV) is only 0.05 eV (easily bridged by kinetic thermal motion)
    </text>
    <text x="420" y="44" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#334155">
      • Narrow Tube: Narrow bore diameter (~1.5 cm) ensures neon atoms at E₂′ collide rapidly with walls to avoid bottlenecking
    </text>
  </g>
</svg>
"""
