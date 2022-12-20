class XmasEventTemplate {
    constructor() {
        this.screens = document.querySelectorAll('.c-xmasParty');
        this.activeClassName = 'c-xmasParty--active';
        this.nextScreenSelectorClassName = 'js-xmasPartyNextScreen';
    }

    nextScreen() {
        const activeScreen = document.querySelector(`.${this.activeClassName}`);
        activeScreen.classList.remove(this.activeClassName);
        activeScreen.nextElementSibling.classList.add(this.activeClassName);
    }
}

class XmasScreenToggler extends XmasEventTemplate {
    constructor() {
        super();
        this.nextButtons = document.querySelectorAll(`.${this.nextScreenSelectorClassName}`)
        this.initialize();
    }

    initialize() {
        if (this.screens == null || this.screens.length == 0) {
            return;
        }

        this.screens[0].classList.add(this.activeClassName);
        this.bindEvents();
    }

    bindEvents() {
        this.nextButtons.forEach((button) => {
            button.addEventListener('click', (event) => {
                event.preventDefault();
                this.nextScreen();
            });
        });
    }
}

class XmasFormSubmission extends XmasEventTemplate {
    constructor() {
        super();
        this.submitButton = document.getElementById('js-submitXmasAttendee');
        this.form = document.getElementById('js-xmasPartyForm');
        this.initialize();
    }

    initialize() {
        if (this.submitButton == null || this.form == null) {
            return;
        }

        this.bindEvents();
    }

    bindEvents() {
        this.form.addEventListener('submit', (event) => {
            event.preventDefault();
            this.submitForm();
            this.nextScreen();
        });
    }

    submitForm() {
        const formData = jQuery(this.form).serializeArray();
        const data = Object.fromEntries(formData.map(item => [item.name, item.value]));
        data.action = 'save_entry_xmas_party';

        jQuery.post(ajax_object.ajax_url, data, () => { });
    }
}

document.addEventListener('DOMContentLoaded', function () {
    new XmasScreenToggler();
    new XmasFormSubmission();
    AOS.init();
});