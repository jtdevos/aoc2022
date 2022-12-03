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
module.exports.readLines = readLines;
