async function loadDashboard(){

const response = await fetch("/metrics")
const metrics = await response.json()

document.getElementById("totalTests").innerText = metrics.total_tests
document.getElementById("failures").innerText = metrics.failures
document.getElementById("screenshots").innerText = metrics.screenshots
document.getElementById("browsers").innerHTML =
`Chromium: ${metrics.browsers.chromium}<br>
Firefox: ${metrics.browsers.firefox}<br>
WebKit: ${metrics.browsers.webkit}`

const passes = metrics.total_tests - metrics.failures

new Chart(document.getElementById("passFailChart"), {

type: "doughnut",

data:{
labels:["Passed","Failed"],
datasets:[{
data:[passes, metrics.failures],
backgroundColor:["#00ffcc","#ff4d4d"]
}]
}

})

const browserLabels = Object.keys(metrics.browsers)
const browserCounts = Object.values(metrics.browsers)

new Chart(document.getElementById("browserChart"), {

type:"doughnut",

data:{
labels:browserLabels,
datasets:[{
data:browserCounts,
backgroundColor:[
"#00ffcc",
"#4da6ff",
"#ffcc66"
]
}]
}

});

}

loadDashboard()

async function loadScreenshots(){

const response = await fetch("/screenshots")
const screenshots = await response.json()

const container = document.getElementById("screenshotList")

screenshots.forEach(s => {

const card = document.createElement("div")
card.className = "card"

const encoded = encodeURIComponent(s.file)

card.innerHTML = `
<h3>${s.browser}</h3>
<img class="failure-img" src="/artifacts/${s.browser}/screenshots/${encoded}">
`

container.appendChild(card)

})

}

loadScreenshots()

document.addEventListener("click", function(e){

if(e.target.classList.contains("failure-img")){

const modal = document.createElement("div")

modal.style.position="fixed"
modal.style.top="0"
modal.style.left="0"
modal.style.width="100%"
modal.style.height="100%"
modal.style.background="rgba(0,0,0,0.9)"
modal.style.display="flex"
modal.style.alignItems="center"
modal.style.justifyContent="center"
modal.style.zIndex="9999"

modal.innerHTML = `<img src="${e.target.src}" style="max-width:90%; max-height:90%;">`

modal.onclick = () => modal.remove()

document.body.appendChild(modal)

}

})