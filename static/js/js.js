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
pre=function(n,p){
    var t=-1
    k=p.keyCode
    if(k==13){
	if(p.shiftKey||false==IsPC()){
	    if(cal(n)){
		if(n==s)mak(++s)
    		t=s
	    }
	}
    }
    else if(k==38)
	if(n==0)
	    t=0
    else
	t=n-1
    else if(k==40)
	if(n==s)
	    t=s
    else
	t=n+1
    if(t!=-1){
	var e=document.getElementById("i"+t)
	e.select()
	return false
    }
    return true;
}
mak=function(n){
    var p=document.createElement("div")
    p.align="center"
    p.innerHTML='\
<p class=i1 onclick="getElementById(\'i\'+'+n+').focus()">\
<span class=i3 align="center">></span>\
<textarea class=i2 id=i'+n+' \
onkeydown="return pre('+n+',event)" \
onfocus="this.select()" \
onMouseOver="this.style.borderColor=\'#55CBDA\'" \
onMouseOut="this.style.borderColor=\'white\'">\
</textarea>\
</p>\
<p class=o1 onclick="getElementById(\'o\'+'+n+').focus()">\
<span class=o3 align="center">=</span>\
<textarea class=o2 id=o'+n+' readonly="readonly" \
onfocus="this.select()" \
onMouseOver="this.style.borderColor=\'#4BE28A\'" \
onMouseOut="this.style.borderColor=\'white\'">\
</textarea>\
</p>'
    document.body.appendChild(p)
}
cal=function(n){
    var i=document.getElementById("i"+n)
    var o=document.getElementById("o"+n)
    if(i.value!=""){
	o.value=eval(i.value,scope)
	return true
    }
    else
	return false
}
if(IsPC()){
    document.getElementById("size").innerHTML=".i1{font-size: 100%;}.o1{font-size: 100%;}"
}
else {
    document.getElementById("size").innerHTML=".i1{font-size: 500%;}.o1{font-size: 500%;}"
}
