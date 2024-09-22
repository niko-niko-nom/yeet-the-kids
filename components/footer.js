class Footer extends HTMLElement {
    constructor() {
      super();
    }

    connectedCallback() {
        this.innerHTML = `
        <style>
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
