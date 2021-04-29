async function eval(){
    var textField = document.getElementById("display");
    let result;
    try {
        result = await eel.evaluate(textField.value)();
    }
    catch (e) {
        result = e.errorText.split("(", 1);
    }
    textField.value = result;
}

function clearField() {
    var textField = document.getElementById("display");
    textField.value = "";
}

function deleteLast() {
    var textField = document.getElementById("display");
    textField.value = textField.value.slice(0, -1);
}

function writeChar(typ) {
    var textField = document.getElementById("display");
    textField.value += typ;
}

document.onkeydown = function (e) {
    e = e || window.event;
    if (document.activeElement.id == "display") {
        return;
    }
    switch (e.key) {
        case "Enter":
            eval();
            break;

        case "0":
        case "1":
        case "2":
        case "3":
        case "4":
        case "5":
        case "6":
        case "7":
        case "8":
        case "9":
        case "+":
        case "-":
        case "*":
        case "/":
        case "^":
        case "(":
        case ")":
        case "!":
            writeChar(e.key);
            break;
        
        case ".":
        case ",":
            writeChar('.');
            break;

        case "Delete":
            clearField();
            break;
        
        case "Backspace":
            deleteLast();
            break;

        case "F2":
            window.open("docs.pdf");
            break;
    
        default:
            break;
    }
};