var up_status = parseInt(document.getElementById('status').textContent);
statusMessage = document.getElementById("message")

if (up_status == 1){
    statusMessage.innerHTML = "Upload realizado com sucesso"
}else if(up_status == -1){
    statusMessage.innerHTML = "Upload realizado com sucesso"
}