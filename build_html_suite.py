import os
import sys

# Ensure local directory is on python path
sys.path.insert(0, r"E:\Google-AntiGravity-Projects\1.PPTs-Lecture-Notes\LASERS-BSc.Physics")
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

def get_shared_css():
    return """
    :root {
      --bg-body: #FFFFFF;
      --text-main: #1E293B;
      --text-muted: #475569;
      --ruby-red: #D50000;
      --ruby-light: #FFEBEE;
      --ruby-border: #FFCDD2;
      --cobalt-blue: #1565C0;
      --blue-light: #E3F2FD;
      --emerald-green: #2E7D32;
      --green-light: #E8F5E9;
      --purple-violet: #7B1FA2;
      --purple-light: #F3E5F5;
      --amber-gold: #E65100;
      --amber-light: #FFF3E0;
      --border-card: #E2E8F0;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg-body);
      color: var(--text-main);
      font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
      font-size: 19px;
      line-height: 1.8;
      padding: 0;
      margin: 0;
    }

    /* Top Sticky Navbar */
    .top-nav {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(10px);
      border-bottom: 2px solid #E2E8F0;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--ruby-red);
      text-decoration: none;
    }
    .laser-dot {
      width: 14px;
      height: 14px;
      background: #FF1744;
      border-radius: 50%;
      box-shadow: 0 0 10px #FF1744, 0 0 20px #FF1744;
      animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.3); opacity: 0.7; }
    }
    .nav-menu {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
    }
    .nav-btn {
      padding: 7px 14px;
      border-radius: 9999px;
      font-size: 0.95rem;
      font-weight: 700;
      text-decoration: none;
      color: #334155;
      background: #F8FAFC;
      border: 1.5px solid #CBD5E1;
      transition: all 0.2s;
    }
    .nav-btn:hover, .nav-btn.active {
      background: var(--ruby-red);
      color: #FFFFFF;
      border-color: var(--ruby-red);
      box-shadow: 0 4px 12px rgba(213, 0, 0, 0.25);
    }
    .nav-actions {
      display: flex;
      gap: 10px;
    }
    .action-pill {
      padding: 8px 18px;
      border-radius: 9999px;
      font-size: 0.95rem;
      font-weight: 700;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }
    .pill-blue {
      background: linear-gradient(135deg, #1E88E5, #1565C0);
      color: white;
      box-shadow: 0 4px 10px rgba(21, 101, 192, 0.25);
    }
    .pill-green {
      background: linear-gradient(135deg, #43A047, #2E7D32);
      color: white;
      box-shadow: 0 4px 10px rgba(46, 125, 50, 0.25);
    }

    /* Container */
    .container {
      max-width: 1320px;
      margin: 0 auto;
      padding: 30px 24px 80px;
    }

    /* Hero */
    .hero {
      background: #FFFFFF;
      border: 2px solid #E2E8F0;
      border-radius: 24px;
      padding: 40px;
      margin-bottom: 40px;
      text-align: center;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
    }
    .badge-hero {
      display: inline-block;
      padding: 6px 20px;
      border-radius: 9999px;
      font-size: 0.95rem;
      font-weight: 800;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      background: linear-gradient(180deg, #FF5252, #D50000);
      color: white;
      box-shadow: 0 4px 12px rgba(213,0,0,0.3), inset 0 2px 2px rgba(255,255,255,0.6);
      margin-bottom: 16px;
    }
    .hero h1 {
      font-size: 2.7rem;
      font-weight: 900;
      color: #0F172A;
      margin-bottom: 12px;
      line-height: 1.25;
    }
    .hero p {
      font-size: 1.3rem;
      color: #475569;
      max-width: 900px;
      margin: 0 auto;
    }

    /* Section Cards */
    .topic-section {
      background: #FFFFFF;
      border: 2px solid var(--border-card);
      border-radius: 20px;
      padding: 36px;
      margin-bottom: 48px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04);
      scroll-margin-top: 85px;
    }

    /* Glossy Headings */
    .glossy-heading {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      padding: 10px 26px;
      border-radius: 9999px;
      font-size: 1.45rem;
      font-weight: 800;
      color: #FFFFFF;
      margin-bottom: 24px;
      box-shadow: 0 6px 18px rgba(0,0,0,0.15), inset 0 2px 3px rgba(255,255,255,0.7), inset 0 -2px 4px rgba(0,0,0,0.2);
      text-shadow: 0 1px 2px rgba(0,0,0,0.3);
    }
    .glossy-subheading {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 20px;
      border-radius: 9999px;
      font-size: 1.15rem;
      font-weight: 700;
      color: #FFFFFF;
      margin: 24px 0 14px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.12), inset 0 2px 2px rgba(255,255,255,0.6);
    }
    .gloss-red { background: linear-gradient(180deg, #FF5252, #D50000 65%, #B71C1C); }
    .gloss-blue { background: linear-gradient(180deg, #448AFF, #1565C0 65%, #0D47A1); }
    .gloss-purple { background: linear-gradient(180deg, #E040FB, #AA00FF 65%, #4A148C); }
    .gloss-green { background: linear-gradient(180deg, #69F0AE, #00C853 65%, #1B5E20); }
    .gloss-amber { background: linear-gradient(180deg, #FFD740, #FF8F00 65%, #E65100); }

    /* Bullet List & Text */
    .bullets {
      list-style: none;
      padding-left: 0;
      margin: 16px 0 24px;
    }
    .bullets li {
      position: relative;
      padding-left: 36px;
      margin-bottom: 16px;
      font-size: 1.18rem;
      color: #1E293B;
    }
    .bullets li::before {
      content: "•";
      position: absolute;
      left: 12px;
      top: -2px;
      font-size: 1.8rem;
      color: var(--ruby-red);
    }
    .bullets.blue-style li::before { color: var(--cobalt-blue); }
    .bullets.purple-style li::before { color: var(--purple-violet); }
    .bullets.green-style li::before { color: var(--emerald-green); }

    .bold-keyword {
      font-weight: 700;
      color: #0F172A;
    }

    /* Real Device Showcase Cards */
    .real-device-card {
      background: #FFFFFF;
      border: 2px solid #E2E8F0;
      border-radius: 16px;
      padding: 24px;
      margin: 28px 0;
      box-shadow: 0 4px 16px rgba(15, 23, 42, 0.05);
    }
    .real-device-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 18px;
      border-bottom: 2px solid #F1F5F9;
      padding-bottom: 12px;
      flex-wrap: wrap;
    }
    .real-badge {
      display: inline-flex;
      align-items: center;
      background: linear-gradient(135deg, #059669, #10B981);
      color: #FFFFFF;
      font-size: 0.88rem;
      font-weight: 800;
      padding: 6px 14px;
      border-radius: 9999px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      box-shadow: 0 2px 6px rgba(16, 185, 129, 0.35);
    }
    .real-device-title {
      font-size: 1.35rem;
      font-weight: 800;
      color: #0F172A;
      margin: 0;
    }
    .real-device-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 22px;
    }
    .real-img-item {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 12px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .real-img-item:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
      border-color: #CBD5E1;
    }
    .real-device-img {
      width: 100%;
      height: 250px;
      object-fit: cover;
      border-radius: 8px;
      border: 1px solid #CBD5E1;
      background: #000000;
    }
    .real-caption {
      margin-top: 12px;
      font-size: 1.05rem;
      line-height: 1.6;
      color: #334155;
    }
    .real-caption strong {
      color: #0F172A;
    }


    /* Diagram Section Box */
    .diagram-box {
      background: #FFFFFF;
      border: 2px solid #CBD5E1;
      border-radius: 16px;
      padding: 22px;
      margin: 28px 0;
      box-shadow: 0 6px 20px rgba(0,0,0,0.03);
    }
    .diagram-nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      border-bottom: 2px solid #E2E8F0;
      padding-bottom: 14px;
      margin-bottom: 20px;
    }
    .diagram-label {
      font-size: 1.25rem;
      font-weight: 800;
      color: #0F172A;
    }
    .diagram-view-tabs {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .view-btn {
      padding: 6px 14px;
      border-radius: 8px;
      border: 1.5px solid #CBD5E1;
      background: #F8FAFC;
      color: #475569;
      font-size: 0.95rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }
    .view-btn.active {
      background: #1565C0;
      color: white;
      border-color: #1565C0;
    }
    .diagram-content-view {
      display: none;
      text-align: center;
      width: 100%;
      min-height: 380px;
    }
    .diagram-content-view.active {
      display: block;
    }
    .diagram-image {
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.06);
      display: block;
      margin: 0 auto;
    }

    /* Diagram Animation Controls */
    .ctrl-bar {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 10px;
      margin-top: 20px;
      padding: 10px 18px;
      background: #F1F5F9;
      border-radius: 9999px;
      width: fit-content;
      margin-left: auto;
      margin-right: auto;
      flex-wrap: wrap;
    }
    .ctrl-btn {
      padding: 8px 16px;
      border-radius: 9999px;
      border: 1.5px solid #CBD5E1;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      background: white;
      color: #1E293B;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .ctrl-btn:hover { background: #E2E8F0; }
    .ctrl-btn.primary {
      background: var(--ruby-red);
      color: white;
      border-color: var(--ruby-red);
    }
    .ctrl-btn.primary:hover { background: #B71C1C; }
    .status-pill {
      font-size: 0.95rem;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 9999px;
      background: #E0F2FE;
      color: #0369A1;
      border: 1px solid #BAE6FD;
    }

    /* Tables */
    .styled-table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      margin: 24px 0;
      border: 2px solid #E2E8F0;
      border-radius: 12px;
      overflow: hidden;
    }
    .styled-table th {
      background: #F8FAFC;
      padding: 16px 20px;
      font-size: 1.15rem;
      font-weight: 800;
      text-align: left;
      border-bottom: 2px solid #CBD5E1;
    }
    .styled-table td {
      padding: 16px 20px;
      font-size: 1.12rem;
      border-bottom: 1px solid #E2E8F0;
      vertical-align: top;
    }
    .styled-table tr:nth-child(even) { background: #F8FAFC; }
    .styled-table tr:last-child td { border-bottom: none; }

    /* Application Cards */
    .applications-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
      gap: 20px;
      margin: 28px 0;
    }
    .app-box {
      background: #FFFFFF;
      border: 2px solid #E2E8F0;
      border-radius: 14px;
      padding: 22px;
      transition: all 0.25s ease;
      cursor: pointer;
    }
    .app-box:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 24px rgba(0,0,0,0.08);
      border-color: #94A3B8;
    }
    .app-box-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 12px;
    }
    .app-box-icon { font-size: 2.2rem; }
    .app-box-title { font-size: 1.15rem; font-weight: 800; color: #0F172A; }
    .app-box-desc { font-size: 1.05rem; color: #334155; line-height: 1.6; }

    /* Interactive Quiz */
    .quiz-card {
      background: #F8FAFC;
      border: 2px solid #CBD5E1;
      border-radius: 14px;
      padding: 24px;
      margin: 32px 0 16px;
    }
    .quiz-question {
      font-size: 1.25rem;
      font-weight: 800;
      color: #0F172A;
      margin-bottom: 16px;
    }
    .quiz-btn {
      display: block;
      width: 100%;
      text-align: left;
      background: white;
      border: 2px solid #E2E8F0;
      border-radius: 8px;
      padding: 12px 18px;
      margin-bottom: 10px;
      font-size: 1.1rem;
      cursor: pointer;
      transition: all 0.2s;
    }
    .quiz-btn:hover {
      border-color: #1565C0;
      background: #F0F9FF;
    }
    .quiz-btn.correct {
      background: #DCFCE7;
      border-color: #16A34A;
      color: #15803D;
      font-weight: bold;
    }
    .quiz-btn.wrong {
      background: #FEE2E2;
      border-color: #DC2626;
      color: #B91C1C;
    }
    .quiz-feedback {
      margin-top: 12px;
      font-size: 1.1rem;
      font-weight: 700;
      display: none;
    }

    footer {
      text-align: center;
      padding: 40px 20px;
      background: #F8FAFC;
      border-top: 2px solid #E2E8F0;
      color: #64748B;
      font-size: 1.05rem;
    }

    .interactive-svg {
      width: 100%;
      max-width: 960px;
      height: auto;
      margin: 0 auto;
      display: block;
      background: #FFFFFF;
      border-radius: 12px;
    }

    /* Pause state for SVG animations */
    .interactive-svg.paused,
    .interactive-svg.paused * {
      animation-play-state: paused !important;
    }

    /* Show complete diagram state: stops animations and forces 100% opacity and full visibility */
    .interactive-svg.show-full,
    .interactive-svg.show-full * {
      animation: none !important;
      opacity: 1 !important;
      visibility: visible !important;
      transform: none !important;
      stroke-dashoffset: 0 !important;
    }
    """

def get_shared_js():
    return """
    // Tab Switcher Function
    function switchDiagramTab(containerId, tabType, btn) {
      const container = document.getElementById(containerId);
      if (!container) return;
      
      // Update Tab Buttons
      const buttons = container.querySelectorAll('.view-btn');
      buttons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      // Update Views
      const views = container.querySelectorAll('.diagram-content-view');
      views.forEach(v => v.classList.remove('active'));
      const activeView = container.querySelector('.' + tabType);
      if (activeView) activeView.classList.add('active');
    }

    // Diagram Animation Controls
    function playDiagramAnim(svgId, statusId) {
      const svg = document.getElementById(svgId);
      const status = document.getElementById(statusId);
      if (svg) {
        svg.classList.remove('paused');
        svg.classList.remove('show-full');
      }
      if (status) {
        status.innerText = "▶ Animation Running";
        status.style.color = "#0369A1";
        status.style.background = "#E0F2FE";
      }
    }

    function pauseDiagramAnim(svgId, statusId) {
      const svg = document.getElementById(svgId);
      const status = document.getElementById(statusId);
      if (svg) svg.classList.add('paused');
      if (status) {
        status.innerText = "⏸ Paused";
        status.style.color = "#854D0E";
        status.style.background = "#FEF9C3";
      }
    }

    function replayDiagramAnim(svgId, statusId) {
      const svg = document.getElementById(svgId);
      const status = document.getElementById(statusId);
      if (svg) {
        svg.classList.remove('paused');
        svg.classList.remove('show-full');
        // Force full restart of all child animations by replacing the node
        const parent = svg.parentNode;
        const next = svg.nextSibling;
        parent.removeChild(svg);
        void svg.offsetWidth;
        parent.insertBefore(svg, next);
      }
      if (status) {
        status.innerText = "↺ Replaying Animation";
        status.style.color = "#0369A1";
        status.style.background = "#E0F2FE";
      }
    }

    function showFullDiagram(svgId, statusId) {
      const svg = document.getElementById(svgId);
      const status = document.getElementById(statusId);
      if (svg) {
        svg.classList.remove('paused');
        svg.classList.add('show-full');
      }
      if (status) {
        status.innerText = "✓ Full Labelled Diagram Visible";
        status.style.color = "#15803D";
        status.style.background = "#DCFCE7";
      }
    }

    // Text-To-Speech Narration
    let isSpeaking = false;
    function speakSection(sectionId, btn) {
      if (!('speechSynthesis' in window)) {
        alert("Text-to-Speech is not supported in this browser.");
        return;
      }
      
      if (isSpeaking) {
        window.speechSynthesis.cancel();
        isSpeaking = false;
        btn.innerHTML = "🔊 Listen to Section";
        return;
      }

      const section = document.getElementById(sectionId);
      if (!section) return;

      const bullets = section.querySelectorAll('.bullets li, .hero-subtitle');
      let textToRead = "";
      bullets.forEach(b => textToRead += b.innerText + ". ");

      if (!textToRead) textToRead = section.innerText;

      const utterance = new SpeechSynthesisUtterance(textToRead);
      utterance.rate = 0.95;
      utterance.pitch = 1.0;
      
      utterance.onend = function() {
        isSpeaking = false;
        btn.innerHTML = "🔊 Listen to Section";
      };

      utterance.onerror = function() {
        isSpeaking = false;
        btn.innerHTML = "🔊 Listen to Section";
      };

      window.speechSynthesis.speak(utterance);
      isSpeaking = true;
      btn.innerHTML = "⏹ Stop Listening";
    }

    // Interactive Quiz Checker
    function checkQuiz(btn, isCorrect, feedbackId, explanation) {
      const parent = btn.parentElement;
      const allBtns = parent.querySelectorAll('.quiz-btn');
      allBtns.forEach(b => {
        b.disabled = true;
        b.style.cursor = 'default';
      });

      const feedback = document.getElementById(feedbackId);
      if (isCorrect) {
        btn.classList.add('correct');
        if (feedback) {
          feedback.style.display = 'block';
          feedback.style.color = '#15803D';
          feedback.innerHTML = "✓ Correct! " + explanation;
        }
      } else {
        btn.classList.add('wrong');
        if (feedback) {
          feedback.style.display = 'block';
          feedback.style.color = '#B91C1C';
          feedback.innerHTML = "✗ Incorrect. " + explanation;
        }
      }
    }

    // Presentation Mode Toggle
    function togglePresentationMode() {
      document.body.classList.toggle('presentation-mode');
      const isPres = document.body.classList.contains('presentation-mode');
      const btn = document.getElementById('presModeBtn');
      if (btn) {
        btn.innerText = isPres ? "Exit Presentation Mode" : "📽 Presentation Mode";
      }
    }
    """

print("Defined get_shared_css and get_shared_js")
