const orb = document.getElementById("orb")
const statusText = document.getElementById("status")

function listeningMode() {
    orb.classList.add("listening")
    statusText.innerText = "Escutando..."
}

function idleMode() {
    orb.classList.remove("listening")
    statusText.innerText = "Aguardando..."
}

setInterval(() => {
    listeningMode()

    setTimeout(() => {
        idleMode()
    }, 3000)

}, 6000)
