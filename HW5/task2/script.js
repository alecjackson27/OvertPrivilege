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
        //this.union();
        //this.alternateEncodings();

        resultsDiv.innerHTML = `<p>Score: ${this.results.score}</p><p>${this.results.description}</p>`;
    }

    numEq() {
        count = 0;
        for (let i = 0; i < this.sql.length; i++) {
            if (this.sql[i] == '=') {
                count++;
            }
        }
        return count;
    }

    // tautologies scan
    tautologies() {
        var tautologies_flag = false;
        if (this.sql.slice(0, 8) == "SELECT I") {
            if (this.numEq() > 1) {
                tautologies_flag = true;
                this.results.score++;
                this.results.description += 'This SQL likely includes a tautologies attack becas ';
            }
        } else if (this.numEq() > 2){
            tautologies_flag = true;
            this.results.score++;
        }
        if (this.sql.includes('<')) {
            tautologies_flag = true;
            this.results.score++;
        }
        if (this.sql.includes('>')) {
            tautologies_flag = true;
            this.results.score++;
        }
        if (tautologies_flag) {
            if (this.sql.includes('--')) {
                this.results.score++;
            }
            if (this.sql.toLowerCase().includes('and')) {
                this.results.score++;
            }
            if (this.sql.toLowerCase().includes('or')) {
                this.results.score++;
            }
            //alert(this.results.score)
            this.results.description += 'This SQL likely includes a tautologies attack. ';
        }
    }

    // illegal/logically incorrect scan

    // union scan
    union() {
        if (this.sql.toLowerCase().includes('union')) {
            this.results.score++;
            this.results.description += 'This SQL likely includes a union attack because it contains "union"';
            if (this.sql.includes('--')) {
                this.results.score++;
                this.results.description += ' and "--"';
            }
            this.results.description += '. ';
        }
    }

    // piggy-back scan
    piggyBack() {
        if (this.sql.includes(';')) {
            this.results.score += 1; // not actually genuine score, don't know how I want to score things...
            this.results.description += 'This SQL likely includes a piggy-back attack because it contains ";"';
            // If the sql also includes "--", it is even more likely to be an attack
            if (this.sql.includes('--')) {
                this.results.score += 1;
                this.results.description += ' and "--"'
            }
            this.results.description += ". "
        }
    }

    // inference scan

    // alternate encodings scan
    alternateEncodings() {
        let alternate_encoding_flag = false;
        if (this.sql.toLowerCase().includes("char(")) {
            this.results.score++;
            alternate_encoding_flag = true;
            this.results.description += 'This SQL likely includes a alternate encoding attack because it contains "char("';
            if (this.sql.toLowerCase().includes("exec(")) {
                this.results.score++;
                this.results.description += ' and "exec("';
            }
        }
        if (alternate_encoding_flag) {
            if (this.sql.includes('--')) {
                this.results.score++;
                this.results.description += ' and "--"';
            }
            this.results.description += '. ';
        }
    }

}
