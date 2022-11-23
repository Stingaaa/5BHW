import words from "wordlist.json" assert {typ: "JSON"}

function startGame(){
    test = document.getElementById("test")
    test.innerText = words
}