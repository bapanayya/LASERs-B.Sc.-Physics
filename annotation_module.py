# High-Performance Annotation System for LASERS Interactive Masterclass
# Viewport-Fixed Canvas Engine with 60-120 FPS Response on Desktop & Mobile

def get_annotation_css():
    return """
    /* --- TEACHER ANNOTATION & LASER POINTER SYSTEM --- */
    #annotationContainer {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 9990;
      pointer-events: none;
      touch-action: none;
      overflow: hidden;
    }
    #annotationContainer.active-drawing {
      pointer-events: auto;
    }
    #annotationContainer.active-laser {
      pointer-events: auto;
      touch-action: none;
      cursor: none;
    }
    #annotationBaseCanvas,
    #annotationActiveCanvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      display: block;
    }
    #annotationContainer.cursor-pen {
      cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="%23D50000" d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>') 2 22, crosshair;
    }
    #annotationContainer.cursor-highlighter {
      cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="%23FFD600" d="M15.24 3.76a2.5 2.5 0 0 1 3.54 0l1.46 1.46a2.5 2.5 0 0 1 0 3.54L10.5 18.5 5 20l1.5-5.5L15.24 3.76z"/></svg>') 4 20, crosshair;
    }
    #annotationContainer.cursor-eraser {
      cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="%2337474F" stroke-width="2"/><circle cx="12" cy="12" r="3" fill="%2337474F"/></svg>') 12 12, cell;
    }

    /* Laser Pointer Dot - GPU Hardware Accelerated */
    #laserPointerDot {
      position: fixed;
      top: 0;
      left: 0;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #FFFFFF;
      pointer-events: none;
      z-index: 9992;
      transform: translate3d(-100px, -100px, 0) translate(-50%, -50%);
      box-shadow: 0 0 6px #FF1744, 0 0 14px #FF1744, 0 0 26px #FF1744, 0 0 40px #D50000;
      display: none;
      will-change: transform;
    }
    #laserPointerDot.active {
      display: block;
    }
    #laserPointerDot.green-laser {
      box-shadow: 0 0 6px #00E676, 0 0 14px #00E676, 0 0 26px #00E676, 0 0 40px #00C853;
    }

    /* Laser Ripple Click Animation */
    .laser-ripple {
      position: fixed;
      top: 0;
      left: 0;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      border: 3px solid #FF1744;
      pointer-events: none;
      z-index: 9991;
      animation: rippleExpand 0.6s cubic-bezier(0.1, 0.8, 0.3, 1) forwards;
      will-change: transform, opacity;
    }
    @keyframes rippleExpand {
      0% { transform: translate3d(var(--rx, 0), var(--ry, 0), 0) translate(-50%, -50%) scale(0.4); opacity: 1; }
      100% { transform: translate3d(var(--rx, 0), var(--ry, 0), 0) translate(-50%, -50%) scale(3.5); opacity: 0; }
    }

    /* Floating Teacher Toolbar */
    #teacherToolbar {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 10000;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(14px);
      border: 2px solid #CBD5E1;
      border-radius: 50px;
      padding: 8px 18px;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.16), 0 4px 12px rgba(0, 0, 0, 0.08);
      user-select: none;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s;
    }
    #teacherToolbar.minimized {
      transform: translateX(-50%) translateY(80px);
      opacity: 0;
      pointer-events: none;
    }

    /* Drag Handle */
    .tb-drag-handle {
      cursor: grab;
      color: #94A3B8;
      font-size: 1.1rem;
      padding: 0 4px;
      display: flex;
      align-items: center;
    }
    .tb-drag-handle:active {
      cursor: grabbing;
    }

    /* Tool Buttons Group */
    .tb-btn-group {
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .tb-btn {
      width: 42px;
      height: 42px;
      border-radius: 50%;
      border: 1.5px solid transparent;
      background: #F1F5F9;
      color: #334155;
      font-size: 1.15rem;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.15s ease;
      position: relative;
    }
    .tb-btn:hover {
      background: #E2E8F0;
      transform: scale(1.06);
    }
    .tb-btn.active {
      background: #1E293B;
      color: #FFFFFF;
      border-color: #0F172A;
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.25);
      transform: scale(1.08);
    }
    .tb-btn.active.tb-laser {
      background: #D50000;
      color: #FFFFFF;
      box-shadow: 0 0 14px rgba(213, 0, 0, 0.5);
    }
    .tb-btn.active.tb-pen {
      background: #2563EB;
      color: #FFFFFF;
    }
    .tb-btn.active.tb-highlighter {
      background: #CA8A04;
      color: #FFFFFF;
    }
    .tb-btn.active.tb-eraser {
      background: #475569;
      color: #FFFFFF;
    }

    /* Dividers */
    .tb-divider {
      width: 1.5px;
      height: 28px;
      background: #E2E8F0;
      margin: 0 4px;
    }

    /* Color Swatches */
    .tb-color-swatch {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      border: 2px solid #FFFFFF;
      box-shadow: 0 0 0 1.5px #CBD5E1;
      cursor: pointer;
      transition: all 0.15s;
    }
    .tb-color-swatch:hover {
      transform: scale(1.15);
    }
    .tb-color-swatch.active {
      transform: scale(1.22);
      box-shadow: 0 0 0 2.5px #0F172A;
    }

    /* Width Selector */
    .tb-size-btn {
      padding: 4px 10px;
      border-radius: 12px;
      background: #F1F5F9;
      border: 1.5px solid transparent;
      font-size: 0.85rem;
      font-weight: 700;
      color: #475569;
      cursor: pointer;
      transition: all 0.15s;
    }
    .tb-size-btn:hover { background: #E2E8F0; }
    .tb-size-btn.active {
      background: #0F172A;
      color: #FFFFFF;
    }

    /* Floating Pill Launcher when Toolbar is minimized */
    #teacherPillLauncher {
      position: fixed;
      bottom: 24px;
      right: 28px;
      z-index: 9998;
      background: linear-gradient(135deg, #D50000, #B71C1C);
      color: white;
      font-size: 1rem;
      font-weight: 800;
      border-radius: 9999px;
      padding: 10px 22px;
      border: 2px solid rgba(255,255,255,0.7);
      box-shadow: 0 8px 24px rgba(213, 0, 0, 0.35);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }
    #teacherPillLauncher:hover {
      transform: translateY(-3px) scale(1.03);
      box-shadow: 0 12px 30px rgba(213, 0, 0, 0.45);
    }
    #teacherPillLauncher.hidden {
      display: none;
    }

    /* Tooltip Helper */
    .tb-tooltip {
      position: absolute;
      bottom: 120%;
      left: 50%;
      transform: translateX(-50%);
      background: #0F172A;
      color: white;
      font-size: 0.78rem;
      font-weight: 600;
      padding: 4px 8px;
      border-radius: 6px;
      white-space: nowrap;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s;
    }
    .tb-btn:hover .tb-tooltip, .tb-color-swatch:hover .tb-tooltip {
      opacity: 1;
    }

    /* Toast Notification */
    #annotationToast {
      position: fixed;
      top: 80px;
      left: 50%;
      transform: translateX(-50%);
      background: #0F172A;
      color: white;
      padding: 10px 24px;
      border-radius: 30px;
      font-size: 1rem;
      font-weight: 700;
      z-index: 10010;
      box-shadow: 0 6px 20px rgba(0,0,0,0.25);
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s;
    }
    #annotationToast.show {
      opacity: 1;
    }

    /* Mobile Responsive Optimizations for Annotation System */
    @media (max-width: 768px) {
      #teacherPillLauncher {
        bottom: 12px;
        right: 12px;
        font-size: 0.82rem;
        padding: 7px 14px;
        gap: 6px;
        box-shadow: 0 4px 14px rgba(213, 0, 0, 0.4);
        z-index: 9998;
      }
      #teacherToolbar {
        bottom: 8px;
        left: 50%;
        transform: translateX(-50%);
        width: 96vw;
        max-width: 96vw;
        padding: 6px 8px;
        border-radius: 20px;
        gap: 5px;
        flex-wrap: wrap;
        justify-content: center;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
      }
      #teacherToolbar.minimized {
        transform: translateX(-50%) translateY(120px);
      }
      .tb-btn {
        width: 36px;
        height: 36px;
        font-size: 0.95rem;
      }
      .tb-divider {
        height: 20px;
        margin: 0 2px;
      }
      .tb-color-swatch {
        width: 22px;
        height: 22px;
      }
      .tb-size-btn {
        padding: 2px 7px;
        font-size: 0.75rem;
      }
      #annotationToast {
        top: 65px;
        font-size: 0.85rem;
        padding: 8px 16px;
        width: 90%;
        text-align: center;
      }
    }
    """

def get_annotation_html():
    return """
  <!-- TEACHER ANNOTATION CANVAS CONTAINER & LASER POINTER -->
  <div id="annotationContainer">
    <canvas id="annotationBaseCanvas"></canvas>
    <canvas id="annotationActiveCanvas"></canvas>
  </div>
  <div id="laserPointerDot"></div>

  <!-- FLOATING ANNOTATION LAUNCHER PILL -->
  <button id="teacherPillLauncher" onclick="toggleAnnotationToolbar()" title="Open Pen & Pointer Toolbar (Shortcut: Alt+P)">
    ✏️ Pen &amp; Pointer Tools
  </button>

  <!-- FLOATING TEACHER TOOLBAR -->
  <div id="teacherToolbar" class="minimized">
    <!-- Drag Handle -->
    <div class="tb-drag-handle" title="Drag toolbar anywhere">⠿</div>

    <!-- Mode Buttons: Cursor, Laser, Pen, Highlighter, Eraser -->
    <div class="tb-btn-group">
      <button id="tool-cursor" class="tb-btn active" onclick="setAnnotationTool('cursor')" title="Interact / Normal Cursor (Key: 1)">
        👆<span class="tb-tooltip">Interact / Scroll (1)</span>
      </button>
      <button id="tool-laser" class="tb-btn tb-laser" onclick="setAnnotationTool('laser')" title="Laser Pointer (Key: 2)">
        🔴<span class="tb-tooltip">Laser Pointer (2)</span>
      </button>
      <button id="tool-pen" class="tb-btn tb-pen" onclick="setAnnotationTool('pen')" title="Pen (Key: 3)">
        ✏️<span class="tb-tooltip">Pen (3)</span>
      </button>
      <button id="tool-highlighter" class="tb-btn tb-highlighter" onclick="setAnnotationTool('highlighter')" title="Highlighter (Key: 4)">
        🖍️<span class="tb-tooltip">Highlighter (4)</span>
      </button>
      <button id="tool-eraser" class="tb-btn tb-eraser" onclick="setAnnotationTool('eraser')" title="Eraser (Key: 5)">
        🧹<span class="tb-tooltip">Eraser (5)</span>
      </button>
    </div>

    <div class="tb-divider"></div>

    <!-- Color Palette -->
    <div class="tb-btn-group" id="colorPalette">
      <div class="tb-color-swatch active" style="background:#D50000;" onclick="setAnnotationColor('#D50000', this)" title="Ruby Red"></div>
      <div class="tb-color-swatch" style="background:#FFD600;" onclick="setAnnotationColor('#FFD600', this)" title="Laser Yellow"></div>
      <div class="tb-color-swatch" style="background:#00E676;" onclick="setAnnotationColor('#00E676', this)" title="Neon Green"></div>
      <div class="tb-color-swatch" style="background:#1565C0;" onclick="setAnnotationColor('#1565C0', this)" title="Electric Blue"></div>
      <div class="tb-color-swatch" style="background:#AA00FF;" onclick="setAnnotationColor('#AA00FF', this)" title="Vivid Purple"></div>
      <div class="tb-color-swatch" style="background:#0F172A;" onclick="setAnnotationColor('#0F172A', this)" title="Dark Ink"></div>
      <input type="color" id="customColorInput" onchange="setAnnotationColor(this.value, null)" style="width:26px; height:26px; border:none; border-radius:50%; cursor:pointer; background:none;" title="Custom Color">
    </div>

    <div class="tb-divider"></div>

    <!-- Stroke Thickness -->
    <div class="tb-btn-group">
      <button id="size-fine" class="tb-size-btn" onclick="setAnnotationSize(2.5, this)">Fine</button>
      <button id="size-med" class="tb-size-btn active" onclick="setAnnotationSize(5.5, this)">Med</button>
      <button id="size-thick" class="tb-size-btn" onclick="setAnnotationSize(14, this)">Bold</button>
    </div>

    <div class="tb-divider"></div>

    <!-- Actions: Undo, Redo, Clear, Toggle View, Minimize -->
    <div class="tb-btn-group">
      <button class="tb-btn" onclick="undoAnnotation()" title="Undo Stroke (Ctrl+Z)">
        ↩️<span class="tb-tooltip">Undo</span>
      </button>
      <button class="tb-btn" onclick="redoAnnotation()" title="Redo Stroke (Ctrl+Y)">
        ↪️<span class="tb-tooltip">Redo</span>
      </button>
      <button class="tb-btn" onclick="toggleCanvasVisibility()" id="btnToggleVis" title="Hide/Show Drawings">
        👁️<span class="tb-tooltip">Hide/Show</span>
      </button>
      <button class="tb-btn" onclick="clearAnnotationCanvas()" title="Clear All Drawings (Key: C)">
        🗑️<span class="tb-tooltip">Clear Board</span>
      </button>
      <button class="tb-btn" onclick="toggleAnnotationToolbar()" title="Minimize Toolbar (Alt+P)">
        ✖<span class="tb-tooltip">Minimize</span>
      </button>
    </div>
  </div>

  <div id="annotationToast"></div>
"""

def get_annotation_js():
    return """
// --- HIGH-PERFORMANCE TEACHER ANNOTATION & LASER POINTER ENGINE ---
let currentTool = 'cursor'; // 'cursor', 'laser', 'pen', 'highlighter', 'eraser'
let currentColor = '#D50000';
let currentSize = 5.5;
let isDrawing = false;
let currentStroke = null;
let strokes = [];
let redoStack = [];
let isCanvasVisible = true;
let drawRafId = null;
let scrollRafId = null;
let isTouchDevice = false;

// Initialize Annotation Engine
function initAnnotationEngine() {
  const container = document.getElementById('annotationContainer');
  const baseCanvas = document.getElementById('annotationBaseCanvas');
  const activeCanvas = document.getElementById('annotationActiveCanvas');
  if (!container || !baseCanvas || !activeCanvas) return;

  isTouchDevice = ('ontouchstart' in window) || (navigator.maxTouchPoints > 0);

  // Resize canvases on window resize and orientation change
  window.addEventListener('resize', resizeCanvases);
  window.addEventListener('orientationchange', resizeCanvases);
  resizeCanvases();

  // Scroll listener: keep strokes in sync with page content
  window.addEventListener('scroll', handleViewportScroll, { passive: true });

  // Pointer events on container for drawing & touch-laser
  container.addEventListener('pointerdown', handlePointerDown);
  window.addEventListener('pointermove', handlePointerMove);
  window.addEventListener('pointerup', handlePointerUp);
  window.addEventListener('pointercancel', handlePointerUp);

  // Desktop mouse laser tracking and clicks on window
  window.addEventListener('pointermove', handleWindowLaserMove);
  window.addEventListener('click', handleLaserClick);

  // Keyboard Shortcuts
  window.addEventListener('keydown', handleAnnotationShortcuts);

  // Draggable Toolbar
  initToolbarDrag();
}

// Resize canvases to exact viewport dimensions (Zero memory bloat, fits mobile GPU limits)
function resizeCanvases() {
  const baseCanvas = document.getElementById('annotationBaseCanvas');
  const activeCanvas = document.getElementById('annotationActiveCanvas');
  if (!baseCanvas || !activeCanvas) return;

  const w = window.innerWidth;
  const h = window.innerHeight;
  const dpr = Math.min(window.devicePixelRatio || 1, 2); // Cap at 2x for ultra performance

  const targetW = Math.round(w * dpr);
  const targetH = Math.round(h * dpr);

  if (baseCanvas.width !== targetW || baseCanvas.height !== targetH) {
    baseCanvas.width = targetW;
    baseCanvas.height = targetH;
    baseCanvas.style.width = w + 'px';
    baseCanvas.style.height = h + 'px';

    activeCanvas.width = targetW;
    activeCanvas.height = targetH;
    activeCanvas.style.width = w + 'px';
    activeCanvas.style.height = h + 'px';

    redrawBaseCanvas();
  }
}

// Handle viewport scroll with rAF throttle
function handleViewportScroll() {
  if (!scrollRafId) {
    scrollRafId = requestAnimationFrame(() => {
      redrawBaseCanvas();
      if (isDrawing && currentStroke) {
        drawActiveStroke();
      }
      scrollRafId = null;
    });
  }
}

// Redraw all committed strokes on the base canvas
function redrawBaseCanvas() {
  const canvas = document.getElementById('annotationBaseCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const dpr = Math.min(window.devicePixelRatio || 1, 2);

  ctx.save();
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.scale(dpr, dpr);
  ctx.translate(-window.scrollX, -window.scrollY);

  if (isCanvasVisible && strokes.length > 0) {
    for (let i = 0; i < strokes.length; i++) {
      drawSingleStroke(ctx, strokes[i]);
    }
  }

  ctx.restore();
}

// Draw only the stroke currently being drawn on activeCanvas (0.05ms render time!)
function drawActiveStroke() {
  const canvas = document.getElementById('annotationActiveCanvas');
  if (!canvas || !currentStroke) return;
  const ctx = canvas.getContext('2d');
  const dpr = Math.min(window.devicePixelRatio || 1, 2);

  ctx.save();
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.scale(dpr, dpr);
  ctx.translate(-window.scrollX, -window.scrollY);

  drawSingleStroke(ctx, currentStroke);
  ctx.restore();
}

function clearActiveCanvas() {
  const canvas = document.getElementById('annotationActiveCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  ctx.save();
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.restore();
}

// High performance stroke rendering
function drawSingleStroke(ctx, stroke) {
  if (!stroke.points || stroke.points.length === 0) return;

  ctx.save();
  ctx.lineCap = 'round';
  ctx.lineJoin = 'round';

  if (stroke.tool === 'highlighter') {
    ctx.globalAlpha = 0.38;
    ctx.strokeStyle = stroke.color;
    ctx.lineWidth = stroke.size * 2.8;
  } else if (stroke.tool === 'eraser') {
    ctx.globalCompositeOperation = 'destination-out';
    ctx.lineWidth = stroke.size * 3.5;
  } else {
    ctx.globalAlpha = 1.0;
    ctx.strokeStyle = stroke.color;
    ctx.lineWidth = stroke.size;
  }

  ctx.beginPath();
  const pts = stroke.points;

  if (pts.length === 1) {
    ctx.arc(pts[0].x, pts[0].y, ctx.lineWidth / 2, 0, Math.PI * 2);
    ctx.fillStyle = ctx.strokeStyle;
    ctx.fill();
  } else {
    ctx.moveTo(pts[0].x, pts[0].y);
    for (let i = 1; i < pts.length - 1; i++) {
      const xc = (pts[i].x + pts[i + 1].x) / 2;
      const yc = (pts[i].y + pts[i + 1].y) / 2;
      ctx.quadraticCurveTo(pts[i].x, pts[i].y, xc, yc);
    }
    ctx.lineTo(pts[pts.length - 1].x, pts[pts.length - 1].y);
    ctx.stroke();
  }

  ctx.restore();
}

// Pointer down event
function handlePointerDown(e) {
  if (currentTool === 'cursor') return;

  if (currentTool === 'laser') {
    // Touch or click in laser mode
    updateLaserPosition(e.clientX, e.clientY);
    triggerLaserRipple(e.clientX, e.clientY, currentColor);
    if (e.target && e.target.setPointerCapture) {
      try { e.target.setPointerCapture(e.pointerId); } catch(err) {}
    }
    return;
  }

  // Pen, Highlighter, Eraser
  e.preventDefault();
  isDrawing = true;

  if (e.target && e.target.setPointerCapture) {
    try { e.target.setPointerCapture(e.pointerId); } catch(err) {}
  }

  const docX = e.clientX + window.scrollX;
  const docY = e.clientY + window.scrollY;

  currentStroke = {
    tool: currentTool,
    color: currentColor,
    size: currentSize,
    points: [{ x: docX, y: docY }]
  };

  drawActiveStroke();
}

// Pointer move event
function handlePointerMove(e) {
  if (currentTool === 'laser') {
    updateLaserPosition(e.clientX, e.clientY);
    return;
  }

  if (!isDrawing || !currentStroke) return;
  e.preventDefault();

  const docX = e.clientX + window.scrollX;
  const docY = e.clientY + window.scrollY;
  currentStroke.points.push({ x: docX, y: docY });

  if (!drawRafId) {
    drawRafId = requestAnimationFrame(() => {
      drawActiveStroke();
      drawRafId = null;
    });
  }
}

// Pointer up event
function handlePointerUp(e) {
  if (currentTool === 'laser') {
    if (e.target && e.target.releasePointerCapture) {
      try { e.target.releasePointerCapture(e.pointerId); } catch(err) {}
    }
    return;
  }

  if (!isDrawing) return;
  isDrawing = false;

  if (e.target && e.target.releasePointerCapture) {
    try { e.target.releasePointerCapture(e.pointerId); } catch(err) {}
  }

  if (currentStroke && currentStroke.points.length > 0) {
    strokes.push(currentStroke);
    redoStack = [];
  }
  currentStroke = null;

  clearActiveCanvas();
  redrawBaseCanvas();
}

// Laser Pointer Tracking for mouse on window
function handleWindowLaserMove(e) {
  if (currentTool === 'laser') {
    updateLaserPosition(e.clientX, e.clientY);
  }
}

// Update Laser Pointer Position using GPU translate3d
function updateLaserPosition(clientX, clientY) {
  const dot = document.getElementById('laserPointerDot');
  if (!dot) return;
  dot.style.display = 'block';
  dot.style.transform = `translate3d(${clientX}px, ${clientY}px, 0) translate(-50%, -50%)`;
}

// Laser Pointer Pulse Ripple on Click
function handleLaserClick(e) {
  if (currentTool !== 'laser') return;

  const toolbar = document.getElementById('teacherToolbar');
  if (toolbar && toolbar.contains(e.target)) return;

  triggerLaserRipple(e.clientX, e.clientY, currentColor);
}

function triggerLaserRipple(clientX, clientY, color) {
  const ripple = document.createElement('div');
  ripple.className = 'laser-ripple';
  ripple.style.setProperty('--rx', clientX + 'px');
  ripple.style.setProperty('--ry', clientY + 'px');
  ripple.style.borderColor = color || currentColor;
  document.body.appendChild(ripple);

  setTimeout(() => {
    if (ripple.parentNode) ripple.parentNode.removeChild(ripple);
  }, 600);
}

// Set Active Annotation Tool
function setAnnotationTool(tool) {
  currentTool = tool;
  const container = document.getElementById('annotationContainer');
  const dot = document.getElementById('laserPointerDot');

  const toolButtons = document.querySelectorAll('.tb-btn[id^="tool-"]');
  toolButtons.forEach(btn => btn.classList.remove('active'));
  const activeBtn = document.getElementById('tool-' + tool);
  if (activeBtn) activeBtn.classList.add('active');

  isTouchDevice = ('ontouchstart' in window) || (navigator.maxTouchPoints > 0);

  if (container) {
    container.classList.remove('active-drawing', 'active-laser', 'cursor-pen', 'cursor-highlighter', 'cursor-eraser');

    if (tool === 'pen') {
      container.classList.add('active-drawing', 'cursor-pen');
      if (dot) dot.style.display = 'none';
      showToast("✏️ Pen Tool Active (Freehand writing & drawing)");
    } else if (tool === 'highlighter') {
      container.classList.add('active-drawing', 'cursor-highlighter');
      if (dot) dot.style.display = 'none';
      showToast("🖍️ Highlighter Active (Semi-transparent highlighting)");
    } else if (tool === 'eraser') {
      container.classList.add('active-drawing', 'cursor-eraser');
      if (dot) dot.style.display = 'none';
      showToast("🧹 Eraser Tool Active (Drag over strokes to erase)");
    } else if (tool === 'laser') {
      if (isTouchDevice) {
        container.classList.add('active-laser');
      }
      if (dot) dot.style.display = 'block';
      showToast("🔴 Laser Pointer Active (Move or touch to point)");
    } else {
      // Normal cursor
      if (dot) dot.style.display = 'none';
      showToast("👆 Normal Cursor Active (Interact & scroll)");
    }
  }

  // Update laser color class
  if (dot) {
    if (currentColor === '#00E676') dot.classList.add('green-laser');
    else dot.classList.remove('green-laser');
  }
}

// Set Annotation Color
function setAnnotationColor(color, swatchEl) {
  currentColor = color;

  const swatches = document.querySelectorAll('.tb-color-swatch');
  swatches.forEach(s => s.classList.remove('active'));
  if (swatchEl) swatchEl.classList.add('active');

  const dot = document.getElementById('laserPointerDot');
  if (dot) {
    if (color === '#00E676') {
      dot.classList.add('green-laser');
      dot.style.boxShadow = '0 0 6px #00E676, 0 0 14px #00E676, 0 0 26px #00E676, 0 0 40px #00C853';
    } else {
      dot.classList.remove('green-laser');
      dot.style.boxShadow = '0 0 6px ' + color + ', 0 0 14px ' + color + ', 0 0 26px ' + color;
    }
  }

  // If in cursor mode, switch to pen automatically
  if (currentTool === 'cursor' || currentTool === 'eraser') {
    setAnnotationTool('pen');
  }
}

// Set Stroke Thickness
function setAnnotationSize(size, btnEl) {
  currentSize = size;
  const sizeBtns = document.querySelectorAll('.tb-size-btn');
  sizeBtns.forEach(b => b.classList.remove('active'));
  if (btnEl) btnEl.classList.add('active');
}

// Undo Last Stroke
function undoAnnotation() {
  if (strokes.length === 0) {
    showToast("Nothing to undo!");
    return;
  }
  const last = strokes.pop();
  redoStack.push(last);
  redrawBaseCanvas();
  showToast("↩️ Undone last stroke");
}

// Redo Stroke
function redoAnnotation() {
  if (redoStack.length === 0) {
    showToast("Nothing to redo!");
    return;
  }
  const restored = redoStack.pop();
  strokes.push(restored);
  redrawBaseCanvas();
  showToast("↪️ Redone stroke");
}

// Clear Entire Canvas
function clearAnnotationCanvas() {
  if (strokes.length === 0) {
    showToast("Canvas is already clear!");
    return;
  }
  redoStack = [...strokes];
  strokes = [];
  redrawBaseCanvas();
  clearActiveCanvas();
  showToast("🗑️ Canvas cleared! (Press Undo to restore)");
}

// Toggle Visibility of Drawings (Without Deleting)
function toggleCanvasVisibility() {
  isCanvasVisible = !isCanvasVisible;
  const btn = document.getElementById('btnToggleVis');
  if (btn) {
    btn.innerHTML = isCanvasVisible ? '👁️<span class="tb-tooltip">Hide Drawings</span>' : '🙈<span class="tb-tooltip">Show Drawings</span>';
  }
  redrawBaseCanvas();
  showToast(isCanvasVisible ? "👁️ Drawings Visible" : "🙈 Drawings Hidden");
}

// Toggle Teacher Toolbar Minimized/Maximized
function toggleAnnotationToolbar() {
  const toolbar = document.getElementById('teacherToolbar');
  const launcher = document.getElementById('teacherPillLauncher');
  if (!toolbar) return;

  const isMin = toolbar.classList.contains('minimized');
  if (isMin) {
    toolbar.classList.remove('minimized');
    if (launcher) launcher.classList.add('hidden');
    // Default to pen when opened if currently cursor
    if (currentTool === 'cursor') setAnnotationTool('pen');
  } else {
    toolbar.classList.add('minimized');
    if (launcher) launcher.classList.remove('hidden');
    setAnnotationTool('cursor');
  }
}

// Show Toast Notification
let toastTimeout = null;
function showToast(msg) {
  const toast = document.getElementById('annotationToast');
  if (!toast) return;
  toast.innerText = msg;
  toast.classList.add('show');
  clearTimeout(toastTimeout);
  toastTimeout = setTimeout(() => {
    toast.classList.remove('show');
  }, 2200);
}

// Keyboard Shortcuts Handler
function handleAnnotationShortcuts(e) {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

  // Alt + P : Toggle Toolbar
  if (e.altKey && (e.key === 'p' || e.key === 'P')) {
    e.preventDefault();
    toggleAnnotationToolbar();
    return;
  }

  // Ctrl + Z : Undo
  if (e.ctrlKey && (e.key === 'z' || e.key === 'Z') && !e.shiftKey) {
    e.preventDefault();
    undoAnnotation();
    return;
  }

  // Ctrl + Y or Ctrl + Shift + Z : Redo
  if ((e.ctrlKey && (e.key === 'y' || e.key === 'Y')) || (e.ctrlKey && e.shiftKey && (e.key === 'z' || e.key === 'Z'))) {
    e.preventDefault();
    redoAnnotation();
    return;
  }

  // Number shortcuts when toolbar is open
  const toolbar = document.getElementById('teacherToolbar');
  if (toolbar && !toolbar.classList.contains('minimized')) {
    if (e.key === '1') { setAnnotationTool('cursor'); }
    else if (e.key === '2') { setAnnotationTool('laser'); }
    else if (e.key === '3') { setAnnotationTool('pen'); }
    else if (e.key === '4') { setAnnotationTool('highlighter'); }
    else if (e.key === '5') { setAnnotationTool('eraser'); }
    else if (e.key === 'c' || e.key === 'C') { clearAnnotationCanvas(); }
  }
}

// Draggable Toolbar Implementation
function initToolbarDrag() {
  const toolbar = document.getElementById('teacherToolbar');
  if (!toolbar) return;
  const handle = toolbar.querySelector('.tb-drag-handle');
  if (!handle) return;

  let isDragging = false;
  let startX, startY, startLeft, startTop;

  handle.addEventListener('pointerdown', (e) => {
    isDragging = true;
    startX = e.clientX;
    startY = e.clientY;
    const rect = toolbar.getBoundingClientRect();
    startLeft = rect.left;
    startTop = rect.top;
    toolbar.style.transform = 'none';
    toolbar.style.left = startLeft + 'px';
    toolbar.style.top = startTop + 'px';
    toolbar.style.bottom = 'auto';
    handle.setPointerCapture(e.pointerId);
  });

  handle.addEventListener('pointermove', (e) => {
    if (!isDragging) return;
    const dx = e.clientX - startX;
    const dy = e.clientY - startY;
    let newLeft = Math.max(10, Math.min(window.innerWidth - toolbar.offsetWidth - 10, startLeft + dx));
    let newTop = Math.max(10, Math.min(window.innerHeight - toolbar.offsetHeight - 10, startTop + dy));
    toolbar.style.left = newLeft + 'px';
    toolbar.style.top = newTop + 'px';
  });

  handle.addEventListener('pointerup', (e) => {
    isDragging = false;
    handle.releasePointerCapture(e.pointerId);
  });
}

// Auto-run init on DOMContentLoaded or window load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initAnnotationEngine);
} else {
  initAnnotationEngine();
}
"""
