# Append get_annotation_js to annotation_module.py

annotation_js_code = """
// --- TEACHER ANNOTATION & LASER POINTER JAVASCRIPT ENGINE ---
let currentTool = 'cursor'; // 'cursor', 'laser', 'pen', 'highlighter', 'eraser'
let currentColor = '#D50000';
let currentSize = 5.5;
let isDrawing = false;
let currentStroke = null;
let strokes = [];
let redoStack = [];
let isCanvasVisible = true;

// Initialize Annotation Engine
function initAnnotationEngine() {
  const canvas = document.getElementById('annotationCanvas');
  if (!canvas) return;

  // Window resize & scroll resize handler
  window.addEventListener('resize', resizeAnnotationCanvas);
  window.addEventListener('orientationchange', resizeAnnotationCanvas);
  
  // Re-check size on diagram tab changes or presentation mode
  const observer = new MutationObserver(() => {
    resizeAnnotationCanvas();
  });
  observer.observe(document.body, { attributes: true, childList: true, subtree: true });

  resizeAnnotationCanvas();

  // Pointer Events on Canvas for drawing
  canvas.addEventListener('pointerdown', handlePointerDown);
  window.addEventListener('pointermove', handlePointerMove);
  window.addEventListener('pointerup', handlePointerUp);
  window.addEventListener('pointercancel', handlePointerUp);

  // Laser Pointer tracking on window
  window.addEventListener('pointermove', handleLaserMove);
  window.addEventListener('click', handleLaserClick);

  // Keyboard Shortcuts
  window.addEventListener('keydown', handleAnnotationShortcuts);

  // Make Toolbar Draggable
  initToolbarDrag();
}

// Resize Canvas to cover full document scroll area
function resizeAnnotationCanvas() {
  const canvas = document.getElementById('annotationCanvas');
  if (!canvas) return;
  
  const width = Math.max(document.documentElement.scrollWidth, window.innerWidth);
  const height = Math.max(document.body.scrollHeight, document.documentElement.scrollHeight, window.innerHeight);

  const dpr = window.devicePixelRatio || 1;
  if (canvas.width !== width * dpr || canvas.height !== height * dpr) {
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    canvas.style.width = width + 'px';
    canvas.style.height = height + 'px';
    redrawAllStrokes();
  }
}

// Redraw all stored vector strokes
function redrawAllStrokes() {
  const canvas = document.getElementById('annotationCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;

  ctx.save();
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.scale(dpr, dpr);

  if (!isCanvasVisible) {
    ctx.restore();
    return;
  }

  strokes.forEach(stroke => {
    drawSingleStroke(ctx, stroke);
  });

  ctx.restore();
}

// Draw a single smooth stroke using quadratic curve interpolation
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
  if (currentTool === 'cursor' || currentTool === 'laser') return;
  e.preventDefault();
  isDrawing = true;

  const point = { x: e.pageX, y: e.pageY };
  currentStroke = {
    tool: currentTool,
    color: currentColor,
    size: currentSize,
    points: [point]
  };

  strokes.push(currentStroke);
  redoStack = []; // Clear redo stack on new action

  // Draw initial point
  const canvas = document.getElementById('annotationCanvas');
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  ctx.save();
  ctx.scale(dpr, dpr);
  drawSingleStroke(ctx, currentStroke);
  ctx.restore();
}

// Pointer move event
function handlePointerMove(e) {
  if (!isDrawing || !currentStroke) return;
  e.preventDefault();

  const point = { x: e.pageX, y: e.pageY };
  currentStroke.points.push(point);

  // Redraw for smooth curves
  redrawAllStrokes();
}

// Pointer up event
function handlePointerUp(e) {
  if (!isDrawing) return;
  isDrawing = false;
  currentStroke = null;
}

// Laser Pointer Tracking
function handleLaserMove(e) {
  const dot = document.getElementById('laserPointerDot');
  if (!dot) return;

  if (currentTool === 'laser') {
    dot.style.display = 'block';
    dot.style.left = e.clientX + 'px';
    dot.style.top = e.clientY + 'px';
  } else {
    dot.style.display = 'none';
  }
}

// Laser Pointer Pulse on Click
function handleLaserClick(e) {
  if (currentTool !== 'laser') return;
  
  // Don't pulse if clicking on toolbar buttons
  const toolbar = document.getElementById('teacherToolbar');
  if (toolbar && toolbar.contains(e.target)) return;

  const ripple = document.createElement('div');
  ripple.className = 'laser-ripple';
  ripple.style.left = e.clientX + 'px';
  ripple.style.top = e.clientY + 'px';
  ripple.style.borderColor = currentColor;
  document.body.appendChild(ripple);

  setTimeout(() => {
    if (ripple.parentNode) ripple.parentNode.removeChild(ripple);
  }, 600);
}

// Set Active Annotation Tool
function setAnnotationTool(tool) {
  currentTool = tool;
  const canvas = document.getElementById('annotationCanvas');
  const dot = document.getElementById('laserPointerDot');

  // Update Toolbar UI buttons
  const toolButtons = document.querySelectorAll('.tb-btn[id^="tool-"]');
  toolButtons.forEach(btn => btn.classList.remove('active'));
  const activeBtn = document.getElementById('tool-' + tool);
  if (activeBtn) activeBtn.classList.add('active');

  if (canvas) {
    canvas.classList.remove('active-drawing', 'cursor-pen', 'cursor-highlighter', 'cursor-eraser');
    if (tool === 'pen') {
      canvas.classList.add('active-drawing', 'cursor-pen');
      showToast("✏️ Pen Tool Active (Freehand Writing & Drawing)");
    } else if (tool === 'highlighter') {
      canvas.classList.add('active-drawing', 'cursor-highlighter');
      showToast("🖍️ Highlighter Tool Active (Semi-Transparent Underlining)");
    } else if (tool === 'eraser') {
      canvas.classList.add('active-drawing', 'cursor-eraser');
      showToast("🧹 Eraser Tool Active (Click or Drag over Strokes to Erase)");
    } else if (tool === 'laser') {
      canvas.classList.remove('active-drawing');
      if (dot) dot.style.display = 'block';
      showToast("🔴 Laser Pointer Active (Click to Pulse & Focus Attention)");
    } else {
      // Normal cursor
      canvas.classList.remove('active-drawing');
      if (dot) dot.style.display = 'none';
      showToast("👆 Normal Cursor Active (Interact & Scroll Page)");
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
  redrawAllStrokes();
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
  redrawAllStrokes();
  showToast("↪️ Redone stroke");
}

// Clear Entire Canvas
function clearAnnotationCanvas() {
  if (strokes.length === 0) {
    showToast("Canvas is already clear!");
    return;
  }
  redoStack = [...strokes]; // Store in redo stack in case user wants it back!
  strokes = [];
  redrawAllStrokes();
  showToast("🗑️ Canvas cleared! (Press Ctrl+Z or Undo to restore)");
}

// Toggle Visibility of Drawings (Without Deleting)
function toggleCanvasVisibility() {
  isCanvasVisible = !isCanvasVisible;
  const btn = document.getElementById('btnToggleVis');
  if (btn) {
    btn.innerHTML = isCanvasVisible ? '👁️<span class="tb-tooltip">Hide Drawings</span>' : '🙈<span class="tb-tooltip">Show Drawings</span>';
  }
  redrawAllStrokes();
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
  // Don't trigger shortcuts if user is typing in an input
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
    toolbar.style.transform = 'none'; // Clear translate(-50%) when moving manually
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

with open(r"E:\Google-AntiGravity-Projects\1.PPTs-Lecture-Notes\LASERS-BSc.Physics\annotation_module.py", "a", encoding="utf-8") as f:
    f.write(f"""
def get_annotation_js():
    return \"\"\"{annotation_js_code}\"\"\"
""")
print("Successfully wrote annotation_module.py with full JS engine!")
