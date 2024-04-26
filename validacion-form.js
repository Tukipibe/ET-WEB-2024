function validarFormulario_nombre(evt){
    let user = document.querySelector("#nombre");
    if(user.value.length >= 6){
        user.classList.add("correct");
        user.classList.remove("error");
        document.querySelector("#error_user").innerHTML = "&nbsp;"
    }else{
        user.classList.remove("correct");
        user.classList.add("error");
        document.querySelector("#error_user").innerHTML = "Error, ingrese 6 caracteres."
    }
}

function validarFormulario_telefono(evt){
    let user = document.querySelector("#telefono");
    if(user.value.length >= 9){
        user.classList.add("correct");
        user.classList.remove("error");
        document.querySelector("#error_tel").innerHTML = "&nbsp;"
    }else{
        user.classList.remove("correct");
        user.classList.add("error");
        document.querySelector("#error_tel").innerHTML = "Error, ingrese 9 caracteres."
    }
}
function validarFormulario_email(evt){
    let user = document.querySelector("#email");
    if(user.value.length >= 9){
        user.classList.add("correct");
        user.classList.remove("error");
        document.querySelector("#error_mail").innerHTML = "&nbsp;"
    }else{
        user.classList.remove("correct");
        user.classList.add("error");
        document.querySelector("#error_mail").innerHTML = "Error, ingrese 9 caracteres."
    }
}

function validarFormulario_mensaje(evt){
    let user = document.querySelector("#mensaje");
    if(user.value.length >= 5){
        user.classList.add("correct");
        user.classList.remove("error");
        document.querySelector("#error_men").innerHTML = "&nbsp;"
    }else{
        user.classList.remove("correct");
        user.classList.add("error");
        document.querySelector("#error_men").innerHTML = "Error, ingrese mas de 5 caracteres."
    }
}