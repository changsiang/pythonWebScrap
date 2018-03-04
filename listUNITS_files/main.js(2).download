
$(function(){

	// Call Foundation 5 scripts
	$(document).foundation({
	    equalizer: {
	        equalize_on_stack: true
	    }
	});

	//IE9 placeholder polyfill
	if (!Modernizr.input.placeholder) {
		$('input[placeholder], textarea[placeholder]').placeholder();
	}

	$.fn.animateRotate = function(startangle, angle, duration, easing, complete) {
		return this.each(function() {
			var $elem = $(this);

			$({deg: startangle}).animate({deg: angle}, {
				duration: duration,
				easing: easing,
				step: function(now) {
					$elem.css({
						transform: 'rotate(' + now + 'deg)'
					});
				},
				complete: complete || $.noop
			});
		});
	};

	$('.dark-site-updates-content .js-show-updates').click(function(e){
		e.preventDefault();

		var $this = $(this),
			$list = $this.parent().find('.list'),
			$hidden_items = $list.find('.is-hidden'),
			$btn_text = $this.find('.btn-text');

		if($list.hasClass('is-expanded')){
			$hidden_items.fadeOut();
			$btn_text.html('View more');
			$list.removeClass('is-expanded');
		}else{

			$hidden_items.fadeIn();
			$btn_text.html('View less');
			$list.addClass('is-expanded');
		}

	});

	$('.myhdb-info .js-myhdb-info-expand').click(function(e){
		var $this = $(this),
			$myhdb_summary = $this.parent();

		if ($myhdb_summary.hasClass('is-expanded')){
			$myhdb_summary.removeClass('is-expanded');
			$myhdb_summary.find('.is-hidden').fadeOut();
			$this.find('.cta-text').text('View more');
		}else{
			$myhdb_summary.addClass('is-expanded');
			$myhdb_summary.find('.is-hidden').fadeIn();
			$this.find('.cta-text').text('view less');
		}
	});


	// Facebook, Twitter tab toggle
	$('.social-feeds .js-tab-toggle').click(function(e){
		var $this = $(this),
			$active_control_tab = $('.social-feed-control-tab.active'),
			$social_feeds_tab = $('.social-feeds-tab'),
			$active_feed_tab = $('.social-feeds-tab.active');

		if(!$this.hasClass('active')){
			$active_control_tab.removeClass('active');
			$this.addClass('active');

			$active_feed_tab.hide();
			$active_feed_tab.removeClass('active');

			$social_feeds_tab.eq($this.index()).stop().fadeIn(function(){
				$(this).addClass('active');
			});
		}
	});

	$('.listing-sort .js-sort-link').click(function(e){
		$this = $(this);

		if($this.hasClass('active')){
			$this.toggleClass('asc');
		}else{
			$('.listing-sort .js-sort-link.active').removeClass('active');
			$this.addClass('active');
		}
	});

	$('#main .accordion-navigation > a').on('click',function(e){
		var $this = $(this);

		// Set timeout so Foundation 5 event listener will be triggered first
		setTimeout(
			function(){
				$('html,body').animate({
		            scrollTop: $this.offset().top
		        });
			}
		,300);
	});


	// Date picker in listing pages
	var pickerFrom = new Pikaday({
		field: document.getElementById('fromDate'),
		onSelect: function(date) {
			pickerTo.setMinDate(date);
		}
	});


	var pickerTo = new Pikaday({
		field: document.getElementById('toDate'),
		onSelect: function(date){
			pickerFrom.setMaxDate(date);
		}
	});


	// Media queries specific JS
	var queries = [
	{
		context: ['mobile'],
		match: function() {
			rr.homepageFeaturesTab.mobile();
			rr.footerCarousel.mobile();
			rr.mobileMenu.mobile();
			rr.composer.mobile_composer();

			if($('.alphabetical-listing-page').length>0){
				rr.alphabeticalPagination.mobile_scrolling();
			}
		}, unmatch:function(){
			rr.homepageFeaturesTab.feature_tab_unbind(true);
			rr.alphabeticalPagination.unbind_scrolling();
		}
	},
	{
		context: 'small',
		match: function() {
			rr.homepageFeaturesTab.small();
			rr.footerCarousel.small();
			rr.mobileMenu.mobile();
			rr.composer.mobile_composer();

			if($('.alphabetical-listing-page').length>0){
				rr.alphabeticalPagination.mobile_scrolling();
			}


		}, unmatch:function(){
			rr.homepageFeaturesTab.feature_tab_unbind();
			rr.alphabeticalPagination.unbind_scrolling();
		}
	},
	{
		context: ['tablet'],
		match: function() {

			rr.homepageFeaturesTab.tablet();
			rr.footerCarousel.tablet();
			rr.mobileMenu.mobile();

			rr.composer.tablet_composer();

			if($('.alphabetical-listing-page').length>0){
				rr.alphabeticalPagination.mobile_scrolling();
			}

		},
		unmatch: function(){
			rr.homepageFeaturesTab.feature_tab_unbind();
			rr.alphabeticalPagination.unbind_scrolling();
		}
	},
	{
		context: 'desktop',
		match: function() {
			rr.homepageFeaturesTab.desktop();
			rr.footerCarousel.desktop();
			rr.megaMenu.desktop();


			rr.composer.desktop_composer();

			if($('.alphabetical-listing-page').length>0){
				rr.alphabeticalPagination.desktop_scrolling();
			}


			$('.video-banner .js-video-lightbox').fancybox({
				helpers : {
					media : {},
					overlay: {
				      locked: false
				    }
				},
				padding:0
			});


		},
		unmatch:function(){
			rr.homepageFeaturesTab.feature_tab_unbind();
			$('.video-banner').unbind('click.fb-start');
			rr.alphabeticalPagination.unbind_scrolling();
		}
	},
	{
		context: 'extralarge',
		match: function() {
			rr.homepageFeaturesTab.desktop();
			rr.footerCarousel.desktop();
			rr.megaMenu.desktop();

			rr.composer.desktop_composer();


			if($('.alphabetical-listing-page').length>0){
				rr.alphabeticalPagination.desktop_scrolling();
			}

			$('.video-banner .js-video-lightbox').fancybox({
				helpers : {
					media : {},
					overlay: {
				      locked: false
				    }
				},
				padding:0
			});



		},unmatch: function(){
			rr.homepageFeaturesTab.feature_tab_unbind();
			$('.video-banner').unbind('click.fb-start');
			rr.alphabeticalPagination.unbind_scrolling();
		}
	}
	];

	MQ.init(queries);


});