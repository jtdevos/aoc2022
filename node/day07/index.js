const readLines = require("../common").readLines

const DIR = Symbol();
const FILE = Symbol();

class FileNode {
    constructor(nodeType, name, fsize) {
        this.name = name;
        this.nodeType = nodeType;
        this.fsize = fsize;
        this.children = []
        this.parent = null;
    }

    size() {
        if(DIR==this.nodeType) {
            var sz = 0;
            this.children.forEach( item => {
                sz += item.size()
            });
        } else {
            return this.fsize
        }}
}

async function main() {
    lines = await readLines('day07/input.txt');
    console.log(`Read file:: total lines:${lines.length}`)

}


main()