'use strict';

const accordionToggle = document.querySelectorAll('.accordion-toggle'),
      textAreaList = document.querySelectorAll('.accordion-text');

accordionToggle.forEach(item => {
    item.addEventListener('click',(e) => {
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

const accordionToggle2 = document.querySelectorAll('.accordion-toggle_2'),
      textAreaList2 = document.querySelectorAll('.accordion-text_2');

accordionToggle2.forEach(item => {
    item.addEventListener('click',(e) => {
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


