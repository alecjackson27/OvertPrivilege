class Scanner {

    constructor() {
        this.sql = '';
        this.results = {
            score: 0,
            description: ''
        };
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
        this.timingInference();
        this.illegal();
        if (this.results.score > 5) {
            this.results.score = 5;
        }

        resultsDiv.innerHTML = `<p>Score: ${this.results.score}</p><p>${this.results.description}</p>`;
    }

    numEq() {
        let count = 0;
        for (let i = 0; i < this.sql.length; i++) {
            if (this.sql[i] == '=') {
                count++;
            }
        }
        return count;
    }

    countOr() {
        let count = 0;
        for (let i = 0; i < this.sql.length; i++) {
            if (this.sql[i].toLowerCase() == 'o') {
                if (this.sql[i+1].toLowerCase() == 'r'){
                    count++;
                }
            }
        }
        return count;
    }

    countAnd() {
        let count = 0;
        for (let i = 0; i < this.sql.length; i++) {
            if (this.sql[i].toLowerCase() == 'a') {
                if (this.sql[i+1].toLowerCase() == 'n' && this.sql[i+2].toLowerCase() == 'd'){
                    count++;
                }
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
                this.results.description += 'This SQL likely includes a tautologies attack or a blind inference attack because it contains "="';
            }
        } else if (this.numEq() > 2){
            tautologies_flag = true;
            this.results.score++;
            this.results.description += 'This SQL likely includes a tautologies attack or a blind inference attack because it contains "="';
        }
        if (this.sql.includes('<')) {
            if (tautologies_flag){
                this.results.description += ' and it contains "<"';
            } else {
                this.results.description += 'This SQL likely includes a tautologies attack or a blind inference attack because it contains "<"';
            }
            tautologies_flag = true;
            this.results.score++;
        }
        if (this.sql.includes('>')) {
            if (tautologies_flag){
                this.results.description += ' and it contains ">"';
            } else {
                this.results.description += 'This SQL likely includes a tautologies attack or a blind inference attack because it contains ">"';
            }
            tautologies_flag = true;
            this.results.score++;
        }
        if (tautologies_flag) {
            if (this.sql.includes('--')) {
                this.results.score++;
                this.results.description += ' and it contains "--"';
            }
            if (this.sql.slice(0, 8) == "SELECT I") {
                if (this.sql.toLowerCase().includes('and')) {
                    this.results.score++;
                    this.results.description += ' and it contains "and"';
                }
            } else if (this.countAnd() > 1) {
                this.results.score++;
                this.results.description += ' and it contains "or"';
            }
            if (this.sql.slice(0, 8) == "SELECT I") {
                if (this.sql.toLowerCase().includes('or')) {
                    this.results.score++;
                    this.results.description += ' and it contains "or"';
                }
            } else if (this.countOr() > 1) {
                this.results.score++;
                this.results.description += ' and it contains "or"';
            }
            this.results.description += ". ";
        }
    }

    // illegal/logically incorrect scan
    illegal() {
        let illegal_flag = false;
        if (this.sql.toLowerCase().includes("convert")){
            this.results.description += 'This SQL may contain an illegal/logically incorrect attack because it contains "convert"';
            this.results.score++;
            illegal_flag = true;
        }
        if (this.sql.includes('"')) {
            this.results.score++;
            if (illegal_flag) {
                this.results.description += ' and "';
            } else {
                this.results.description += 'This SQL may contain an illegal/logically incorrect attack because it contains "';
            }
        }
        this.results.description += '. ';
    }

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
            // If the sql also includes "--" or "update", it is even more likely to be an attack
            if (this.sql.includes('--')) {
                this.results.score += 1;
                this.results.description += ' and "--"'
            }
            if (this.sql.toLowerCase().includes('update')) {
                this.results.score += 1;
                this.results.description += ' and "update"'
            }
            this.results.description += ". "
        }
    }

    // inference scan
    timingInference() {
        if (this.sql.toLowerCase().includes("waitfor")) {
            this.results.score++;
            this.results.description += 'This SQL likely includes a timing inference attack because it contains "waitfor"';
            if (this.sql.includes("--")) {
                this.results.score++;
                this.results.description += ' and it contains "--"';
            }
            if (this.sql.toLowerCase().includes("ascii")) {
                this.results.score++;
                this.results.description += ' and it contains "ascii"';
            }
            if (this.sql.toLowerCase().includes("substring")) {
                this.results.score++;
                this.results.description += ' and it contains "substring"';
            }
            this.results.description += '. ';
        }
    }

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
