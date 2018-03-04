// version 1.3
	var i3header = (function(parent, $){
		var h 	= h_config.rschost,		
    wcmsUrl = h_config.wcmsUrl,
    esvcUrl = h_config.esvcUrl,
    lnUrl 	= h_config.eserhost.replace("http:","https:");
		var wcmsHost = wcmsUrl.replace("/cs/infoweb", "");
		
		var config = {
			
			nav_bar : 
				[
{ name: 'Home', url: '/cs/infoweb/homepage', html: '<span class="visuallyhidden">Home</span><span class="icon icon-home"></span>' },
{
	  name:"About Us",
	  url:"/cs/infoweb/about-us",
	  items:[
		{
		  name:"Vision, Mission, and Values",
		  url:"/cs/infoweb/about-us/vision-mission-and-values",
		  items:[
			{
			  name:"Vision and Mission",
			  url:"/cs/infoweb/about-us/vision-mission-and-values/vision-and-mission",
			},
			{
			  name:"Shared Values",
			  url:"/cs/infoweb/about-us/vision-mission-and-values/shared-values",
			},
			{
			  name:"Brand Values",
			  url:"/cs/infoweb/about-us/vision-mission-and-values/brand-values",
			},
			{
			  name:"Environmental Policy",
			  url:"/cs/infoweb/about-us/vision-mission-and-values/environmental-policy",
			}
		]
		},
		{
		  name:"Our Role",
		  url:"/cs/infoweb/about-us/our-role",
		  items:[
			{
			  name:"Public Housing - A Singapore Icon",
			  url:"/cs/infoweb/about-us/our-role/public-housing--a-singapore-icon",
			},
			{
			  name:"HDB Gallery",
			  url:"/cs/infoweb/about-us/our-role/hdb-gallery",
			},
			{
			  name:"Visitors' Photo Gallery",
			  url:"/cs/infoweb/about-us/our-role/visitors-photo-gallery",
			},
			{
			  name:"Smart and Sustainable Living",
			  url:"/cs/infoweb/about-us/our-role/smart-and-sustainable-living",
			}
		]
		},
		{
		  name:"Our Logo",
		  url:"/cs/infoweb/about-us/our-logo",
		},
		{
		  name:"History",
		  url:"/cs/infoweb/about-us/history",
		  items:[
			{
			  name:"HDB Towns, Your Home",
			  url:"/cs/infoweb/about-us/history/hdb-towns-your-home",
			}
		]
		},
		{
		  name:"Organisation Structure",
		  url:"/cs/infoweb/about-us/organisation-structure",
		},
		{
		  name:"Achievements and Accolades",
		  url:"/cs/infoweb/about-us/achievements-and-accolades",
		  items:[
			{
			  name:"Achievements",
			  url:"/cs/infoweb/about-us/achievements-and-accolades/achievements",
			},
			{
			  name:"Customers' Experience",
			  url:"/cs/infoweb/about-us/achievements-and-accolades/customers-experience",
			},
			{
			  name:"Awards for Business Partners",
			  url:"/cs/infoweb/about-us/achievements-and-accolades/awards-for-business-partners",
			}
		]
		},
		{
		  name:"Careers",
		  url:"/cs/infoweb/about-us/careers",
		  items:[
			{
			  name:"Development Opportunities and Staff Benefits",
			  url:"/cs/infoweb/about-us/careers/development-opportunities-and-staff-benefits",
			},
			{
			  name:"Career Opportunities",
			  url:"/cs/infoweb/about-us/careers/career-opportunities",
			},
			{
			  name:"Top 10 Reasons to Join HDB",
			  url:"/cs/infoweb/about-us/careers/top-10-reasons-to-join-hdb",
			}
		]
		},
		{
		  name:"Scholarships and Internships",
		  url:"/cs/infoweb/about-us/scholarships-and-internships",
		  items:[
			{
			  name:"Scholarships",
			  url:"/cs/infoweb/about-us/scholarships-and-internships/scholarships",
			},
			{
			  name:"Specialist Scholarship",
			  url:"/cs/infoweb/about-us/scholarships-and-internships/the-hdb-specialist-scholarship",
			},
			{
			  name:"Internships",
			  url:"/cs/infoweb/cs/infoweb/internships",
			}
		]
		},
		{
		  name:"News and Publications",
		  url:"/cs/infoweb/about-us/news-and-publications",
		  items:[
			{
			  name:"Press Releases",
			  url:"/cs/infoweb/about-us/news-and-publications/press-releases",
			},
			{
			  name:"Letters to the Media",
			  url:"/cs/infoweb/about-us/news-and-publications/letters-to-the-media",
			},
			{
			  name:"Annual Reports",
			  url:"/cs/infoweb/about-us/news-and-publications/annual-reports",
			},
			{
			  name:"Financial Statements",
			  url:"/cs/infoweb/about-us/news-and-publications/financial-statements",
			},
			{
			  name:"Credit Rating",
			  url:"/cs/infoweb/about-us/news-and-publications/credit-rating",
			},
			{
			  name:"Publications",
			  url:"/cs/infoweb/about-us/news-and-publications/publications",
			}
		]
		},
		{
		  name:"Events and Talks",
		  url:"/cs/infoweb/about-us/events-and-talks",
		  items:[
			{
			  name:"Events Calendar",
			  url:"/cs/infoweb/about-us/events-and-talks/events-calendar",
			},
			{
			  name:"Heartland Talks",
			  url:"/cs/infoweb/about-us/events-and-talks/heartland-talks",
			}
		]
		}
	]
	},
	{
	  name:"Residential",
	  url:"/cs/infoweb/residential",
	  items:[
		{
		  name:"Buying a Flat ",
		  url:"/cs/infoweb/residential/buying-a-flat",
		  items:[
			{
			  name:"New",
			  url:"/cs/infoweb/residential/buying-a-flat/new",
			},
			{
			  name:"Resale",
			  url:"/cs/infoweb/residential/buying-a-flat/resale",
			}
		]
		},
		{
		  name:"Financing a Flat Purchase",
		  url:"/cs/infoweb/residential/financing-a-flat-purchase",
		  items:[
			{
			  name:"Step-By-Step Guide to Financial Planning",
			  url:"/cs/infoweb/residential/financing-a-flat-purchase/step-by-step-guide-to-financial-planning",
			},
			{
			  name:"Housing Loan from HDB",
			  url:"/cs/infoweb/residential/financing-a-flat-purchase/housing-loan-from-hdb",
			},
			{
			  name:"Housing Loan from Banks",
			  url:"/cs/infoweb/residential/financing-a-flat-purchase/housing-loan-from-banks",
			}
		]
		},
		{
		  name:"Servicing Your HDB Housing Loan",
		  url:"/cs/infoweb/residential/servicing-your-hdb-loan",
		  items:[
			{
			  name:"Loan Matters",
			  url:"/cs/infoweb/residential/servicing-your-hdb-loan/loan-matters",
			},
			{
			  name:"CPF Rules and Early Repayment",
			  url:"/cs/infoweb/residential/servicing-your-hdb-loan/cpf-rules-and-early-repayment",
			},
			{
			  name:"Citizen Top-Up",
			  url:"/cs/infoweb/residential/buying-a-flat/new/citizen-top-up",
			}
		]
		},
		{
		  name:"Selling a Flat",
		  url:"/cs/infoweb/residential/selling-a-flat",
		  items:[
			{
			  name:"Eligibility",
			  url:"/cs/infoweb/residential/selling-a-flat/eligibility",
			},
			{
			  name:"Additional Information",
			  url:"/cs/infoweb/residential/selling-a-flat/additional-information",
			},
			{
			  name:"Selling Statistics",
			  url:"/cs/infoweb/residential/selling-a-flat/selling-statistics",
			},
			{
			  name:"Ways to Sell",
			  url:"/cs/infoweb/residential/selling-a-flat/ways-to-sell",
			},
			{
			  name:"Options for Your Next Flat",
			  url:"/cs/infoweb/residential/selling-a-flat/options-for-your-next-flat",
			},
			{
			  name:"Finance",
			  url:"/cs/infoweb/residential/selling-a-flat/finance",
			},
			{
			  name:"Selling Process",
			  url:"/cs/infoweb/residential/selling-a-flat/selling-process",
			}
		]
		},
		{
		  name:"Renting a Flat",
		  url:"/cs/infoweb/residential/renting-a-flat",
		  items:[
			{
			  name:"Renting from HDB",
			  url:"/cs/infoweb/residential/renting-a-flat/renting-from-hdb",
			},
			{
			  name:"Renting from the Open Market",
			  url:"/cs/infoweb/residential/renting-a-flat/renting-from-the-open-market",
			}
		]
		},
		{
		  name:"Renting Out a Flat/ Bedroom",
		  url:"/cs/infoweb/residential/renting-out-a-flat-room",
		  items:[
			{
			  name:"Renting Out Your Flat",
			  url:"/cs/infoweb/residential/renting-out-a-flat-room/renting-out-your-flat",
			},
			{
			  name:"Renting Out Your Bedroom",
			  url:"/cs/infoweb/residential/renting-out-a-flat-room/renting-out-your-room",
			}
		]
		},
		{
		  name:"Living in an HDB Flat",
		  url:"/cs/infoweb/residential/living-in-an-hdb-flat",
		  items:[
			{
			  name:"Moving In",
			  url:"/cs/infoweb/residential/living-in-an-hdb-flat/moving-in",
			},
			{
			  name:"Renovation",
			  url:"/cs/infoweb/residential/living-in-an-hdb-flat/renovation",
			},
			{
			  name:"For Our Seniors",
			  url:"/cs/infoweb/residential/living-in-an-hdb-flat/for-our-seniors",
			},
			{
			  name:"Home Maintenance",
			  url:"/cs/infoweb/residential/living-in-an-hdb-flat/home-maintenance",
			},
			{
			  name:"Fire Insurance ",
			  url:"/cs/infoweb/residential/living-in-an-hdb-flat/fire-insurance",
			},
			{
			  name:"Sale of Recess Area",
			  url:"/cs/infoweb/residential/living-in-an-hdb-flat/sale-of-recess-area",
			},
			{
			  name:"Keeping Pets",
			  url:"/cs/infoweb/residential/living-in-an-hdb-flat/keeping-pets",
			},
			{
			  name:"Changing Owners/ Occupiers",
			  url:"/cs/infoweb/residential/living-in-an-hdb-flat/changing-owners-occupiers",
			},
			{
			  name:"My Neighbourhood",
			  url:"/cs/infoweb/residential/living-in-an-hdb-flat/my-neighbourhood",
			},
			{
			  name:"Acquiring Private Property",
			  url:"/cs/infoweb/residential/living-in-an-hdb-flat/acquiring-private-property",
			},
			{
			  name:"SERS and Upgrading Programmes",
			  url:"/cs/infoweb/residential/living-in-an-hdb-flat/sers-and-upgrading-programmes",
			},
			{
			  name:"Home Business",
			  url:"/cs/infoweb/residential/living-in-an-hdb-flat/home-business",
			}
		]
		},
		{
		  name:"Season Parking",
		  url:"/cs/infoweb/residential/season-parking",
		  items:[
			{
			  name:"Season Parking Ticket",
			  url:"/cs/infoweb/residential/season-parking/season-parking-ticket",
			},
			{
			  name:"Family Season Parking Ticket",
			  url:"/cs/infoweb/residential/season-parking/family-season-parking",
			},
			{
			  name:"Temporary Parking Ticket for Bereaved Family Members",
			  url:"/cs/infoweb/residential/season-parking/temporary-parking-ticket-for-family-members-of-the-bereaved",
			},
			{
			  name:"Season Parking for Commercial Vehicle",
			  url:"/cs/infoweb/residential/season-parking/season-parking-for-commercial-vehicle",
			},
			{
			  name:"Concessionary Season Parking Ticket for Motorcycles",
			  url:"/cs/infoweb/residential/season-parking/concessionary-season-parking-ticket-for-motorcycles",
			},
			{
			  name:"Park &amp; Ride Scheme",
			  url:"/cs/infoweb/residential/season-parking/park-and-ride",
			}
		]
		}
	]
	},
	{
	  name:"Community",
	  url:"/cs/infoweb/heartlandbeat",
	  items:[
		{
		  name:"HDB Community Week ",
		  url:"/cs/infoweb/community/hdb-community-week",
		  items:[
			{
			  name:"HDB Community Building Seminar &amp; Build-a-thon 2016",
			  url:"/cs/infoweb/community/hdb-community-week/community-building-seminar-and-build-a-thon-2016",
			},
			{
			  name:"HDB Friendly Faces, Lively Places Fund",
			  url:"/cs/infoweb/community/hdb-community-week/hdb-friendly-faces-lively-places-fund-page",
			},
			{
			  name:"Good Neighbours Project 2016",
			  url:"/cs/infoweb/community/hdb-community-week/good-neighbours-project-2016",
			},
			{
			  name:"'Celebrating LIFE in the Heartlands' Photo Competition 2016",
			  url:"/cs/infoweb/community/hdb-community-week/celebrating-life-in-the-heartlands-photo-competition-2016",
			},
			{
			  name:"Heartland Youthoria! 2016",
			  url:"/cs/infoweb/community/hdb-community-week/heartland-youthoria-2016",
			},
			{
			  name:"Past Community Weeks",
			  url:"/cs/Satellite?c=Page&amp;cid=1383799232216&amp;pagename=InfoWEB%2FPage%2FExternalPage",
			}
		]
		},
		{
		  name:"Care for Your Neighbours",
		  url:"/cs/infoweb/community/care-for-your-neighbours",
		  items:[
			{
			  name:"Get to Know Your Neighbours",
			  url:"/cs/infoweb/community/care-for-your-neighbours/get-to-know-your-neighbours",
			},
			{
			  name:"Being a Good Neighbour",
			  url:"/cs/infoweb/community/care-for-your-neighbours/being-a-good-neighbour",
			},
			{
			  name:"Good Neighbours Movement",
			  url:"/cs/infoweb/community/care-for-your-neighbours/good-neighbours-movement",
			},
			{
			  name:"Heartland Ambassador Programme",
			  url:"/cs/infoweb/community/care-for-your-neighbours/heartland-ambassador-programme",
			},
			{
			  name:"Initiatives for the Young and Youth",
			  url:"/cs/infoweb/youngandyouth",
			},
			{
			  name:"Initiatives for Seniors",
			  url:"/cs/infoweb/community/care-for-your-neighbours/initiatives-for-seniors",
			}
		]
		},
		{
		  name:"Practise Eco-Living",
		  url:"/cs/infoweb/community/practise-eco-living",
		  items:[
			{
			  name:"Eco Learning Journey",
			  url:"/cs/infoweb/community/practise-eco-living/eco-learning-journey",
			},
			{
			  name:"Eco@Yuhua",
			  url:"/cs/infoweb/community/practise-eco-living/eco@yuhua",
			},
			{
			  name:"Eco@Punggol",
			  url:"/cs/infoweb/community/practise-eco-living/eco@punggol",
			},
			{
			  name:"Community in-Bloom",
			  url:"/cs/infoweb/community/practise-eco-living/community-in-bloom",
			},
			{
			  name:"Eco-Living Tips",
			  url:"/cs/infoweb/community/practise-eco-living/eco-living-tips",
			}
		]
		},
		{
		  name:"Shape Your Neighbourhood",
		  url:"/cs/infoweb/community/shape-your-neighbourhood",
		  items:[
			{
			  name:"ACE! in the Heartlands",
			  url:"/cs/infoweb/community/shape-your-neighbourhood/ace!-in-the-heartlands",
			},
			{
			  name:"Hello Neighbour! @ Tampines Central",
			  url:"/cs/infoweb/community/shape-your-neighbourhood/hello-neighbour--tampines-central",
			},
			{
			  name:"Building Our Neighbourhood Dreams (BOND!)",
			  url:"/cs/infoweb/community/shape-your-neighbourhood/building-our-neighbourhood-dreams-bond",
			},
			{
			  name:"Let's Play-Make@ Canberra",
			  url:"/cs/infoweb/community/shape-your-neighbourhood/lets-play-make-canberra",
			},
			{
			  name:"Siglap East's Walls of Inspiration and Mango Festival",
			  url:"/cs/infoweb/community/shape-your-neighbourhood/siglap-easts-walls-of-inspiration-and-mango-festival",
			}
		]
		},
		{
		  name:"Enjoy Vibrant Community Places",
		  url:"/cs/infoweb/community/enjoy-vibrant-community-places",
		  items:[
			{
			  name:"Town Plazas",
			  url:"/cs/infoweb/community/enjoy-vibrant-community-places/town-plazas",
			},
			{
			  name:"Punggol Waterway",
			  url:"/cs/infoweb/community/enjoy-vibrant-community-places/punggol-waterway",
			}
		]
		},
		{
		  name:"Community Partners",
		  url:"/cs/infoweb/community/community-partners",
		  items:[
			{
			  name:"Teachers",
			  url:"/cs/infoweb/community/community-partners/teachers",
			},
			{
			  name:"Community Building Practitioners",
			  url:"/cs/infoweb/community/community-partners/community-building-practitioners",
			},
			{
			  name:"Engaging our Heartlanders (EOH) Network",
			  url:"/cs/infoweb/community/community-partners/engaging-our-heartlanders-eoh-network",
			}
		]
		},
		{
		  name:"Heartland Stories",
		  url:"/cs/infoweb/community/heartland-stories",
		  items:[
			{
			  name:"Heartland Scoops",
			  url:"/cs/infoweb/community/heartland-stories/heartland-scoops",
			},
			{
			  name:"Life Storeys",
			  url:"/cs/infoweb/community/heartland-stories/life-storeys",
			},
			{
			  name:"Maddie and Friends",
			  url:"/cs/infoweb/community/heartland-stories/maddie-makes-friends",
			},
			{
			  name:"The HeART of Neighbourliness Publication",
			  url:"/cs/infoweb/community/heartland-stories/the-heart-of-neighbourliness",
			}
		]
		},
		{
		  name:"New and Upcoming Events",
		  url:"/cs/Satellite?c=Page&amp;cid=1383798897891&amp;pagename=InfoWEB%2FPage%2FExternalPage",
		}
	]
	},
	{
	  name:"Business",
	  url:"/cs/infoweb/business",
	  items:[
		{
		  name:"Commercial",
		  url:"/cs/infoweb/business/commercial",
		  items:[
			{
			  name:"Renting from HDB",
			  url:"/cs/infoweb/business/commercial/renting-from-hdb",
			},
			{
			  name:"Renting from the Open Market",
			  url:"/cs/infoweb/business/commercial/renting-from-the-open-market",
			},
			{
			  name:"Buying from the Open Market",
			  url:"/cs/infoweb/business/commercial/buying-from-the-open-market",
			},
			{
			  name:"Selling in the Open Market",
			  url:"/cs/infoweb/business/commercial/selling-in-the-open-market",
			},
			{
			  name:"Managing Your Unit",
			  url:"/cs/infoweb/business/commercial/managing-your-unit",
			},
			{
			  name:"List of Shopping and Office Complexes ",
			  url:"/cs/infoweb/business/commercial/list-of-shopping-and-office-complexes",
			},
			{
			  name:"Pro-Business Measures and Services",
			  url:"/cs/infoweb/business/commercial/pro-business-measures-and-services",
			},
			{
			  name:"Newsletter",
			  url:"/cs/infoweb/business/commercial/newsletter",
			},
			{
			  name:"Business Expectations Survey",
			  url:"/cs/infoweb/business/commercial/business-expectations-survey",
			}
		]
		},
		{
		  name:"Industrial",
		  url:"/cs/infoweb/business/industrial",
		},
		{
		  name:"Building Professionals (BGBiz)",
		  url:"/cs/infoweb/business/building-professionals",
		  items:[
			{
			  name:"e-Services",
			  url:"/cs/infoweb/business/building-professionals/e-services",
			},
			{
			  name:"Technical Resources",
			  url:"/cs/infoweb/business/building-professionals/techinical-resources",
			},
			{
			  name:"Submitting Building Plans",
			  url:"/cs/infoweb/business/building-professionals/submitting-building-plans",
			},
			{
			  name:"Renovation and Addition &amp; Alteration (A&amp;A) Works",
			  url:"/cs/infoweb/business/building-professionals/renovation-and-a-and-a-works",
			},
			{
			  name:"Updates and Announcements",
			  url:"/cs/infoweb/business/building-professionals/updates-and-announcements",
			},
			{
			  name:"Enquiry and Forms",
			  url:"/cs/infoweb/business/building-professionals/enquiry-and-forms",
			}
		]
		},
		{
		  name:"Renovation and Repair Contractors",
		  url:"/cs/infoweb/business/renovation-and-repair-contractors",
		  items:[
			{
			  name:"Renovation",
			  url:"/cs/infoweb/business/renovation-and-repair-contractors/renovation",
			},
			{
			  name:"Windows",
			  url:"/cs/infoweb/business/renovation-and-repair-contractors/windows",
			},
			{
			  name:"Spalling Concrete",
			  url:"/cs/infoweb/business/renovation-and-repair-contractors/spalling-concrete",
			}
		]
		},
		{
		  name:"Land Developers and Land Users",
		  url:"/cs/infoweb/business/land-developers-and-land-users",
		  items:[
			{
			  name:"Buying Land (Land Sales)",
			  url:"/cs/infoweb/business/land-developers-and-land-users/buying-land-land-sales",
			},
			{
			  name:"Renting of Land on Temporary Occupation Licence (TOL)",
			  url:"/cs/infoweb/business/land-developer-and-land-users/renting-land-tol",
			}
		]
		},
		{
		  name:"Tenderers ",
		  url:"/cs/infoweb/business/tenderers",
		  items:[
			{
			  name:"HDB Tender Opportunities",
			  url:"/cs/infoweb/business/tenderers/hdb-tender-opportunities",
			},
			{
			  name:"Tender Notices",
			  url:"/cs/Satellite?c=Page&amp;cid=1383798876642&amp;pagename=InfoWEB%2FPage%2FExternalPage",
			},
			{
			  name:"Tender Schedules",
			  url:"/cs/Satellite?c=Page&amp;cid=1383799076901&amp;pagename=InfoWEB%2FPage%2FExternalPage",
			},
			{
			  name:"Tender Awards",
			  url:"/cs/Satellite?c=Page&amp;cid=1383799078859&amp;pagename=InfoWEB%2FPage%2FExternalPage",
			}
		]
		},
		{
		  name:"Estate Agents and Salespersons",
		  url:"/cs/infoweb/business/estate-agents-and-salespersons",
		  items:[
			{
			  name:"Buying a Resale Flat",
			  url:"/cs/infoweb/business/estate-agents-and-salespersons/buying-a-resale-flat",
			},
			{
			  name:"Selling a Flat",
			  url:"/cs/infoweb/business/estate-agents-and-salespersons/selling-a-flat",
			},
			{
			  name:"Renting a Flat",
			  url:"/cs/infoweb/business/estate-agents-and-salespersons/renting-a-flat",
			},
			{
			  name:"Renting Out a Flat or Bedroom ",
			  url:"/cs/infoweb/business/estate-agents-and-salespersons/renting-out-a-flat-or-room",
			},
			{
			  name:"Letters to KEOs",
			  url:"/cs/infoweb/business/estate-agents-and-salespersons/letters-to-keo",
			},
			{
			  name:"Continuing Professional Development CPD Courses",
			  url:"/cs/infoweb/business/estate-agents-and-salespersons/continuing-professional-development-cpd-courses",
			},
			{
			  name:"Resources",
			  url:"/cs/infoweb/estate-agents-and-salespersons/Resources",
			}
		]
		}
	]
	},
	{
	  name:"Car Parks",
	  url:"/cs/infoweb/car-parks",
	  items:[
		{
		  name:"Types of HDB Car Parks",
		  url:"/cs/infoweb/car-parks/types-of-hdb-car-parks",
		},
		{
		  name:"Car Park Signboards",
		  url:"/cs/infoweb/car-parks/car-park-signboards",
		},
		{
		  name:"Parking Lot Line Markings",
		  url:"/cs/infoweb/car-parks/parking-lot-line-markings",
		},
		{
		  name:"Car Park Location Map",
		  url:"/cs/infoweb/car-parks/car-park-location-map",
		},
		{
		  name:"Parking Offences",
		  url:"/cs/infoweb/car-parks/parking-offences",
		  items:[
			{
			  name:"Parking Rules and Penalties",
			  url:"/cs/infoweb/car-parks/parking-offences/parking-rules-and-penalties",
			},
			{
			  name:"Payment Procedure",
			  url:"/cs/infoweb/car-parks/parking-offences/payment-procedure",
			},
			{
			  name:"Reporting of Illegal Parking",
			  url:"/cs/infoweb/car-parks/parking-offences/reporting-of-illegal-parking",
			}
		]
		},
		{
		  name:"Season Parking",
		  url:"/cs/infoweb/car-parks/season-parking",
		  items:[
			{
			  name:"Season Parking",
			  url:"/cs/infoweb/car-parks/season-parking/season-parking-ticket",
			},
			{
			  name:"Family Season Parking Ticket",
			  url:"/cs/infoweb/car-parks/season-parking/family-season-parking",
			},
			{
			  name:"Temporary Parking Ticket for Bereaved Family Members",
			  url:"/cs/infoweb/car-parks/season-parking/temporary-parking-ticket-for-bereaved-family-members",
			},
			{
			  name:"Season Parking for Commercial Vehicles",
			  url:"/cs/infoweb/car-parks/season-parking/season-parking-for-commercial-vehicles",
			},
			{
			  name:"Concessionary Season Parking Ticket for Motorcycles",
			  url:"/cs/infoweb/car-parks/season-parking/concessionary-season-parking-ticket-for-motorcycles",
			},
			{
			  name:"Park &amp; Ride Scheme",
			  url:"/cs/infoweb/car-parks/season-parking/park-and-ride",
			}
		]
		},
		{
		  name:"Short-Term Parking",
		  url:"/cs/infoweb/car-parks/short-term-parking",
		  items:[
			{
			  name:"Coupon Parking",
			  url:"/cs/infoweb/car-parks/short-term-parking/coupon-parking",
			},
			{
			  name:"Electronic Parking",
			  url:"/cs/infoweb/car-parks/short-term-parking/electronic-parking",
			},
			{
			  name:"Free Parking Scheme on Sundays and Public Holidays",
			  url:"/cs/infoweb/car-parks/short-term-parking/free-parking",
			},
			{
			  name:"Park &amp; Ride Scheme",
			  url:"/cs/infoweb/car-parks/short-term-parking/park-and-ride",
			}
		]
		},
		{
		  name:"Car Parks for Business Activities",
		  url:"/cs/infoweb/car-parks/car-parks-for-business-activities",
		  items:[
			{
			  name:"Guidelines",
			  url:"/cs/infoweb/business/commercial/renting-from-hdb/guidelines",
			},
			{
			  name:"Application Procedure",
			  url:"/cs/infoweb/business/commercial/renting-from-hdb/car-parks-for-business-activities/application-procedure",
			}
		]
		}
	]
	},	
					
					{
						name: "e-Services",
						url: esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList",
						
						items:[
                               {
                                 name:"Residential",
                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Buying_a_New_Flat",
                              



                                               items:[
                                               {
                                                 name:"Buying a New Flat",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Buying_a_New_Flat",
                                               },
                                               {
                                                 name:"Buying a Resale Flat",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Buying_a_Resale_Flat",
                                               },
                               {
                                                 name:"Financing a Flat Purchase",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Financing_a_Flat_Purchase",
                                               },

                                               {
                                                 name:"Servicing your HDB Housing Loan",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Servicing_your_HDB_Loan",
                                               },
                                               {
                                                 name:"Selling a Flat",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Selling_a_Flat",
                                               },
                                               {
                                                 name:"Renting a Flat ",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Renting_a_Flat",
                                               },

                                               {
                                                 name:"Renting Out a Flat/ Bedroom",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Renting_Out_a_FlatRoom",
                                               },
                                              
                                               {
                                                 name:"Living in an HDB Flat",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Living_in_an_HDB_Flat",
                                               },
                                               {
                                                 name:"Season Parking",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Season_Parking",
                                               }

                                               ]
                                              
                               },

                               {
                                 name:"Business",
                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Commercial",
                                                                              
                                               items:[
                                               {
                                                 name:"Commercial",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Commercial",
                                               },
                                               {
                                                 name:"Building Professionals",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Building_Professionals",
                                               },
                               {
                                                 name:"Renovation and Repair Contractors",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Renovation_and_Repair_Contractors",
                                               },

                                               {
                                                 name:"Land Developers and Land Users",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Land_Developer_and_Land_Users",
                                               },
                                               {
                                                 name:"Estate Agents and Salespersons ",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Estate_Agents_and_Salesperson",
                                               }

                                               ]


                               },

                               {
                                 name:"Car Parks",
                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Car_Park_Information",
                                               items:[
                                               {
                                                 name:"Car Park Information",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Car_Park_Information",
                                               },
                                              
                                               {
                                                 name:"Season Parking",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Car_Season_Parking",
                                               },

                                               {
                                                 name:"Parking Offences",
                                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=Parking_Offense",
                                               }
                                               ]
                               },
                              
                              
                               {
                                 name:"General",
                                 url:esvcUrl + "/webapp/FI10AWESVCLIST/FI10SEServiceList?category=General",
                                                                                                                                                                                                                                                                                                                                                 
                               }
                              
                              
                              
                              
                              

]
						
					}
					
				],
			
			preview_panel : 
			[
			   {
			     	name: "About Us",
			     	html: [
'<div class="preview-panel aboutus" >',
'  <div class="preview active">',
'    <h2 class="title">Overview</h2>',
'    <p class="text"> The Housing & Development Board (HDB) is Singapore\'s public housing authority and a statutory board under the Ministry of National Development. HDB provides affordable, quality homes through developing public housing to give Singaporeans quality homes and a better living environment. Focusing on a community spirit with public housing policies and schemes formulated to meet changing needs and aspirations, whilst maintaining racial harmony and stronger family ties. </p>',
'  </div>',
'</div>'			     	       
			     	       ]
			   },			   
			   {
			     	name: "Residential",
			     	html: [
'<div class="preview-panel residential">',
'  <div class="preview active">',
'    <h2 class="title">Overview</h2>',
'    <p class="text"> Whether you are buying, selling or already live in an HDB flat, everything you need to know about 	residential properties is housed here. </p>',
'  </div>',
'</div>'			     	       
			     	       ]
			   },
			   {
			     	name: "Community",
			     	html: [
'<div class="preview-panel community">',
'  <div class="preview active">',
'    <h2 class="title">Overview</h2>',
'    <p class="text"> More than homes, our HDB towns are vibrant places to enjoy to the fullest. There is so much in place for you to nurture great bonds with your neighbours to form an active and cohesive community. </p>',
'  </div>',
'</div>'			     	       
			     	       ]
			   },
			   {
			     	name: "Business",
			     	html: [
'<div class="preview-panel business">',
'  <div class="preview active">',
'    <h2 class="title">Overview</h2>',
'    <p class="text"> Get the information you need for any business involving HDB homes, properties, commercial spaces, or land under our management. </p>',
'  </div>',
'</div>'		     	       
			     	       ]
			   },
			   {
			     	name: "Car Parks",
			     	html: [
'<div class="preview-panel carparks">',
'  <div class="preview active">',
'    <h2 class="title">Overview</h2>',
'    <p class="text"> To find out more about the types of car parks, important car park information, and parking offences, click through for more details. </p>',
'  </div>',
'</div>'		     	       
			     	       ]
			   },
			   
			   {
                   name: "e-Services",
                   html: [
'<div class="preview-panel e-Services" >',
'<div class="megamenu-sub-panel" style="height: 163px; margin-left: -28%; background:#707070; margin-top: -8px; display:inline; z-index:1;">',
'  <div class="preview active">',
'    <h2 class="title">Popular e-Services</h2>',
' <p class="text">',
'  <ul class="list" style="width:50%;">',

'<li class="mega-nav-item"><a href="http://www.hdb.gov.sg/myhdbpage" class="link"><span class="icon icon-chevron-right"></span>My HDBPage</a></li>',

'<li class="mega-nav-item"><a href="'+esvcUrl+'/webapp/BB31AWDashboardWeb/BB31PLogin.jsp" class="link"><span class="icon icon-chevron-right"></span>HDB Resale Portal</a></li>',

'<li class="mega-nav-item"><a href="'+esvcUrl+'/webapp/BN22ERENEW/BN22PRenewTerms.jsp" class="link"><span class="icon icon-chevron-right"></span>Renewal of Season Parking</a></li>',
                                                                                                                                                                 

'  </ul>',
'  </p>',
'</div>',
'</div>','</div>'                                                                       
                          ]
      }          

			                 
			],	
		
			sitetools_nav : 
			[
				{ name: 'contact', url: '{urlcontact}', title: 'Contact Us' },
				{ name: 'faq', url: '{urlfaq}', title: 'FAQ' },
				{ name: 'feedback', url: '{urlfeedback}', title: 'Feedback' },
				{ name: 'sitemap', url: '{urlsitemap}', title: 'Sitemap' }
				/* { name: 'events', url: '{urlevents}', title: 'Events' },
				{ name: 'careers', url: '{urlcareers}', title: 'Careers' },
				{ name: 'newsroom', url: '{urlnewsroom}', title: 'Newsroom' },
				{ name: 'exhibitions', url: '{urlexhibitions}', title: 'Exhibitions' }*/
				
			]
					   
		
		} ;

		
		var primary_item_tpl = [
	  '<!-- primary-item -->',
		'	<li class="primary-nav-item js-primary-nav">', 
		'	<a href="{URL}" class="primary-nav-link">', 
		'	  	{TITLE}',
		'	  </a> ',
		'	  {MENU}',
		'	</li>',
		'<!-- end-primary-item -->'
		].join("\n");
		
		var menu_tpl = [
		'        <div class="megamenu-panel">',
		'           <div class="wrapper">',
		'                <nav class="mega-nav">',
		'                    <ul class="list">',
		'{LIST}',
		'                    </ul>',
		'                </nav>',
		'{PREVIEW}',
		'            </div>',
		'        </div>'                
		].join("\n");
		
		var menu_item_tpl = [
		'<li class="mega-nav-item js-mega-nav">',
		'	<a href="{URL}" class="link">',
		'    	<span class="icon icon-chevron-right"></span>{TITLE}</a>',
		'{MENU}',
		'</li>'		                     
		].join("\n");
		
		var sub_menu_tpl = [
		'  <div class="megamenu-sub-panel">',
		'    <div class="tertiaries">',
		'{LIST}',   
		'    </div>',
		'  </div>'
		].join("\n");
		
		var primary_nav_html = [

		'    <nav class="primary-nav desktop" role="navigation">',
		'      <ul class="primary-nav-list list clearfix">',
		'{LIST}',
		'      </ul>',
		'    </nav>'
	
		].join("\n");
		
		
		
		var getPrimaryNavHTML = function(data) {
			
			if (!data.length || data[0] == "" ) { return ""; }
			var tmp_html = [];
			var i = 0;
			for(; i < data.length; i++) {
				var item = data[i],
					title = (item.html?item.html:item.name);
				
				
				var tmp_tpl = primary_item_tpl
					.replace("{TITLE}", title)
					.replace("{URL}", (item.url.indexOf("http")<0? (wcmsHost + item.url): item.url ) )
					.replace("{MENU}", getMenuHTML(item.items, 1))
					.replace("{PREVIEW}", getPreviewPanel(item.name));
				
					tmp_html.push(tmp_tpl);
			}			
			
			return primary_nav_html.replace("{LIST}", tmp_html.join("\n"));
			
		};
		
		var getPreviewPanel = function(item_key) {
			var i = 0;
			for (; i < config.preview_panel.length; i++ ) {
				var lookup_item = config.preview_panel[i];
				 
				if ( lookup_item.name.toLowerCase() == item_key.toLowerCase() ) {
					return lookup_item.html.join("\n");
				} 			
			}
			
			return "";
			
		};
		
		var getMenuHTML = function(items_data, level){
			if (!items_data || !items_data.length || items_data[0] == "" ) { return ""; }
			
			var temp_tpl = (level<2?menu_tpl:sub_menu_tpl),
				temp_list = [],
				item;
			var i = 0;
			
			if ( level > 1 ) {
				temp_list.push('      <div class="col">')
				temp_list.push('        <ul class="list">');
			}			
			
			for (; i < items_data.length; i++ ) {
				var item = items_data[i];
				if(!item) continue;
				
				if ( level > 1 && (i%5==0)) { //split
					temp_list.push('        </ul>')
					temp_list.push('      </div> ')
					temp_list.push('      <div class="col">')
					temp_list.push('        <ul class="list">');											
				}
				
				var temp_item_tpl = menu_item_tpl.replace("{TITLE}", item.name)
					.replace("{URL}", (item.url.indexOf("http")<0? (wcmsHost + item.url): item.url ) )
					.replace("{MENU}", getMenuHTML(item.items, level+1));;
				temp_list.push(temp_item_tpl);
			}
			
			if ( level > 1 ) { 
				temp_list.push('        </ul>')
				temp_list.push('      </div> ');					
			}
			
			return temp_tpl.replace("{LIST}", temp_list.join("\n"));
			
		};
		
		//console.log(getPrimaryNavHTML(config.nav_bar))
		var m_nav_tpl = [
			'<nav class="mobile-nav" role="navigation" aria-hidden="true">',
			'	<ul class="list">',
			'{LIST}',
			'    </ul>',
			'</nav>'
		].join("\n");
		
		var m_nav_subpanel = [
			'<div class="mobile-nav-subpanel">',
			'	<p class="title"><a href="/">Home</a></p>',
			'	<div class="subpanel-header">',
			'		<a href="#" class="mobile-nav-back js-mobile-nav-back">',
			'			<span class="icon icon-chevron-left"><span class="visuallyhidden">Left arrow icon</span></span> {TITLE}',
			'		</a>',
			'	</div>',
			'	<ul class="list mobile-subnav">',
			'	{MENU}',
			' </ul>',
			'</div>'            
		].join("\n");
		
		var m_nav_item = [
			'		<li class="mobile-nav-item">',
			'			<a tabindex="-1" href="{URL}" class="link">{TITLE}</a>',			
			'			{MENU}',
			'		</li>'		  
		].join("\n");
		
		
		var m_expand_tpl = [
			'	<a tabindex="-1" href="#" class="mobile-nav-expand js-mobile-nav-expand">',
			'		<span class="icon icon-chevron-right"><span class="visuallyhidden">Right arrow icon</span></span>',
			'	</a>'		                    
		].join("\n");
		
		var getMobileNavHTML = function(data) {
			
			if (!data.length || data[0] == "" ) { return ""; }
			var tmp_html = [
				'		<li class="mobile-nav-item">',
				'			<a  tabindex="-1" href="'+wcmsUrl+'/homepage" class="link">Home</a>',
				'		</li>',
				'		',
				'		<li class="mobile-nav-item">',
				'			<a tabindex="-1" href="'+esvcUrl+'/webapp/FI10PPORTAL/FI10PAtAGlance.jsp" class="link account-link">',
				'				<span class="icon icon-user"></span>',
				'				My HDBPage',
				'			</a>',
				'		</li>',
				'		<li class="mobile-nav-item">',
				'			<a tabindex="-1" href="'+esvcUrl+'/webapp/FI10AWBIZ/FI10PBizOverview.jsp" class="link account-link">',
				'				<span class="icon icon-briefcase"></span>',
				'				My Business',
				'			</a>',
				'		</li>',	
				(h_config.showlogout?tplLogoutMobile.join(""):"")                
			];
			var i = 1; //starts at 1, skip first entry: Home, 			
			
			for(; i < data.length; i++) { 
				var item = data[i],
					title = item.name;				
				
				var tmp_tpl = m_nav_item
					.replace("{TITLE}", title)
					.replace("{URL}", (item.url.indexOf("http")<0? (wcmsHost + item.url): item.url ) )
					.replace("{MENU}", getMobileMenuHTML(item.items, title));				
					tmp_html.push(tmp_tpl);
			}			
			
			return m_nav_tpl.replace("{LIST}", tmp_html.join("\n"));
			
		};
		
		
		var getMobileMenuHTML = function( items_data, parent_title ) {
			if (!items_data || !items_data.length || items_data[0] == "" ) { return ""; }
			
			var temp_tpl = m_nav_subpanel.replace("{TITLE}", parent_title),
				temp_list = [],
				item;
			var i = 0;
			
			
			for (; i < items_data.length; i++ ) {
				var item = items_data[i];
				if(!item) continue;
				
				
				
				var temp_item_tpl = m_nav_item
					.replace("{TITLE}", item.name)
					.replace("{URL}", (item.url.indexOf("http")<0? (wcmsHost + item.url): item.url ) )
					.replace("{MENU}", getMobileMenuHTML(item.items, item.name ));;
				temp_list.push(temp_item_tpl);
			}
									
			//return [ m_expand_tpl, temp_tpl].join("\n");
			return [ m_expand_tpl, temp_tpl.replace("{MENU}", temp_list.join("\n"))].join("\n");
			
		};
	
		
		var tplLogoutMobile = [
'		<li class="mobile-nav-item">',
'			<a tabindex="-1" href="#" class="link logout-link" onclick="logoutClick();">',
'				<span class="icon icon-sign-out"></span>',
'				Logout',
'			</a>',
'		</li>'
];
	
	
		
		var tplLogout = [
'                                <div class="account">',
'                                    <a href="#" class="logout-link" onclick="logoutClick();">',           
'                                        <span class="icon icon-sign-out"></span>', 
'                                        <span class="account-text">Logout</span>',
'                                    </a>',
'                                </div>'
		                 ];
		

		
		
		var tpl = [
'		<!--[if lt IE 9]>',
'            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>',
'        <![endif]-->',

'        <div class="off-canvas-wrap"  data-offcanvas>',
'            <div class="inner-wrap">',

'                <div class="left-off-canvas-menu">',
getMobileNavHTML(config.nav_bar),
'                </div>',
'                <a href="javascript:;" class="exit-off-canvas">',
'                    <span class="visuallyhidden">Close mobile menu</span>',
'                </a>',

'                <a href="#" class="mobile-nav-close js-mobile-nav-close exit-off-canvas" tabindex="-1">',
'                    <span class="visuallyhidden">Close</span>',
'                    <span class="icon icon-chevron2-right"></span>',
'                    <span class="icon icon-chevron2-left"></span>',
'                </a>',

'            <!-- Add your site or application content here -->',

'                <header class="header" role="banner">',
'                    <div class="wrapper clearfix">',
'                        <div class="site-logo">',
'                            <a href="' + wcmsHost + '" tabindex="1" class="link">',
'                                <img src="' + h + '/images/site-logo.jpg" alt="Housing & Development Board Logo" class="site-logo-img">',
'                                <h2 class="visuallyhidden">Housing & Development Board Homepage</h2>',
'                            </a>',
'                        </div>',
'                        <a href="#main" tabindex="2" class="skiplink">Skip to main</a>',

'                        <section class="site-tools">',
'                            <h2 class="visuallyhidden">Site tools</h2>',
'                            <div class="singgov">',
'                                <a href="http://www.gov.sg" target="_blank" class="singgove-link">',
'                                    <img src="' + h + '/images/singapore_govt.jpg" alt="Singapore Government">',
'                                </a>',
'                            </div>',

'                            <nav class="header-nav desktop">',
'                                <ul class="list">',
'                                    <li class="header-nav-item">',
'                                        <a href="http://askhdb.hdb.gov.sg/" class="header-nav-link">FAQ</a>',
'                                    </li>',
'                                    <li class="header-nav-item">',
'                                        <a href="'+wcmsUrl+'/contact-us" class="header-nav-link">Contact Us</a>',
'                                    </li>',
'                                    <li class="header-nav-item">',
'                                        <a href="'+wcmsUrl+'/sitemap" class="header-nav-link">Sitemap</a>',
'                                    </li>',
'                                    <li class="header-nav-item">',

'                                        <a href="' + lnUrl + '/fi10/fi10400p.nsf/FI10FHDBService/?OpenForm&feature=feedback" class="header-nav-link">Feedback</a>',
'                                    </li>',
'                                </ul>',
'                            </nav>',

'                            <div class="right">',
'                                <div class="social-channels desktop">',
'                                    <a href="https://www.facebook.com/SingaporeHDB" target="_blank" class="social-channel fb">',
'                                        <span class="visuallyhidden">Facebook</span>',
'                                        <span class="icon icon-facebook"></span>',
'                                    </a>',
'                                    <a href="https://twitter.com/singapore_hdb" target="_blank" class="social-channel twitter">',
'                                        <span class="visuallyhidden">Twitter</span>',
'                                        <span class="icon icon-twitter"></span>',
'                                    </a>',
'                                    <a href="https://www.youtube.com/user/singaporeHDB" target="_blank" class="social-channel youtube">',
'                                        <span class="visuallyhidden">Youtube</span>',
'                                        <span class="icon icon-youtube-play"></span>',
'                                    </a>',
'                                </div>',
'                                <div class="site-search">',
'                                    <div action="/search/" class="form" role="search">',
'                                        <label for="inputSearch" class="visuallyhidden">Keyword</label>',
'                                        <input type="search" id="inputSearch" class="input-txt js-input-search ignore" name="searchKeyword" placeholder="Search our website">',
'                                        <button class="site-search-clear-btn js-clear-search" type="button">',
'                                            <span class="icon icon-cross"></span>',
'                                            <span class="visuallyhidden">Clear search</span>',
'                                        </button>',
'                                        <button type="submit" class="site-search-btn"  aria-label="submit form">',
'                                            <span class="visuallyhidden">Search</span>',
'                                            <span class="icon icon-search"></span>',
'                                        </button>',
'                                    </div>',
'                                </div>',
'                            </div>',
'                        </section>',
'                    </div>',

'                    <div class="nav-bar">',
'                        <div class="wrapper clearfix">',

'                            <button class="navbar-toggle left-off-canvas-toggle" type="button">',
'                                <span class="visuallyhidden">Toggle navigation</span>',
'                                <span class="icon-bar"></span>',
'                                <span class="icon-bar"></span>',
'                                <span class="icon-bar"></span>',
'                            </button>',
getPrimaryNavHTML(config.nav_bar),
'                            <div class="right clearfix">',
'                                <div class="mobile-site-search">',
'                                    <button class="mobile-site-search-toggle">',
'                                        <span class="visuallyhidden">Search</span>',
'                                        <span class="icon icon-search"></span>',
'                                    </button>',

'                                    <div action="/search/" class="mobile-site-search-form" role="search">',
'                                        <label for="inputSearchMobile" class="visuallyhidden">Search Keyword</label>',
'                                        <input type="search" id="inputSearchMobile" placeholder="Search our website" class="input-txt js-input-search ignore" name="searchKeyword">',
'                                        <button class="site-search-clear-btn js-clear-search" type="button">',
'                                            <span class="icon icon-cross"></span>',
'                                            <span class="visuallyhidden">Clear search</span>',
'                                        </button>',
'                                        <button type="submit" class="site-search-btn">',
'                                            <span class="visuallyhidden">Search</span>',
'                                            <span class="icon icon-search"></span>',
'                                        </button>',
'                                    </div>',
'                                </div>',
'                                <div class="account">',
'                                    <a href="#js-login" class="account-link highlight">',
'                                        <span class="icon icon-lock2"></span>',
'                                        <span class="account-text">Login</span>',
'                                    </a>',
'                               <div class="account-login-box">',
'                                        <a href="'+esvcUrl+'/webapp/FI10PPORTAL/FI10PAtAGlance.jsp" class="account-link account-login ">',
'                                 <span class="icon icon-user"></span>',
'                               <span class="account-text">Login to My HDBPage</span>',
'                               </a>',
'                              <a href="'+esvcUrl+'/webapp/FI10AWBIZ/FI10PBizOverview.jsp" class="account-link account-login ">',
'                               <span class="icon icon-briefcase"></span>',
'                               <span class="account-text">Login to My Business</span>',
'                              </a></div>',
'                                </div>',
(h_config.showlogout?tplLogout.join(""):""),
'                                <div class="alert active" style="display: none;">',
'                                    <a href="#" class="alert-link js-toggle-alert-bar">',
'                                        <span class="visuallyhidden">Alert</span>',
'                                        <span class="icon icon-warning"></span>',
'                                    </a>',
'                                </div>',
'                            </div>',
'                        </div>',
'                    </div>',
'                    <div class="alert-bar">',
//'                        <div class="wrapper">',
//'                            <h2 class="alert-bar-title"><span class="icon icon-warning"></span> Maintenance</h2>',
//'                            <p class="alert-bar-text">Please note that you may experience slow access to HDB e-Service on 6 Jul 2014 (Sun), from 1.00am to 1.00pm, due to maintenance works. <a class="alert-bar-link" href="#">Find out more about the maintenance details here</a>.</p>',
//'                            <a href="#" class="alert-bar-close js-alert-bar-close">',
//'                                <span class="icon icon-cross"></span>',
//'                                <span class="visuallyhidden">Close alert bar</span>',
//'                            </a>',
//'                        </div>',
'                    </div>',
'                </header>',		           
		           
		           ];
		
		
				
		document.write(tpl.join(""));
		//document.write(getPrimaryNavHTML(config.nav_bar));
		parent.nav_data = config.nav_bar;
		
		return parent;
		
	}(i3header || {}, {}));