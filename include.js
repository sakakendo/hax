var page=require('webpage').create();

page.open('https://sakakendo.pythonanywhere.com',function(status){
	console.log("index.html\nStatus "+status);
	if(status == "success"){
		console.log("title "+page.title);
		console.log("content "+page.content);
	}
	page.evaluate(function(){
		a=document.getElementByTagName("a");
		console.log(a+"href"+a.href);
	});


	phantom.exit();
});
