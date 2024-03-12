document.addEventListener('DOMContentLoaded', () => {
    let toggleDropdown = document.getElementById('toggleDropdown');
    let dropdownMenu = document.getElementById('dropdownMenu');
    let chevronIcon = document.getElementById('chevronIcon');

    dropdownMenu.style.display = 'none';
    chevronIcon.classList.add('transform', 'rotate-0');

    toggleDropdown.addEventListener('click', () => {
        dropdownMenu.style.display = dropdownMenu.style.display === 'none' ? 'block' : 'none';
        if (dropdownMenu.style.display === 'block') {
            chevronIcon.classList.remove('rotate-0');
            chevronIcon.classList.add('rotate-180');
        } else {
            chevronIcon.classList.remove('rotate-180');
            chevronIcon.classList.add('rotate-0');
        }
    });

    window.addEventListener('click', event => {
        if (!toggleDropdown.contains(event.target)) {
            dropdownMenu.style.display = 'none';
            chevronIcon.classList.remove('transition-transform', 'duration-500', 'ease-in-out', 'transform', 'hover:rotate-180');
            chevronIcon.classList.add('rotate-0');
        }
    });
});