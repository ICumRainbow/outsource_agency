'use strict';

const accordionToggle = document.querySelectorAll('.accordion-toggle'),
    textAreaList = document.querySelectorAll('.accordion-text');

accordionToggle.forEach(item => {
    item.addEventListener('click', (e) => {
        const textAreaParent = item.parentElement;
        const textAreaSibling = textAreaParent.nextElementSibling;
        const textArea = textAreaSibling.firstElementChild;

        textAreaList.forEach(item => {
            if (item !== textArea) {
                item.style.maxHeight = '0px';
                item.style.paddingBottom = '0px';
            }
        })
        if (textArea.style.maxHeight === `120px`) {
            e.target.style.transform = 'rotate(0deg)';
            e.target.style.transition = '.2s';
            textArea.style.maxHeight = '0px';
            textArea.style.paddingBottom = '0px';
        } else {
            e.target.style.transform = 'rotate(135deg)';
            e.target.style.transition = '.2s';
            textArea.style.maxHeight = '120px';
            textArea.style.paddingBottom = '40px';
        }
    })
});

const slides = document.querySelectorAll('.members-container'),
    slideNext = document.querySelectorAll('.button-next'),
    slidePrev = document.querySelectorAll('.button-prev'),
    slider = document.querySelectorAll('.pagination'),
    indicators = document.createElement('ol');

/*slider.forEach(item => item.style.position = 'relative');*/
/*indicators.classList.add('carousel-indicators');

slider.forEach(item => item.append(indicators));

for(let i = 0; i < slides.length; i++) {
    const dot = document.createElement('li');
    dot.setAttribute('data-slide-to', i + 1);
    indicators.append(dot);
}*/

if (slides.length > 0) {

    let slideIndex = 1;

    showSlides(slideIndex);

    function showSlides(n) {
        if (n > slides.length) {
            slideIndex = 1;
        }

        if (n < 1) {
            slideIndex = slides.length;
        }

        slides.forEach(item => item.style.display = 'none');

        slides[slideIndex - 1].style.display = 'block';
    }

    function plusSlides(n) {
        showSlides(slideIndex += n);
    }

    slidePrev.forEach(item => {
        item.addEventListener('click', () => {
            plusSlides(-1);
        })
    })

    slideNext.forEach(item => {
        item.addEventListener('click', () => {
            plusSlides(1);
        })
    })
}

const accordionToggle2 = document.querySelectorAll('.accordion-toggle_2'),
    textAreaList2 = document.querySelectorAll('.accordion-text_2');

accordionToggle2.forEach(item => {
    item.addEventListener('click', (e) => {
        const textAreaParent = item.parentElement;
        const textAreaSibling = textAreaParent.nextElementSibling;
        const textArea = textAreaSibling.firstElementChild;
        textAreaList2.forEach(item => {
            if (item !== textArea) {
                item.style.maxHeight = '0px';
                item.style.paddingBottom = '0px';
            }
        })
        if (textArea.style.maxHeight === `120px`) {
            e.target.style.transform = 'rotate(0deg)';
            e.target.style.transition = '.2s';
            textArea.style.maxHeight = '0px';
            textArea.style.paddingBottom = '0px';
        } else {
            e.target.style.transform = 'rotate(135deg)';
            e.target.style.transition = '.2s';
            textArea.style.maxHeight = '120px';
            textArea.style.paddingBottom = '40px';
        }
    })
});

let prevScrollPos = window.pageYOffset;

window.onscroll = function () {
    let currentScrollPos = window.pageYOffset;

    if (prevScrollPos > currentScrollPos) {
        document.querySelector(".header-wrapper").style.top = "0";
    } else {
        document.querySelector(".header-wrapper").style.top = "-100px";
    }

    if (currentScrollPos <= 20) {
        document.querySelector(".header-wrapper").style.zIndex = "9999";
        document.querySelector(".header-wrapper").style.backgroundColor = "transparent";
    } else {
        document.querySelector(".header-wrapper").style.backgroundColor = "white";
    }

    prevScrollPos = currentScrollPos;
}

window.addEventListener('DOMContentLoaded', () => {
    const exampleElements = document.querySelectorAll('.example_element');

    for (let i = 1; i < exampleElements.length; i += 2) {
        exampleElements[i].classList.add("reversed");
    }
})

const navButtonsList = document.querySelectorAll('.nav-button'),
    pageLinkList = document.querySelectorAll('.page-link'),
    buttonsWrapper = document.querySelector('.buttons'),
    paginationWrapper = document.querySelector('.pagination');

// navButtonsList.forEach(item => {
//     item.addEventListener('click',(e) => {
//             navButtonsList.forEach(item => {
//                 item.classList.remove('active');
//             })
//         if (e.target && e.target.tagName === 'DIV') {
//             e.target.classList.add('active');
//         }
//     })
// })
//
// pageSwitchList.forEach(item => {
//     item.addEventListener('click',(e) => {
//         pageSwitchList.forEach(item => {
//             item.classList.remove('page-active');
//         })
//         if (e.target && e.target.tagName === 'LI') {
//             e.target.classList.add('page-active');
//         }
//     })
// })

let prevButton = navButtonsList[0];

if (buttonsWrapper) {
    buttonsWrapper.addEventListener('click', (e) => {
        const isButton = e.target.nodeName === 'DIV';

        if (!isButton || prevButton === e.target) {
            return
        }

        e.target.classList.add('active');

        if (prevButton !== null) {
            prevButton.classList.remove('active');
        }

        prevButton = e.target;
    })
}

let prevPageButton = pageLinkList[0];

if (paginationWrapper) {
    paginationWrapper.addEventListener('click', (e) => {
        const isButton = e.target.nodeName === 'A';

        e.preventDefault();

        if (!isButton || prevPageButton === e.target) {
            return
        }

        e.target.classList.add('page-active');

        if (prevPageButton !== null) {
            prevPageButton.classList.remove('page-active');
        }

        prevPageButton = e.target;
    })
}

window.addEventListener('DOMContentLoaded', () => {
    const textImage = document.querySelectorAll('.transparency-text-image');

    for (let i = 0; i < textImage.length; i += 2) {
        textImage[i].classList.add("reversed");
    }
})

const dropdownsList = document.querySelectorAll('.dropdown-wrapper');

dropdownsList.forEach(item => {
    item.addEventListener('click',(e) => {
        dropdownsList.forEach(item => {
            item.nextElementSibling.classList.remove('dropdown-active')
            item.classList.remove('wrapper-active');
        });

        const target = e.target;

        if (item.nextElementSibling.classList.contains('dropdown-active')) {
            item.nextElementSibling.classList.remove('dropdown-active');
            item.classList.remove('wrapper-active');
        } else {
            item.nextElementSibling.classList.add('dropdown-active');
            item.classList.add('wrapper-active');
        }
    });
})

$(document).ready(function() {
    $('select').niceSelect();
});

const filterButton = document.querySelector('.filter-button');

filterButton.addEventListener('click',(e) => {
    e.preventDefault();
});