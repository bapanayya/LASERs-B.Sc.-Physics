import os

base_dir = r"E:\Google-AntiGravity-Projects\1.PPTs-Lecture-Notes\LASERS-BSc.Physics"

# Common Header, Styles, and Navigation Bar
def get_common_head(title="LASERS: Interactive Physics Masterclass"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  :root {{
    --bg-main: #FFFFFF;
    --bg-card: #FFFFFF;
    --text-primary: #1E293B;
    --text-secondary: #475569;
    --primary-red: #D50000;
    --primary-blue: #1565C0;
    --primary-purple: #7B1FA2;
    --primary-green: #2E7D32;
    --primary-amber: #E65100;
    --border-color: #E2E8F0;
    --border-radius-lg: 20px;
    --border-radius-md: 12px;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    background-color: var(--bg-main);
    color: var(--text-primary);
    font-family: 'Segoe UI', system-ui, -apple-system, Roboto, sans-serif;
    font-size: 19px;
    line-height: 1.75;
    padding: 0;
    margin: 0;
  }}

  /* Top Navigation Bar */
  .navbar {{
    position: sticky;
    top: 0;
    z-index: 1000;
    background: rgba(255, 255, 255, 0.96);
    backdrop-filter: blur(12px);
    border-bottom: 2px solid #E2E8F0;
    padding: 12px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
  }}

  .nav-brand {{
    font-size: 1.4rem;
    font-weight: 800;
    color: #D50000;
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
  }}

  .nav-brand .laser-icon {{
    display: inline-block;
    width: 14px;
    height: 14px;
    background: #FF1744;
    border-radius: 50%;
    box-shadow: 0 0 12px #FF1744, 0 0 24px #FF1744;
    animation: pulse-glow 1.5s infinite;
  }}

  @keyframes pulse-glow {{
    0%, 100% {{ transform: scale(1); opacity: 1; }}
    50% {{ transform: scale(1.3); opacity: 0.8; }}
  }}

  .nav-links {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    align-items: center;
  }}

  .nav-pill {{
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 0.95rem;
    font-weight: 600;
    text-decoration: none;
    color: #334155;
    background: #F1F5F9;
    border: 1px solid #CBD5E1;
    transition: all 0.2s ease;
  }}

  .nav-pill:hover, .nav-pill.active {{
    background: #D50000;
    color: #FFFFFF;
    border-color: #D50000;
    box-shadow: 0 4px 12px rgba(213, 0, 0, 0.25);
  }}

  .nav-actions {{
    display: flex;
    gap: 10px;
  }}

  .action-btn {{
    padding: 8px 16px;
    border-radius: 9999px;
    font-size: 0.95rem;
    font-weight: 700;
    border: none;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    transition: all 0.2s;
  }}

  .btn-presentation {{
    background: linear-gradient(135deg, #1E88E5, #1565C0);
    color: white;
    box-shadow: 0 4px 10px rgba(21, 101, 192, 0.25);
  }}

  .btn-presentation:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(21, 101, 192, 0.35);
  }}

  .btn-audio {{
    background: linear-gradient(135deg, #43A047, #2E7D32);
    color: white;
    box-shadow: 0 4px 10px rgba(46, 125, 50, 0.25);
  }}

  /* Main Container */
  .main-container {{
    max-width: 1350px;
    margin: 0 auto;
    padding: 32px 24px 60px;
  }}

  /* Hero Section */
  .hero-banner {{
    background: #FFFFFF;
    border: 2px solid #E2E8F0;
    border-radius: var(--border-radius-lg);
    padding: 40px;
    margin-bottom: 40px;
    text-align: center;
    position: relative;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
  }}

  .hero-badge {{
    display: inline-block;
    padding: 6px 20px;
    border-radius: 9999px;
    font-size: 1rem;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
    background: linear-gradient(180deg, #FF5252, #D50000);
    color: white;
    box-shadow: 0 4px 12px rgba(213,0,0,0.3), inset 0 2px 2px rgba(255,255,255,0.6);
    margin-bottom: 16px;
  }}

  .hero-title {{
    font-size: 2.8rem;
    font-weight: 900;
    color: #0F172A;
    margin-bottom: 14px;
    line-height: 1.25;
  }}

  .hero-subtitle {{
    font-size: 1.35rem;
    color: #475569;
    max-width: 900px;
    margin: 0 auto 20px;
  }}

  /* Glossy Badges & Headers */
  .glossy-header {{
    display: inline-flex;
    align-items: center;
    gap: 12px;
    padding: 10px 24px;
    border-radius: 9999px;
    font-size: 1.45rem;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 24px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.15), inset 0 2px 3px rgba(255, 255, 255, 0.7), inset 0 -2px 4px rgba(0, 0, 0, 0.2);
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.35);
  }}

  .glossy-subheading {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 18px;
    border-radius: 9999px;
    font-size: 1.15rem;
    font-weight: 700;
    color: #FFFFFF;
    margin: 20px 0 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12), inset 0 2px 2px rgba(255, 255, 255, 0.6);
  }}

  .glossy-red {{ background: linear-gradient(180deg, #FF5252 0%, #D50000 60%, #B71C1C 100%); }}
  .glossy-blue {{ background: linear-gradient(180deg, #448AFF 0%, #1565C0 60%, #0D47A1 100%); }}
  .glossy-purple {{ background: linear-gradient(180deg, #E040FB 0%, #AA00FF 60%, #4A148C 100%); }}
  .glossy-green {{ background: linear-gradient(180deg, #69F0AE 0%, #00C853 60%, #1B5E20 100%); }}
  .glossy-amber {{ background: linear-gradient(180deg, #FFD740 0%, #FF8F00 60%, #E65100 100%); }}
  .glossy-teal {{ background: linear-gradient(180deg, #64FFDA 0%, #00BFA5 60%, #004D40 100%); }}

  /* Content Cards */
  .section-card {{
    background: #FFFFFF;
    border: 2px solid #E2E8F0;
    border-radius: var(--border-radius-lg);
    padding: 36px;
    margin-bottom: 50px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
    scroll-margin-top: 90px;
  }}

  /* Bullet points and text */
  .bullet-list {{
    list-style: none;
    padding-left: 0;
    margin: 16px 0 24px;
  }}

  .bullet-list li {{
    position: relative;
    padding-left: 36px;
    margin-bottom: 16px;
    font-size: 1.18rem;
    color: #1E293B;
  }}

  .bullet-list li::before {{
    content: "•";
    position: absolute;
    left: 12px;
    top: -2px;
    font-size: 1.8rem;
    color: #D50000;
  }}

  .bullet-list.blue-bullets li::before {{ color: #1565C0; }}
  .bullet-list.purple-bullets li::before {{ color: #7B1FA2; }}
  .bullet-list.green-bullets li::before {{ color: #2E7D32; }}

  .key-phrase {{
    font-weight: 700;
    color: #0F172A;
  }}

  .highlight-tag {{
    display: inline-block;
    padding: 2px 10px;
    border-radius: 6px;
    font-weight: 700;
    font-size: 0.95em;
  }}
  .tag-red {{ background: #FFEBEE; color: #C62828; border: 1px solid #FFCDD2; }}
  .tag-blue {{ background: #E3F2FD; color: #1565C0; border: 1px solid #BBDEFB; }}
  .tag-green {{ background: #E8F5E9; color: #2E7D32; border: 1px solid #C8E6C9; }}
  .tag-purple {{ background: #F3E5F5; color: #7B1FA2; border: 1px solid #E1BEE7; }}
  .tag-amber {{ background: #FFF3E0; color: #E65100; border: 1px solid #FFE0B2; }}

  /* Layman Box / Analogy */
  .layman-box {{
    background: #F8FAFC;
    border: 2px dashed #94A3B8;
    border-radius: var(--border-radius-md);
    padding: 20px 24px;
    margin: 20px 0 28px;
    display: flex;
    gap: 16px;
    align-items: flex-start;
  }}

  .layman-icon {{
    font-size: 2.2rem;
    line-height: 1;
    flex-shrink: 0;
  }}

  .layman-title {{
    font-size: 1.2rem;
    font-weight: 800;
    color: #0F172A;
    margin-bottom: 6px;
  }}

  .layman-text {{
    font-size: 1.12rem;
    color: #334155;
    line-height: 1.7;
  }}

  /* Diagram Area & Switcher */
  .diagram-wrapper {{
    background: #FFFFFF;
    border: 2px solid #CBD5E1;
    border-radius: var(--border-radius-md);
    padding: 20px;
    margin: 28px 0;
    box-shadow: 0 6px 20px rgba(0,0,0,0.03);
  }}

  .diagram-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    border-bottom: 2px solid #E2E8F0;
    padding-bottom: 14px;
    margin-bottom: 18px;
  }}

  .diagram-title {{
    font-size: 1.25rem;
    font-weight: 800;
    color: #0F172A;
  }}

  .diagram-tabs {{
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
  }}

  .d-tab {{
    padding: 6px 14px;
    border-radius: 8px;
    border: 1.5px solid #CBD5E1;
    background: #F8FAFC;
    color: #475569;
    font-size: 0.95rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
  }}

  .d-tab.active {{
    background: #1565C0;
    color: white;
    border-color: #1565C0;
  }}

  .diagram-view {{
    display: none;
    text-align: center;
    width: 100%;
    min-height: 380px;
    position: relative;
  }}

  .diagram-view.active {{
    display: block;
  }}

  .diagram-img {{
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    display: block;
    margin: 0 auto;
  }}

  /* Diagram Controls (Play, Pause, Step, Replay) */
  .anim-controls {{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    margin-top: 18px;
    padding: 10px;
    background: #F1F5F9;
    border-radius: 9999px;
    width: fit-content;
    margin-left: auto;
    margin-right: auto;
  }}

  .anim-btn {{
    padding: 8px 18px;
    border-radius: 9999px;
    border: none;
    font-weight: 700;
    font-size: 0.95rem;
    cursor: pointer;
    background: white;
    color: #1E293B;
    border: 1.5px solid #CBD5E1;
    transition: all 0.2s;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }}

  .anim-btn:hover {{
    background: #E2E8F0;
  }}

  .anim-btn.primary {{
    background: #D50000;
    color: white;
    border-color: #D50000;
  }}

  .anim-btn.primary:hover {{
    background: #B71C1C;
  }}

  .anim-status-badge {{
    font-size: 0.95rem;
    font-weight: 700;
    padding: 6px 14px;
    border-radius: 9999px;
    background: #E0F2FE;
    color: #0369A1;
    border: 1px solid #BAE6FD;
  }}

  /* Comparison Table */
  .comparison-table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 24px 0;
    border: 2px solid #E2E8F0;
    border-radius: var(--border-radius-md);
    overflow: hidden;
  }}

  .comparison-table th {{
    background: #F8FAFC;
    padding: 16px 20px;
    font-size: 1.15rem;
    font-weight: 800;
    text-align: left;
    border-bottom: 2px solid #CBD5E1;
  }}

  .comparison-table td {{
    padding: 16px 20px;
    font-size: 1.12rem;
    border-bottom: 1px solid #E2E8F0;
    vertical-align: top;
  }}

  .comparison-table tr:last-child td {{
    border-bottom: none;
  }}

  .comparison-table tr:nth-child(even) {{
    background: #F8FAFC;
  }}

  /* Interactive Application Grid */
  .app-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 20px;
    margin: 28px 0;
  }}

  .app-card {{
    background: #FFFFFF;
    border: 2px solid #E2E8F0;
    border-radius: var(--border-radius-md);
    padding: 22px;
    transition: all 0.25s ease;
    cursor: pointer;
  }}

  .app-card:hover {{
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.08);
    border-color: #94A3B8;
  }}

  .app-card-header {{
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
  }}

  .app-icon {{
    font-size: 2rem;
  }}

  .app-card-title {{
    font-size: 1.15rem;
    font-weight: 800;
    color: #0F172A;
  }}

  .app-card-body {{
    font-size: 1.05rem;
    color: #334155;
    line-height: 1.6;
  }}

  /* Interactive Quiz Section */
  .quiz-box {{
    background: #F8FAFC;
    border: 2px solid #CBD5E1;
    border-radius: var(--border-radius-md);
    padding: 24px;
    margin: 32px 0 16px;
  }}

  .quiz-title {{
    font-size: 1.25rem;
    font-weight: 800;
    color: #0F172A;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 10px;
  }}

  .quiz-option {{
    display: block;
    background: white;
    border: 2px solid #E2E8F0;
    border-radius: 8px;
    padding: 12px 18px;
    margin-bottom: 10px;
    font-size: 1.1rem;
    cursor: pointer;
    transition: all 0.2s;
  }}

  .quiz-option:hover {{
    border-color: #1565C0;
    background: #F0F9FF;
  }}

  .quiz-option.correct {{
    background: #DCFCE7;
    border-color: #16A34A;
    color: #15803D;
    font-weight: bold;
  }}

  .quiz-option.wrong {{
    background: #FEE2E2;
    border-color: #DC2626;
    color: #B91C1C;
  }}

  .quiz-feedback {{
    margin-top: 12px;
    font-size: 1.1rem;
    font-weight: 700;
    display: none;
  }}

  /* Footer */
  footer {{
    text-align: center;
    padding: 40px 20px;
    background: #F8FAFC;
    border-top: 2px solid #E2E8F0;
    color: #64748B;
    font-size: 1.05rem;
  }}

  /* SVG Canvas Styling */
  .svg-canvas {{
    width: 100%;
    max-width: 1000px;
    height: auto;
    margin: 0 auto;
    display: block;
    background: #FFFFFF;
    border-radius: 12px;
  }}

  /* Presentation Mode Overlay */
  body.presentation-mode {{
    background: #FFFFFF;
  }}
  body.presentation-mode .navbar {{
    position: fixed;
    width: 100%;
  }}
  body.presentation-mode .section-card {{
    min-height: 90vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }}

  @media (max-width: 768px) {{
    body {{ font-size: 17px; }}
    .hero-title {{ font-size: 2rem; }}
    .glossy-header {{ font-size: 1.2rem; padding: 8px 16px; }}
    .section-card {{ padding: 20px; }}
  }}
</style>
</head>
"""

print("Common template defined.")
