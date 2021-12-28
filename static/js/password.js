
const btn = document.querySelector("#btn-copy")

document.querySelector("#btn-copy").addEventListener("click", ()=>{

    const password = document.querySelector("#password").innerHTML

    navigator.clipboard.writeText(password)
    btn.textContent = "Copied"

})

