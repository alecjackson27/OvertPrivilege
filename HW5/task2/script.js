class Scanner {

    constructor() {
        this.sql = '';
        this.results = {
            score: 0,
            description: ''
        };

        //document.getElementById('scanBtn').onclick = this.scanBox;
    }

    scanBox() {
        let resultsDiv = document.getElementById('resultsDiv');
        resultsDiv.innerHTML = '';
        this.sql = document.getElementById('SQLBox').value;
        
        // process sql and populate results class member
        this.piggyBack();
        this.tautologies();
        this.union();
        this.alternateEncodings();

        resultsDiv.innerHTML = `<p>Score: ${this.results.score}</p><p>${this.results.description}</p>`;
    }

    // tautologies scan
    tautologies() {
        let tautologies_flag = false;
        if (this.sql.includes('=')) {
            tautologies_flag == true;
            this.results.score++;
        }
        if (this.sql.includes('<')) {
            tautologies_flag == true;
            this.results.score++;
        }
        if (this.sql.includes('>')) {
            tautologies_flag == true;
            this.results.score++;
        }
        if (tautologies_flag) {
            if (this.sql.includes('--')) {
                this.results.score++;
            }
            if (this.sql.toLower().includes('and')) {
                this.results.score++;
            }
            if (this.sql.toLower().includes('or')) {
                this.results.score++;
            }
            this.results.description += 'This SQL likely includes a tautologies attack. ';
        }
    }

    // illegal/logically incorrect scan

    // union scan
    union() {
        if (this.sql.toLower().includes('union')) {
            this.results.score++;
            if (this.sql.includes('--')) {
                this.results.score++;
            }
            this.results.description += 'This SQL likely includes a union attack. ';
        }
    }

    // piggy-back scan
    piggyBack() {
        if (this.sql.includes(';')) {
            this.results.score += 1; // not actually genuine score, don't know how I want to score things...
            // If the sql also includes "--", it is even more likely to be an attack
            if (this.sql.includes('--')) {
                this.results.score += 1;
            }
            this.results.description += 'This SQL likely includes a piggy-back attack. ';
        }
    }

    // inference scan

    // alternate encodings scan
    alternateEncodings() {
        let alternate_encoding_flag = false;
        if (this.sql.toLowerCase().includes("char(")) {
            this.results.score++;
            alternate_encoding_flag = true;
        }
        if (this.sql.toLowerCase().includes("exec(")) {
            this.results.score++;
            alternate_encoding_flag = true;
        }
        if (alternate_encoding_flag) {
            if (this.sql.includes('--')) {
                this.results.score++;
            }
            this.results.description += 'This SQL likely includes a alternate encoding attack. ';
        }
    }

}
