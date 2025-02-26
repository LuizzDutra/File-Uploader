var up_status = parseInt(document.getElementById('status').textContent);
status_message = document.getElementById("message");

var download_status = parseInt(document.getElementById('download_status').textContent);
download_status_message = document.getElementById("download_message");

if (up_status == 1){
    status_message.innerHTML = "Successful Upload"
}else if(up_status == -1){
    status_message.innerHTML = "Something went wrong"
}

if(download_status == 0){
    download_status_message.innerHTML = "No files to download on server"
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