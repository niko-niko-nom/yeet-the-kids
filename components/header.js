class Header extends HTMLElement {
    constructor() {
      super();
    }

    connectedCallback() {
        this.innerHTML = `
        <header>
            <nav id="nav">
                <a href="dashboard.html"><div>Home</div></a>
                <a href="index.html"><div>SCRUM</div></a>
                <a href="index.html"><div>hbo-ICT</div></a>
                <a href="index.html"><div>Help Ik Groei</div></a>
                <a href="Kaas.inc/kaas.html"><div>🧀</div></a>
            </nav>
            <a href="dashboard.html"><img src="./images/NextStep no bg.png"/></a>
        </header>
        `;
    }
}

customElements.define('header-component', Header);