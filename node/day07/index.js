"use strict"
const readLines = require("../common").readLines

const DIR = "DIR";
const FILE = "FILE";
const PARENT_DIR = '..';
const ROOT_DIR = '/';
const REGEX_DIR = /^dir (\S+)$/;
const REGEX_LS = /^\$ ls$/;
const REGEX_CD = /^\$ cd (.+)$/;
const REGEX_FILE = /^(\d+) (\S+)$/;
class Node {
    static {
        Node.root = new Node(DIR, "/");
    }
    constructor(nodeType, name, fsize) {
        this.name = name;
        this.nodeType = nodeType;
        this.fsize = fsize;
        this.children = []
        this.parent = null;
    }
    
    static reset() {
        Node.root = new Node(DIR, "/");
    }

    size() {
        if (DIR == this.nodeType) {
            var sz = 0;
            this.children.forEach(item => {
                sz += item.size()
            });
            return sz;
        } else {
            return this.fsize;
        }
    };

    addFile(name, fsize) {
        var f = new Node(FILE, name, fsize);
        f.parent = this;
        this.children.push(f);
        return this;
    }

    mkdir(name) {
        var d = new Node(DIR, name)
        d.parent = this;
        this.children.push(d);
        return this;
    }

    addChild(childNode) {
        this.children.push(childNode);
        return this;
    }

    cd(name) {
        if(ROOT_DIR === name) {return Node.root};
        if(PARENT_DIR === name) {
            return this.parent;
        } else {
            return this.children.find( n => n.nodeType === DIR && n.name === name);
        }
    }

    iter(cb, depth) {
        if(typeof depth === "undefined") {
            depth = 0;
        }
        if(this.isFile()) throw "tried to call iter() on file"
        for (var n of this.children) {
            if(n.isDir()) {
                cb(n, depth);
                n.iter(cb, depth + 1);
            } else {
                cb(n, depth);
            }
        }
    }

    isDir() {
        return this.nodeType === DIR;
    }

    isFile() {
        return this.nodeType === FILE;
    }

    toString() {
        return `${this.name} (${this.isDir() ? 'd' : 'f'})`
    }
}


function fileNode(name, fsize) {
    var n = new Node(FILE, name, fsize);
    return n;
}

function report(dirNode) {
    console.log("----File Listing----");
    dirNode.iter((node, depth) => {
        var space = '\t'.repeat(depth);
        if(node.isDir()){
            console.log(`${space}(d)${node.name}\t (${node.size()})`)
        } else {
            console.log(`${space}${node.name}\t ${node.size()}`)
        }
    })
    console.log(`All dirs: ${dirList(Node.root)}`);
}

//return a list 
function dirList(node) {
    var dirs = [];
    node.iter( (n,d) => {
        if(n.isDir()) {
            dirs.push(n);
        }
    });
    return dirs;
}

function assert(tst) {
    if(!tst) {
        throw "assertion failed";
    }
}

function test() {
    var root = Node.root;
    var curdir = root;

    root.addFile('a.txt', 100);
    root.addFile('b.txt', 200);

    root.mkdir('items');
    root
        .cd('items')
            .addFile('aa.txt', 50)
            .addFile('bb.txt', 50)
            .mkdir("sub-items")
            .cd("sub-items")
                .addFile('ccc.txt', 1000);
    // root.iter((f, d) => {
    //     console.log(`${'  '.repeat(d)}${f.nodeType}: ${f.name}`)
    // }, 0);
    report(root);

    var curdir = Node.root.cd("items");
    assert(curdir.name === "items");
    curdir = curdir.cd("sub-items")
    assert(curdir.name === "sub-items");
    assert(curdir.cd("/").name === "/")
}

function test2(lines) {
    var cds = lines.filter(line => line.match(REGEX_CD));
    assert(cds.length > 0);
    
    var lss = lines.filter(line => line.match(REGEX_LS));
    assert(lss.length > 0);
    
    var dirs = lines.filter(line => line.match(REGEX_DIR));
    assert(dirs.length > 0);
    assert(dirs.length > 0);
    
    var files = lines.filter(line => line.match(REGEX_FILE));
    var files = files.map( m => m[1])
    assert(files.length > 0);



}


function parseLines(lines) {
    var root = Node.root;
    var curdir = root;
    for(let line of lines) {
        var mcd = line.match(REGEX_CD);
        var mls = line.match(REGEX_LS);
        var mdir = line.match(REGEX_DIR);
        var mfile= line.match(REGEX_FILE);

        if(mcd) {
            var dirname = mcd[1];
            // console.log(`CD ${dirname}`)
            curdir = curdir.cd(dirname);
        } 
        else if(mls){} //no-op for now
        else if(mdir){
            var dirname = mdir[1]
            //console.log(`DIR> ${dirname}`);
            curdir.mkdir(dirname);
        }
        else if(mfile){
            var fsize = parseInt(mfile[1]);
            var fname = mfile[2];
            curdir.addFile(fname, fsize);
        } else {
            throw `Unexpected for line "${line}"`
        }
    }
    return root;
}

function part1(lines) {
    var root = parseLines(lines);
    //find dirs with size 100000 or less 
    var dirs = dirList(root).filter( d => d.size() <= 100000);
    var dirsum = dirs.reduce((ds, d) => ds += d.size(), 0);
    console.log(`Dirs matching: ${dirs.length}\t total: ${dirsum}`);
}

function part2(lines) {
    Node.reset();
    const SPACE_MAX = 70000000;
    const SPACE_FREE_MIN = 30000000;
    
    var root = parseLines(lines);
    var spaceUsed = root.size();
    var dirs = dirList(root);
    dirs.sort((a,b) => {
        return a.size() - b.size();
    });
    // dirs.forEach(a => console.log(`dir: ${a.size()}`));
    var spaceFree = SPACE_MAX - spaceUsed;
    var mindir = dirs.find(d => {
        return (spaceFree + d.size()) > SPACE_FREE_MIN
    });

    console.log(`
 Total Storage: ${SPACE_MAX}
Storage Needed: ${SPACE_FREE_MIN}
  Storage Used: ${spaceUsed}
    Free Space: ${spaceFree}
Min Delete dir: ${mindir.name}::${mindir.size()} (available space after: ${spaceFree + mindir.size()})

    `)


}

async function main() {
    var lines = await readLines('day07/input.txt');
    var testLines = await readLines('day07/sample.txt');
    console.log(`Read file:: total lines:${lines.length}`);
    // test();
    // test2(lines);
    // var parsedDir = parseLines(lines);
    // report(parsedDir)
    part1(lines);

    part2(lines);



}


main()