
// Select the <div> and <button> from the HTML
const $METRICS = document.querySelector("#metrics");
const $BUTTON = document.querySelector("#btn");

// On button click, make an API request to FastAPI backend
$BUTTON.addEventListener("click", () => {
  fetch("http://127.0.0.1:8000/metrics")
    .then((response) => response.json())
    .then((data) => {
      renderMetrics(data); // Pass received data to render function!
    })
    .catch((error) => console.error("Error:", error));
});

// Old school solution, works directly on objects.
/*function renderMetrics(data) {
  $METRICS.innerHTML = "";
  for (let outterKey in data) {
    if (typeof data[outterKey] === "object") {
      for (let innerKey in data[outterKey]) {
        $METRICS.innerHTML += `<h3>${outterKey} - ${innerKey}:</h3><p>${data[outterKey][innerKey]}</p>`;
      }
    } else {
      $METRICS.innerHTML += `<h3>${outterKey}:</h3><p>${data[outterKey]}</p>`;
    }
  }
}*/

// Render the system metrics onto the page
function renderMetrics(data) {
  $METRICS.innerHTML = ""; // Clear previous content

// for of with Object.entries(), clean and readable!
  for (const [key, value] of Object.entries(data)) {
    // If value is an object, loop through its keys
    if (typeof value == "object") {
      for (const [key2, value2] of Object.entries(value)){
        $METRICS.innerHTML += `<h3>${key} - ${key2}: ${value2}</h3>`;
      }
    } else {
      // If value is simple/not object (like timestamp), print directly
      $METRICS.innerHTML += `<h3>${key}: ${value}</h3>`;
    }
  }
}
