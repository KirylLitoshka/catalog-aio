"use strict";

let phone_area = document.querySelector('.phone-area');
let phone_block = document.querySelector('.phone-block');

function set_active(elem) {
    if (phone_area.classList.contains('active')) {
        phone_area.classList.remove('active');
    } else {
        phone_area.classList.add('active');
    }
}

phone_block.addEventListener('click', set_active)