function toggleSection(sectionId) {
  const sections = document.querySelectorAll('.content-section');
  sections.forEach((section) => {
    section.classList.remove('active');
  });

  const activeSection = document.getElementById(sectionId);
  if (activeSection) {
    activeSection.classList.add('active');
  }
}
