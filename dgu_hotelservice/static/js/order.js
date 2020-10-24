function showAddress(){
    if (ship_different_address.style.display == "block"){ //열려있다면
        document.querySelector('#ship_different_address').style.display = "none";
    }
    else{
        document.querySelector('#ship_different_address').style.display = "block";
    }
}
