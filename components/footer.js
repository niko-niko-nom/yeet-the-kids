class Footer extends HTMLElement {
    constructor() {
      super();
    }

    connectedCallback() {
        this.innerHTML = `
        <style>
            /* footer elements */
            footer {
                width: 100%;
                bottom: 0;
                height: 60px;
                display: flex;
                flex-direction: column;
                background-color: var(--light);
                padding: 10px;
            }

            footer p {
                width: 100%;
                height: 50%;
                text-align: center;
            }

            #footer-container {
                width: 100%;
                height: 50%;
                display: flex;
                justify-content: center;
                gap: 5px;
            }        
        </style>

        <footer>
            <p id="copyright">&copy; 2024 Yeet The Kids</p>
            <div id="footer-container">
                <p class="credits">Jeroen van de Geest</p>
                <p class="credits">Sem Out</p>
                <p class="credits">Nicole Spierenburg</p>
                <p class="credits">Ahmad Akkad</p>
                <p class="credits">Thomas Middelbos</p>
                <p class="credits">Jochem Hoekstra</p>
            </div>
        </footer>
        `;
    }
}

customElements.define('footer-component', Footer);