run=function(){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET","/python?run="+document.getElementById("in").value, false);
    xmlHttp.send(null);
    document.getElementById("out").value=xmlHttp.responseText;
    return true
}
