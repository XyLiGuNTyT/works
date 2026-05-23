function manyChecksIfElse() {
    let a = Math.floor(Math.random() * 20) + 1;
    console.log(`a = ${a}`);

    let result = '';

    if (a > 10) {
        result += 'a больше чем 10 ';
    } else {
        result += 'a меньше или равно 10 ';
        if (a === 5) {
            result += 'пример особого случая ';
        }
    }

    if (a === 15) {
        result += 'но a не 15';
    }

    if (a > 5) {
        result += 'и a это больше чем 5';
    } else {
        result += 'и a меньше или равно 5';
    }

    if (a % 2) {
        result += ' и a это нечётное';
    } else {
        result += ' и a это четное';
    }

    return result;
}

console.log(manyChecksIfElse());