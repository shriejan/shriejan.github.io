function appendCharacter(character) {
    var screen = document.getElementById("screen")
    screen.value += character
}


function removeOneCharacter() {
    var screen = document.getElementById("screen")
    screen.value = screen.value.slice(0, -1)
}


function clearScreen() {
    var screen = document.getElementById("screen")
    screen.value = ""
}   

function calculate() {
    var screen = document.getElementById("screen")
    if (screen.value === "") {
        screen.value = "Error"
        return
    }
    screen.value = eval(screen.value) 
}
function squareRoot() {
    var screen = document.getElementById("screen")
    screen.value = Math.sqrt(screen.value)
}
function square() {
    var screen = document.getElementById("screen")
    screen.value = Math.pow(screen.value, 2)
}