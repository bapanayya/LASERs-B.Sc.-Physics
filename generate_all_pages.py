# Master script to assemble index.html and all 7 individual topic pages
import os
import sys

sys.path.insert(0, r"E:\Google-AntiGravity-Projects\1.PPTs-Lecture-Notes\LASERS-BSc.Physics")
from build_html_suite import get_shared_css, get_shared_js
from annotation_module import get_annotation_css, get_annotation_html, get_annotation_js
from svg_diagrams import (
    get_ordinary_vs_laser_svg,
    get_spontaneous_vs_stimulated_svg,
    get_population_inversion_svg,
    get_laser_principle_svg,
    get_ruby_laser_construction_svg,
    get_ruby_laser_energy_level_svg,
    get_hene_laser_construction_svg,
    get_hene_laser_energy_level_svg
)

base_dir = r"E:\Google-AntiGravity-Projects\1.PPTs-Lecture-Notes\LASERS-BSc.Physics"

def get_section_1_html():
    return f"""
    <!-- SECTION 1: WHAT IS LASER & PROPERTIES -->
    <section id="section-1" class="topic-section">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
        <div class="glossy-heading gloss-red">
          <span>1. What is LASER? What are the Properties of LASERS?</span>
        </div>
        <button class="action-pill pill-blue" onclick="speakSection('section-1', this)">🔊 Listen to Section</button>
      </div>

      <div class="glossy-subheading gloss-red">What Does LASER Stand For?</div>
      <ul class="bullets">
        <li><span class="bold-keyword">LASER</span> is an acronym for: <span class="bold-keyword" style="color:#D50000;">L</span>ight <span class="bold-keyword" style="color:#D50000;">A</span>mplification by <span class="bold-keyword" style="color:#D50000;">S</span>timulated <span class="bold-keyword" style="color:#D50000;">E</span>mission of <span class="bold-keyword" style="color:#D50000;">R</span>adiation.</li>
        <li>It is a device that generates an extraordinarily intense, highly directional, and single-colored (monochromatic) beam of coherent light.</li>
        <li><span class="bold-keyword">Theoretical Prediction:</span> Albert Einstein predicted the theoretical basis of stimulated emission in 1917.</li>
        <li><span class="bold-keyword">First Practical Microwave Device:</span> In 1954, Charles H. Townes and co-workers developed the MASER (Microwave Amplification by Stimulated Emission of Radiation).</li>
        <li><span class="bold-keyword">First Optical Laser:</span> In 1960, Theodore H. Maiman constructed the first working optical laser using a synthetic Ruby crystal rod, emitting deep red light at wavelength <b>694.3 nm (6943 Å)</b>.</li>
        <li><span class="bold-keyword">First Continuous Gas Laser:</span> In 1961, Ali Javan, William Bennett, and Donald Herriot created the Helium-Neon (He-Ne) gas laser, producing continuous red light at <b>632.8 nm</b>.</li>
      </ul>

      <!-- Real-World Laser Device Showcase -->
      <div class="real-device-card">
        <div class="real-device-header">
          <span class="real-badge">📷 Real-World Apparatus</span>
          <h4 class="real-device-title">Physical Laser Devices in the Laboratory</h4>
        </div>
        <div class="real-device-grid">
          <div class="real-img-item">
            <img src="./real-devices/real_laser_lab_experiment.jpg" alt="Real Laser Optics Physics Experiment" class="real-device-img">
            <p class="real-caption"><strong>Modern Physics Laboratory Laser:</strong> Coherent, collimated optical laser beam propagated along precision mirror mounts on an optical bench in an active photonics research laboratory.</p>
          </div>
          <div class="real-img-item">
            <img src="./real-devices/real_laser_green_beam.jpg" alt="Real High-Intensity Laser Beam in Air" class="real-device-img">
            <p class="real-caption"><strong>Extreme Directionality &amp; Coherence:</strong> Visible laser beam in air demonstrating razor-thin pencil propagation with near-zero angular divergence across long distances.</p>
          </div>
        </div>
      </div>

      <div class="glossy-subheading gloss-red">Four Fundamental Properties of LASER Light</div>
      <ul class="bullets">
        <li><span class="bold-keyword">1. High Degree of Coherence:</span> All emitted light waves possess identical frequency and maintain a constant phase difference over space and time (spatial and temporal coherence). Waves propagate in perfect phase synchronization.</li>
        <li><span class="bold-keyword">2. High Directionality:</span> Ordinary light diverges and radiates in all directions. Laser light propagates in an extremely parallel beam with negligible angular divergence, allowing it to travel immense distances (e.g., Earth to Moon telemetry) with minimal beam spread.</li>
        <li><span class="bold-keyword">3. Extraordinary Monochromaticity:</span> Ordinary light sources emit a broad spectral band containing multiple wavelengths. Laser light exhibits an extremely narrow spectral linewidth (Δλ ≈ 10⁻⁴ Å), producing exceptionally pure single-wavelength radiation.</li>
        <li><span class="bold-keyword">4. Immense Intensity (Brightness):</span> Because laser radiation is concentrated into a narrow, non-diverging beam, immense energy is focused per unit area. Even a low-power milliwatt laser has a localized brightness vastly higher than conventional high-wattage lamps.</li>
      </ul>

      <!-- DIAGRAM 1: LIGHT COMPARISON & PROPERTIES -->
      <div id="diagram-box-1" class="diagram-box">
        <div class="diagram-nav">
          <div class="diagram-label">Diagram 1: Comparison of Ordinary Light vs LASER Light</div>
          <div class="diagram-view-tabs">
            <button class="view-btn active" onclick="switchDiagramTab('diagram-box-1', 'tab-anim', this)">✨ Animated Interactive Diagram</button>
            <button class="view-btn" onclick="switchDiagramTab('diagram-box-1', 'tab-digitized', this)">🖼️ High-Res Digitized Image</button>
          </div>
        </div>

        <!-- 1. Animated View -->
        <div class="diagram-content-view tab-anim active">
          {get_ordinary_vs_laser_svg()}
          <div class="ctrl-bar">
            <button class="ctrl-btn primary" onclick="replayDiagramAnim('svg-prop', 'status-prop')">↺ Replay Animation</button>
            <button class="ctrl-btn" onclick="pauseDiagramAnim('svg-prop', 'status-prop')">⏸ Pause</button>
            <button class="ctrl-btn" onclick="playDiagramAnim('svg-prop', 'status-prop')">▶ Play</button>
            <button class="ctrl-btn" onclick="showFullDiagram('svg-prop', 'status-prop')">👁️ Show Complete Diagram</button>
            <span id="status-prop" class="status-pill">▶ Animation Running</span>
          </div>
        </div>

        <!-- 2. Digitized View -->
        <div class="diagram-content-view tab-digitized">
          <img src="./digitized-diagrams/laser_properties_comparison.png" alt="Laser Properties Comparison" class="diagram-image">
        </div>
      </div>

      <!-- MAIN COMPONENTS OF A LASER -->
      <div class="glossy-subheading gloss-red">The Three Essential Components of Any LASER System</div>
      <ul class="bullets">
        <li><span class="bold-keyword">1. Active Medium (Laser Material):</span> The material (solid, liquid, gas, or semiconductor) containing active quantum centers with suitable metastable energy levels to achieve population inversion.</li>
        <li><span class="bold-keyword">2. Energy Source (Pumping System):</span> An external energy supply (such as optical flash lamps, high-voltage electric discharge, or chemical reactions) that raises atoms from the ground state into higher excited states.</li>
        <li><span class="bold-keyword">3. Optical Resonator (Resonant Cavity):</span> A pair of strictly parallel mirrors bounding the active medium. One mirror is 100% fully reflective and the other is partially reflective (transmitting ~1% to 10%), providing directional feedback and optical amplification.</li>
      </ul>

      <!-- DIAGRAM 1B: COMPONENTS OF LASER -->
      <div id="diagram-box-1b" class="diagram-box">
        <div class="diagram-nav">
          <div class="diagram-label">Diagram 1B: Main Components of a Laser</div>
        </div>
        <div class="diagram-content-view tab-digitized active">
          <img src="./digitized-diagrams/laser_components.png" alt="Main Components of a Laser" class="diagram-image">
        </div>
      </div>

      <!-- Knowledge Check Quiz -->
      <div class="quiz-card">
        <div class="quiz-question">Quick Quiz: Which property of LASER light allows it to focus huge energy onto a tiny spot without spreading?</div>
        <button class="quiz-btn" onclick="checkQuiz(this, true, 'fb-q1', 'High directionality and coherence allow laser rays to travel strictly parallel with virtually zero angular spread, focusing maximum energy on a pinpoint spot!')">A) High Directionality &amp; Coherence</button>
        <button class="quiz-btn" onclick="checkQuiz(this, false, 'fb-q1', 'Random divergence causes light to scatter outwards in all directions, reducing focus!')">B) Broad divergence in all directions</button>
        <button class="quiz-btn" onclick="checkQuiz(this, false, 'fb-q1', 'Polychromatic light contains multiple wavelengths that refract at different angles!')">C) Multi-color broad spectrum</button>
        <div id="fb-q1" class="quiz-feedback"></div>
      </div>
    </section>
    """

def get_section_2_html():
    return f"""
    <!-- SECTION 2: SPONTANEOUS VS STIMULATED EMISSION -->
    <section id="section-2" class="topic-section">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
        <div class="glossy-heading gloss-blue">
          <span>2. Distinguish Between Spontaneous Emission &amp; Stimulated Emission</span>
        </div>
        <button class="action-pill pill-blue" onclick="speakSection('section-2', this)">🔊 Listen to Section</button>
      </div>

      <div class="glossy-subheading gloss-blue">Preliminary: Absorption of Radiation</div>
      <ul class="bullets blue-style">
        <li>When an atom residing in the lower energy ground state (energy <span class="bold-keyword">E₁</span>) interacts with an electromagnetic photon of frequency <b>ν</b> satisfying <b>hν = E₂ - E₁</b>, it absorbs the incident energy.</li>
        <li>The atom is promoted to the higher excited state (energy <span class="bold-keyword">E₂</span>). This process is known as <span class="bold-keyword">Stimulated Absorption</span>.</li>
        <li>The atom cannot remain in this excited state indefinitely; it possesses a natural finite lifetime of approximately <b>10⁻⁸ seconds</b>.</li>
      </ul>

      <div class="glossy-subheading gloss-blue">A. Spontaneous Emission</div>
      <ul class="bullets blue-style">
        <li>Following the natural lifetime of ~10⁻⁸ s, the excited atom drops back to the lower energy state <span class="bold-keyword">E₁</span> spontaneously without external stimulation.</li>
        <li>During this transition, it emits a photon carrying energy <b>hν = E₂ - E₁</b>.</li>
        <li>Because atoms in a macroscopic assembly emit independently at random instants, emitted photons possess <span class="bold-keyword">random directions</span> and <span class="bold-keyword">random phases</span>.</li>
        <li>The emitted radiation is <span class="bold-keyword">incoherent</span>, non-directional, and has a <span class="bold-keyword">broad spectral width</span> (characteristic of conventional thermal sources like incandescent lamps).</li>
      </ul>

      <div class="glossy-subheading gloss-blue">B. Stimulated (Induced) Emission</div>
      <ul class="bullets blue-style">
        <li>While an atom resides in the excited state <span class="bold-keyword">E₂</span>, an external incident photon of energy matching <b>hν = E₂ - E₁</b> interacts with the atom.</li>
        <li>The electromagnetic field of the incident photon induces the excited atom to undergo a downward transition to level <span class="bold-keyword">E₁</span> immediately.</li>
        <li>The atom emits a <span class="bold-keyword">second photon</span> having the <b>identical frequency, phase, direction of propagation, and polarization</b> as the incident triggering photon.</li>
        <li>Both photons emerge in lockstep; their amplitudes add constructively, producing <span class="bold-keyword">coherent light amplification</span>.</li>
        <li>This phenomenon, established theoretically by Albert Einstein in 1917, is the physical foundation of the LASER.</li>
      </ul>

      <!-- DIAGRAM 2: SPONTANEOUS VS STIMULATED EMISSION -->
      <div id="diagram-box-2" class="diagram-box">
        <div class="diagram-nav">
          <div class="diagram-label">Diagram 2: Spontaneous Emission vs Stimulated Emission (Before &amp; After)</div>
          <div class="diagram-view-tabs">
            <button class="view-btn active" onclick="switchDiagramTab('diagram-box-2', 'tab-anim-2', this)">✨ Animated Interactive Diagram</button>
            <button class="view-btn" onclick="switchDiagramTab('diagram-box-2', 'tab-digitized-2', this)">🖼️ High-Res Digitized Image</button>
          </div>
        </div>

        <!-- 1. Animated View -->
        <div class="diagram-content-view tab-anim-2 active">
          {get_spontaneous_vs_stimulated_svg()}
          <div class="ctrl-bar">
            <button class="ctrl-btn primary" onclick="replayDiagramAnim('svg-emission', 'status-emission')">↺ Replay Animation</button>
            <button class="ctrl-btn" onclick="pauseDiagramAnim('svg-emission', 'status-emission')">⏸ Pause</button>
            <button class="ctrl-btn" onclick="playDiagramAnim('svg-emission', 'status-emission')">▶ Play</button>
            <button class="ctrl-btn" onclick="showFullDiagram('svg-emission', 'status-emission')">👁️ Show Complete Diagram</button>
            <span id="status-emission" class="status-pill">▶ Animation Running</span>
          </div>
        </div>

        <!-- 2. Digitized View -->
        <div class="diagram-content-view tab-digitized-2">
          <img src="./digitized-diagrams/spontaneous_vs_stimulated_emission.png" alt="Spontaneous vs Stimulated Emission Digitized" class="diagram-image">
        </div>
      </div>

      <!-- COMPARISON TABLE -->
      <div class="glossy-subheading gloss-blue">Distinction Table: Spontaneous vs. Stimulated Emission</div>
      <table class="styled-table">
        <thead>
          <tr style="background:#E3F2FD;">
            <th style="width:25%; color:#0D47A1;">Characteristic</th>
            <th style="width:37%; color:#0D47A1;">Spontaneous Emission</th>
            <th style="width:38%; color:#B71C1C;">Stimulated Emission</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="bold-keyword">1. Triggering Mechanism</span></td>
            <td>Occurs spontaneously after natural lifetime (~10⁻⁸ s) without external radiation.</td>
            <td>Induced by an external incident photon of energy matching <b>hν = E₂ - E₁</b>.</td>
          </tr>
          <tr>
            <td><span class="bold-keyword">2. Direction of Photons</span></td>
            <td>Emitted photons propagate in completely <b>random directions</b> (isotropic).</td>
            <td>Emitted photon propagates in the <b>exact same direction</b> as the incident photon.</td>
          </tr>
          <tr>
            <td><span class="bold-keyword">3. Phase Relationship</span></td>
            <td>Random phase differences between emitted photons (out of step).</td>
            <td>Identical phase (coherent lockstep with incident wave).</td>
          </tr>
          <tr>
            <td><span class="bold-keyword">4. Degree of Coherence</span></td>
            <td><b>Incoherent radiation</b>.</td>
            <td><b>Highly Coherent radiation</b>.</td>
          </tr>
          <tr>
            <td><span class="bold-keyword">5. Spectral Nature</span></td>
            <td>Polychromatic / broad spectrum with wide linewidth.</td>
            <td>Strictly <b>monochromatic</b> single wavelength radiation.</td>
          </tr>
          <tr>
            <td><span class="bold-keyword">6. Optical Amplification</span></td>
            <td>No amplification (independent emissions).</td>
            <td><b>Optical Amplification achieved</b> (1 incident photon yields 2 coherent photons).</td>
          </tr>
          <tr>
            <td><span class="bold-keyword">7. Transition Rate</span></td>
            <td>Rate = <b>A₂₁ · N₂</b> (proportional solely to population N₂).</td>
            <td>Rate = <b>B₂₁ · ρ(ν) · N₂</b> (proportional to radiation energy density ρ(ν) and N₂).</td>
          </tr>
        </tbody>
      </table>

      <!-- Knowledge Check Quiz -->
      <div class="quiz-card">
        <div class="quiz-question">Quick Quiz: In stimulated emission, what is the relationship between the incident photon and the newly emitted photon?</div>
        <button class="quiz-btn" onclick="checkQuiz(this, true, 'fb-q2', 'Stimulated emission produces a twin photon having the identical phase, frequency, direction, and polarization, amplifying the light!')">A) They have identical phase, frequency, direction, and polarization</button>
        <button class="quiz-btn" onclick="checkQuiz(this, false, 'fb-q2', 'Random phase and direction characterize spontaneous emission, not stimulated emission!')">B) They have random phases and travel in opposite directions</button>
        <button class="quiz-btn" onclick="checkQuiz(this, false, 'fb-q2', 'The emitted photon has the exact same energy (hν = E₂ - E₁), not double!')">C) The emitted photon has double the frequency of the incoming photon</button>
        <div id="fb-q2" class="quiz-feedback"></div>
      </div>
    </section>
    """

def get_section_3_html():
    return f"""
    <!-- SECTION 3: METASTABLE STATES & POPULATION INVERSION -->
    <section id="section-3" class="topic-section">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
        <div class="glossy-heading gloss-purple">
          <span>3. What are Metastable States &amp; Explain Population Inversion</span>
        </div>
        <button class="action-pill pill-blue" onclick="speakSection('section-3', this)">🔊 Listen to Section</button>
      </div>

      <div class="glossy-subheading gloss-purple">What is a Metastable State?</div>
      <ul class="bullets purple-style">
        <li>In general atomic systems, an atom excited to an upper level has an extraordinarily brief lifetime of approximately <span class="bold-keyword">10⁻⁸ seconds</span> before decaying.</li>
        <li>Because of this immediate decay, atoms cannot build up in ordinary excited states even with continuous energy excitation.</li>
        <li>However, in certain active media and dopant structures, particular energy levels exist where quantum mechanical selection rules forbid rapid spontaneous dipole transitions to lower levels.</li>
        <li>In these unique states, an excited atom remains for an unusually extended period: typically <span class="bold-keyword">10⁻³ seconds to 10⁻² seconds</span>.</li>
        <li>This represents a lifetime roughly <span class="bold-keyword">100,000 times longer</span> than an ordinary excited level. Such a state is termed a <span class="bold-keyword">Metastable State</span>.</li>
        <li><span class="bold-keyword">Physical Significance:</span> The metastable state functions as an energy reservoir where atoms accumulate in large concentrations, providing the foundation for population inversion.</li>
      </ul>

      <div class="glossy-subheading gloss-purple">What is Population Inversion?</div>
      <ul class="bullets purple-style">
        <li>Under thermal equilibrium governed by <span class="bold-keyword">Boltzmann's Distribution Law</span>, the atomic population <span class="bold-keyword">N₁</span> in lower energy state E₁ is always significantly greater than the population <span class="bold-keyword">N₂</span> in higher state E₂: <br>
          <span style="display:inline-block; margin:8px 0; padding:4px 16px; background:#F1F5F9; border-radius:6px; font-weight:bold; color:#1E293B;">N₂ = N₁ · e^(-(E₂ - E₁) / kT)  ⟹  N₁ &gt;&gt; N₂</span></li>
        <li>In this normal equilibrium, any incident radiation is predominantly attenuated through stimulated absorption rather than amplified.</li>
        <li><span class="bold-keyword">Definition:</span> The non-equilibrium state in which the atomic population of a specific higher energy level exceeds that of a lower energy level (<span class="bold-keyword" style="color:#D50000;">N₂ &gt; N₁</span>) is defined as <span class="bold-keyword">Population Inversion</span>.</li>
        <li>A medium or system maintaining population inversion is referred to as an <span class="bold-keyword">Active System</span>.</li>
        <li>Under population inversion, the rate of stimulated emission surpasses the rate of stimulated absorption, yielding <span class="bold-keyword">net optical amplification</span>.</li>
      </ul>

      <div class="glossy-subheading gloss-purple">Pumping Methods to Achieve Population Inversion</div>
      <ul class="bullets purple-style">
        <li>The external energy input mechanism used to transfer atoms from ground levels to excited levels to sustain population inversion is termed <span class="bold-keyword">Pumping</span>.</li>
        <li><span class="bold-keyword">1. Optical Pumping:</span> Strong light irradiation from external discharge flash lamps excites atoms (utilized in the <b>Ruby Laser</b>).</li>
        <li><span class="bold-keyword">2. Electric Discharge:</span> High-voltage electric fields accelerate electrons which collide inelastically with gas atoms to produce excitation (utilized in the <b>Helium-Neon (He-Ne) Laser</b>).</li>
        <li><span class="bold-keyword">3. Direct Electrical Injection:</span> Forward-biased semiconductor p-n junctions inject minority carriers directly into the recombination zone (utilized in <b>Semiconductor / Diode Lasers</b>).</li>
        <li><span class="bold-keyword">4. Chemical Reaction:</span> Energy released during exothermic molecular chemical reactions directly excites reaction products (utilized in <b>Carbon Dioxide (CO₂) &amp; Chemical Lasers</b>).</li>
      </ul>

      <!-- DIAGRAM 3: POPULATION INVERSION & METASTABLE STATE -->
      <div id="diagram-box-3" class="diagram-box">
        <div class="diagram-nav">
          <div class="diagram-label">Diagram 3: Process of Population Inversion in a 3-Level Quantum System</div>
          <div class="diagram-view-tabs">
            <button class="view-btn active" onclick="switchDiagramTab('diagram-box-3', 'tab-anim-3', this)">✨ Animated Interactive Diagram</button>
            <button class="view-btn" onclick="switchDiagramTab('diagram-box-3', 'tab-digitized-3', this)">🖼️ High-Res Digitized Image</button>
          </div>
        </div>

        <!-- 1. Animated View -->
        <div class="diagram-content-view tab-anim-3 active">
          {get_population_inversion_svg()}
          <div class="ctrl-bar">
            <button class="ctrl-btn primary" onclick="replayDiagramAnim('svg-pop-inv', 'status-pop')">↺ Replay Animation</button>
            <button class="ctrl-btn" onclick="pauseDiagramAnim('svg-pop-inv', 'status-pop')">⏸ Pause</button>
            <button class="ctrl-btn" onclick="playDiagramAnim('svg-pop-inv', 'status-pop')">▶ Play</button>
            <button class="ctrl-btn" onclick="showFullDiagram('svg-pop-inv', 'status-pop')">👁️ Show Complete Diagram</button>
            <span id="status-pop" class="status-pill">▶ Animation Running</span>
          </div>
        </div>

        <!-- 2. Digitized View -->
        <div class="diagram-content-view tab-digitized-3">
          <img src="./digitized-diagrams/metastable_population_inversion.png" alt="Metastable Population Inversion Digitized" class="diagram-image">
        </div>
      </div>

      <!-- Knowledge Check Quiz -->
      <div class="quiz-card">
        <div class="quiz-question">Quick Quiz: Why is a metastable state mandatory to achieve population inversion?</div>
        <button class="quiz-btn" onclick="checkQuiz(this, true, 'fb-q3', 'Because ordinary excited states last only ~10⁻⁸ s, atoms immediately drop down. The ~10⁻³ s lifetime of the metastable state lets atoms pile up until N₂ > N₁!')">A) It holds excited atoms for ~100,000× longer (~10⁻³ s), allowing atoms to accumulate until N₂ &gt; N₁</button>
        <button class="quiz-btn" onclick="checkQuiz(this, false, 'fb-q3', 'Metastable states prevent quick spontaneous transitions, which is why atoms accumulate!')">B) It causes atoms to drop down faster than any other level</button>
        <button class="quiz-btn" onclick="checkQuiz(this, false, 'fb-q3', 'Metastable states occur in crystals and gases without needing zero kelvin!')">C) It only exists at absolute zero temperature (0 Kelvin)</button>
        <div id="fb-q3" class="quiz-feedback"></div>
      </div>
    </section>
    """

def get_section_4_html():
    return f"""
    <!-- SECTION 4: PRINCIPLE OF LASER -->
    <section id="section-4" class="topic-section">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
        <div class="glossy-heading gloss-green">
          <span>4. Explain the Principle of LASER</span>
        </div>
        <button class="action-pill pill-blue" onclick="speakSection('section-4', this)">🔊 Listen to Section</button>
      </div>

      <div class="glossy-subheading gloss-green">Fundamental Requirement for Laser Action</div>
      <ul class="bullets green-style">
        <li>Laser operation requires that <span class="bold-keyword">the population of the metastable state must exceed that of the lower energy level</span> (Population Inversion).</li>
        <li>Under this condition, stimulated emissions triggered by photons traversing the medium dominate over absorption losses.</li>
        <li>Laser action proceeds systematically through <span class="bold-keyword">Three Sequential Steps</span>:</li>
      </ul>

      <div class="glossy-subheading gloss-green">The Three Sequential Steps in Laser Action</div>
      <ul class="bullets green-style">
        <li><span class="bold-keyword">Step 1: Pumping:</span><br>
          External excitation energy is supplied to the medium, pumping atoms from the ground state (<span class="bold-keyword">E₀</span>) to the higher excited band (<span class="bold-keyword">E₂</span>) via stimulated absorption of radiation at frequency <b>ν₀</b> where <b>hν₀ = E₂ - E₀</b>.</li>
        <li><span class="bold-keyword">Step 2: Population Inversion:</span><br>
          From the short-lived level E₂ (~10⁻⁸ s), atoms undergo rapid spontaneous radiationless transitions to an intermediate metastable state (<span class="bold-keyword">E₁</span>). Because level E₁ has a prolonged lifetime (~10⁻³ s), atoms accumulate while the ground state E₀ is depleted, establishing <span class="bold-keyword" style="color:#D50000;">N₁ &gt; N₀</span>.</li>
        <li><span class="bold-keyword">Step 3: Stimulated Emission &amp; Avalanche Amplification:</span><br>
          An initial spontaneously emitted photon of energy <b>hν = E₁ - E₀</b> traveling along the longitudinal optical axis stimulates an excited atom in E₁ to de-excite, yielding two in-phase coherent photons. These photons trigger further stimulated transitions, initiating a coherent photon cascade.</li>
      </ul>

      <div class="glossy-subheading gloss-green">Role &amp; Action of the Optical Resonator Cavity</div>
      <ul class="bullets green-style">
        <li>The active medium is bounded by two plane-parallel mirrors: a <span class="bold-keyword">Fully Reflecting Mirror (100% R)</span> and a <span class="bold-keyword">Partially Reflecting Mirror (~90% to 99% R)</span>.</li>
        <li><span class="bold-keyword">Directional Selectivity:</span> Photons propagating at oblique angles escape through the lateral boundaries of the cavity. Only photons oriented strictly parallel to the optical axis bounce repeatedly between the mirrors.</li>
        <li><span class="bold-keyword">Multi-Pass Amplification:</span> Axial photons traverse the active medium repeatedly, triggering thousands of stimulated transitions and exponentially increasing the optical intensity.</li>
        <li><span class="bold-keyword">Laser Threshold Condition:</span> Once optical gain per pass balances internal cavity losses and mirror transmission, laser oscillations stabilize.</li>
        <li>An intense, highly collimated, monochromatic, and coherent beam is transmitted through the partially reflecting mirror as the output <span class="bold-keyword">LASER BEAM</span>.</li>
      </ul>

      <!-- DIAGRAM 4: LASER ACTION & PRINCIPLE -->
      <div id="diagram-box-4" class="diagram-box">
        <div class="diagram-nav">
          <div class="diagram-label">Diagram 4: Principle of Laser Action (3-Step Energy Process)</div>
          <div class="diagram-view-tabs">
            <button class="view-btn active" onclick="switchDiagramTab('diagram-box-4', 'tab-anim-4', this)">✨ Animated Interactive Diagram</button>
            <button class="view-btn" onclick="switchDiagramTab('diagram-box-4', 'tab-digitized-4', this)">🖼️ High-Res Digitized Image</button>
          </div>
        </div>

        <!-- 1. Animated View -->
        <div class="diagram-content-view tab-anim-4 active">
          {get_laser_principle_svg()}
          <div class="ctrl-bar">
            <button class="ctrl-btn primary" onclick="replayDiagramAnim('svg-principle', 'status-principle')">↺ Replay Animation</button>
            <button class="ctrl-btn" onclick="pauseDiagramAnim('svg-principle', 'status-principle')">⏸ Pause</button>
            <button class="ctrl-btn" onclick="playDiagramAnim('svg-principle', 'status-principle')">▶ Play</button>
            <button class="ctrl-btn" onclick="showFullDiagram('svg-principle', 'status-principle')">👁️ Show Complete Diagram</button>
            <span id="status-principle" class="status-pill">▶ Animation Running</span>
          </div>
        </div>

        <!-- 2. Digitized View -->
        <div class="diagram-content-view tab-digitized-4">
          <img src="./digitized-diagrams/laser_principle_action.png" alt="Laser Principle Action Digitized" class="diagram-image">
        </div>
      </div>

      <!-- Knowledge Check Quiz -->
      <div class="quiz-card">
        <div class="quiz-question">Quick Quiz: What happens to photons that travel in random diagonal directions inside the optical cavity?</div>
        <button class="quiz-btn" onclick="checkQuiz(this, true, 'fb-q4', 'Only strictly parallel photons bounce back and forth between the end mirrors to get amplified; diagonal photons leak out through the sides and die away!')">A) They escape through the sides of the resonator and are discarded, leaving only parallel photons to amplify</button>
        <button class="quiz-btn" onclick="checkQuiz(this, false, 'fb-q4', 'No, mirrors only reflect photons that hit them directly on-axis!')">B) They get reflected back by the glass walls</button>
        <button class="quiz-btn" onclick="checkQuiz(this, false, 'fb-q4', 'Diagonal photons do not make multiple passes, so they cannot form the main beam!')">C) They form the main laser output beam</button>
        <div id="fb-q4" class="quiz-feedback"></div>
      </div>
    </section>
    """

def get_section_5_html():
    return f"""
    <!-- SECTION 5: APPLICATIONS OF LASERS -->
    <section id="section-5" class="topic-section">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
        <div class="glossy-heading gloss-amber">
          <span>5. Write the Applications of Lasers</span>
        </div>
        <button class="action-pill pill-blue" onclick="speakSection('section-5', this)">🔊 Listen to Section</button>
      </div>

      <div class="glossy-subheading gloss-amber">Eight Major Technical &amp; Scientific Application Domains</div>

      <div class="applications-grid">
        <!-- 1. Communications -->
        <div class="app-box">
          <div class="app-box-header">
            <span class="app-box-icon">🌐</span>
            <span class="app-box-title" style="color:#1565C0;">1. Telecommunications &amp; Space</span>
          </div>
          <div class="app-box-desc">
            • <b>Optical Fiber Transmission:</b> Transmits vast channels of voice and digital data simultaneously over glass fibers with minimal attenuation.<br>
            • <b>Space Telemetry:</b> Negligible angular divergence permits Earth-Moon and interplanetary laser ranging with millimeter accuracy.<br>
            • <b>Underwater Communications:</b> Specific green-blue laser wavelengths penetrate water with minimal absorption.
          </div>
        </div>

        <!-- 2. Computers & Data Storage -->
        <div class="app-box">
          <div class="app-box-header">
            <span class="app-box-icon">💾</span>
            <span class="app-box-title" style="color:#00838F;">2. Computers &amp; Memory</span>
          </div>
          <div class="app-box-desc">
            • <b>High-Density Optical Storage:</b> CDs, DVDs, and Blu-ray disks utilize diffraction-limited laser spots for massive data density.<br>
            • <b>High-Speed Interconnects:</b> Optical interconnects enable ultra-fast transfer of entire memory banks between supercomputers at light speed.
          </div>
        </div>

        <!-- 3. Industry & Manufacturing -->
        <div class="app-box">
          <div class="app-box-header">
            <span class="app-box-icon">⚙️</span>
            <span class="app-box-title" style="color:#E65100;">3. Industrial Processing</span>
          </div>
          <div class="app-box-desc">
            • <b>Cutting, Drilling &amp; Welding:</b> Focused laser beams generate local temperatures exceeding <b>1000 K</b>.<br>
            • <b>Hard Material Piercing:</b> Blasts precise micro-holes through diamonds, sapphires, ceramics, and hardened alloy steels without mechanical tool wear.
          </div>
        </div>

        <!-- 4. Medicine & Surgery -->
        <div class="app-box">
          <div class="app-box-header">
            <span class="app-box-icon">🩺</span>
            <span class="app-box-title" style="color:#C2185B;">4. Medicine &amp; Surgery</span>
          </div>
          <div class="app-box-desc">
            • <b>Ophthalmology:</b> Non-invasive photocoagulation welds detached retinas painlessly through the pupil.<br>
            • <b>Bloodless Laser Scalpel:</b> Vaporizes target tissue while simultaneously cauterizing severed blood vessels.<br>
            • <b>Oncology:</b> Delivers localized thermal destruction to malignant tumors without damaging adjacent healthy cells.
          </div>
        </div>

        <!-- 5. Military & Defense -->
        <div class="app-box">
          <div class="app-box-header">
            <span class="app-box-icon">🎯</span>
            <span class="app-box-title" style="color:#C62828;">5. Defense &amp; Guidance</span>
          </div>
          <div class="app-box-desc">
            • <b>Range Finders &amp; Target Designators:</b> Instantaneous distance calculation and high-precision terminal guidance for munitions.<br>
            • <b>Directed Energy Systems:</b> High-energy laser systems configured for defensive interception of missiles and airborne targets.
          </div>
        </div>

        <!-- 6. Chemical Research -->
        <div class="app-box">
          <div class="app-box-header">
            <span class="app-box-icon">🧪</span>
            <span class="app-box-title" style="color:#7B1FA2;">6. Chemical Spectroscopy</span>
          </div>
          <div class="app-box-desc">
            • <b>Laser Raman Spectroscopy:</b> High monochromatic intensity provides rapid, detailed Raman vibrational spectra from minute chemical samples.<br>
            • <b>Photochemistry:</b> Selectively initiates molecular bond cleavages, catalyzes reactions, and facilitates isotope separation.
          </div>
        </div>

        <!-- 7. Meteorology -->
        <div class="app-box">
          <div class="app-box-header">
            <span class="app-box-icon">⛅</span>
            <span class="app-box-title" style="color:#2E7D32;">7. Atmospheric Meteorology</span>
          </div>
          <div class="app-box-desc">
            • <b>Atmospheric LIDAR:</b> Analyzes backscattered laser signals to map cloud layer elevations, thickness, and wind velocity profiles.<br>
            • <b>Pollution Monitoring:</b> Measures particulate concentrations, smog distributions, and aerosol density across atmospheric altitudes.
          </div>
        </div>

        <!-- 8. Holography & Photography -->
        <div class="app-box">
          <div class="app-box-header">
            <span class="app-box-icon">📸</span>
            <span class="app-box-title" style="color:#F57F17;">8. 3D Holography &amp; Metrology</span>
          </div>
          <div class="app-box-desc">
            • <b>Lensless 3D Photography:</b> Exploits coherent optical interference to record amplitude and phase, producing parallax-enabled 3D holograms.<br>
            • <b>Security Authentication:</b> Micro-holographic anti-counterfeiting features on identification documents and currency.
          </div>
        </div>
      </div>

      <!-- Knowledge Check Quiz -->
      <div class="quiz-card">
        <div class="quiz-question">Quick Quiz: Why is a laser scalpel superior to a metal scalpel during delicate surgery?</div>
        <button class="quiz-btn" onclick="checkQuiz(this, true, 'fb-q5', 'The laser beam vaporizes tissue while instantly sealing blood vessels (photocoagulation), keeping the surgical site bloodless and infection-free!')">A) It simultaneously cuts tissue and cauterizes blood vessels, resulting in bloodless surgery</button>
        <button class="quiz-btn" onclick="checkQuiz(this, false, 'fb-q5', 'Cold surgery is cryosurgery (liquid nitrogen), not laser surgery!')">B) It freezes the tissue to absolute zero</button>
        <button class="quiz-btn" onclick="checkQuiz(this, false, 'fb-q5', 'Laser surgery is micro-targeted and minimizes bleeding and scarring!')">C) It causes heavy bleeding to clean the wound</button>
        <div id="fb-q5" class="quiz-feedback"></div>
      </div>
    </section>
    """

def get_section_6_html():
    return f"""
    <!-- SECTION 6: RUBY LASER (CONSTRUCTION & WORKING) -->
    <section id="section-6" class="topic-section">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
        <div class="glossy-heading gloss-red">
          <span>6. Construction &amp; Working of Ruby Laser</span>
        </div>
        <button class="action-pill pill-blue" onclick="speakSection('section-6', this)">🔊 Listen to Section</button>
      </div>

      <div class="glossy-subheading gloss-red">A. Construction of the Ruby Laser</div>
      <ul class="bullets">
        <li>The Ruby Laser was the <span class="bold-keyword">first operational laser device</span>, developed in 1960 by Theodore H. Maiman.</li>
        <li>It operates as a <span class="bold-keyword">three-level solid-state pulsed laser</span>. Its construction comprises the following main parts:</li>
        <li><span class="bold-keyword">1. Active Medium (Ruby Rod):</span><br>
          A synthetic cylindrical crystal rod of Corundum / Aluminum Oxide (<b>Al₂O₃</b>) in which approximately <b>0.05%</b> of the aluminum atoms are substituted by Chromium atoms (<b>Cr₂O₃</b>).<br>
          • The active centers generating laser radiation are the trivalent <span class="bold-keyword">Chromium ions (Cr³⁺)</span>, giving the crystal a characteristic pink color.<br>
          • Standard rod dimensions are approximately <span class="bold-keyword">4 cm in length</span> and <span class="bold-keyword">0.5 cm in diameter</span>.<br>
          • The end faces are ground strictly flat and polished optically parallel to within fractions of an optical wavelength.</li>
        <li><span class="bold-keyword">2. Optical Resonant Cavity:</span><br>
          The two ends of the rod are silvered directly:<br>
          • One end face is <span class="bold-keyword">100% silvered (fully reflecting mirror)</span>.<br>
          • The opposing end face is <span class="bold-keyword">partially silvered (~90% reflection, ~10% transmission)</span> to allow beam emission.</li>
        <li><span class="bold-keyword">3. Optical Pumping System:</span><br>
          A <span class="bold-keyword">Helical Xenon flash discharge tube</span> surrounds the ruby rod.<br>
          • Connected to a high-voltage capacitor power supply discharging thousands of joules of electrical energy in millisecond pulses.<br>
          • Emits intense green radiation around <span class="bold-keyword">5500 Å</span>, coinciding with the strong absorption band of Cr³⁺ ions.</li>
        <li><span class="bold-keyword">4. Cooling Jacket:</span><br>
          Because only a modest fraction of the flash energy contributes to optical excitation while the remainder produces thermal heating of the crystal, a double-walled glass tube with circulating cooling water or liquid nitrogen surrounds the assembly.</li>
      </ul>

      <!-- Real-World Ruby Laser Device Showcase -->
      <div class="real-device-card">
        <div class="real-device-header">
          <span class="real-badge">📷 Real Physical Apparatus</span>
          <h4 class="real-device-title">The Historic Ruby Laser (Theodore Maiman, 1960)</h4>
        </div>
        <div class="real-device-grid">
          <div class="real-img-item">
            <img src="./real-devices/real_ruby_laser_components_maiman.jpg" alt="Components of Theodore Maiman's Original 1960 Ruby Laser" class="real-device-img">
            <p class="real-caption"><strong>Original 1960 Ruby Laser Components:</strong> The actual disassembled apparatus built by Dr. Theodore Maiman at Hughes Research Laboratories, showing the pink synthetic ruby crystal rod, the surrounding helical Xenon flash lamp, and the machined cylindrical reflective casing.</p>
          </div>
          <div class="real-img-item">
            <img src="./real-devices/real_ruby_crystal_rod.jpg" alt="Real Synthetic Ruby Crystal Rod" class="real-device-img">
            <p class="real-caption"><strong>Synthetic Ruby Rod (Al₂O₃ doped with 0.05% Cr³⁺):</strong> High optical transparency synthetic corundum crystal rod with polished parallel flat ends, responsible for emitting the 694.3 nm deep-red laser pulses.</p>
          </div>
        </div>
      </div>

      <!-- DIAGRAM 6A: RUBY LASER CONSTRUCTION -->
      <div id="diagram-box-6a" class="diagram-box">
        <div class="diagram-nav">
          <div class="diagram-label">Diagram 6A: Construction of Ruby Laser (Labelled Schematic)</div>
          <div class="diagram-view-tabs">
            <button class="view-btn active" onclick="switchDiagramTab('diagram-box-6a', 'tab-anim-6a', this)">✨ Animated Interactive Diagram</button>
            <button class="view-btn" onclick="switchDiagramTab('diagram-box-6a', 'tab-digitized-6a', this)">🖼️ High-Res Digitized Image</button>
          </div>
        </div>

        <div class="diagram-content-view tab-anim-6a active">
          {get_ruby_laser_construction_svg()}
          <div class="ctrl-bar">
            <button class="ctrl-btn primary" onclick="replayDiagramAnim('svg-ruby-const', 'status-ruby-const')">↺ Replay Animation</button>
            <button class="ctrl-btn" onclick="pauseDiagramAnim('svg-ruby-const', 'status-ruby-const')">⏸ Pause</button>
            <button class="ctrl-btn" onclick="playDiagramAnim('svg-ruby-const', 'status-ruby-const')">▶ Play</button>
            <button class="ctrl-btn" onclick="showFullDiagram('svg-ruby-const', 'status-ruby-const')">👁️ Show Complete Diagram</button>
            <span id="status-ruby-const" class="status-pill">▶ Animation Running</span>
          </div>
        </div>

        <div class="diagram-content-view tab-digitized-6a">
          <img src="./digitized-diagrams/ruby_laser_construction.png" alt="Ruby Laser Construction Digitized" class="diagram-image">
        </div>
      </div>

      <div class="glossy-subheading gloss-red">B. Working of Ruby Laser (Energy Level Diagram)</div>
      <ul class="bullets">
        <li>The operation of the ruby laser is described through the <span class="bold-keyword">3-Level Quantum Energy Scheme</span> of the Chromium ion (Cr³⁺):</li>
        <li><span class="bold-keyword">Step 1: Optical Pumping (Transition 1, E₁ ⟶ E₃):</span><br>
          In the ground level (<span class="bold-keyword">E₁</span>), Cr³⁺ ions absorb green photons of wavelength <b>5500 Å</b> produced by the xenon flash, exciting them to the broad absorption band (<span class="bold-keyword">E₃</span>).</li>
        <li><span class="bold-keyword">Step 2: Radiationless Non-Radiative Decay (Transition 2, E₃ ⟶ E₂):</span><br>
          Level E₃ has a very short lifetime (~10⁻⁸ s). The excited Cr³⁺ ions decay rapidly to the intermediate <span class="bold-keyword">Metastable State E₂</span> by transferring non-radiative vibrational energy directly to the crystal lattice as heat.</li>
        <li><span class="bold-keyword">Step 3: Establishment of Population Inversion (E₂):</span><br>
          The metastable level E₂ exhibits a prolonged lifetime of approximately <span class="bold-keyword">10⁻³ seconds</span> (~100,000 times longer than E₃). Pumping transfers ions into E₂ faster than they can decay, depleting ground level E₁ and producing <span class="bold-keyword" style="color:#D50000;">Population Inversion (N₂ &gt; N₁)</span>.</li>
        <li><span class="bold-keyword">Step 4: Spontaneous Initiation (Transition 3, E₂ ⟶ E₁):</span><br>
          A few Cr³⁺ ions drop spontaneously from E₂ to ground level E₁, emitting fluorescent photons at <span class="bold-keyword">6943 Å (694.3 nm, deep red)</span>.</li>
        <li><span class="bold-keyword">Step 5: Stimulated Laser Cascade (Transition 4, E₂ ⟶ E₁):</span><br>
          Photons oriented parallel to the axis reflect back and forth between the mirrored ends, stimulating excited ions in E₂ to emit identical 6943 Å photons in phase. An intense, coherent laser pulse of wavelength <span class="bold-keyword">6943 Å</span> bursts through the partially silvered mirror.</li>
      </ul>

      <!-- DIAGRAM 6B: RUBY LASER ENERGY LEVELS -->
      <div id="diagram-box-6b" class="diagram-box">
        <div class="diagram-nav">
          <div class="diagram-label">Diagram 6B: Energy Level Diagram of Ruby Laser (Working Scheme)</div>
          <div class="diagram-view-tabs">
            <button class="view-btn active" onclick="switchDiagramTab('diagram-box-6b', 'tab-anim-6b', this)">✨ Animated Interactive Diagram</button>
            <button class="view-btn" onclick="switchDiagramTab('diagram-box-6b', 'tab-digitized-6b', this)">🖼️ High-Res Digitized Image</button>
          </div>
        </div>

        <div class="diagram-content-view tab-anim-6b active">
          {get_ruby_laser_energy_level_svg()}
          <div class="ctrl-bar">
            <button class="ctrl-btn primary" onclick="replayDiagramAnim('svg-ruby-energy', 'status-ruby-energy')">↺ Replay Animation</button>
            <button class="ctrl-btn" onclick="pauseDiagramAnim('svg-ruby-energy', 'status-ruby-energy')">⏸ Pause</button>
            <button class="ctrl-btn" onclick="playDiagramAnim('svg-ruby-energy', 'status-ruby-energy')">▶ Play</button>
            <button class="ctrl-btn" onclick="showFullDiagram('svg-ruby-energy', 'status-ruby-energy')">👁️ Show Complete Diagram</button>
            <span id="status-ruby-energy" class="status-pill">▶ Animation Running</span>
          </div>
        </div>

        <div class="diagram-content-view tab-digitized-6b">
          <img src="./digitized-diagrams/ruby_laser_energy_levels.png" alt="Ruby Laser Energy Levels Digitized" class="diagram-image">
        </div>
      </div>

      <div class="glossy-subheading gloss-red">Drawbacks &amp; Limitations of the Ruby Laser</div>
      <ul class="bullets">
        <li><span class="bold-keyword">1. High Pumping Threshold:</span> Because the lower laser level is the ground state (E₁), more than 50% of all chromium ions in the crystal must be excited to achieve population inversion.</li>
        <li><span class="bold-keyword">2. Low Energy Efficiency:</span> Only the green spectral fraction (~5500 Å) of the broad xenon flash is utilized; non-resonant radiation is dissipated as crystal heat.</li>
        <li><span class="bold-keyword">3. Pulsed (Non-Continuous) Output:</span> Emits radiation in short microsecond bursts rather than a continuous beam.</li>
        <li><span class="bold-keyword">4. Thermal Inhomogeneities:</span> Crystal heating causes refractive index variations and requires active cooling.</li>
      </ul>

      <!-- Knowledge Check Quiz -->
      <div class="quiz-card">
        <div class="quiz-question">Quick Quiz: What is the exact wavelength and color of light emitted by the Ruby Laser?</div>
        <button class="quiz-btn" onclick="checkQuiz(this, true, 'fb-q6', 'The Ruby laser produces deep red light at wavelength 6943 Å (694.3 nm) during the E₂ → E₁ stimulated transition!')">A) 6943 Å (694.3 nm), Deep Red Light</button>
        <button class="quiz-btn" onclick="checkQuiz(this, false, 'fb-q6', '5500 Å is the green light absorbed by the crystal during optical pumping, not emitted!')">B) 5500 Å, Green Light</button>
        <button class="quiz-btn" onclick="checkQuiz(this, false, 'fb-q6', '632.8 nm is the wavelength of the Helium-Neon gas laser!')">C) 632.8 nm, Neon Red Light</button>
        <div id="fb-q6" class="quiz-feedback"></div>
      </div>
    </section>
    """

def get_section_7_html():
    return f"""
    <!-- SECTION 7: HELIUM-NEON (He-Ne) LASER -->
    <section id="section-7" class="topic-section">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
        <div class="glossy-heading gloss-blue">
          <span>7. Construction &amp; Working of Helium-Neon (He-Ne) Laser</span>
        </div>
        <button class="action-pill pill-blue" onclick="speakSection('section-7', this)">🔊 Listen to Section</button>
      </div>

      <div class="glossy-subheading gloss-blue">A. Construction of the He-Ne Laser</div>
      <ul class="bullets blue-style">
        <li>The Helium-Neon laser was the <span class="bold-keyword">first continuous-wave (CW) gas laser</span>, developed in 1961 by Ali Javan, William Bennett, and Donald Herriot.</li>
        <li>It operates as a <span class="bold-keyword">four-level gas laser system</span>. Its primary components include:</li>
        <li><span class="bold-keyword">1. Fused Quartz Discharge Tube:</span><br>
          A cylindrical tube of fused quartz, approximately <span class="bold-keyword">80 cm in length</span> and <span class="bold-keyword">1.5 cm in internal diameter</span>, terminating in bulbous end enclosures.</li>
        <li><span class="bold-keyword">2. Active Gas Mixture:</span><br>
          The tube contains a gaseous mixture of <span class="bold-keyword">Helium (He) and Neon (Ne) in an approximate ratio of 10 : 1</span>.<br>
          • Helium is maintained at a partial pressure of about <span class="bold-keyword">1 mm of Hg</span>.<br>
          • Neon is maintained at a partial pressure of about <span class="bold-keyword">0.1 mm of Hg</span> (the active lasing center).</li>
        <li><span class="bold-keyword">3. Optical Resonator Mirrors:</span><br>
          Two optically flat, dielectric-coated mirrors form the optical cavity:<br>
          • One mirror is a <span class="bold-keyword">Perfect Reflector (100% reflective)</span>.<br>
          • The opposite mirror is a <span class="bold-keyword">Partial Reflector (~99% reflective, ~1% transmission)</span> providing continuous beam output.</li>
        <li><span class="bold-keyword">4. Pumping / Excitation System:</span><br>
          A <span class="bold-keyword">High-Frequency Radio Frequency (R.F.) Generator</span> operating in the range of tens of megahertz (MHz) with approximately <span class="bold-keyword">50 W</span> input power, connected to external cylindrical electrodes wrapped around the quartz envelope.</li>
      </ul>

      <!-- Real-World He-Ne Laser Device Showcase -->
      <div class="real-device-card">
        <div class="real-device-header">
          <span class="real-badge">📷 Real Physical Apparatus</span>
          <h4 class="real-device-title">Real Helium-Neon (He-Ne) Gas Laser in Operation</h4>
        </div>
        <div class="real-device-grid">
          <div class="real-img-item">
            <img src="./real-devices/real_hene_laser_discharge_glow.jpg" alt="Operating Helium-Neon Laser at Kastler-Brossel Laboratory" class="real-device-img">
            <p class="real-caption"><strong>Operating He-Ne Discharge Tube:</strong> Demonstration at Kastler-Brossel Laboratory (ENS Paris) showing the electrical discharge exciting the 10:1 He-Ne gas mixture, producing the glowing plasma column and emitting the 632.8 nm continuous red laser beam.</p>
          </div>
          <div class="real-img-item">
            <img src="./real-devices/real_hene_laser_tube_action.jpg" alt="Commercial He-Ne Laser Tube Assembly" class="real-device-img">
            <p class="real-caption"><strong>Commercial Glass Tube Assembly:</strong> Fused quartz capillary tube showing the internal cathode, anode, and precision mirror alignment for continuous wave (CW) operation.</p>
          </div>
        </div>
      </div>

      <!-- DIAGRAM 7A: HE-NE LASER CONSTRUCTION -->
      <div id="diagram-box-7a" class="diagram-box">
        <div class="diagram-nav">
          <div class="diagram-label">Diagram 7A: Construction of Helium-Neon Gas Laser</div>
          <div class="diagram-view-tabs">
            <button class="view-btn active" onclick="switchDiagramTab('diagram-box-7a', 'tab-anim-7a', this)">✨ Animated Interactive Diagram</button>
            <button class="view-btn" onclick="switchDiagramTab('diagram-box-7a', 'tab-digitized-7a', this)">🖼️ High-Res Digitized Image</button>
          </div>
        </div>

        <div class="diagram-content-view tab-anim-7a active">
          {get_hene_laser_construction_svg()}
          <div class="ctrl-bar">
            <button class="ctrl-btn primary" onclick="replayDiagramAnim('svg-hene-const', 'status-hene-const')">↺ Replay Animation</button>
            <button class="ctrl-btn" onclick="pauseDiagramAnim('svg-hene-const', 'status-hene-const')">⏸ Pause</button>
            <button class="ctrl-btn" onclick="playDiagramAnim('svg-hene-const', 'status-hene-const')">▶ Play</button>
            <button class="ctrl-btn" onclick="showFullDiagram('svg-hene-const', 'status-hene-const')">👁️ Show Complete Diagram</button>
            <span id="status-hene-const" class="status-pill">▶ Animation Running</span>
          </div>
        </div>

        <div class="diagram-content-view tab-digitized-7a">
          <img src="./digitized-diagrams/hene_laser_construction.png" alt="He-Ne Laser Construction Digitized" class="diagram-image">
        </div>
      </div>

      <div class="glossy-subheading gloss-blue">B. Working of He-Ne Laser (Energy Level Diagram)</div>
      <ul class="bullets blue-style">
        <li>The operation relies on <span class="bold-keyword">Resonant Inelastic Collisions</span> between excited Helium atoms and ground-state Neon atoms:</li>
        <li><span class="bold-keyword">Step 1: Electron Collision Excitation of Helium:</span><br>
          When the RF electrical discharge is initiated, energetic accelerated electrons collide with ground-state Helium atoms (<span class="bold-keyword">E₁</span>), pumping them into metastable states <span class="bold-keyword">E₂ (19.81 eV)</span> and <span class="bold-keyword">E₃ (20.61 eV)</span>.<br>
          • Radiative transitions from these levels to the ground state are quantum-forbidden, allowing Helium to accumulate energy as an excitation reservoir.</li>
        <li><span class="bold-keyword">Step 2: Resonant Energy Transfer to Neon (Collisions of the Second Kind):</span><br>
          The metastable levels of Helium closely match the excitation energies of Neon:<br>
          • He level <b>E₃ (20.61 eV)</b> matches Ne level <b>E₅' (20.66 eV)</b> with an energy discrepancy of only <span class="bold-keyword">ΔE ≈ 0.05 eV</span>.<br>
          • He level <b>E₂ (19.81 eV)</b> matches Ne level <b>E₄' (19.82 eV)</b> with an energy discrepancy of only <span class="bold-keyword">ΔE ≈ 0.01 eV</span>.<br>
          • During inelastic collisions, excited Helium atoms transfer energy to ground Neon atoms (<span class="bold-keyword">E₁'</span>): <br>
          <span style="display:inline-block; margin:6px 0; padding:4px 16px; background:#F1F5F9; border-radius:6px; font-weight:bold; color:#0F172A;">He* + Ne ⟶ He (Ground E₁) + Ne* (Excited E₅' / E₄') + ΔE (Kinetic)</span><br>
          • Helium atoms return to ground state E₁, while Neon atoms are pumped into metastable states <b>E₅'</b> and <b>E₄'</b>.</li>
        <li><span class="bold-keyword">Step 3: Establishment of Population Inversion in Neon:</span><br>
          Levels E₅' and E₄' in Neon have relatively long lifetimes, whereas the lower intermediate level <span class="bold-keyword">E₃' (18.70 eV)</span> has a very short lifetime. Consequently, <span class="bold-keyword" style="color:#D50000;">Population Inversion is maintained continuously between E₅' and E₃'</span> (and between E₄' and E₃').</li>
        <li><span class="bold-keyword">Step 4: Stimulated Laser Transitions:</span><br>
          Stimulated de-excitation from E₅' to E₃' emits coherent photons:<br>
          • <span class="bold-keyword" style="color:#D50000;">Main Visible Output (E₅' ⟶ E₃'):</span> Produces the classic continuous red laser radiation at <span class="bold-keyword" style="color:#D50000;">λ = 632.8 nm (6328 Å)</span>.<br>
          • Infrared transitions at <b>1.15 μm (E₄' ⟶ E₃')</b> and <b>3.39 μm (E₅' ⟶ E₄')</b> are suppressed by tuning mirror dielectric reflection bands.</li>
        <li><span class="bold-keyword">Step 5: Rapid Spontaneous Decay (E₃' ⟶ E₂'):</span><br>
          From level E₃', Neon atoms undergo rapid spontaneous radiative decay down to level <span class="bold-keyword">E₂' (16.70 eV)</span>, emitting incoherent light (~6000 Å). This fast clearance prevents atomic bottlenecking in the lower laser state.</li>
        <li><span class="bold-keyword">Step 6: De-excitation to Ground State via Wall Collisions (E₂' ⟶ E₁'):</span><br>
          Level E₂' is metastable. Trapped atoms would absorb laser photons and degrade population inversion. To eliminate this, Neon atoms diffuse to the narrow walls of the quartz tube, where wall collisions de-excite them immediately back to ground state <span class="bold-keyword">E₁'</span>. This necessitates a narrow tube diameter (~1.5 cm).</li>
      </ul>

      <!-- DIAGRAM 7B: HE-NE LASER ENERGY LEVELS -->
      <div id="diagram-box-7b" class="diagram-box">
        <div class="diagram-nav">
          <div class="diagram-label">Diagram 7B: Energy Level Diagram of He-Ne Laser (Working Scheme)</div>
          <div class="diagram-view-tabs">
            <button class="view-btn active" onclick="switchDiagramTab('diagram-box-7b', 'tab-anim-7b', this)">✨ Animated Interactive Diagram</button>
            <button class="view-btn" onclick="switchDiagramTab('diagram-box-7b', 'tab-digitized-7b', this)">🖼️ High-Res Digitized Image</button>
          </div>
        </div>

        <div class="diagram-content-view tab-anim-7b active">
          {get_hene_laser_energy_level_svg()}
          <div class="ctrl-bar">
            <button class="ctrl-btn primary" onclick="replayDiagramAnim('svg-hene-energy', 'status-hene-energy')">↺ Replay Animation</button>
            <button class="ctrl-btn" onclick="pauseDiagramAnim('svg-hene-energy', 'status-hene-energy')">⏸ Pause</button>
            <button class="ctrl-btn" onclick="playDiagramAnim('svg-hene-energy', 'status-hene-energy')">▶ Play</button>
            <button class="ctrl-btn" onclick="showFullDiagram('svg-hene-energy', 'status-hene-energy')">👁️ Show Complete Diagram</button>
            <span id="status-hene-energy" class="status-pill">▶ Animation Running</span>
          </div>
        </div>

        <div class="diagram-content-view tab-digitized-7b">
          <img src="./digitized-diagrams/hene_laser_energy_levels.png" alt="He-Ne Laser Energy Levels Digitized" class="diagram-image">
        </div>
      </div>

      <div class="glossy-subheading gloss-blue">Key Advantages of He-Ne Laser over Ruby Laser</div>
      <table class="styled-table">
        <thead>
          <tr style="background:#E3F2FD;">
            <th style="color:#0D47A1;">Feature / Parameter</th>
            <th style="color:#D50000;">Ruby Laser</th>
            <th style="color:#0288D1;">Helium-Neon (He-Ne) Laser</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="bold-keyword">Type of Laser</span></td>
            <td>Solid-state crystal laser (3-level)</td>
            <td>Gas laser (4-level)</td>
          </tr>
          <tr>
            <td><span class="bold-keyword">Nature of Output Beam</span></td>
            <td><b>Pulsed output</b> (short microsecond bursts)</td>
            <td><b>Continuous Wave (CW)</b> steady beam</td>
          </tr>
          <tr>
            <td><span class="bold-keyword">Emission Wavelength</span></td>
            <td>694.3 nm (6943 Å, deep red)</td>
            <td>632.8 nm (6328 Å, bright orange-red)</td>
          </tr>
          <tr>
            <td><span class="bold-keyword">Monochromaticity &amp; Purity</span></td>
            <td>Moderate monochromaticity</td>
            <td><b>Exceptionally high purity</b> and narrow spectral linewidth</td>
          </tr>
          <tr>
            <td><span class="bold-keyword">Pumping Source</span></td>
            <td>Optical pumping (Helical Xenon flash lamp)</td>
            <td>Electrical discharge (R.F. generator electron collisions)</td>
          </tr>
          <tr>
            <td><span class="bold-keyword">Power Input Required</span></td>
            <td>Extremely high energy pulses (thousands of joules)</td>
            <td>Low power continuous input (~50 Watts)</td>
          </tr>
        </tbody>
      </table>

      <!-- Knowledge Check Quiz -->
      <div class="quiz-card">
        <div class="quiz-question">Quick Quiz: How do excited Helium atoms transfer their energy to Neon atoms in the He-Ne laser?</div>
        <button class="quiz-btn" onclick="checkQuiz(this, true, 'fb-q7', 'Helium atoms in metastable states E₂ and E₃ collide inelastically with ground Neon atoms, resonantly transferring their energy because the energy levels match almost perfectly (ΔE ≈ 0.01-0.05 eV)!')">A) Through resonant inelastic atom-atom collisions (Collision of the second kind)</button>
        <button class="quiz-btn" onclick="checkQuiz(this, false, 'fb-q7', 'Helium atoms transfer energy directly through mechanical collision, not by emitting green photons!')">B) By emitting green photons absorbed by Neon</button>
        <button class="quiz-btn" onclick="checkQuiz(this, false, 'fb-q7', 'Chemical bonding does not occur between noble gases like Helium and Neon!')">C) By forming covalent chemical bonds with Neon</button>
        <div id="fb-q7" class="quiz-feedback"></div>
      </div>
    </section>
    """

def build_master_index():
    css = get_shared_css()
    js = get_shared_js()
    ann_css = get_annotation_css()
    ann_html = get_annotation_html()
    ann_js = get_annotation_js()

    s1 = get_section_1_html()
    s2 = get_section_2_html()
    s3 = get_section_3_html()
    s4 = get_section_4_html()
    s5 = get_section_5_html()
    s6 = get_section_6_html()
    s7 = get_section_7_html()

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LASERS: Interactive Physics Masterclass | B.Sc. Physics</title>
<style>
{css}
{ann_css}
</style>
</head>
<body>

  <!-- Top Sticky Navbar -->
  <nav class="top-nav">
    <a href="#top" class="brand">
      <span class="laser-dot"></span>
      <span>LASERS MASTERCLASS</span>
    </a>

    <div class="nav-menu">
      <a href="#section-1" class="nav-btn">1. What is Laser?</a>
      <a href="#section-2" class="nav-btn">2. Spontaneous vs Stimulated</a>
      <a href="#section-3" class="nav-btn">3. Population Inversion</a>
      <a href="#section-4" class="nav-btn">4. Laser Principle</a>
      <a href="#section-5" class="nav-btn">5. Applications</a>
      <a href="#section-6" class="nav-btn">6. Ruby Laser</a>
      <a href="#section-7" class="nav-btn">7. He-Ne Laser</a>
    </div>

    <div class="nav-actions">
      <button class="action-pill pill-red" onclick="toggleAnnotationToolbar()" title="Draw, write, underline, or laser-point on the page (Shortcut: Alt+P)">✏️ Pen &amp; Pointer</button>
      <button id="presModeBtn" class="action-pill pill-blue" onclick="togglePresentationMode()">📽 Presentation Mode</button>
    </div>
  </nav>

  <div class="container" id="top">
    <!-- Hero Banner -->
    <header class="hero">
      <div class="badge-hero">B.Sc. Physics • Unified Physics II • Chapter 12</div>
      <h1>LASERS: Interactive Lecture &amp; Visual Guide</h1>
      <p>
        Digitized, animated, and clearly explained in structured bullet points for BSc Physics students and educators. Explore interactive quantum simulations, digitized diagrams, and master laser physics!
      </p>
      
      <!-- Subpage Links Banner -->
      <div style="margin-top:24px; display:flex; gap:10px; justify-content:center; flex-wrap:wrap;">
        <span style="font-size:0.95rem; font-weight:bold; color:#475569; align-self:center;">Jump to Dedicated Pages:</span>
        <a href="1_what_is_laser.html" class="nav-btn">Topic 1 Page</a>
        <a href="2_spontaneous_vs_stimulated.html" class="nav-btn">Topic 2 Page</a>
        <a href="3_metastable_population_inversion.html" class="nav-btn">Topic 3 Page</a>
        <a href="4_principle_of_laser.html" class="nav-btn">Topic 4 Page</a>
        <a href="5_applications_of_laser.html" class="nav-btn">Topic 5 Page</a>
        <a href="6_ruby_laser.html" class="nav-btn">Topic 6 Page</a>
        <a href="7_hene_laser.html" class="nav-btn">Topic 7 Page</a>
      </div>
    </header>

    <!-- SECTION 1 -->
    {s1}

    <!-- SECTION 2 -->
    {s2}

    <!-- SECTION 3 -->
    {s3}

    <!-- SECTION 4 -->
    {s4}

    <!-- SECTION 5 -->
    {s5}

    <!-- SECTION 6 -->
    {s6}

    <!-- SECTION 7 -->
    {s7}
  </div>

  <footer>
    <p style="font-weight:bold; color:#1E293B; margin-bottom:8px;">
      Interactive LASERS Physics Masterclass • Chapter 12: Lasers, Fibre Optics and Holography
    </p>
    <p>
      Digitized from BSc Physics Lecture Notes &bull; High-Resolution Vector Visualizations &bull; Built with HTML5, CSS3 &amp; Interactive SVG
    </p>
  </footer>

  {ann_html}

  <script>
{js}
{ann_js}
  </script>
</body>
</html>
"""
    out_path = os.path.join(base_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Master index.html created successfully at {out_path} ({len(html)} bytes)")

def build_individual_pages():
    css = get_shared_css()
    js = get_shared_js()
    ann_css = get_annotation_css()
    ann_html = get_annotation_html()
    ann_js = get_annotation_js()

    pages = [
        ("1_what_is_laser.html", "1. What is LASER? Properties of LASERS", get_section_1_html(), "section-1"),
        ("2_spontaneous_vs_stimulated.html", "2. Spontaneous vs Stimulated Emission", get_section_2_html(), "section-2"),
        ("3_metastable_population_inversion.html", "3. Metastable States & Population Inversion", get_section_3_html(), "section-3"),
        ("4_principle_of_laser.html", "4. Principle of LASER", get_section_4_html(), "section-4"),
        ("5_applications_of_laser.html", "5. Applications of Lasers", get_section_5_html(), "section-5"),
        ("6_ruby_laser.html", "6. Construction & Working of Ruby Laser", get_section_6_html(), "section-6"),
        ("7_hene_laser.html", "7. Construction & Working of He-Ne Laser", get_section_7_html(), "section-7"),
    ]

    for filename, title, section_content, sec_id in pages:
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | LASERS Masterclass</title>
<style>
{css}
{ann_css}
</style>
</head>
<body>
  <!-- Top Sticky Navbar -->
  <nav class="top-nav">
    <a href="index.html" class="brand">
      <span class="laser-dot"></span>
      <span>LASERS MASTERCLASS</span>
    </a>

    <div class="nav-menu">
      <a href="index.html" class="nav-btn">🏠 All Topics</a>
      <a href="1_what_is_laser.html" class="nav-btn {'active' if filename == '1_what_is_laser.html' else ''}">1. What is Laser?</a>
      <a href="2_spontaneous_vs_stimulated.html" class="nav-btn {'active' if filename == '2_spontaneous_vs_stimulated.html' else ''}">2. Emission Types</a>
      <a href="3_metastable_population_inversion.html" class="nav-btn {'active' if filename == '3_metastable_population_inversion.html' else ''}">3. Population Inversion</a>
      <a href="4_principle_of_laser.html" class="nav-btn {'active' if filename == '4_principle_of_laser.html' else ''}">4. Laser Principle</a>
      <a href="5_applications_of_laser.html" class="nav-btn {'active' if filename == '5_applications_of_laser.html' else ''}">5. Applications</a>
      <a href="6_ruby_laser.html" class="nav-btn {'active' if filename == '6_ruby_laser.html' else ''}">6. Ruby Laser</a>
      <a href="7_hene_laser.html" class="nav-btn {'active' if filename == '7_hene_laser.html' else ''}">7. He-Ne Laser</a>
    </div>

    <div class="nav-actions">
      <button class="action-pill pill-red" onclick="toggleAnnotationToolbar()" title="Draw, write, underline, or laser-point on the page (Shortcut: Alt+P)">✏️ Pen &amp; Pointer</button>
      <button class="action-pill pill-blue" onclick="togglePresentationMode()">📽 Presentation</button>
    </div>
  </nav>

  <div class="container">
    <div style="margin-bottom:20px;">
      <a href="index.html" style="color:#1565C0; font-weight:bold; text-decoration:none; font-size:1.05rem;">
        &larr; Back to Master Index (All 7 Sections)
      </a>
    </div>

    {section_content}

    <!-- Navigation between topics -->
    <div style="display:flex; justify-content:space-between; margin-top:30px; flex-wrap:wrap; gap:12px;">
      <a href="index.html" class="action-pill pill-blue">&larr; Return to All Chapters</a>
      <a href="index.html#{sec_id}" class="action-pill pill-green">View in Master Overview &rarr;</a>
    </div>
  </div>

  <footer>
    <p style="font-weight:bold; color:#1E293B; margin-bottom:8px;">
      Interactive LASERS Physics Masterclass • B.Sc. Physics Chapter 12
    </p>
    <p>
      <a href="index.html" style="color:#1565C0; text-decoration:none; font-weight:bold;">Return to Home Overview</a>
    </p>
  </footer>

  {ann_html}

  <script>
{js}
{ann_js}
  </script>
</body>
</html>
"""
        filepath = os.path.join(base_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created topic page: {filename}")

if __name__ == "__main__":
    build_master_index()
    build_individual_pages()
    print("All interactive HTML pages generated successfully with clean BSc Physics layout!")
