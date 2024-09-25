class Success extends HTMLElement {
    constructor() {
      super();
    }

    connectedCallback() {
        this.innerHTML = `
            <style>

                :root {
                --yeet: #89cdc6;
                --the: #338296;
                --kids: #e43d82;
                --light: #fef5f7;
                --dark: #1a4c5d;
                --darker: #073b4c;
                --borderRadius: 18px;
                }

                /* Style for the success message */
                #success-message {
                    position: fixed;
                    top: 20px;
                    left: 50%;
                    transform: translateX(-50%);
                    background-color: var(--darker)
                    color: var(--light);
                    padding: 15px;
                    border-radius: var--(borderRadius);
                    z-index: 1200;
                    opacity: 0; /* Initially hidden */
                    transition: opacity 0.5s;
                }

                .hidden {
                    display: none;
                }

            </style>

            <!-- Success message container -->
            <div id="success-message" class="hidden">
                Your information was changed successfully!
            </div>

            <script src="success_script.js"></script>
        `;
    }
}

customElements.define('success-component', Success);
