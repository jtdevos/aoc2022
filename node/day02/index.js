const fs = require('node:fs');
const readline = require('node:readline');

const [R, P, S] = ['rock', 'paper', 'scissors']
const [LOSS, TIE, WIN] = [0, 3, 6];

async function readLines(path) {
    const fileStream = fs.createReadStream(path);
    var lines = [];

    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity,
    });
    // Note: we use the crlfDelay option to recognize all instances of CR LF
    // ('\r\n') in input.txt as a single line break.

    for await (const line of rl) {
        if (line === "") {
            console.log(`---- Line Blank ----`)
        }
        // Each line in input.txt will be successively available here as `line`.
        // console.log(`Line from file: ${line}`);
        lines.push(line);
    }
    return lines;
}


function rpsValues(val) {
    return {
        [R]: 1,
        [P]: 2,
        [S]: 3 
    }[val]
}

function codeToRps (code) {
    return {
        'A': R,
        'B': P,
        'C': S,

        'X': R,
        'Y': P,
        'Z': S
    }[code]
}

function rps(p1Val, p2Val) {
    return {
        [R]: {[R]: TIE, [P]: LOSS, [S]: WIN},
        [P]: {[R]: WIN, [P]: TIE, [S]: LOSS},
        [S]: {[R]: LOSS, [P]: WIN, [S]: TIE},
    }[p1Val][p2Val] + rpsValues(p1Val);
}

/**
 * Return the outcome value (lose, draw, win) given specified outcome code (x,y,z)
 * @param {*} code 
 */
function lookupOutcome(code){
    return {
        'X': LOSS,
        'Y': TIE,
        'Z': WIN
    }[code]
}

/** 
 * return the required counter move from p2 required to acheive the specified
 * outcome, give the specified move from p1
 **/
function rpsCounter(p1Val, outcome){
    return {
        [R]: {[LOSS]: S, [TIE]: R, [WIN]: P},
        [P]: {[LOSS]: R, [TIE]: P, [WIN]: S},
        [S]: {[LOSS]: P, [TIE]: S, [WIN]: R},
    }[p1Val][outcome]
}

function tabulateMatches(lines) {
    var matches = lines.map(line => line.split(/\s+/)
                ).map(m => [codeToRps(m[0]), codeToRps(m[1])]);
    // console.log(`matches: ${matches}`);
    // console.log(`matches[0]: ${matches[0]}`);
    var scores = matches.map(m => rps(m[1], m[0]));
    var total = scores.reduce((sum, score) => {return sum+= score}, 0)
    console.log(`scores part1: ${total}`);
}

function tabulateCounters(lines) {
    var matches = lines.map(line => line.split(/\s+/))
                    .map(m => [codeToRps(m[0]), lookupOutcome(m[1])])
                    .map(m => [m[0], rpsCounter(m[0], m[1])])
    // console.log(`matches[0]: ${matches[0]}`)
    // .map(m => [codeToRps(m[0]), codeToRps(m[1])]);
    var scores = matches.map(m => rps(m[1], m[0]));
    var total = scores.reduce((sum, score) => {return sum+= score}, 0)
    console.log(`scores part2: ${total}`);

                
}

async function main() {
    console.log("sup");
    lines = await readLines('day02/input.txt');
    console.log("finished reading lines");
    tabulateMatches(lines);

    tabulateCounters(lines);

}

main();