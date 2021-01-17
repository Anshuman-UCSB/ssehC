const board = document.querySelector(".board");
const boardletters = document.querySelector(".letters");
const boardnumbers = document.querySelector(".numbers");
let letters = ["A", "B", "C", "D", "E", "F", "G", "H"];
let index = 0;
let beige = false;
let num = 1;


for (let i = 0; i < 8; i++){
    let letter = document.createElement("li");
    letter.textContent = letters[i];
    boardletters.appendChild(letter);

    let numbers = document.createElement("li");
    numbers.textContent = num ++;
    boardnumbers.appendChild(numbers);
}

for (let i = 1; i <= 64; i++){
    const square = document.createElement("div");
    if (beige){
        square.classList.add("square");
        square.classList.add("beige");
        index++;
        beige = !beige;
    }
    else {
        square.classList.add("square");
        square.classList.add("sandybrown");
        index++;
        beige = !beige;
    }

    board.appendChild(square);
    if(index===8){
        beige = !beige;
        index = 0;
    }
}