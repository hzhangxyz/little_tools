run=function(){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET","/python?run="+encodeURIComponent(document.getElementById("in").value), false);
    xmlHttp.send(null);
    document.getElementById("out").value=xmlHttp.responseText;
    return true
}
