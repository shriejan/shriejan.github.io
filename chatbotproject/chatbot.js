// We make first some sample responses

// We make a variable that will link with input
const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

// make response on saying hi
async function geminiResponse(input) {
    const api_key = "AIzaSyBcdKfkJJ5bjqqLmfnRFJe43XvoNLmU0qQ";
    const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${api_key}`;
    const headers = {'Content-Type': 'application/json'};
    
    const payload = {
        contents: [{
            parts: [{text: input}]
        }]
    };
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(payload)
        });
        const data = await response.json();
        console.log(data);
        return data.candidates[0].content.parts[0].text;
    } catch (error) {
        return "I'm sorry, bot not responding"; 
    }
}

// When I click the button from HTML, JavaScript should trigger a function to take input and return back output
async function handleInput() {
    const userInputX = document.getElementById("user-input"); // get all properties from text
    const userInput = userInputX.value;
    const botResponse = await geminiResponse(userInput);
    chatBox.innerHTML += `<p><strong>User::</strong> ${userInput}</p><p><strong>Shriejan's bot:</strong> ${botResponse}</p>`;
    userInputX.value = "";
    // remove whatever is in the input box
}

sendBtn.addEventListener("click", handleInput);

// add enter to send message
userInput.addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        handleInput();
    }
});