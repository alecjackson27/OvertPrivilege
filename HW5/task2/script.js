class Scanner {

    constructor() {
        this.sql = '';
        this.results = {
            score: '',
            description: ''
        };

        document.getElementById('scanBtn').onclick = this.scanBox();
    }

    scanBox() {
        let resultsDiv = document.getElementById('resultsDiv');
        resultsDiv.innerHTML = '';
        this.sql = document.getElementById('SQLBox').value;
        
        // process sql and populate results class member
        this.piggyBack();

        resultsDiv.innerHTML = `<p>Score: ${this.results.score}</p><p>${this.results.description}</p>`;
    }

    // tautologies scan
    tautologies() {
        if (this.sql.includes('=')) {
            let indices = [];
            for(let i=0; i < this.sql.length; i++) {
                if (str[i] === '=') indices.push(i);
            }
            for (let i = 0; i < indices.length; i++) {
                index = indices[i];
                let tautologies_flag = false;
                if (this.sql[i-1] === this.sql[i+1]){
                    this.score++;
                    tautologies_flag = true;
                }
            }
            if (tautologies_flag) {
                this.results.description += 'This SQL likely includes a tautologies attack. ';
            }
        }
    }

    // illegal/logically incorrect scan

    // union scan

    // piggy-back scan
    piggyBack() {
        if (this.sql.includes(';')) {
            this.results.score += 1; // not actually genuine score, don't know how I want to score things...
            this.results.description += 'This SQL likely includes a piggy-back attack. ';
        }
    }

    // inference scan

    // alternate encodings scan

}
