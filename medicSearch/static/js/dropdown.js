let dropdown = document.querySelector('#chevronBtn');

dropdown.addEventListener('click', function(event) {
    event.stopPropagation();
    let dropdownMenu = this.querySelector('#userDropdownMenu');
    dropdownMenu.classList.remove('hidden');
    dropdownMenu.classList.add('block');
});

window.addEventListener('click', function(event) {
    let dropdownMenu = document.querySelector('#userDropdownMenu');
    if (dropdownMenu.classList.contains('block')) {
        dropdownMenu.classList.remove('block');
        dropdownMenu.classList.add('hidden');
    }
});