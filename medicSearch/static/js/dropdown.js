document.addEventListener('DOMContentLoaded', () => {
  let toggleDropdown = document.getElementById('toggleDropdown');
  let dropdownMenu = document.getElementById('dropdownMenu');
  let chevronIcon = document.getElementById('chevronIcon');

  dropdownMenu.style.display = 'none';
  chevronIcon.classList.add('rotate-0');

  toggleDropdown.addEventListener('click', () => {
    dropdownMenu.style.display = dropdownMenu.style.display === 'none' ? 'block' : 'none';

    if (dropdownMenu.style.display === 'block') {
      chevronIcon.classList.remove('rotate-0');
      chevronIcon.classList.add('rotate-180');
    } else {
      chevronIcon.classList.remove('rotate-180');
      chevronIcon.classList.add('rotate-0');
    }

    window.onclick = (e) => {
      if(!toggleDropdown.contains(e.target)) {
        dropdownMenu.style.display = 'none';
        chevronIcon.classList.remove('rotate-180');
      }
    }
  });

});
