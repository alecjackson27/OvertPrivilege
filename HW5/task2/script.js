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

    // illegal/logically incorrect scan

    // union scan

    // piggy-back scan
    piggyBack() {
        if (this.sql.includes(';')) {
            this.results.score += 5; // not actually genuine score, don't know how I want to score things...
            this.results.description += 'This SQL likely includes a piggy-back attack. ';
        }
    }

    // inference scan

    // alternate encodings scan

}
