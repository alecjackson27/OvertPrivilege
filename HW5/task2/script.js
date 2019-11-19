class Scanner {

    constructor() {
        this.sql = '';
        this.results = {
            score: '',
            description: ''
        };
    }

    scanBox() {
        let resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';
        this.sql = document.getElementById('SQLBox').value;
        
        // process sql and populate results class member

        resultsDiv.innerHTML = `<p>Score: ${this.results.score}</p><p>${description}</p>`
    }

    // tautologies scan

    // illegal/logically incorrect scan

    // union scan

    // piggy-back scan

    // inference scan

    // alternate encodings scan

}