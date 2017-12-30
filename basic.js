var page=require('webpage').create();
page.onResourceReceived=function(responce){
	console.log("onResourceReceived\nurl:"+responce.url+"\nheaders:"+responce.headers+"\nstatus:"+responce.status);

}
page.settings.userName="XXX";
page.settings.password="xxx";
page.open('https://sakakendo.pythonanywhere.com/basic',function(status){
	console.log("index.html\nStatus "+status);
	if(status == "success"){
		page.render('sakakendo.pythonanywhere.png');
		console.log("title "+page.title);
		console.log("content "+page.content);
	}
	phantom.exit();
});
