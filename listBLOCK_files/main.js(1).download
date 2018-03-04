/**
 *  RR UTILS - Set cookie for alert bar
 */
var rr = (function(parent, $) {
    var $header = $('.header'),
        $alert_bar = $('.alert-bar', $header),
        $alert_toggle = $('.js-toggle-alert-bar', $header),
        $mobile_search = $('.mobile-site-search-form');

    var get_cookie = function (sKey) {
        if (!sKey) { return null; }
        //return decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*" + encodeURIComponent(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=\\s*([^;]*).*$)|^.*$"), "$1")) || null;
        return $.cookie(sKey);
    }

    var set_cookie = function (cname, cvalue, exdays) {
        var d = new Date();
        d.setTime(d.getTime() + (exdays*24*60*60*1000));
        var expires = "expires="+d.toUTCString();   
        $.cookie(cname, cvalue, { expires: d, path: "/", domain: location.host.slice(location.host.indexOf(".")) });		
    }
        
    parent.fill_alerts = function(data) {
    	var newflag = false;
    	
      if (!data || !data.length) {
    		
    		return;
    	} else {
    		$alert_toggle.parent().animate({width:'toggle'}, 350);
    	}
    	    	
    	for(i in data) { //loop for all msgs ignoring type for now    	              		 
    	  var info = data[i];    		
    	  if(get_cookie("info-msg-" + info.id)!= 'true' ) {
	    		newflag = true;
	    		set_cookie("info-msg-" + info.id,'true',7); 
    	  }    	  
    	  add_alert(info, i);    	  
    	}
    	
    	    	
    	if( newflag ) {
    		$alert_toggle.parent().addClass('active');
        $alert_bar.slideDown();
    	}                
    	                 
    } // end fill_alerts
    
    var add_alert = function(info, index) {
    	var tpl = [
'                        <div class="wrapper">',
'                            <h2 class="alert-bar-title"><span class="icon icon-warning"></span> {TYPE}</h2>',
'                            <p class="alert-bar-text">{MESSAGE}</p>',
'{CLOSE}',
'                        </div>'
    	           ]
    	           
    	var tpl_close = [
'                            <a href="#" class="alert-bar-close js-alert-bar-close">',
'                                <span class="icon icon-cross"></span>',
'                                <span class="visuallyhidden">Close alert bar</span>',
'                            </a>'    	                 
    	                 ]
    	                 
    	var html = tpl.join('');
	    html = html.replace('{MESSAGE}', info.msg);
	    html = html.replace('{TYPE}', info.type);
    	html = html.replace('{CLOSE}', (index>0?'':tpl_close.join('')));
    	
    	$alert_bar.append(html);
    	
    }
    
    
    var setup = function(){  
    	
    		    	
    	
        $('.header .js-toggle-alert-bar').click(function(e){        
            e.preventDefault();
            $mobile_search.hide();
            
            $parent = $(this).parent();
            if($alert_bar.is(':visible')){          
                $alert_bar.slideUp(function(){
                    $parent.removeClass('active');  
                });         
            }else{
                $alert_bar.slideDown();
                $parent.addClass('active');
            }
        });

        $('.alert-bar').on('click', '.js-alert-bar-close', function(e){
          e.preventDefault();
          if($alert_bar.is(':visible')){
              $alert_bar.slideUp(function(){
                  $('.alert.active').removeClass('active');   
              }); 
          }
      });
        
      	var u = h_config.eserhost;
      	
      	$.ajax({
              url: u + "/fi10/fi10301p.nsf/(SiteNotes)?Open",
              type: "GET",
              data: { callback :"rr.fill_alerts"},
              dataType: "jsonp",
              jsonpCallback: "rr.fill_alerts",
              cache: false
          });  
        
    };


    /**
     * Export module method
     */
    parent.alertBar = {
        setup: setup
    };

    return parent;

}(rr || {}, jQuery));

jQuery(function($){
  rr.alertBar.setup();
});

   // e-Service Common function      	
   //   $(function(){$(document).foundation();})

      //function to test mobile devices 
      ;function isMobile(){ var a = navigator.userAgent||navigator.vendor||window.opera; return(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(a)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(a.substr(0,4)))}

      function doGoogleSearch(site){
      	   
        if($.trim($("#inputSearch").val())=="") { $("#inputSearch").trigger('blur'); return false; }
         
      	$("#gceq").val($("#inputSearch").val())	;
      	$("form[name=SearchPlugInfrm]").submit();
      }
      	
      function initGoogleCSE(googlecx){
      	
      		$(".header .js-input-search, .nav-bar .js-input-search").unbind('keypress').keypress(function (e) {
      			if (e.which == 13) {
      				doGoogleSearch();
      				e.preventDefault();
      				return false;
      			} 
      		}); 

      		$(".header .js-input-search, .nav-bar .js-input-search").off('keyup paste').on('keyup paste', function(){
      			var $this = $(this);
      			var elems = $(".header .js-input-search, .nav-bar .js-input-search").not($this);      			
      			elems.val($this.val());      			
      		})	

      	var $clear_search = $('.header .js-clear-search, .nav-bar .js-clear-search');
      	
      	$clear_search.click(function(e){
            e.preventDefault();
            
            $clear_search.each(function(){
            	 var $this = $(this),
               $input_search = $this.parent().find('.js-input-search');
            	 $input_search.val('');
            	 $this.hide();            	
            });
        });
      		
     		

      	if(typeof(googlecx)=="undefined") {
      		googlecx = "001280152692293166068:bnfb9e030fm"; //HDB Default account
      	}

      	//add google form using jquery

      	var form = $("<form/>")
      	form.attr( {name:"SearchPlugInfrm",
      	//action:"http://www.google.com/cse",
      	//action:"http://www.hdb.gov.sg/cs/infoweb/search-result",  
    	action:"//services2.hdb.gov.sg/web/fi10/search/search-result.html",  
      	target:"_blank",
      	style:"display:none"});

      	var input_q = $("<input type='hidden' name='q' id='gceq' />")
      	var input_cx = $('<input type="hidden" name="cx" value="' + googlecx + '" />');
      	var input_ie = $('<input type="hidden" name="ie" value="UTF-8" />');


      	form.append(input_q).append(input_cx).append(input_ie);

      	$("body").append(form);

      	//init click on search button
      	$(".site-search-btn").click(function(e){
      		e.stopPropagation();
      		e.preventDefault();
      		doGoogleSearch();      		
      	});
         
      }

      $(function(){initGoogleCSE(); });//add to ready queue
      $(function(){ $(document).on('click', '.disabled', function(e){ e.preventDefault(); })});
      
      
      
      function initCheckableUI(){
			
    		var tags = $("form.custom-1 [type=radio], form.custom-1 [type=checkbox]").not('.no-custom')
    				
    		tags.bind("change.ui", function(){
    				var el = $(this);
    		
    				if(_global_validator==null) return false;
    						
    				if (!_global_validator.element(el)) {
    					$(this).closest(".app-group-elements").addClass("error");
    				} else {
    					$(this).closest(".app-group-elements").removeClass("error");
    				}
    						
    		})			
 			
    	}

 
    	$(function(){ initCheckableUI(); })
    	;$(function(){ initExpandables(); })
    	;function initExpandables() {
    					
    					$(".expandable-container .title-box a").click(function(){
    						var $el = $(this)
    						var $box = $el.closest(".expandable-container")
    						var state = $box.hasClass("expanded");
    						var content = $box.find(".content");
    						if(state) {
    							content.slideUp()
    							$box.removeClass("expanded");
    						} else {
    							content.slideDown()
    							$box.addClass("expanded");
    						}					
    						
    						return false;
    					});
    					$(".expandable-container").removeClass("expanded")
    				}
    	
    	// print button function	  

function showHideSavePdfBtn(id,grid_large_num,grid_small_num,grid_medium_num){	

var gridlarge  = (typeof(grid_large_num )== 'undefined'? "": grid_large_num);
var gridsmall  = (typeof(grid_small_num )== 'undefined'? "": grid_small_num);
var gridmedium = (typeof(grid_medium_num)== 'undefined'? "": grid_medium_num);

var gridval ="";

gridlarge = (gridlarge==""?"":" large-" + gridlarge);
gridsmall = (gridsmall==""?"":" small-" + gridsmall);
gridmedium= (gridmedium==""?"":" medium-" + gridmedium);

gridval = gridlarge + gridmedium + gridsmall ;

var PrintButton =
		'<div class="'+gridval+' columns"> '+
		   '<input type="button" class="button expand radius secondary" name="Print" value="Print" onClick="printPage()">'+
		'</div>'+
		'<input type="hidden" id="hidPrintContent" name="hidPrintContent" /> '+
		'<input type="hidden" id="hidReferer" name="hidReferer" />' +
		'<input type="hidden" id="hidCustomPrefix" name="hidCustomPrefix" value="1" />'	;
		
		if(!isMobile()) $('#'+id).append(PrintButton);  

}
    	
    		//end print button function

//start hide print button in mobile

if(isMobile())
{
$('.printBtn').hide();
}

// end hide print button in mobile
    		//Start of Side NAV
    		function initSidenav() {
    			
    			
    			
    			//add accordion like effect
    			var ols = $(".side-nav > .subheader");
    			var olis= $(".side-nav > li");
    			var oactive = $(".side-nav > .subheader.open");
    			oactive = oactive.eq(0);

    			$('.side-nav .subheader ul').slideUp();	
    			
    			$('.side-nav .subheader .icon')
    				.addClass('icon-chevron-down')
    				.removeClass('fa-chevron-right');

    			ols.unbind('click.sidenav').bind('click.sidenav',function() {
    				var thisols = ols;
    				var self = $(this);

    				var tmpols = thisols.not(self);

    				var selful = $('> ul', self);


    				//$('> ul', tmpols).slideUp();
    				var icon = self.find('.icon');
    				if (self.hasClass('open')) {
    					selful.slideUp();
    					icon.animateRotate(180,0);
    					self.removeClass('open');
    				} else {
    					selful.slideDown();
    					icon.animateRotate(0,180);
    					self.addClass('open');
    				}
    				

   			


    				return false;

    				});
    			oactive.removeClass('open');	
    			oactive.click();
    			oactive.removeClass('initopen');

    			//handle event propagation of inner lis of subheader
    			var iols = $('> ul', ols);

    			iols.unbind('click.sidenav').bind('click.sidenav', function(e){
    				e.stopPropagation();
    			})


    			//add onchange event on the select element
    			$('.sidenavselect').unbind('change.sidenav').bind('change.sidenav', function(){
    				location = $(this).val();
    			})

    			
    		}
    		//end of Side NAV
    	
    		//IOS6 bug fix
	
	

function fixIOS6PlaceHolderBug() {
	var $this, originalPlaceholder =  "";
	
	$(document).find("input[placeholder]").each( function(){
		$this = $(this);
		originalPlaceholder = $this.attr('placeholder');
		$this.removeAttr('placeholder')
		.attr("placehoder", originalPlaceholder);
	});
	
}

$(function(){
	$(window).on("orientationchange", fixIOS6PlaceHolderBug);
})

//end of iOS6 bug fix
    		
// Start of print function

function printPage(){
	var printWidth = 800;
	var h = h_config.rschost,		
	e = h_config.logserver;
	
	var winOptions 	= 'toolbar=no, directories=no,' 
						+ 'location=no,status=yes, menubar=yes,'
						+ 'resizable=yes, scrollbars=yes,'
						+ 'width=830, height=500';
	var prin		= window.open('','_blank',winOptions);
	
	var esvccss1 	= h + "/css/foundation.min.css",
		esvccss2 	= h + "/css/main.css",
		esvccss3 	= h + "/css/i3.css",
		esvccss4 	= h + "/css/i3-print-grid.css",

		mapcss1 	=  e + "/web/ej03/arcgis/jsapi/3.12/dijit/themes/tundra/tundra.css",
		mapcss2		=  e + "/web/ej03/arcgis/jsapi/3.12/esri/dijit/css/InfoWindow.css",
		mapcss3		=  e + "/web/ej03/arcgis/jsapi/3.12/esri/css/jsapi.css";
	    mapcss4     =  e + "/web/ej03/arcgis/jsapi/3.12/esri/css/esri.css";                                                              
		
	var temp 		= "" + 
	"<link rel='stylesheet' href='"+esvccss1+"' type='text/css'>\n" +
  "<link rel='stylesheet' href='" + esvccss2 + "' type='text/css'>\n" +
  "<link rel='stylesheet' href='" + esvccss3 + "' type='text/css'>\n" +
  "<link rel='stylesheet' href='" + esvccss4 + "' type='text/css'>\n" +
	"<link rel='stylesheet' href='" + mapcss1 + "' type='text/css'>\n" +
	"<link rel='stylesheet' href='" + mapcss2 + "' type='text/css'>\n" +
	                "<link rel='stylesheet' href='" + mapcss3 + "' type='text/css'>\n" +
                "<link rel='stylesheet' href='" + mapcss4 + "' type='text/css'>\n";             

	
	var temp1 		="<style media='print'>.printHidden { display:none; }</style>";
	
	var hdbcorpimg = h + "/images/hdbcorp.png";
  
	var strHTML 	= '<div class="row"><div class="small-12 columns">'
						+ '<IMG border="0" src="'+hdbcorpimg+'" width="192" '
						+ 'height="50"><br><br>'
						+ '<a href="#" onclick="window.print();return false;" class="hide-for-print" >'
						+ 'Print This Page</a></div></div>';
	
	var strHTML = [];
	
	
	strHTML.push("<!DOCTYPE html>\n");
	strHTML.push("<html>\n");
	strHTML.push("<head><meta http-equiv=\"X-UA-Compatible\" content=\"IE=Edge\" />\n");
	strHTML.push("<title>E-Services Printer Friendly page</title>\n")
	strHTML.push(temp + "\n");
	strHTML.push(temp1 + "\n");
	strHTML.push("</head>\n");	
	strHTML.push("<body>\n");
	strHTML.push("<div class=\"row\"><div class=\"small-12 columns\">\n");
	strHTML.push("<IMG border=\"0\" src=\"" + hdbcorpimg + "\" width=\"192\" height=\"50\"><br><br>\n");
	strHTML.push("<a href=\"#\" onclick=\"window.print();return false;\" class=\"hide-for-print\" >Print This Page</a>\n");
	strHTML.push("</div>\n</div>\n");	
	strHTML.push("<div style=\"text-align:left;width:800px\" >\n");
	$('#printPDFHeader script').remove();
                if ($("#printPDFHeader").html() != null )
                {
                               strHTML.push($("#printPDFHeader").html());
                }
	$('#print script').remove();
	strHTML.push($("#print").html());
	 $('#printPDFFooter script').remove();
      if ($("#printPDFFooter").html() != null )
                {
                  strHTML.push($("#printPDFFooter").html());
                } 
	strHTML.push("</div>\n");
	strHTML.push("</body></html>\n");
		
	
	prin.document.write(strHTML.join(""));


	prin.document.close();
}

// end of print function


$(function(){
	//initialise warning message
	
	var u = h_config.eserhost;

 
	//load Help, T&C
	initServiceLinks($);
	

	//jsLogging();
  commonLogging();
	LastUsedEservices();
	
})

//common logging for webSphere
function jsLogging(){
		
		var h = h_config.logserver
		if (undefined == h) {
			h = location.host
		}
		var u = location.protocol + "//" + h + "/" + "webapp/FI10AWCOMMON/FI10SAjaxHandlerNP";
		
		if(h_config.showlogout) {
	    u = location.protocol + "//" + h + "/" + "webapp/FI10AWCOMMON/FI10SAjaxHandlerP";	
		}  
    
		
		$.ajax({
	        url: u,
	        type: "POST",
	        data: { title: document.title, url: location.href, esvcid: h_config.eserviceid, callback :"swallowLog"},
	        dataType: "jsonp",
	        jsonpCallback: "swallowLog",
	        timeout : 2000,
	        error:function(){/*user not login,swallow error*/}	
	    });
				
		
	return false;
}

function swallowLog() {/* do nothing */}

//format date JS
function formatDate(fld) { //argument can be native dom or jquery object
	var value= "";
	var padZero = function(num) { return ( "0" + num ).slice(-2); };

	if (typeof(fld) == "string") { 
		value = fld
	} else if (typeof(fld) == "object") { //hoping to be input type
		value = $(fld).val()
	} else { // other types
		value = ""
	}	
	//match yyyy-mm-dd
	var temp = value.match(/^[0-9]{4}-(((0[13578]|(10|12))-(0[1-9]|[1-2][0-9]|3[0-1]))|(02-(0[1-9]|[1-2][0-9]))|((0[469]|11)-(0[1-9]|[1-2][0-9]|30)))$/);
	if (temp != null && typeof(temp[0]) != "undefined") {
	var newdate = new Date(value);
	//return padZero(newdate.getDate()) + "/" + padZero((newdate.getMonth() + 1)) + "/" + newdate.getFullYear();	
	return newdate.getFullYear() + "-" + padZero((newdate.getMonth() + 1)) + "-" +  padZero(newdate.getDate());
	}
	//match dd mmm yyyy and translate to yyyy-mm-dd
	temp = value.match(/(([0-9])|([0-2][0-9])|([3][0-1])) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}/)
	if (temp != null && typeof(temp[0]) != "undefined") {
	var newdate = new Date(value);
	return newdate.getFullYear() + "-" + padZero((newdate.getMonth() + 1)) + "-" +  padZero(newdate.getDate());
	}
	
	//match dd/mm/yyyy and translate to yyyy-mm-dd 'android default browser
	temp = value.match(/^(?:(?:31(\/)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$/)
	if (temp != null && typeof(temp[0]) != "undefined") {		
	var newdate = value.split("/");
	return padZero(newdate[2]) + "-" + padZero(newdate[1]) + "-" + padZero(newdate[0]);
	}
	
	
	//return null if does not match with the expected formats yyyy-mm-dd or dd mmm yyyy 
	return null;
}
// End of Date format


//get help and t & c
var initServiceLinks = function($){
	var u = h_config.eserhost + '/fi10/fi10200p.nsf/(jsonpeserhandler)?Open&key=' + h_config.eserviceid;
			
	//var $ = window.jQuery	;
	$.ajax({
        url: u,
        type: "POST",
        data: { key: h_config.eserviceid, callback :"setEserLinks"},
        dataType: "jsonp",
        jsonpCallback: "setEserLinks",
        error:function(e){}	
    });
	
}

var setEserLinks = function(data) {
	var highlightSubHeaderLink  = function(data) {
	var url = 'FI10PPORTAL/FI10PAtAGlance.jsp';
	var title = 'My HDBPage';
	if (data.mybusiness) {
	url = "FI10AWBIZ/FI10PBizOverview.jsp"
	title = "My Business" 
	}
	var html = [
	'                                    <a href="'+h_config.esvcUrl+'/webapp/' + url + '" class="account-link">',
	'                                        <span class="account-text">' + title + '</span>',
	'                                    </a>'
	           ]
	           
	           
	$btn = $(html.join(""));
	$btn.addClass('highlight'); 
	$header = $(".title-section .e-subheader");
	$header.prepend($btn);            
	}
	if (data.mybusiness || data.myhdbpage) {
	highlightSubHeaderLink(data);
	}
	if( h_config.noeservicelinks ) {
	$(".footer-eservice-links").parent().remove();
	return;
	} 
	var h = h_config.eserhost; 
	var foot_ul = $(".footer-eservice-links ul");
	if ( !h_config.staticpage )  {
	foot_ul.addClass("top"); 
	}
	var help_tpl = [
	              ' <li class="first"><a class="cta dark" href="{help_url}" target="_blank">',
	              '<span class="icon icon-help"></span>',
	              'Get Help</a> </li>'
	            ].join("");
	             
	var tc_tpl = [
	            ' <li><a href="{tc_url}" class="cta dark" target="_blank">',
	            '<span class="icon icon-file"></span>',
	            'Terms & Conditions</a> </li>'
	           ].join(""); 
	var fdback_tpl = [
	            ' <li><a href="{fdback_url}" class="cta dark" target="_blank">',
	            '<span class="icon icon-feedback"></span>',
	            'Feedback</a> </li>'
	                 ].join("");
	var rate_url = "/fi10/fi10400p.nsf/FI10FHDBService/?OpenForm&feature=eservice&EServiceID={eserviceid}";
	var rate_tpl = [
	          ' <li><a href="' + h + rate_url + '" class="cta dark new-win-desktop" target="' + (isMobile()?'':'_blank') + '">',
	          '<span class="icon icon-star"></span>',
	          'Rate this Service</a> </li>'                
	               ].join("");

	var markup = [];

	if ("" != data.tcurl) { //push tcurl first, order of code matters
	markup.push( tc_tpl.replace("{tc_url}", data.tcurl) ); 
	}
	if (h_config.service_link_show_help) {
	if ("" != data.helpurl) {
	markup.push( help_tpl.replace("{help_url}", data.helpurl) );
	} 
	}
	var fd_host = h_config.logserver;
	var pageurl = encodeURIComponent(location.href);
	var fd_url = fd_host + "/webapp/BE05Feedback/BE05SFrontController?service=ServiceFeedback&operation=createFeedback&FB_Subject=E-Service&FB_EServiceID="
	+  h_config.eserviceid + "&FB_EServiceURL=" + pageurl
	if (!h_config.service_link_use_site_feedback) {
	fd_url = h_config.eserhost + "/fi10/fi10400p.nsf/FI10FHDBService/?OpenForm&feature=feedback";
	}
	if (h_config.service_link_show_feedback) {
	markup.push( fdback_tpl.replace("{fdback_url}", fd_url ) );
	}
	if (h_config.showrateservice) {
	markup.push( rate_tpl.replace("{eserviceid}", h_config.eserviceid ) );
	}
	foot_ul.prepend(markup.join(""));
	}

//end get help and t & c


var cookieAtid1      = "atid";
var cookieAccess1   = "AccessType";
//common logging for webSphere
function commonLogging(){
		var h = h_config.logserver
           var u ;
		if (undefined == h) {
			h = location.host
		}             

 		if(h_config.showlogout || h_config.eservicelist)
		    u =  h + "/" + "webapp/FI10AWCOMMON/FI10SAjaxHandlerP";	
           else
	         u =  h + "/" + "webapp/FI10AWCOMMON/FI10SAjaxHandlerNP";
		$.ajax({
	        url: u,
	        type: "POST",
	        data: { title: document.title, url: location.href, esvcid: h_config.eserviceid, callback :"swallowLog"},
	        dataType: "jsonp",
	        jsonpCallback: "swallowLog",
			timeout : 3000,
	        error:function(){/*user not login,swallow error*/}	
	    });
				
		
	return false;
}

//common logging for rate-of-eservices
function LastUsedEservices(){
		var h = h_config.logserver
           var u ;
		if (undefined == h) {
			h = location.host
		}    
//If customer is logged in && eserviceid is not null && Rate this e-Service is true {	
    // var cookieLTPA = "";
                        
    if( cookieCheckInSession() && (h_config.eserviceid != null && h_config.eserviceid != "")&& h_config.showrateservice){
       if(h_config.eserviceid!="P000001"){    	
 		if(h_config.showlogout)
			   u =   h + "/" + "webapp/FI10AWCOMMON/FI10SRateOfEservicesP";	
			   else
				 u =  h + "/" + "webapp/FI10AWCOMMON/FI10SRateOfEservicesNP";
			$.ajax({
				url: u,
				type: "POST",
				data: { title: document.title, url: location.href, esvcid: h_config.eserviceid, callback :"swallowLog"},
				dataType: "jsonp",
				jsonpCallback: "swallowLog",
				timeout : 3000,
				error:function(){/*user not login,swallow error*/}	
			});
				
		}
    }
	return false;
}
function cookieCheckInSession() {
	if (allGetCookie(cookieAtid1) == null) return false;
	if (allGetCookie(cookieAccess1) != null) return false;
	
	return true;
}

function allGetCookie(cookieName) {
	var cookies = document.cookie;
	if (cookies == null) return null;
	
	var cookieNameEQ = cookieName + "=";
	var cookieStart = cookies.indexOf(cookieNameEQ);
	if (cookieStart < 0) return null;
	
	cookieStart += cookieNameEQ.length;
	var cookieEnd = cookies.indexOf(";", cookieStart);
	if (cookieEnd < 0) cookieEnd = cookies.length;
	
	var val = cookies.substring(cookieStart, cookieEnd);
	if (val == "") val = null;
	
	return val;
}

/* JQUERY URL PLUGIN */
/*! url - v1.8.6 - 2013-11-22 */window.url=function(){function a(a){return!isNaN(parseFloat(a))&&isFinite(a)}return function(b,c){var d=c||window.location.toString();if(!b)return d;b=b.toString(),"//"===d.substring(0,2)?d="http:"+d:1===d.split("://").length&&(d="http://"+d),c=d.split("/");var e={auth:""},f=c[2].split("@");1===f.length?f=f[0].split(":"):(e.auth=f[0],f=f[1].split(":")),e.protocol=c[0],e.hostname=f[0],e.port=f[1]||("https"===e.protocol.split(":")[0].toLowerCase()?"443":"80"),e.pathname=(c.length>3?"/":"")+c.slice(3,c.length).join("/").split("?")[0].split("#")[0];var g=e.pathname;"/"===g.charAt(g.length-1)&&(g=g.substring(0,g.length-1));var h=e.hostname,i=h.split("."),j=g.split("/");if("hostname"===b)return h;if("domain"===b)return/^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/.test(h)?h:i.slice(-2).join(".");if("sub"===b)return i.slice(0,i.length-2).join(".");if("port"===b)return e.port;if("protocol"===b)return e.protocol.split(":")[0];if("auth"===b)return e.auth;if("user"===b)return e.auth.split(":")[0];if("pass"===b)return e.auth.split(":")[1]||"";if("path"===b)return e.pathname;if("."===b.charAt(0)){if(b=b.substring(1),a(b))return b=parseInt(b,10),i[0>b?i.length+b:b-1]||""}else{if(a(b))return b=parseInt(b,10),j[0>b?j.length+b:b]||"";if("file"===b)return j.slice(-1)[0];if("filename"===b)return j.slice(-1)[0].split(".")[0];if("fileext"===b)return j.slice(-1)[0].split(".")[1]||"";if("?"===b.charAt(0)||"#"===b.charAt(0)){var k=d,l=null;if("?"===b.charAt(0)?k=(k.split("?")[1]||"").split("#")[0]:"#"===b.charAt(0)&&(k=k.split("#")[1]||""),!b.charAt(1))return k;b=b.substring(1),k=k.split("&");for(var m=0,n=k.length;n>m;m++)if(l=k[m].split("="),l[0]===b)return l[1]||"";return null}}return""}}(),"undefined"!=typeof jQuery&&jQuery.extend({url:function(a,b){return window.url(a,b)}});

/* ANCHOR SETUP */
var rr = (function(parent, $) {

	var setup = function() {
		var anchor = $.url("?anchor");
		
		if (anchor != null) {
			var $anchor = $("#" + anchor );
			var $accordion = $anchor.closest(".accordion-navigation")
			
			if (!$accordion.hasClass("active")) {
				$(".accordion-navigation-link", $accordion).click();
			}
			
			$('html, body').stop().animate({
        'scrollTop':   $anchor.offset().top
     }, 700);
			
			
		}
	}

	/** Export module method  */
	    parent.anchor = {
	        setup: setup
	    };

	return parent;
	    
	}(rr || {}, jQuery));

	jQuery(function($){
	  rr.anchor.setup();
	});

	//init login button
$(function(){
 
var show = function(){
   var $this = $(this);
   $this.addClass('account-link-tapped')
     
        .find('.account-login-box')
        .stop().show();
}
 
var hide = function(){
   var $this = $(this);
   if ($this.hasClass('active')) return;
   $this.removeClass('account-link-tapped')
     
        .find('.account-login-box')
        .stop().hide();
}
 
 
$('.nav-bar .account')
.click(function(e){
var $this = $(this);
$this.toggleClass('account-link-tapped');
if (!$this.hasClass('active')) {
$this.addClass('active');
show.call($this)
} else {
$this.removeClass('active');
hide.call($this)
}
 
}).hoverIntent({
   over: show,
   out: hide,
   timeout: 300 
});
})

$(function(){
 
$("div.preview-panel.e-Services").parent().css("padding-bottom","6.5%");
})