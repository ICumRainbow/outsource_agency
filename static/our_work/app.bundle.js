/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./src/index.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/index.js":
/*!**********************!*\
  !*** ./src/index.js ***!
  \**********************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _style_scss__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./style.scss */ "./src/style.scss");
/* harmony import */ var _style_scss__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_style_scss__WEBPACK_IMPORTED_MODULE_0__);
 // accordions

function accordions(wrapperID) {
  var wrapper = document.getElementById(wrapperID);

  if (wrapper !== null) {
    var acc = wrapper.querySelectorAll(".accordion");
    var accordions = Array.prototype.slice.call(acc);
    var i;

    for (i = 0; i < accordions.length; i++) {
      accordions[i].firstElementChild.addEventListener("click", function () {
        this.parentElement.classList.toggle("active");
        var panel = this.nextElementSibling.firstElementChild;

        if (!this.parentElement.classList.contains('active')) {
          panel.style.maxHeight = null;
        } else {
          var active = wrapper.querySelectorAll(".accordion.active");

          for (var j = 0; j < active.length; j++) {
            active[j].classList.remove("active");
            active[j].children[1].children[0].style.maxHeight = null;
          }

          this.parentElement.classList.toggle("active");
          panel.style.maxHeight = panel.scrollHeight + "px";
        }
      });
    }
  }
}

function accordionsMultiple() {
  var wrapper = document.querySelectorAll(".c-twoColumnAccordions__finder");

  if (wrapper !== null) {
    var i;

    for (i = 0; i < wrapper.length; i++) {
      var acc = wrapper[i].querySelectorAll(".accordion");
      var accordions = Array.prototype.slice.call(acc);
      var k;

      for (k = 0; k < accordions.length; k++) {
        accordions[k].firstElementChild.addEventListener("click", function () {
          this.parentElement.classList.toggle("active");
          var panel = this.nextElementSibling.firstElementChild;

          if (!this.parentElement.classList.contains('active')) {
            panel.style.maxHeight = null;
          } else {
            var active = document.querySelectorAll(".accordion.active");

            for (var j = 0; j < active.length; j++) {
              active[j].classList.remove("active");
              active[j].children[1].children[0].style.maxHeight = null;
            }

            this.parentElement.classList.toggle("active");
            panel.style.maxHeight = panel.scrollHeight + "px";
          }
        });
      }
    }
  }
}

accordions("faq");
accordions("wrapper");
accordionsMultiple(); //  **************************** menu *********************************************

var hamburger = document.getElementById("hamburger");
var header = document.getElementById("header");
var fakeScroll = document.createElement('div');
fakeScroll.classList.add('scrollbarReplace');

function getScrollbarWidth() {
  return window.innerWidth - document.documentElement.clientWidth;
}

var hamPosition = window.getComputedStyle(hamburger, null).getPropertyValue('right');
hamburger.addEventListener('click', function () {
  var barWidth = getScrollbarWidth();

  if (hamburger.classList.contains('open')) {
    hamburger.classList.remove('open');
    header.classList.remove('show');
    document.body.classList.remove('fixed-bod');
    document.body.style.paddingRight = 0;
    hamburger.style.right = hamPosition;
    fakeScroll.remove();
  } else {
    hamburger.classList.add('open');
    header.classList.add('show');
    document.body.className += ' fixed-bod';
    document.body.appendChild(fakeScroll);
    document.body.style.paddingRight = barWidth + 'px';
    fakeScroll.style.width = barWidth + 'px';
    hamburger.style.right = parseInt(hamPosition.replace(/px/, "")) + barWidth + "px";
  }
});

window.onload = function () {
  (function () {
    var doc = document.documentElement;
    var w = window;
    var prevScroll = w.scrollY || doc.scrollTop;
    var curScroll;
    var direction = 0;
    var prevDirection = 0;
    var header = document.getElementById("header");

    var checkScroll = function checkScroll() {
      curScroll = w.scrollY || doc.scrollTop;

      if (curScroll > prevScroll) {
        direction = 2;
      } else if (curScroll < prevScroll) {
        direction = 1;
      }

      if (direction !== prevDirection) {
        toggleHeader(direction, curScroll);
      }

      prevScroll = curScroll;

      if (curScroll < 60) {
        header.classList.remove('scrolledHeader');
      }
    };

    var toggleHeader = function toggleHeader(direction, curScroll) {
      if (direction === 2 && curScroll > 60) {
        //replace 101 with the height of your header in px
        header.classList.add('hide');
        header.classList.remove('scrolledHeader');
        prevDirection = direction;
      } else if (direction === 1) {
        header.classList.remove('hide');
        header.classList.add('scrolledHeader');
        prevDirection = direction;
      }
    };

    window.addEventListener('scroll', checkScroll);
  })();

  if (window.scrollY !== 0) {
    header.classList.add('hide');
    header.classList.remove('scrolledHeader');
  } // SLIDER


  var swiper = new Swiper(".c-swiper", {
    spaceBetween: 500,
    fadeEffect: {
      crossFade: true
    },
    effect: "fade",
    loop: true,
    pagination: {
      el: ".swiper-my-pagination",
      clickable: true
    },
    navigation: {
      nextEl: ".swiper-arrow-next",
      prevEl: ".swiper-arrow-prev"
    }
  }); // SLIDER AWARDS

  var swiper = new Swiper(".c-listItems--mobile", {
    slidesPerView: "auto",
    centeredSlides: true,
    autoHeight: true,
    spaceBetween: 0,
    navigation: {
      nextEl: ".swiper-button-next-awards",
      prevEl: ".swiper-button-prev-awards"
    }
  }); //  **************************** accordion for awards  *********************************************

  var listAwards = document.getElementsByClassName('c-listItems');

  if (listAwards.length) {
    document.querySelectorAll('.c-listItems--desktop .accordion-listItems')[0].classList.add('active');
    document.querySelectorAll('.c-listItems--desktop .c-listItems__accordionContent')[0].classList.add('active');
    document.querySelectorAll('.c-listItems--tablet .accordion-listItems')[0].classList.add('active');
    document.querySelectorAll('.c-listItems--tablet .c-listItems__accordionContent')[0].classList.add('active');
  }

  ;
  var awardsBasic = Array.prototype.slice.call(document.querySelectorAll('.c-listItems--notMobile .accordion-listItems'));
  var i = 0;

  for (i = 0; i < awardsBasic.length; i++) {
    awardsBasic[i].addEventListener("click", function (e) {
      var panel = document.querySelector('[data-content="' + this.getAttribute('data-value') + '"]');
      var active = document.querySelectorAll(".c-listItems__accordionContent.active");

      if (e.target == this.querySelector('.c-listItems__title') || e.target == this.querySelector('.c-listItems__anchor')) {
        // TOOLTIPS
        for (var j = 0; j < active.length; j++) {
          if (panel != active[j]) {
            // var fadeElements = Array.prototype.slice.call(document.querySelectorAll('.fade'));
            // if(fadeElements.length){
            //     for(let m = 0; j < fadeElements.length; j++){
            //         console.log(fadeElements);
            //         if(this.classList.contains("fade")){
            //             this.classList.remove("fade");
            //         }
            //         console.log('maknuo')
            //     }
            // }
            // active[j].classList.add("fade");
            // setTimeout(() => {
            //     active[j].classList.remove("fade");
            // }, "500")
            active[j].classList.remove("active");
            active[j].style.maxHeight = null;
            active[j].style.zIndex = 1;
          }
        } // TOGGLERS


        var actWrappers = document.querySelectorAll(".c-listItems__accordion");
        var activeWrappers = Array.prototype.slice.call(actWrappers);

        for (var _j = 0; _j < activeWrappers.length; _j++) {
          if (this.getAttribute('data-value') !== activeWrappers[_j].getAttribute('data-value')) {
            activeWrappers[_j].classList.remove("active");
          }

          if (this.classList.contains("active")) {
            this.classList.remove("active");
          } else {
            this.classList.add("active");
          }
        }

        panel.classList.toggle("active");

        if (panel.classList.contains("active")) {
          // panel.style.maxHeight = panel.scrollHeight + "px";
          panel.style.zIndex = 10;
        } else {
          panel.style.maxHeight = null;
          panel.style.zIndex = 1;
        }
      }
    });
  } //  **************************** close button (awards)  *********************************************


  var exit = document.getElementsByClassName("c-listItems__exit");
  var exitArray = Array.prototype.slice.call(exit);
  var s;

  for (s = 0; s < exitArray.length; s++) {
    exitArray[s].addEventListener("click", function (e) {
      if (e.target == this) {
        var panel = document.querySelector('[data-content="' + this.getAttribute('data-value') + '"]');
        var active = document.querySelectorAll(".c-listItems__accordionContent.active");

        for (var k = 0; k < active.length; k++) {
          if (panel != active[k]) {
            active[k].classList.remove("active");
            active[k].style.maxHeight = null;
            active[k].style.zIndex = 1;
          }
        }

        var activeWrappers = document.querySelectorAll(".c-listItems__accordion.active");

        for (var _k = 0; _k < activeWrappers.length; _k++) {
          if (panel != activeWrappers[_k]) {
            activeWrappers[_k].classList.remove("active");
          }
        }
      }
    });
  } //  **************************** IMG2SVG  *********************************************
  // document.querySelectorAll('img.svg').forEach((el) => {
  //     const imgID = el.getAttribute('id');
  //     const imgClass = el.getAttribute('class');
  //     const imgURL = el.getAttribute('src');
  //     fetch(imgURL)
  //         .then(data => data.text())
  //         .then(response => {
  //             const parser = new DOMParser();
  //             const xmlDoc = parser.parseFromString(response, 'text/html');
  //             let svg = xmlDoc.querySelector('svg');
  //             if (typeof imgID !== 'undefined') {
  //                 svg.setAttribute('id', imgID);
  //             }
  //             if(typeof imgClass !== 'undefined') {
  //                 svg.setAttribute('class', imgClass + ' replaced-svg');
  //             }
  //             svg.removeAttribute('xmlns:a');
  //             el.parentNode.replaceChild(svg, el);
  //         })
  // });
  //  **************************** FORM SELECT  *********************************************


  var formSelect = document.getElementById('fluentform_5');

  if (formSelect !== null) {
    var customSelects = formSelect.querySelectorAll('.e-select__Btn');
    formSelect.addEventListener("submit", function () {
      for (var z = 0; z < customSelects.length; z++) {
        var message = document.createElement("div");
        message.innerHTML = "This field is required";
        message.classList.add('text-danger');

        if (customSelects[z].getAttribute('data-type') == 0) {
          customSelects[z].parentNode.appendChild(message);
        }
      }
    }, {
      once: true
    });
  } // each select has to have the data-name set equal to custom selects ID


  var selectArray = document.querySelectorAll(".c-oneColumnForm select:not(.ff_has_multi_select)");
  var selectCount;

  for (var selectCount = 0; selectCount < selectArray.length; selectCount++) {
    var select2 = document.getElementById(selectArray[selectCount].getAttribute('data-name'));
    var replacedSelect = selectArray[selectCount].innerHTML.replaceAll('option', 'div');
    select2.innerHTML = replacedSelect;
    var select2Children = select2.children;
    var select2ChildrenArray = Array.prototype.slice.call(select2Children);
    var childrenCount;

    for (var childrenCount = 0; childrenCount < select2ChildrenArray.length; childrenCount++) {
      var child = select2ChildrenArray[childrenCount];
      child.classList.add('option');
      child.setAttribute('data-type', childrenCount);
      child.setAttribute('data-count', selectCount);
      child.addEventListener("click", function () {
        selectArray[this.getAttribute('data-count')].value = this.getAttribute('value');

        if (this.parent != null) {
          if (this.getAttribute('value') != 0) {
            this.parentElement.nextElementSibling.style.display = 'none';
          } else {
            this.parentElement.nextElementSibling.style.display = 'block';
          }
        }
      });
    }
  }

  var selectArrayNew = document.querySelectorAll(".e-select");

  if (selectArrayNew.length > 0) {
    document.addEventListener("click", function (evt) {
      var targetEl = evt.target; // clicked element    

      if (targetEl.classList.contains('e-select__Btn')) {} else {
        var activeSelects = document.querySelectorAll(".e-select__Btn.box");
        var activeSelectsArray = Array.from(activeSelects);
        activeSelectsArray.forEach(function (a) {
          a.classList.remove('box');
          a.nextElementSibling.classList.remove('toggle');
        });
      }
    });
  } // custom select


  function customSelect() {
    var select = document.querySelectorAll('.e-select__Btn');
    var option = document.querySelectorAll('.option');
    var index = 2;
    select.forEach(function (a) {
      a.addEventListener('click', function (b) {
        var activeSelects = document.querySelectorAll(".e-select__Btn.box");
        var activeSelectsArray = Array.from(activeSelects);
        var next = b.target.nextElementSibling;
        activeSelectsArray.forEach(function (g) {
          g.classList.remove('box');
          g.nextElementSibling.classList.remove('toggle');
          next.classList.toggle('toggle');
          b.target.classList.toggle('box');
        });
        next.classList.toggle('toggle');
        b.target.classList.toggle('box');
        next.style.zIndex = index++;
      });
    });
    option.forEach(function (a) {
      a.addEventListener('click', function (b) {
        b.target.parentElement.classList.remove('toggle');
        b.target.parentElement.previousElementSibling.classList.remove('box');
        var parent = b.target.closest('.e-select').children[0];
        parent.setAttribute('data-type', b.target.getAttribute('data-type'));
        parent.innerText = b.target.innerText;
      });
    });
  }

  customSelect(); // ***************** Contact form slideup ****************

  var contactSubmit = document.querySelector('button[type="submit"]');

  if (contactSubmit != null) {
    contactSubmit.addEventListener("click", function () {
      var scrollHeightForm = document.getElementsByClassName('fluentform');
      var scrollHeightFormHeight = offset(scrollHeightForm[0]);
      setTimeout(function () {
        window.scrollTo(0, scrollHeightFormHeight.top + scrollHeightForm[0].clientHeight / 4);
        AOS.init();
      }, 1000);
    });
  } // CHECKBOX TO HIDDEN FIELD


  var checkboxes = document.querySelectorAll('.ff-el-form-check input');
  var checks;
  var fieldValue = '';
  var interestHidden = document.getElementById("ff_9_interests");

  for (checks = 0; checks < checkboxes.length; checks++) {
    checkboxes[checks].addEventListener("click", function (e) {
      if (this.parentElement.parentElement.classList.contains('ff_item_selected')) {
        // console.log(e);
        fieldValue = fieldValue.replace(this.value + ', ', '');
        interestHidden.setAttribute('value', fieldValue);
      } else {
        fieldValue += this.value + ', ';
        interestHidden.setAttribute('value', fieldValue);
      }
    });
  }

  AOS.init();
}; // get element offset 


function offset(el) {
  var rect = el.getBoundingClientRect(),
      scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,
      scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  return {
    top: rect.top + scrollTop,
    left: rect.left + scrollLeft
  };
}

/***/ }),

/***/ "./src/style.scss":
/*!************************!*\
  !*** ./src/style.scss ***!
  \************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

// extracted by mini-css-extract-plugin

/***/ })

/******/ });
//# sourceMappingURL=app.bundle.js.map