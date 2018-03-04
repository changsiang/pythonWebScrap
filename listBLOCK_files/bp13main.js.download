/**
 * 
 */

function openmypagenew2(pg,windowResize,windowWidth,windowHeight){
	var foc;
	//var server = "http://his77b.hdb.gov.sg";
	var server = getResourceServer(window.location.hostname);
	//var page = server + pg;
	var page = server + pg;
	foc = window.open(page, "openmypage", "toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=" + windowResize + ",width=" + windowWidth + ",height=" + windowHeight + ",top=50,left=50"); 
	if(foc!=null){
		foc.focus(); 
	}
}

function openmypage(pg,windowResize,windowWidth,windowHeight){
	//var dteBallot = pg.substr(pg.indexOf("dteBallot=")+10, 6);
	
	//if(dteBallot=="201502") {
	if(pg.indexOf("BP13PFlatSearch.jsp") != -1) {
		var foc;
		var page;
		page = "http://"+window.location.hostname+ pg;	
		foc = window.open(page, "openmypage1", "toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=1,width=480,height=590,top=5,left=5"); 
		if(foc!=null){
			foc.focus(); 
		}
	} else {
		//var foc;
		var page;
		page = "http://"+window.location.hostname+ pg;	
		//window.location.href = page;
		window.open(page,"_self");
		//foc = window.open(page, "openmypage1", "toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=1,width=505,height=590,top=5,left=5"); 
		/*foc = window.open(page, "openmypage1", "toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=1,width=1030,height=720,top=5,left=5");
		if(foc!=null){
			foc.focus(); 
		}*/
		//window.location.href=pg;
	}
}


function doSubmit(town,flat) { //sel=SER	//(20070906-LCJ2) sel=BE //(20071004-LCJ2) sel=BE (link to brochure)
	//alert("town=="+town+ "===flat==="+flat);
	document.forms[0].new_town.value = town;
	document.forms[0].flat_type.value = flat;
	document.forms[0].ethnicA.value = 'Y';
	document.forms[0].ethnicC.value = 'N';
	document.forms[0].ethnicM.value = 'N';
	document.forms[0].ethnicO.value = 'N';
	document.forms[0].numSPR.value = 'N';
	
	document.forms[0].action="BP13ESSBULIST_SER";
	document.forms[0].method="post";
	document.forms[0].target="_self";
	document.forms[0].submit();
}

function doSubmitBTO(town,flat) { //(20070906-LCJ2) sel=BTO, town=Punggol //(20071029-LCJ2) link to brochure
    document.forms[0].new_town.value = town;
	document.forms[0].flat_type.value = flat;
	document.forms[0].ethnicA.value = 'Y';
	document.forms[0].ethnicC.value = 'N';
	document.forms[0].ethnicM.value = 'N';
	document.forms[0].ethnicO.value = 'N';
	document.forms[0].numSPR.value = 'N';
	
	document.forms[0].action="BP13ESSBULIST_BTO";
	document.forms[0].method="post";
	document.forms[0].target="_self";
	document.forms[0].submit();
}

function getResourceServer(server) {
	var resourceServer ="";

	if	(server == "his62.hdb.gov.sg" || server == "hist2a.hdb.gov.sg" || server == "intranet-appd.hdb.gov.sg"){
		resourceServer="http://his77b.hdb.gov.sg"; 
	}
	else if	(server == "his64.hdb.gov.sg" || server == "hiss2a.hdb.gov.sg" || server == "intranet-apps.hdb.gov.sg")	{
		resourceServer="http://his77b.hdb.gov.sg"; 
	}
	else if	(server == "uat2.hdb.gov.sg" ||	server == "uat2a.hdb.gov.sg" ||	server == "intranet-appu.hdb.gov.sg") {
		resourceServer="http://his77b.hdb.gov.sg"; 
	}
	else if	(server == "intranet2.hdb.gov.sg" || server == "intranet-app.hdb.gov.sg"  || server == "intranet-app-pre.hdb.gov.sg") {
		resourceServer="http://intranet.hdb.gov.sg"; 
	}
	else if	(server == "www4.nicehomes.com.sg" || server == "wwws1a.nicehomes.com.sg" || server == "services2s.nicehomes.com.sg") {
		resourceServer="http://wwwuat.nicehomes.com.sg"; 
	}
	else if	(server == "www6c.nicehomes.com.sg" || server == "services2.nicehomes.com.sg" || server == "services2u.nicehomes.com.sg") {
		resourceServer="http://wwwuat.nicehomes.com.sg"; 
	}
	else if	(server == "services.hdb.gov.sg" || server == "services2.hdb.gov.sg" || server == "services2-pre.hdb.gov.sg") {
		resourceServer="http://www.hdb.gov.sg"; 
	}
	else {
		resourceServer="http://his77b.hdb.gov.sg"; 
	}

	return resourceServer;
}

var isgtwn = refineTownName(getUrlParameters("Town", "", true));
var isgctr = getUrlParameters("Neighbourhood", "") + getUrlParameters("Contract", "");	
var isgblk = getUrlParameters("Block", "");
var flattype = refineFlatType(getUrlParameters("Flat", ""));
var ballot = getUrlParameters("dteBallot", "");

function refineTownName(givenParameter) {
	if(givenParameter != null && givenParameter.length > 0){
		givenParameter = givenParameter.replace("%20"," ").replace("%20"," ");
		if(givenParameter == "Kallang+/+Whampoa") {
		 givenParameter = givenParameter.replace("+","").replace("+","");	
		} else {
	     givenParameter = givenParameter.replace("+"," ").replace("+"," ");
		}
		
		if (givenParameter=="Ang Mo Kio") givenParameter = "AMK";
		if (givenParameter=="Bedok") givenParameter = "BD";
		if (givenParameter=="Bishan") givenParameter = "BH";
		if (givenParameter=="Bukit Batok") givenParameter = "BB";
		if (givenParameter=="Bukit Merah") givenParameter = "BM";
		if (givenParameter=="Bukit Panjang") givenParameter = "BP";
		if (givenParameter=="Bukit Timah") givenParameter = "BT";
		if (givenParameter=="Clementi") givenParameter = "CL";
		if (givenParameter=="Central") givenParameter = "CT";
		if (givenParameter=="Choa Chu Kang") givenParameter = "CCK";
		if (givenParameter=="Geylang") givenParameter = "GL";
		if (givenParameter=="Hougang") givenParameter = "HG";
		if (givenParameter=="Jurong East") givenParameter = "JE";
		if (givenParameter=="Jurong West") givenParameter = "JW";
		if (givenParameter=="Kallang/Whampoa") givenParameter = "KWN";
		if (givenParameter=="Marine Parade") givenParameter = "MP";
		if (givenParameter=="Pasir Ris") givenParameter = "PRC";
		if (givenParameter=="Punggol") givenParameter = "PG";
		if (givenParameter=="Queenstown") givenParameter = "QT";
		if (givenParameter=="Sembawang") givenParameter = "SB";
		if (givenParameter=="Serangoon") givenParameter = "SGN";
		if (givenParameter=="Sengkang") givenParameter = "SK";
		if (givenParameter=="Tampines") givenParameter = "TAP";
		if (givenParameter=="Toa Payoh") givenParameter = "TP";
		if (givenParameter=="Woodlands") givenParameter = "WL";
		if (givenParameter=="Yishun") givenParameter = "YS";
	}
    return givenParameter;
}

function refineFlatType(givenParameter) {
	if(givenParameter != null && givenParameter.length > 0){
		givenParameter=givenParameter.toUpperCase();
		givenParameter = cleanParameter(givenParameter);
		if (givenParameter=="1-ROOM") givenParameter = "1rm";
		if (givenParameter=="2-ROOM") givenParameter = "2rm";
		if (givenParameter=="3-ROOM") givenParameter = "3rm";
		if (givenParameter=="2-Room Flexi (Short Lease/99-Year Lease)" 
			|| givenParameter=="2-ROOM FLEXI (SHORT LEASE/99-YEAR LEASE)") givenParameter = "2rm";
		if (givenParameter=="3-ROOM (INCOME CEILING $6,000)" 
			|| givenParameter=="3-ROOM (INCOME CEILING $12,000)") givenParameter = "3rm";
		if (givenParameter=="4-ROOM" || givenParameter=="S1") givenParameter = "4rm";
		if (givenParameter=="5-ROOM" || givenParameter=="S2") givenParameter = "5rm";
		if (givenParameter=="5-ROOM/3GEN") givenParameter = "5rm";
		if (givenParameter=="EXECUTIVE") givenParameter = "EX";
		if (givenParameter=="STUDIO") givenParameter = "SA";
		
	}
    return givenParameter;
}
function cleanParameter(param) {
	param = param.replace("%28","(").replace("%2F","/").replace("%29",")").replace("%24","$").replace("%2C",",");
	param = param.replace("+"," ").replace("+"," ").replace("+"," ").replace("+"," ");
	return param;
}
function getUrlParameters(parameter,staticURL,decode) 
{
   /*
    Function: getUrlParameters
    Description: Get the value of URL parameters either from 
                 current URL or static URL
    Author: Tirumal
    URL: www.code-tricks.com
   */
   var currLocation = (staticURL.length)? staticURL : window.location.search,
       parArr = currLocation.split("?")[1].split("&"),
       returnBool = true;

   for(var i = 0; i < parArr.length; i++){
        parr = parArr[i].split("=");
        if(parr[0] == parameter){
            return (decode) ? decodeURIComponent(parr[1]) : parr[1];
            returnBool = true;
        }else{
            returnBool = false;            
        }
   }

   if(!returnBool) return false;  
}