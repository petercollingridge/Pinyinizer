const pinyinTonemarks = {
    a: ['a', 'ā', 'á', 'ǎ', 'à'],
    e: ['e', 'ē', 'é', 'ě', 'è'],
    i: ['i', 'ī', 'í', 'ǐ', 'ì'],
    o: ['o', 'ō', 'ó', 'ǒ', 'ò'],
    u: ['u', 'ū', 'ú', 'ǔ', 'ù'],
    v: ['ü', 'ǖ', 'ǘ', 'ǚ', 'ǜ'],
    ve: ['üe', 'üē', 'üé', 'üě', 'üè']
};

const rePinyinUe = /(ve?)([0-5])/g;
const rePinyinVowel = /(a[io]?|ei?|[iou])(?:n|ng)?r?([0-5])/g;

const newInput = function() {
    const input = document.getElementById('pinyiniser-input').value;
    let result = input.replace(rePinyinUe, (_, $1, $2) => pinyinTonemarks[$1][$2 % 5]);
    result = result.replace(rePinyinVowel, ($0, $1, $2) => pinyinTonemarks[$1[0]][$2 % 5] + $0.substring(1, $0.length-1));
      //result = escape(input);
    document.getElementById('pinyiniser-output').innerHTML = result;
};

document.getElementById("pinyiniser-input").addEventListener("keyup", (event) => {
    newInput();
});
