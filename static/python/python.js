run=function(){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET","/python?run="+encodeURIComponent(document.getElementById("in").value), false);
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
document.querySelector("textarea").addEventListener('keydown',function(e) {
    if(e.keyCode === 9) { // tab was pressed
        // get caret position/selection
        var start = this.selectionStart;
        var end = this.selectionEnd;

        var target = e.target;
        var value = target.value;

        // set textarea value to: text before caret + tab + text after caret
        target.value = value.substring(0, start)
                    + "\t"
                    + value.substring(end);

        // put caret at right position again (add one for the tab)
        this.selectionStart = this.selectionEnd = start + 1;

        // prevent the focus lose
        e.preventDefault();
    }
},false);
