$(document).ready(function () {
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".message").textillate('start');
        $(".message").text(message);
    }


    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#Circle").attr("hidden", true);
        
    }

});