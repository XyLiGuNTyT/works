let a = Math.floor(Math.random() * 100);
let result;

let firstPart;
if (a > 10) {
    firstPart = a;
} else {
    firstPart = a * 2;
}

if (firstPart > 5) {
    result = (2 * a) + 1;
} else {
    let secondPart;
    if (a < 3) {
        secondPart = 1;
    } else {
        secondPart = 2 * (a - 2);
    }

    if (secondPart > 4) {
        result = 5;
    } else {
        if (a % 2 == 0) {
            result = 6;
        } else {
            result = 7;
        }
    }
}

console.log(`Результат для a = ${a}, результат = ${result}`);