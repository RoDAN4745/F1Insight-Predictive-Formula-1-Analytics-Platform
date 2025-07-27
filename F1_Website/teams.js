function openModal(title, content) {
  document.getElementById('modalTitle').innerHTML = title;
  document.getElementById('modalBody').innerHTML = content;
  document.getElementById('teamModal').style.display = 'block';
}

function closeModal() {
  document.getElementById('teamModal').style.display = 'none';
}

window.onclick = function(event) {
  const modal = document.getElementById('teamModal');
  if (event.target === modal) {
    modal.style.display = 'none';
  }
};

document.querySelectorAll('.team-card').forEach((card, i) => {
  card.style.opacity = 0;
  card.style.transform = 'translateY(20px)';
  setTimeout(() => {
    card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    card.style.opacity = 1;
    card.style.transform = 'translateY(0)';
  }, 100 * i);
});
