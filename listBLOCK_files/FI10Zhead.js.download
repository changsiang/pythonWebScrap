var h_defaults = { 
		showlogout	: false,
		eserviceid	: "",
		sysid		: "",
		spinshost	: "",
		showrateservice : false,
		isportal	: true,
		feedbackurl : "",
		jsaddons	: "",
		usehost		: "",
		service_link_show_feedback : true,
		service_link_show_help: true,
		service_link_use_site_feedback: false,
		userscpath		: "",
		logserver	: "",
		spinshost	: "",
		staticpage: false,
		noeservicelinks: false,
		excludefastclick: false,
		usepath: "",
		logouturl: "",
		useprotocol: ""
			}

function init_h_config() {
	var p = (location.protocol!="file:"?location.protocol:"http:");
	//merge defaults
	for(x in h_defaults){
		if(typeof(h_config[x])!="undefined"){
			h_defaults[x] = h_config[x]
		}			
	}
	h_config = h_defaults;
	var host = "services2.hdb.gov.sg";
	host 	 = location.host;
	var dominopath 	= "/fi10/fi10297p.nsf/fi10/infoweb/common"; 
	var wspath		= "/web/fi10/infoweb/common";
	
	host = getRSCHost();
	
	if ("" != h_config.usehost) {
		host = h_config.usehost;
	}	
	
	//var path = (location.pathname.indexOf('.nsf') > -1 )? dominopath: wspath;	
	var path = wspath;
	
	if ("" != h_config.userscpath) {
		path = h_config.userscpath;
	}	
	
	h_config.rschost 	= p + "//" + host + path;
	h_config.rschostname 	= p + "//" + host;
	h_config.wcmsUrl = "http://www.hdb.gov.sg/cs/infoweb"; 
	
	var prodhosts = ["services2-pre.hdb.gov.sg", 
   "services2.hdb.gov.sg",
   "services3.hdb.gov.sg",
   "services3-pre.hdb.gov.sg",
		"services2-preprod.hdb.gov.sg",
		"services3-preprod.hdb.gov.sg",
		"share.hdb.gov.sg"]
	
	
	var getEservicesHost = function(){
		var eserhost		= ( host.indexOf('www.') > -1 ? "www.hdb.gov.sg" : "www20.hdb.gov.sg" );
		eserhost  = ( host.indexOf('www20-pre.') > -1 ? "www20-pre.hdb.gov.sg" : eserhost );
		if (host.indexOf('intranet79.hdb.gov.sg') > -1 || host.indexOf('IS78')  > -1 || host.indexOf('IS79') > -1 ) {
			eserhost = "intranet79.hdb.gov.sg";
		}else if (prodhosts.indexOf(host) > -1) {
			eserhost = 'www20.hdb.gov.sg';
		}
		
		return eserhost;
		
	}
			
	
	var eserhost		= getEservicesHost();
		
	h_config.eserhost	= p + "//" +eserhost;		
	h_config.eserdb		= p + "//" + eserhost + "/fi10/fi10200p.nsf" 
			
	
	var getLogServer = function(){		

		var dominoprodhosts = ["www.hdb.gov.sg","www20.hdb.gov.sg", "intranet.hdb.gov.sg", "intranet79.hdb.gov.sg", "www69A.hdb.gov.sg", "www69B.hdb.gov.sg", "www68a.hdb.gov.sg", "www68b.hdb.gov.sg"],		
			isprod	= (prodhosts.indexOf(host) > -1) || (dominoprodhosts.indexOf(host) > -1),
			isdomino = (location.pathname.indexOf('.nsf') > -1 );
		
		var server	= ( isprod ? "services2-pre.hdb.gov.sg" : "services2s.nicehomes.com.sg" ); 
		
		server = h_config.rschostname; 
		
		return server;
	}
	
		
	h_config.logserver  = getLogServer();
	
	var optICPS = getOptICPSHost();	

		optICPS = p + "//"+ optICPS;
		
	var esvcUrl = host.indexOf('services3')> -1? optICPS : h_config.logserver;
	//esvcUrl = (location.href).indexOf('.nsf')> -1? "services2u-pre.nicehomes.com.sg" : esvcUrl;
	
    var esvcUrl1 = esvcUrl.replace("http:","https:");
	
	h_config.esvcUrl = esvcUrl1;
	
	
	
	
	
}

function getRSCHost(){
  
  var host = location.href.toLowerCase(); 
  
    if ( host.indexOf('intranet.') > -1 ) {
    return "intranet.hdb.gov.sg";
	} else if ( host.indexOf('intranet79.') > -1 ) {
    return "intranet79.hdb.gov.sg";
	}else if ( host.indexOf('intranet-app-pre') > -1 ) {
		return "intranet-app-pre.hdb.gov.sg";
	}else if ( host.indexOf('intranet-app') > -1 ) {
		return "intranet-app.hdb.gov.sg";
	}else if ( host.indexOf('www.tcportal.sg') > -1 ) {
	    return "www.tcportal.sg";
	}else if ( host.indexOf('services2-pre.hdb.gov.sg') > -1 ) {
	    return "services2-pre.hdb.gov.sg";
	}else if ( host.indexOf('services2-preprod.hdb.gov.sg') > -1 ) {
	    return "services2-preprod.hdb.gov.sg";
	}else if ( host.indexOf('services2.hdb.gov.sg') > -1 ) {
	    return "services2.hdb.gov.sg";
	}else if ( host.indexOf('services20-pre.hdb.gov.sg') > -1 ) {
	    return "services20-pre.hdb.gov.sg";
	}else if ( host.indexOf('services20.hdb.gov.sg') > -1 ) {
	    return "services20.hdb.gov.sg";
	}else if ( host.indexOf('services3.hdb.gov.sg') > -1 ) {
	    return "services3.hdb.gov.sg";
	}else if ( host.indexOf('services3-pre.hdb.gov.sg') > -1 ) {
	    return "services3-pre.hdb.gov.sg";
	}else if ( host.indexOf('services3-preprod.hdb.gov.sg') > -1 ) {
	    return "services3-preprod.hdb.gov.sg";
	}else if ( host.indexOf('share.hdb.gov.sg') > -1 ) {
	    return "share.hdb.gov.sg";
	} else if ( host.indexOf('www20-pre.') > -1 ) {
		return "www20-pre.hdb.gov.sg";
	} else {
	    if(host.indexOf('.nsf') > -1){	    			
	          return ( host.indexOf('www.') > -1 ? "www.hdb.gov.sg" : "www20.hdb.gov.sg" );	          
	    }else{
	          return "services2.hdb.gov.sg";
	    }
	}   
     
}

function getICPSHost(){
  
  var host = location.host.toLowerCase(); 
 
     if ( host.indexOf('services2-pre.hdb.gov.sg') > -1 ) {
	    return "services3-pre.hdb.gov.sg";
	}else if ( host.indexOf('services2-preprod.hdb.gov.sg') > -1 ) {
	    return "services3-preprod.hdb.gov.sg";
	}else if ( host.indexOf('services2.hdb.gov.sg') > -1 ) {
	    return "services3.hdb.gov.sg";
	}else if ( host.indexOf('services3.hdb.gov.sg') > -1 ) {
	    return "services3.hdb.gov.sg";	    
	}else {
	    return "services3.hdb.gov.sg";
	}  
}

function getOptICPSHost(){
  
  var host = location.host.toLowerCase(); 
  
     if ( host.indexOf('services3-pre.hdb.gov.sg') > -1 ) {
	    return "services2-pre.hdb.gov.sg";
	}else if ( host.indexOf('services3-preprod.hdb.gov.sg') > -1 ) {
	    return "services2-preprod.hdb.gov.sg";
	}else if ( host.indexOf('services3.hdb.gov.sg') > -1 || host.indexOf('www.hdb.gov.sg') > -1 || host.indexOf('www20.hdb.gov.sg') > -1) {
	    return "services2.hdb.gov.sg";
	}else {
	    return "services2.hdb.gov.sg";
	}  
}



function writeHead(){
var h = h_config.rschost;
var markup = [
'	<meta charset="utf-8">',
'	<meta http-equiv="X-UA-Compatible" content="IE=edge">',
'	<meta name="format-detection" content="telephone=no">',
'	<meta name="description" content="HDB InfoWEB">',
'	<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=2.0, user-scalable=yes">',
'	',
'	<!-- Place favicon.ico and apple-touch-icon.png in the root directory -->',
'	',
'	<link rel="icon" href="/favicon.ico">',
'	<!--[if IE]><link rel="shortcut icon" href="/favicon.ico"/><![endif]-->',
'	<link rel="stylesheet" href="' + h + '/css/fancybox/jquery.fancybox.css">',
'	<link rel="stylesheet" href="' + h + '/css/normalize.css">',
'	<link rel="stylesheet" href="' + h + '/css/foundation.min.css">',
'	<link rel="stylesheet" href="' + h + '/css/idangerous.swiper.css">',
'	<link rel="stylesheet" href="' + h + '/css/pikaday.css">',
'	<link rel="stylesheet" href="' + h + '/css/main.css">',
'	<link rel="stylesheet" href="' + h + '/css/i3.css">',
'	<link rel="stylesheet" href="' + h + '/css/datepicker.css">',
'	',
'	<script src="' + h + '/js/vendor/modernizr-2.8.0.min.js"></script>',
'	',
'	<link href="//fonts.googleapis.com/css?family=Cabin:400,600,700,400italic,600italic,700italic" rel="stylesheet" type="text/css">',
'	',
'	<!--[if IE]>',
'	    <link rel="stylesheet" type="text/css" href="' + h + '/css/ie.css" />',
'	<![endif]-->',
'	',
'	<!--[if lt IE 9]>',
'	  <script src="' + h + '/js/vendor/respond.min.js"></script>',
'	<![endif]-->'
];

document.write(markup.join(""));
}
init_h_config();
writeHead();