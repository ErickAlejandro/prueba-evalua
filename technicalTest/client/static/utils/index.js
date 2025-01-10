const inputNumberArray = document.getElementById("inputNumberArray");
const valArray = document.getElementById("valArray");
const inputNumTarget = document.getElementById("inputNumTarget");
const btnGetSubArrays = document.getElementById("btnGetSubArrays");
const valSubArray = document.getElementById("valSubArray");

let arrayNum = [];

// Funcionalidad del Input
inputNumberArray.addEventListener("keydown", function(event){
    if (event.key === 'Enter') {
        event.preventDefault();
        
        const value = inputNumberArray.value.trim();
        if (value) {
            arrayNum.push(value);
            inputNumberArray.value = ''; 
        }
        valArray.textContent = JSON.stringify(arrayNum);
    }
})

btnGetSubArrays.addEventListener("click", function() {
    const listNumbers = arrayNum;
    const target = inputNumTarget.value == "" ? 0 : inputNumTarget.value;

    const requestBody = {
        array: listNumbers,
        target: parseInt(target, 10)
    };
    
    fetch('/getTargetNum/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
    })
    .then(response => response.json())
    .then(data => {
        if (data.subarray) {
            valSubArray.textContent = `Subarreglo encontrado: ${JSON.stringify(data.subarray)}`;
        } else {
            alert("No se encontró ningún subarreglo.");
        }
    })
    .catch(error => console.error("Error:", error));
});
