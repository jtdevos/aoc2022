const fs = require('node:fs');
const readline = require('node:readline');

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

async function buildElves() {
    let elves = [];
    let lines = await readLines("day01/input.txt");
    elf = [];
    for(const line of lines) {
        if(line==="") {
            console.log(`Adding another elf (backback size:${elf.length}\t cals:${elfCalorieLoad(elf)})`);
            elves.push(elf);
            elf = [];
        } else {
            let val = parseInt(line);
            elf.push(val);
        }
    }
    elves.push(elf)
    // console.log(`Done! Total Lines: ${lines.length}`);
    console.log(`Done calculating elves. elfcount: ${elves.length}`);
    return elves;
}

function elfCalorieLoad(backback) {
    return backback.reduce((sum, item) => sum += item)
}

function mostCalories(elves) {
    var currentMax = 0;
    for(elf of elves) {
        let cals = elfCalorieLoad(elf);
        currentMax = cals > currentMax ? cals : currentMax;
    }
    return currentMax;
}


async function main() {
    let elves = await buildElves();
    console.log(`number of elves:\t${elves.length}`)
    console.log(`most calories:\t ${mostCalories(elves)}`);
    
    let elfLoads = elves.map((elf) => elfCalorieLoad(elf));
    elfLoads.sort((a,b) => b-a);
    console.log(`top three elf cals: ${elfLoads.slice(0,3)}`)
    let topThreeCals = elfLoads.slice(0,3).reduce((sum, load) => sum += load);
    console.log(`top 3 cals:\t ${topThreeCals}`);
    
}


main();