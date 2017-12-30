var page=require('webpage').create();
page.open("https://github.com/sakakendo0321",function(){
	page.includeJs("https://raw.githubusercontent.com/blueimp/JavaScript-MD5/master/js/md5.js",
		function(){
		(page.evaluate(function(){
			console.log("load md5.min.js");
		}))
	});

	console.log("hello md5",md5("hello md5"));
	console.log("hello md5");
	phantom.exit();
});

/*
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
	page.evaluate(function(){
		a=document.getElementByTagName("a");
		console.log(a+"href"+a.href);
	});


	phantom.exit();
});
*/
