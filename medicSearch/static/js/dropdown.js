document.addEventListener('DOMContentLoaded', () => {
    let toggleDropdown = document.getElementById('toggleDropdown');
    let dropdownMenu = document.getElementById('dropdownMenu');

    dropdownMenu.style.display = 'none';

    toggleDropdown.addEventListener('click', () => {
        dropdownMenu.style.display = dropdownMenu.style.display === 'none' ? 'block' : 'none';
    });

    window.addEventListener('click', event => {
        if (!toggleDropdown.contains(event.target)) {
            dropdownMenu.style.display = 'none';
        }
    });
});