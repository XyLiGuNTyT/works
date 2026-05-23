let a = Math.floor(Math.random() * 100);
let result;

switch (a) {
    case (a > 10 ? a : a * 2) > 5:
        result = (2 * a) + 1;
        break;
    default:
        let secondPart;
        switch (a) {
            case a < 3:
                secondPart = 1;
                break;
            default:
                secondPart = 2 * (a - 2);
        }
        switch (a) {
            case secondPart > 4:
                result = 5;
                break;
            default:
                result = (a % 2 === 0) ? 6 : 7;
        }
        break;
}

console.log(`Результат для a = ${a}, результат = ${result}`);