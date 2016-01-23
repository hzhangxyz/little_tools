run=function(){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET","/c?run="+encodeURIComponent(document.getElementById("in").value), false);
    xmlHttp.send(null);
    document.getElementById("out").value=xmlHttp.responseText;
    return true
}
pre=function(e){
    if((e.keyCode==13)&&(e.shiftKey)){
	run()
	return false
    }
    return true
}
IsPC=function(){   
    var system = {        
	win :false,       
	mac :false,       
	xll :false
    }
    var p = navigator.platform
    system.win = p.indexOf("Win") == 0
    system.mac = p.indexOf("Mac") == 0
    system.x11 = (p =="X11") || (p.indexOf("Linux") == 0)
    if(system.win || system.mac || system.xll)
	return true
    else
	return false
}
if(IsPC()){
    document.getElementById("size").innerHTML=".i1{font-size: 100%;}.o1{font-size: 100%;}.b{font-size: 100%}"
}
else {
    document.getElementById("size").innerHTML=".i1{font-size: 500%;}.o1{font-size: 500%;}.b{font-size: 500%}"
}
