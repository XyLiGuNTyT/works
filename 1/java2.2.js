function manyChecksSwitch() {
    let a = Math.floor(Math.random() * 20) + 1;
    console.log(`a = ${a}`);

    let result = '';

    switch (a) {
        case a > 10:
            result += 'a больше чем 10';
            break;
        default:
            result += 'a меньше или равно 10 ';
            switch (a) {
                case a === 5:
                    result += 'пример особого случая ';
                    break;
            }
    }

    switch (a) {
        case a === 15:
            result += 'но a не 15';
            break;
    }

    switch (a) {
        case a > 5:
            result += 'и a это больше чем 5';
            break;
        default:
            result += 'и a меньше или равно 5';
    }

    switch (a) {
        case a % 2 === 1:
            result += ' и a это нечётное';
            break;
        default:
            result += ' и a это чётное';
    }

    return result;
}

console.log(manyChecksSwitch());