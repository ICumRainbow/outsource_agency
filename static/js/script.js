'use strict';

const accordionToggle = document.querySelectorAll('.accordion-toggle'),
    textAreaList = document.querySelectorAll('.accordion-text');

document.addEventListener('click',(e) => {
    console.log(e.target)
})

accordionToggle.forEach(item => {
    item.addEventListener('click', (e) => {
        /*const textAreaParent = item.parentElement;
        const textAreaSibling = textAreaParent.nextElementSibling;
        const textArea = textAreaSibling.firstElementChild;*/

        const textAreaParentContainer = item.parentElement;
        const textAreaParent = textAreaParentContainer.parentElement;
        const textAreaSibling = textAreaParent.nextElementSibling;
        const textArea = textAreaSibling.firstElementChild;

        textAreaList.forEach(item => {
            if (item !== textArea) {
                item.style.maxHeight = '0px';
                item.style.paddingBottom = '0px';
            }
        })

        if (e.target.tagName === 'BUTTON') {
            if (!e.target.classList.contains('accordion-active')) {
                accordionToggle.forEach(item => {
                    item.classList.remove('accordion-active');
                })
                e.target.classList.add('accordion-active');
                e.target.style.transition = '.4s';
                textArea.style.maxHeight = 'fit-content';
                textArea.style.paddingBottom = '40px';
            } else {
                e.target.classList.remove('accordion-active');
                e.target.style.transition = '.4s';
                textArea.style.maxHeight = '0px';
                textArea.style.paddingBottom = '0';
            }
        } else if (e.target.parentElement.tagName === 'BUTTON') {
            if (!e.target.parentElement.classList.contains('accordion-active')) {
                accordionToggle.forEach(item => {
                    item.classList.remove('accordion-active');
                })
                e.target.parentElement.classList.add('accordion-active');
                e.target.parentElement.style.transition = '.4s';
                textArea.style.maxHeight = 'fit-content';
                textArea.style.paddingBottom = '40px';
            } else {
                e.target.parentElement.classList.remove('accordion-active');
                e.target.parentElement.style.transition = '.4s';
                textArea.style.maxHeight = '0px';
                textArea.style.paddingBottom = '0';
            }
        }
    })
});

const slides = document.querySelectorAll('.reviews-container'),
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

        slides.forEach(item => item.classList.remove('reviews-element-active'));

        slides[slideIndex - 1].classList.add('reviews-element-active');
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


const membersSlides = document.querySelectorAll('.members-container');
/*slideNext = document.querySelectorAll('.button-next'),
slidePrev = document.querySelectorAll('.button-prev'),
slider = document.querySelectorAll('.pagination'),
indicators = document.createElement('ol');*/

/*slider.forEach(item => item.style.position = 'relative');*/
/*indicators.classList.add('carousel-indicators');

slider.forEach(item => item.append(indicators));

for(let i = 0; i < slides.length; i++) {
    const dot = document.createElement('li');
    dot.setAttribute('data-slide-to', i + 1);
    indicators.append(dot);
}*/

if (membersSlides.length > 0) {

    let slideIndex = 1;

    membersShowSlides(slideIndex);

    function membersShowSlides(n) {
        if (n > membersSlides.length) {
            slideIndex = 1;
        }

        if (n < 1) {
            slideIndex = membersSlides.length;
        }

        membersSlides.forEach(item => item.classList.remove('element-active'));

        membersSlides[slideIndex - 1].classList.add('element-active');
    }

    function membersPlusSlides(n) {
        membersShowSlides(slideIndex += n);
    }

    slidePrev.forEach(item => {
        item.addEventListener('click', () => {
            membersPlusSlides(-1);
        })
    })

    slideNext.forEach(item => {
        item.addEventListener('click', () => {
            membersPlusSlides(1);
        })
    })
}


const accordionToggle2 = document.querySelectorAll('.accordion-toggle_2'),
    textAreaList2 = document.querySelectorAll('.accordion-text_2');

accordionToggle2.forEach(item => {
    item.addEventListener('click', (e) => {
        const textAreaParentContainer = item.parentElement;
        const textAreaParent = textAreaParentContainer.parentElement;
        const textAreaSibling = textAreaParent.nextElementSibling;
        const textArea = textAreaSibling.firstElementChild;

        textAreaList2.forEach(item => {
            if (item !== textArea) {
                item.style.maxHeight = '0px';
                item.style.paddingBottom = '0px';
            }
        })

        if (e.target.tagName === 'BUTTON') {
            if (!e.target.classList.contains('accordion-active')) {
                accordionToggle2.forEach(item => {
                    item.classList.remove('accordion-active');
                })
                e.target.classList.add('accordion-active');
                e.target.style.transition = '.2s';
                textArea.style.maxHeight = 'fit-content';
                textArea.style.paddingBottom = '40px';
            } else {
                e.target.classList.remove('accordion-active');
                e.target.style.transition = '.2s';
                textArea.style.maxHeight = '0px';
                textArea.style.paddingBottom = '0';
            }
        } else if (e.target.parentElement.tagName === 'BUTTON') {
            if (!e.target.parentElement.classList.contains('accordion-active')) {
                accordionToggle2.forEach(item => {
                    item.classList.remove('accordion-active');
                })
                e.target.parentElement.classList.add('accordion-active');
                e.target.parentElement.style.transition = '.2s';
                textArea.style.maxHeight = 'fit-content';
                textArea.style.paddingBottom = '40px';
            } else {
                e.target.parentElement.classList.remove('accordion-active');
                e.target.parentElement.style.transition = '.2s';
                textArea.style.maxHeight = '0px';
                textArea.style.paddingBottom = '0';
            }
        }
    })
});

let prevScrollPos = window.pageYOffset;

window.onscroll = function () {
    let currentScrollPos = window.pageYOffset;

    if (prevScrollPos > currentScrollPos) {
        document.querySelector(".header-wrapper").style.top = "0";
    } else {
        document.querySelector(".header-wrapper").style.top = "-120px";
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
    pageLinkList = document.querySelectorAll('.page-switch'),
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

if (prevButton) {
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
}

let prevPageButton = pageLinkList[0];

if (paginationWrapper) {
    paginationWrapper.addEventListener('click', (e) => {
        const isButton = e.target.nodeName === 'LI';

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

window.addEventListener('DOMContentLoaded', () => {
    const cultureTextImage = document.querySelectorAll('.culture-text-image');

    for (let i = 0; i < cultureTextImage.length; i += 2) {
        cultureTextImage[i].classList.add("reversed");
    }
})

const dropdownsList = document.querySelectorAll('.dropdown-wrapper');

dropdownsList.forEach(item => {
    item.addEventListener('click', (e) => {
        dropdownsList.forEach(item => {
            item.nextElementSibling.classList.remove('dropdown-active')
            item.classList.remove('wrapper-active');
        });

        if (item.nextElementSibling.classList.contains('dropdown-active')) {
            item.nextElementSibling.classList.remove('dropdown-active');
            item.classList.remove('wrapper-active');
        } else {
            item.nextElementSibling.classList.add('dropdown-active');
            item.classList.add('wrapper-active');
        }
    });
})

$(document).ready(function () {
    $('select').niceSelect();
});

const filterButton = document.querySelector('.filter-button');

if (filterButton) {
    filterButton.addEventListener('click', (e) => {
        e.preventDefault();
    });
}

const navLinksList = document.querySelectorAll('.navigation_link');

navLinksList.forEach(item => {
    item.addEventListener('click', () => {
        navLinksList.forEach(item => {
            item.classList.remove('nav-link-active')
        })
        item.classList.add('nav-link-active')
    })
})

const checkboxElementList = document.querySelectorAll('.checkbox-element');

checkboxElementList.forEach(item => {
    item.addEventListener('click', () => {
        const checkboxFirstChild = item.firstElementChild,
            checkboxElement = checkboxFirstChild.firstElementChild;
        if (!checkboxElement.classList.contains("checkbox-active")) {
            checkboxElement.classList.add('checkbox-active');
        } else {
            checkboxElement.classList.remove('checkbox-active');
        }
    })
})

$(document).ready(function () {
    $('.menu-burger-icon').click(function () {
        $(this).toggleClass('open');
    });
});

const burgerElementsList = document.querySelectorAll('.burger-element'),
      burgerWrapper = document.querySelector('.burger-menu-wrapper'),
      mobileNav = document.querySelector('.mobile-nav');

if (burgerWrapper) {
    burgerWrapper.addEventListener('click', () => {
        if (burgerElementsList[0].classList.contains('burger-element-top-active') &&
            burgerElementsList[1].classList.contains('burger-element-bottom-active')) {
            burgerElementsList[0].classList.remove('burger-element-top-active');
            burgerElementsList[1].classList.remove('burger-element-bottom-active');
            mobileNav.classList.remove('mobile-nav-active');
            document.body.style.overflow = 'auto';
        } else {
            burgerElementsList[0].classList.add('burger-element-top-active');
            burgerElementsList[1].classList.add('burger-element-bottom-active');
            mobileNav.classList.add('mobile-nav-active');
            document.body.style.overflow = 'hidden';
        }
    })
}

const modalWindow = document.querySelector('[data-modal]'),
      modalTrigger = document.querySelector('.apply-button_link'),
      modalCloseButton = document.querySelector('.modal-close'),
      modalSubstrate = document.querySelector('.form-wrapper');

if (modalWindow) {
    modalTrigger.addEventListener('click', (e) => {
        e.preventDefault();
        if (!modalWindow.classList.contains('modal-active')) {
            modalSubstrate.style.animation = 'background-fadeIn 1s both';
            modalSubstrate.style.animationDelay = '.5s'
            modalSubstrate.classList.add('substrate-active');
            modalWindow.classList.add('modal-active');
            document.body.style.overflowY = 'hidden';
        } else if (modalWindow.classList.contains('modal-active')) {
            modalSubstrate.style.animation = 'none';
            modalSubstrate.classList.remove('substrate-active');
            modalWindow.classList.remove('modal-active');
            document.body.style.overflowY = 'auto';
        }
    })
    const fileInput = document.querySelector('input[type="file"]');
    fileInput.addEventListener('change',() => {
        const selectedFile = fileInput.files[0],
              fileSize = selectedFile.size,
              maxFileSize = 1024 * 1024 * 5;
        if (fileSize > maxFileSize) {
            document.getElementById('size').innerHTML = 'File size exceeds the limit of 5MB';
            fileInput.value = '';
        } else {
            document.getElementById('size').innerHTML = '';
        }
    })
}



if (modalCloseButton) {
    modalCloseButton.addEventListener('click', () => {
        modalSubstrate.style.animation = 'none';
        modalSubstrate.classList.remove('substrate-active');
        modalWindow.classList.remove('modal-active');
        document.body.style.overflowY = 'auto';
    })
}

if (modalSubstrate) {
    modalSubstrate.addEventListener('click', (e) => {
        if (e.target === modalSubstrate) {
            modalSubstrate.style.animation = 'none';
            modalSubstrate.classList.remove('substrate-active');
            modalWindow.classList.remove('modal-active');
            document.body.style.overflowY = 'auto';
        }
    })
}

const searchClearButton = document.querySelector('.search-clear'),
      searchField = document.querySelector('.nav-search'),
      searchClearWrapper = searchClearButton.parentElement;

if (searchField) {
    searchField.addEventListener('input', () => {
        if (searchField.value !== '') {
            searchClearButton.style.display = 'inline';
        }
    })
}

if (searchField) {
    searchField.addEventListener('click', () => {
        if (searchField.value !== '') {
            searchClearButton.style.display = 'inline';
        }
    })
}

console.log(searchClearButton.parentElement);

if (searchClearButton) {
    searchClearButton.addEventListener('click', (e) => {
        if (e.target.tagName === 'IMG') {
            searchField.value = '';
            searchClearButton.style.display = 'none';
        }
    })
}

searchClearWrapper.addEventListener('click',(e) => {
    if (e.target.firstElementChild === searchClearButton) {
        searchField.value = '';
        searchClearButton.style.display = 'none';
    }
})

document.addEventListener('click',(e) => {
    if (e.target !== searchField) {
        searchClearButton.style.display = 'none';
    }
})