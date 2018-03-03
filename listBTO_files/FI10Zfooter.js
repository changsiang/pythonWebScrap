
	var i3footer = (function(parent, $){
		var h = h_config.rschost;
		var wcmsUrl =h_config.wcmsUrl;
		var esvcUrl = h_config.esvcUrl;
		var config = {
			footer_links : [
					{ name: 'home', url:'/cs/infoweb/homepage', title: 'Home' },
					{ name: 'careers', url:'/cs/infoweb/about-us/careers', title: 'Careers' },
					{ name: 'mobile', url:'#', title: 'Mobile@HDB' },
					{ name: 'usefullink', url:'#', title: 'Useful Links' },
					{ name: 'contactus', url: '/cs/infoweb/contact-us', title: 'Contact Us' },
					{ name: 'termsofuse', url: '/cs/infoweb/terms-of-use', title: 'Terms of Use' },
					{ name: 'privacystatement', url: '/cs/infoweb/privacy-statement', title: 'Privacy Statement' },
					{ name: 'siterequirements', url:'/cs/infoweb/site-requirements', title: 'Site Requirements' },
					{ name: 'rateourwebsite', url: h + '/fi10/fi10400p.nsf/FI10FHDBService/?OpenForm', title: 'Rate Our Website' }
			],
			
			megafooterdata : i3header.nav_data ,
	    sitetoolsdata : {
				"FOOT_FAQ_URL" : "#",
				"FOOT_SUB_URL" : "#",
				"FB_URL": "#",
				"TWITTER_URL": "#",
				"YOUTUBE_URL": "#"
				}
		};
		
		var col_tpl = [
'        <li class="footer-nav-col">',
'            <a href="{URL}" class="footer-nav-link">',
'                {TITLE}',
'            </a>',
'            <ul class="footer-nav-sublist list">',
'{LIST}',
'            </ul>',
'        </li>'
		               ].join("\n");
		
		var item_tpl = [
'                <li class="footer-nav-item">',
'                    <a href="{URL}" class="footer-nav-link">{TITLE}</a>',
'                </li>'		                
		                ].join("\n");

		var nav_tpl = [
'<nav class="footer-nav small-12 large-9 columns" role="navigation">',
'    <ul class="footer-nav-list list small-block-grid-1 large-block-grid-5">',
'{LIST}',
'    </ul>',
'</nav>'
		               ].join("\n");
		
		var wcmsHost = wcmsUrl.replace("/cs/infoweb", "");
		
		var getNavHTML = function(data){
			
			var categories = [ /* categories to display */
			                   "about us", "residential", "community", "business", "car parks"
			                  ];
			
			
			if (!data.length || data[0] == "" ) { return ""; }
			var tmp_html = [];
			var i = 0;
			for(; i < data.length; i++) {
				var item = data[i],
					title = item.name;
				
				if ( categories.indexOf( title.toLowerCase() ) < 0  ) { continue; } 
				
				var tmp_tpl = col_tpl
					.replace("{TITLE}", title)
					.replace("{URL}", (item.url.indexOf("http")<0? (wcmsHost + item.url): item.url ) )
					.replace("{LIST}", getMenuHTML(item.items));					
				
					tmp_html.push(tmp_tpl);
			}			
			
			return nav_tpl.replace("{LIST}", tmp_html.join("\n"));
			
		}
		
		var getMenuHTML = function(items_data){
			if (!items_data || !items_data.length || items_data[0] == "" ) { return ""; }
			
			var temp_list = [];				
			var i = 0;
					
			for (; i < items_data.length; i++ ) {
				var item = items_data[i];
				if(!item) continue;
								
				var temp_item_tpl = item_tpl.replace("{TITLE}", item.name)
					.replace("{URL}", (item.url.indexOf("http")<0? (wcmsHost + item.url): item.url ) );					
				temp_list.push(temp_item_tpl);
			}
			
			return temp_list.join("\n");
			
		};
		
		
		
		var footerSite = [
'                        <div class="footer-site-tools small-12 large-3 columns clearfix">',
'                            <div class="faq">',

'                                <h2 class="footer-title"><a class="footer-title-link" href="http://askhdb.hdb.gov.sg/">FAQ</a></h2>',
'                                <a href="http://askhdb.hdb.gov.sg/" class="btn faq-btn">',
'                                    Ask Us a Question <span class="icon icon-chevron-right"></span>',
'                                </a>',
'                            </div>',
'                            <div class="subscribe">',
'                                <h2 class="footer-title"><a class="footer-title-link" href="'+esvcUrl+'/webapp/BF08CESS/Index.jsp">HDB eAlert Service</a></h2>',
'                                <a href="'+esvcUrl+'/webapp/BF08CESS/Index.jsp" class="btn subscribe-btn">',
'                                    New Subscription <span class="icon icon-chevron-right"></span>',
'                                </a>',
'                            </div>',

'                            <div class="mobile-app">',
'                                <a href="'+wcmsUrl+'/mobile-hdb" class="mobile-app-link">',
'                                    <img src="' + h + '/images/content/hdb_mobile.jpg" alt="Mobile@HDB" class="img">',
'                                </a>',
'                            </div>',

'                            <div class="footer-social-channels">',
'                                <span class="footer-social-channels-text">Follow us</span>',
'                                <a href="https://www.facebook.com/SingaporeHDB" class="social-channel fb">',
'                                    <span class="visuallyhidden">Facebook</span>',
'                                    <span class="icon icon-facebook"></span>',
'                                </a>',
'                                <a href="https://twitter.com/singapore_hdb" class="social-channel twitter">',
'                                    <span class="visuallyhidden">Twitter</span>',
'                                    <span class="icon icon-twitter"></span>',
'                                </a>',
'                                <a href="https://www.youtube.com/user/singaporeHDB" class="social-channel youtube">',
'                                    <span class="visuallyhidden">Youtube</span>',
'                                    <span class="icon icon-youtube-play"></span>',
'                                </a>',
'                            </div>',

'                        </div>'

		                  ];
		
		
		var getFooterURL = function(link_name) {
			for(a in config.footer_links) {
				var item = config.footer_links[a];
				if (item.title == link_name) {
					return item.url;
				}				
			}
			
			return "";
		}
		
		
		var tpl = [

'                <footer class="footer">',
'                   <div class="wrapper row">',
'                    <div class="footer-eservice-links large-12 columns">',
'													<ul class="list inline-list"></ul>',
'										 </div>',
'										</div>',
'                    <div class="wrapper row">',
'                        <div class="back-to-top">',
'                            <a href="javascript:;" class="back-to-top-link js-back-to-top">',
'                                <span class="icon icon-chevron2-up"></span>',
'                                <span class="back-to-top-text">Back to top</span>',
'                            </a>',
'                        </div>',

(!h_config.staticpage?"":getNavHTML(i3header.nav_data)),

(!h_config.staticpage?"":footerSite.join("")),

'										</div>',	

'                    <div class="footer-bottom">',
'                        <div class="wrapper row">',
'                            <div class="small-12 columns">',
'                                <div class="footer-border"></div>',
'                            </div>',

//'                            <p class="last-review small-12 large-3 columns">Last reviewed on 16 March 2015</p>',
'                            ',
'                            <nav class="secondary-footer-nav  small-12 large-9 columns ">',
'                                <a href="' + (wcmsHost + getFooterURL("Home")) + '" class="secondary-footer-nav-link">Home</a>',
'                                <a href="' + (wcmsHost + getFooterURL("Careers"))+ '" class="secondary-footer-nav-link">Careers</a>                                ',
'                                <a href="' + (wcmsHost + getFooterURL("Contact Us"))+ '" class="secondary-footer-nav-link">Contact Us</a>',
'                                <a href="' + (wcmsHost + getFooterURL("Terms of Use"))+ '" class="secondary-footer-nav-link">Terms of Use</a>',
'                                <a href="' + (wcmsHost + getFooterURL("Privacy Statement"))+ '" class="secondary-footer-nav-link">Privacy Statement</a>',
'                                <a href="' + (wcmsHost + getFooterURL("Site Requirements"))+ '" class="secondary-footer-nav-link">Site Requirements</a>',
'                                <a href="' + h_config.eserhost.replace("http:", "https:") + '/fi10/fi10400p.nsf/FI10FHDBService/?OpenForm" class="secondary-footer-nav-link">Rate Our Website</a>',
'                            </nav>',
'                            <p class="footer-text small-12 columns">&copy; 2018 Housing & Development Board</p>',

'                        </div>',
'                    </div>',

'                </footer>',

'            </div> <!-- Inner wrap close -->',
'        </div> <!-- Off canvas wrap close -->'



		           ];
			
		
		document.write(tpl.join(""));

		
		//write jquery
		var vstr = navigator.userAgent;
	
		
		
		
		
	
		var jsmarkup = [
      //'<script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-523196364d2b9b64" async></script>',		                
		  //'<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>',
		  '<script>window.jQuery || document.write(\'<scr\' + \'ipt src="' + h + '/js/vendor/jquery-1.11.1.min.js"><\/scr\' + \'ipt>\')</script>',
		  '<scr' + 'ipt> if(typeof dojo !== "undefined") define.amd = null;</scr' + 'ipt>',		  
		  (!h_config.excludefastclick?'<scr' + 'ipt src="' + h_config.rschost + '/js/vendor/fastclick.js"></scr' + 'ipt>':''),
			'<scr' + 'ipt src="' + h_config.rschost + '/js/vendor/handlebars-v2.0.0.js"></scr' + 'ipt>',
			'<scr' + 'ipt src="' + h_config.rschost + '/js/vendor/jquery.cookie.js"></scr' + 'ipt>',
			'<scr' + 'ipt src="' + h_config.rschost + '/js/vendor/scrollto.min.js"></scr' + 'ipt>',
			'<scr' + 'ipt src="' + h_config.rschost + '/js/vendor/foundation.min.js"></scr' + 'ipt>',
		  '<scr' + 'ipt src="' + h_config.rschost + '/js/base/main.js"></scr' + 'ipt>',			
			'<scr' + 'ipt src="' + h_config.rschost + '/js/plugins.js"></scr' + 'ipt>',
			'<scr' + 'ipt src="' + h_config.rschost + '/js/modules.js"></scr' + 'ipt>',
			'<scr' + 'ipt src="' + h_config.rschost + '/js/dynamic-nav.js"></scr' + 'ipt>',

			'<scr' + 'ipt src="' + h_config.rschost + '/js/main.js"></scr' + 'ipt>',
			'<!-- insert for vendor js -->'
		];
		   
		
		document.write(jsmarkup.join(""));	
		
		var o = h_config.jsaddons;
		if("undefined" != typeof(o)) {
			var list = o.split(",");
			var jsaddons = [];
			var subfolder, name;
			for(i in list) {
				 name = list[i];
				 
				 if(!name){ continue; }
				 
				 if("maps" == name)
				 {
					jsaddons.push( '<scr' + 'ipt defer src="' + h_config.rschostname + '/web/ej03/scripts/OneMap/EJ03MapProperties.js"></scr' + 'ipt>');
				 } else
				 {
				 
					 subfolder = "plugins";
						
						if ("datepicker" == name ) { subfolder = "plugins"; }
						      
						if ("filereader" == name) {
							subfolder = "vendor/FileReader";
							//include dependency
							jsaddons.push( '<scr' + 'ipt src="' + h_config.rschost + '/js/' + subfolder + '/swfobject.js"></scr' + 'ipt>');
							name = "jquery.FileReader"
						}
						
						jsaddons.push( '<scr' + 'ipt src="' + h_config.rschost + '/js/' + subfolder + '/' + name + '.js"></scr' + 'ipt>');
				 
				 }
				 
				 
			}			
			document.write(jsaddons.join(""))
		}			
		
			//add google analytics different than tracking code in base/main.js
		var addGAScript = function ()
		{
      
	      //switch tracker account
	      var ga_account  = "UA-5554471-1";
	      var ga_domain  = ".hdb.gov.sg";
	      var host = window.location.hostname;
	      
	      var iprodhosts = [ //internet production 
	      "www.hdb.gov.sg", "www101.hdb.gov.sg", "www20.hdb.gov.sg",
	      "services2.hdb.gov.sg", "services2-pre.hdb.gov.sg",
	      "services3.hdb.gov.sg", "services3-pre.hdb.gov.sg",
	      "services2-preprod.hdb.gov.sg", "services3-preprod.hdb.gov.sg",
	      "esales.hdb.gov.sg"
	      ]; 
	      
	      var aprodhosts = [ //intranet production
	      "intranet79.hdb.gov.sg",
	      "intranet.hdb.gov.sg",
	      "intranet-app.hdb.gov.sg"
	      ];
	      
	      
	      if ( iprodhosts.indexOf(host) > -1 ) {  
	      		ga_account  = "UA-5554471-2"; ga_domain = ".hdb.gov.sg"
	      } else if( aprodhosts.indexOf(host) > -1 ) { 
	      		ga_account  = "UA-5554471-3"; ga_domain = ".hdb.gov.sg"
	      }
	      
	      
	      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
	      	(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
	      	m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
	      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
	
	      ga('create', ga_account, 'auto');
	      ga('require', 'displayfeatures');
	      ga('send', 'pageview');
	      
		}
		
		addGAScript();
		
		
		function updateGAeServiceUsage() {
			var value = 0;
			var esvcid=h_config.eserviceid;
			if (h_config.showrateservice) value=1;
			if (h_config.eserviceid == "") esvcid="undefined";
	            ga('send', 'event', 'e-ServiceUsage', 'PageLoad', esvcid, value, {nonInteraction: true});
	         }
			
			updateGAeServiceUsage();
	
		
		return parent;
		
	}(i3footer || {}, {}));
	
	//*****Start: SPINS *****
	if (!spinsLoaded) var spinsLoaded = false;
	var spinsIsInSession = false;
	if (typeof(spinsHost)== "undefined" || spinsHost == "" ) { 	var spinsHost = h_config.rschostname; 


	} 


	if (h_config.showlogout) {
			document.write('<scr'+'ipt src="' +h_config.rschostname+ '/webapp/SX05AWSPCP/script/session_spcp.js" type="text/javascript"></scr'+'ipt>');
		}


	function logoutClick() {
	    var url=h_config.logouturl;
		if (confirm('Would you like to log out of the session now?')) {
		 self.location.href = h_config.rschostname + "/webapp/SX05AWSPCP/SX05SLogoutServlet?redURL="+url;
		}
	}
	// ***** End: SPINS *****