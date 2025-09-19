function toggleSection(sectionId) {
  const sections = document.querySelectorAll('.content-section');
  sections.forEach((section) => {
    section.classList.remove('active');
  });

  const activeSection = document.getElementById(sectionId);
  if (activeSection) {
    activeSection.classList.add('active');
  }
  
  //hide moblie nav after clicking
  const nav=document.getElementById('navMenu');
  if(window.innerWidth <=600){
  nav.classList.remove('show');
  }
}

//toggle hamburger menu
const hamburger =document.getElementById('hamburger');
const navMenu =document.getElementById('navMenu');

hamburger.addEventListener('click', ()=>{
  navMenu.classList.toggle('show');
});


