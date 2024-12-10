let scale = 1;
const zoomImage = document.getElementById('zoom-image');
let isDragging = false;
let startX, startY, initialX, initialY;

// Zoom In
function zoomIn() {
    scale += 0.1;
    zoomImage.style.transform = `scale(${scale})`;
    zoomImage.style.transition = "transform 0.2s";  // Smooth transition on zoom
}

// Zoom Out
function zoomOut() {
    if (scale > 0.2) {
        scale -= 0.1;
        zoomImage.style.transform = `scale(${scale})`;
        zoomImage.style.transition = "transform 0.2s";
    }
}

// Reset Zoom
function resetZoom() {
    scale = 1;
    zoomImage.style.transform = `scale(${scale})`;
    zoomImage.style.transition = "transform 0.2s";
    zoomImage.style.left = "0px";
    zoomImage.style.top = "0px";
}

// Mouse Down Event to Start Dragging
zoomImage.addEventListener('mousedown', function(e) {
    if (scale > 1) {  // Allow dragging only if zoomed in
        isDragging = true;
        initialX = e.clientX - zoomImage.offsetLeft;
        initialY = e.clientY - zoomImage.offsetTop;
        zoomImage.style.cursor = "grabbing";
    }
});

// Mouse Move Event to Drag Image
window.addEventListener('mousemove', function(e) {
    if (isDragging) {
        e.preventDefault();  // Prevent default behavior like text selection
        let moveX = e.clientX - initialX;
        let moveY = e.clientY - initialY;
        zoomImage.style.left = moveX + "px";
        zoomImage.style.top = moveY + "px";
    }
});

// Mouse Up Event to Stop Dragging
window.addEventListener('mouseup', function() {
    isDragging = false;
    zoomImage.style.cursor = "grab";
});