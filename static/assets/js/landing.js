// AI Nodes Animation
const canvas = document.getElementById('ai-nodes');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const nodes = [];
const numNodes = 50;
const colors = ['#4C5D96', '#45558D'];

class Node {
    constructor() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.radius = Math.random() * 3 + 1;
        this.color = colors[Math.floor(Math.random() * colors.length)];
        this.vx = (Math.random() - 0.5) * 2;
        this.vy = (Math.random() - 0.5) * 2;
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.closePath();
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;

        if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
        if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
    }
}

for (let i = 0; i < numNodes; i++) {
    nodes.push(new Node());
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw nodes and connections
    nodes.forEach(node => {
        node.update();
        node.draw();

        nodes.forEach(otherNode => {
            const dist = Math.hypot(node.x - otherNode.x, node.y - otherNode.y);
            if (dist < 100) {
                ctx.beginPath();
                ctx.moveTo(node.x, node.y);
                ctx.lineTo(otherNode.x, otherNode.y);
                ctx.strokeStyle = `rgba(76, 93, 150, ${1 - dist / 100})`;
                ctx.lineWidth = 1;
                ctx.stroke();
            }
        });
    });

    requestAnimationFrame(animate);
}

animate();

// Resize canvas on window resize
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});