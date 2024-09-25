class Header extends HTMLElement {
    constructor() {
      super();
    }

    connectedCallback() {
        this.innerHTML = `
        <style>    

            /* header elements */
            header {
                background-color: var(--the);
                position: fixed;
                top: 0;
                width: 100%;
                height: 60px;
                display: flex;
                align-items: center;
                font-size: auto;
                z-index: 1000;
            }

            nav {
                width: 100%;
                height: 100%;
                display: flex;
                justify-content: center;
                padding: 5px;
                color: var(--light);
            }

            nav a {
                height: 100%;
                text-decoration: none;
                color: var(--light);
            }

            nav div {
                height: 100%;
                width: auto;
                padding: 0 25px 0 25px;
                display: flex;
                justify-content: center;
                align-items: center;
                font-weight: bold;
            }

            nav div:hover {
                box-shadow: inset 0 0 0 4px var(--yeet), 
                            inset 0 0 0 8px var(--the);
                background: var(--darker);
                transition: 0.2s;
            }

            header img {
                max-height: 60px;
                padding: 5px;
            }

        </style>


        <header>
            <nav id="nav">
                <a href="dashboard.html"><div>Home</div></a>
                <a href="scrum.html"><div>SCRUM</div></a>
                <a href="index.html"><div>hbo-ICT</div></a>
                <a href="./vacatureoverzicht.html"><div>Help Ik Groei</div></a>
                <a href="Kaas.inc/kaas.html"><div>🧀</div></a>
            </nav>
            <a href="dashboard.html"><img src="/APPYTK/static/images/NextStep no bg.png"/></a>
        </header>
        `;
    }
}

customElements.define('header-component', Header);