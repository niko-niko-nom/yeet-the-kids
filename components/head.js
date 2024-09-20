class Head extends HTMLElement {
    constructor() {
      super();
    }

    connectedCallback() {
        this.innerHTML = `
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheets -->
                <title>Your Next Step</title>
            </head>
        `;
    }
}

customElements.define('head-component', Head);