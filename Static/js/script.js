// Select the <nav> element in the document
// const nav = document.querySelector("nav");

// // Add a scroll event listener to the window
// window.addEventListener("scroll", function() {
//     // Toggle the "sticky" class based on the scroll position
//     nav.classList.toggle("sticky", this.window.scrollY > 0);
// });


  // Get all nav links
  const navLinks = document.querySelectorAll('.nav-link');

  // Loop through each link
  navLinks.forEach(link => {
    // Compare the link's href to the current URL
    if (link.href === window.location.href) {
      // Remove active class from any other link
      document.querySelector('.nav-link.active')?.classList.remove('active');
      // Add active class to the current link
      link.classList.add('active');
    }
  });


// // scroll sections
// let sections = document.querySelectorAll('section');
// let navLinks = document.querySelectorAll('header nav a');

// window.onscroll = () => {
//     sections.forEach(sec =>{
//         let top = window.scrollY;
//         let offset = sec.offsetTop - 100;
//         let height = sec.offsetHeight;
//         let id = sec.getAttribute('id');

//         if(top >= offset && top < offset + height){
//             // active navbar links
//             navLinks.forEach(links => {
//                 links.classList.remove('active');
//                 document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
//             });
//             // active section for animation on scroll
//             sec.classList.add('show-animate') 
//         }
//         // if want to use animation that repeats on scroll use this 
//         else{
//             sec.classList.remove('show-animate'); 
//         }
//     });



// Subscribe
document.querySelector('.submit-email').addEventListener('mousedown', (e) => {
    e.preventDefault();
    document.querySelector('.subscription').classList.add('done');
  });
  // Remove the label by its ID
var label = document.getElementById('id_username');
if (label) {
label.parentNode.removeChild(label);
}

// // in bootstrap scroll active
// document.addEventListener('scroll', function() {
//   const sections = document.querySelectorAll('section');
//   const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

//   let scrollPosition = window.scrollY;

//   sections.forEach(section => {
//       const sectionTop = section.offsetTop;
//       const sectionHeight = section.offsetHeight;
//       const sectionId = section.getAttribute('id');

//       if (scrollPosition >= sectionTop - sectionHeight / 3 &&
//           scrollPosition < sectionTop + sectionHeight - sectionHeight / 3) {
//           navLinks.forEach(link => {
//               link.classList.remove('active');
//               if (link.getAttribute('href') === '#' + sectionId) {
//                   link.classList.add('active');
//               }
//           });
//       }
//   });
// });

