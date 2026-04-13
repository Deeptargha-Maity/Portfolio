/* main.js — Deeptargha Maity Portfolio */

/* ---- Custom Cursor ---- */
const cursor     = document.getElementById('cursor');
const cursorRing = document.getElementById('cursorRing');
let mx = 0, my = 0, rx = 0, ry = 0;

document.addEventListener('mousemove', e => {
  mx = e.clientX; my = e.clientY;
  cursor.style.left = mx + 'px';
  cursor.style.top  = my + 'px';
});
setInterval(() => {
  rx += (mx - rx) * 0.15;
  ry += (my - ry) * 0.15;
  cursorRing.style.left = rx + 'px';
  cursorRing.style.top  = ry + 'px';
}, 16);

/* ---- Particle Canvas (Fireflies) ---- */
const canvas = document.getElementById('bg-canvas');
const ctx    = canvas.getContext('2d');

function resizeCanvas() {
  canvas.width  = window.innerWidth;
  canvas.height = window.innerHeight;
}
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

const particles = Array.from({ length: 65 }, () => ({
  x:     Math.random() * canvas.width,
  y:     Math.random() * canvas.height,
  r:     Math.random() * 1.8 + 0.4,
  vx:    (Math.random() - 0.5) * 0.3,
  vy:    (Math.random() - 0.5) * 0.3,
  alpha: Math.random(),
  da:    (Math.random() - 0.5) * 0.008,
  color: Math.random() > 0.5 ? '#4ec76a' : '#86efac',
}));

function drawParticles() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  particles.forEach(p => {
    p.x += p.vx; p.y += p.vy;
    p.alpha += p.da;
    if (p.alpha <= 0 || p.alpha >= 1) p.da *= -1;
    if (p.x < 0) p.x = canvas.width;
    if (p.x > canvas.width)  p.x = 0;
    if (p.y < 0) p.y = canvas.height;
    if (p.y > canvas.height) p.y = 0;
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
    ctx.fillStyle   = p.color;
    ctx.globalAlpha = p.alpha * 0.55;
    ctx.fill();
    ctx.globalAlpha = 1;
  });
  requestAnimationFrame(drawParticles);
}
drawParticles();

/* ---- Hamburger Nav ---- */
const hamburger = document.getElementById('hamburger');
const navLinks  = document.getElementById('navLinks');
hamburger && hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('open');
});
document.querySelectorAll('.nav-links a').forEach(a => {
  a.addEventListener('click', () => navLinks.classList.remove('open'));
});

/* ---- Scroll Reveal + Skill Bars + Counters ---- */
const revealEls = document.querySelectorAll('.reveal');
const observer  = new IntersectionObserver(entries => {
  entries.forEach((entry, i) => {
    if (!entry.isIntersecting) return;
    setTimeout(() => entry.target.classList.add('visible'), i * 80);
    observer.unobserve(entry.target);

    // Animate skill bars
    entry.target.querySelectorAll('.skill-bar').forEach(bar => {
      bar.style.width = bar.dataset.width + '%';
    });

    // Animate counters
    entry.target.querySelectorAll('[data-count]').forEach(el => {
      const target = parseInt(el.dataset.count);
      const suffix = el.dataset.suffix || '';
      let count = 0;
      const step = () => {
        count++;
        el.textContent = count + suffix;
        if (count < target) setTimeout(step, 70);
      };
      step();
    });
  });
}, { threshold: 0.15 });
revealEls.forEach(el => observer.observe(el));

/* ---- Contact Form (AJAX) ---- */
const contactForm    = document.getElementById('contactForm');
const formSuccess    = document.getElementById('formSuccess');
const formError      = document.getElementById('formError');
const submitBtn      = document.getElementById('submitBtn');

contactForm && contactForm.addEventListener('submit', async e => {
  e.preventDefault();
  submitBtn.textContent = 'Sending...';
  submitBtn.disabled    = true;
  formSuccess.style.display = 'none';
  formError.style.display   = 'none';

  try {
    const res  = await fetch('/contact', { method: 'POST', body: new FormData(contactForm) });
    const data = await res.json();
    if (data.success) {
      formSuccess.textContent   = data.message;
      formSuccess.style.display = 'block';
      contactForm.reset();
    } else {
      formError.textContent   = data.error || 'Something went wrong.';
      formError.style.display = 'block';
    }
  } catch {
    formError.textContent   = 'Network error. Please try again.';
    formError.style.display = 'block';
  } finally {
    submitBtn.textContent = 'Send Message';
    submitBtn.disabled    = false;
  }
});
