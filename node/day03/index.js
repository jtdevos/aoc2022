const readLines = require("../common").readLines
const OFFSET_UPPER = 27
const OFFSET_LOWER = 1
console.log("hello world");

function charCode(c) {
    return c.charCodeAt(0);
}

function itemPriority(item) {
    var val = -1;
    if(item >= 'a' && item <= 'z') {
        val =  charCode(item) - charCode('a') + OFFSET_LOWER
    } else if(item >= 'A' && item <= 'Z') {
        val = charCode(item) - charCode('A') + OFFSET_UPPER
    }
    return val
}

function findCommonItem(items) {
    //split list in half
    var pocket1 = items.slice(0, items.length / 2);
    var pocket2 = items.slice(items.length / 2, items.length);

    //find common item
    var common = pocket1.filter(item => pocket2.includes(item));
    return common[0];
}

async function main() {
    var lines = await readLines('day03/input.txt');
    var itemLists = lines.map(line => line.split(''));
    var priorityLists = itemLists.map(il => il.map(item => itemPriority(item)));
    console.log(`read all lines. Linecount: ${(await lines).length}`);
    console.log('rucksacks:');
    for(var i = 0; i < lines.length; i++) {
        console.log(`\nRuckSack ${i}`);
        console.log(`\titems:\t\t ${itemLists[i]}`)
        console.log(`\tpriorities\t ${priorityLists[i]}`)
        console.log(`\tCommon Item for sack ${i}: ${findCommonItem(itemLists[i])}`);
    }

    var commonItems = itemLists.map(itemList => findCommonItem(itemList));
    console.log(`Common Items: ${commonItems}`)
    for(var i = 0; i < commonItems.length; i++) {
        console.log(`Item: ${commonItems[i]}\t priority:${itemPriority(commonItems[i])}`)
    }

    var prioritySum = commonItems.reduce((sum, item) => sum += itemPriority(item), 0);
    console.log(`Sum of Priorities: ${prioritySum}`);


}

main();