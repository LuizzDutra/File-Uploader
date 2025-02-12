var up_status = parseInt(document.getElementById('status').textContent);
statusMessage = document.getElementById("message");

if (up_status == 1){
    statusMessage.innerHTML = "Successful Upload"
}else if(up_status == -1){
    statusMessage.innerHTML = "Something went wrong"
}

//check cached selection from browser
if(document.getElementById("id_file").files[0]){
    document.getElementById("id_file").style.backgroundImage = `url(${checkIcon})`;;
}

document.getElementById("id_file").addEventListener("change", function(e){
    if(e.target.files[0]){
        e.target.style.backgroundImage = `url(${checkIcon})`;;
    }
})