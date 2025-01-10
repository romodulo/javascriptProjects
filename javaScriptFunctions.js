console.log('hello')

function sFunc(text) {
    return text
}
// sFunc('text')
const eFunc = (text) => text
console.log(eFunc('test-a'))

const hiBaby_Value = sFunc('test-b')
console.log(hiBaby_Value)

//create a new "Function" Here:
//but, create some initial variables:
let arr = [7,4,3,1,2,5,5];
let pushA = [null];
function fuji(arr) {
    let pushA = []; for (i of arr) {pushA.push(i)}; return pushA
};
//console.log
//but, first..run the fuji function
pushB = fuji(arr)
console.log("pushA:", pushB)

//Examine an anonymous function
//>with a for loop
//but, first..initialize an arr array:
arr = [7,4,3,1,2,5,5];
const Fuji = (arr) => {let pushA = []; for (i of arr) {pushA.push(i)}; return pushA}

//a new console.log
//>of pushA
//but, first..assign Fuji to a variable
console.log(Fuji(arr))

//new concept tested
const FujiObject = {'Fuji' : [
    {
        'Product' : 'Chahan',
        'Cost': 9.90,
        'Tag': 'Fuji-Ichiban'
    },
    {
        'Product': 'Yaki-soba',
        'Cost': 9.90,
        'Tag': 'Fuji-Ichiban'
    }
]
}

for (i in FujiObject) {
    // console.log(i)
    for (ii of FujiObject[i]) {
        console.log(ii.Product)
    }
}


