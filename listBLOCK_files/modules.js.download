
/**
 *  RR UTILS - Alphabetical Pagination Scrolling
 */
var rr = (function(parent, $) {
    var $alphabetical_listing = $('.alphabetical-listing '),
        $result_list = $('.result-list', $alphabetical_listing),
        $pagination = $('.alphabetical-pagination', $alphabetical_listing);

    var set_absolute = function($result_list, $scroll_top, $pagination, window_height){
        if($result_list.offset().top > $scroll_top && $pagination.hasClass('is-fixed')) {
            // Pagination scrolled to the top
            // Use absolute positioning

            $pagination.removeClass('is-fixed');
            $pagination.css('top',10);
        }

        if($scroll_top < ( $result_list.offset().top + $result_list.outerHeight() - window_height) ){
            
            // If windows is not scrolled at the bottom of the page
            $pagination.removeClass('is-absolute-bottom');
        }
    }

    var set_fixed = function($result_list, $scroll_top, $pagination, window_height){                

        if($result_list.offset().top < $scroll_top && !$pagination.hasClass('is-fixed')) {
            
            // If the page is scrolled after the top position of the result list
            $pagination.addClass('is-fixed');

        }

        if( $scroll_top > ( $result_list.offset().top + $result_list.outerHeight() - window_height) ){
            
            // If the page is scrolled at the bottom of the page
            $pagination.addClass('is-absolute-bottom');
        }
    }
    
    var mobile_scrolling = function(){        
        
        // Handles the positioning update of the alphabets while the page is being scrolled.
        var temp = $(window).scrollTop();
         
        if( $(window).height() > 800 ){

            $('.alphabetical-pagination-item-link', $pagination).css('padding', '6px 4px');

        } else if( $(window).height() > 625 ){

            $('.alphabetical-pagination-item-link', $pagination).css('padding', '4px');

        }else if( $(window).height() >= 460 ){
            
            $('.alphabetical-pagination-item-link', $pagination).css('padding', '1px 4px');

        } 

        $(window).scroll(function(){

            var $window = $(window),
                window_height = $window.height(),
                $scroll_top = $window.scrollTop(),
                height_offset = $pagination.outerHeight() - window_height;



            if(temp > $scroll_top ) {

                set_absolute($result_list, $scroll_top, $pagination, window_height);

            }else{

                set_fixed($result_list, $scroll_top, $pagination, window_height);

            }

            temp = $scroll_top;

        });

    }; 

    var desktop_scrolling = function(){

        // Handles the positioning update of the alphabets while the page is being scrolled.
        var temp = temp = $(window).scrollTop();

        $(window).scroll(function(){

            var $window = $(window),
                window_height = $window.height(),
                $scroll_top = $window.scrollTop(),
                height_offset = $pagination.outerHeight() - window_height;                

            if(temp > $scroll_top ) {

                if( $pagination.hasClass('is-fixed') && ($pagination.outerHeight() > window_height) ){
                    // Scroll up the alphabets, while the page is scrolled up                    
                    
                    if( $pagination.position().top < 0 && ($pagination.position().top + 150) < 0) {
                        
                        // If the top of the alphabets not visible, add the top position
                        $pagination.css('top', $pagination.position().top + 150 );

                    }else{

                        // Else set the top position to 0
                        if(!$pagination.hasClass('is-absolute-bottom')) { 
                            $pagination.css('top',0);
                        }
                    }
                }

                set_absolute($result_list, $scroll_top, $pagination, window_height);

            }else if(temp < $scroll_top) {                

                if( $pagination.hasClass('is-fixed') && ($pagination.outerHeight() > window_height) ){
                    // Scroll down the alphabets, while the page is scrolled down
                    
                    if( Math.abs($pagination.position().top) < height_offset &&  Math.abs($pagination.position().top) + 150 < height_offset ){

                        // If the bottom of the alphabets not visible, substract the top position
                        $pagination.css('top', $pagination.position().top - 150 );

                    }else{

                        // Else set the top position to the bottom of the alphabet
                        $pagination.css('top', -height_offset - 20);
                    }
                }

                set_fixed($result_list, $scroll_top, $pagination, window_height);

            }

            temp = $scroll_top;

        });

    };

    var unbind_scrolling = function(){
        $(window).unbind('scroll');
    };

    var setup = function(){        

        $('.js-alphabetical-scroll', $pagination).on('click', function(e){
            e.preventDefault();
            
            if( $( $(this).attr('href')).length > 0 ){
                $('html, body').stop().animate({
                   'scrollTop':   $($(this).attr('href')).offset().top
                }, 700);
            }            
        });
    };


    /**
     * Export module method
     */
    parent.alphabeticalPagination = {
        setup: setup,
        mobile_scrolling : mobile_scrolling,
        desktop_scrolling : desktop_scrolling,
        unbind_scrolling : unbind_scrolling
    };

    return parent;

}(rr || {}, jQuery));

jQuery(function($){
    rr.alphabeticalPagination.setup();
});/**
 *  RR UTILS - Article Carousel
 */
var rr = (function(parent, $) {
    var $carousel = $('.carousel'),
        $carousel_prev = $('.js-carousel-prev', $carousel),
        $carousel_next = $('.js-carousel-next', $carousel),
        $js_carousel_nav = $('.js-carousel-nav', $carousel);

    var add_carousel_index = function(idx, length) {
        if(idx == length - 1 ){
            $js_carousel_nav.eq(0).addClass('active');
        }else{
            $js_carousel_nav.eq(idx + 1).addClass('active');
        } 
    };

    var reduce_carousel_index = function(idx, length) {
        if(idx < 1){
            $js_carousel_nav.eq(length -1).addClass('active');
        }else{
            $js_carousel_nav.eq(idx -1).addClass('active');
        }   
    };

    var setup = function(){

        var $internal_carousel = $('.wrapper', $carousel).swiper({
            mode:'horizontal',
            wrapperClass:'list',
            slideClass:'carousel-item',
            slidesPerView:1,
            loop:true,
            calculateHeight:true,
            onSlideNext: function(){
                var idx = $('.js-carousel-nav.active').index(),
                length = $js_carousel_nav.length;
                $js_carousel_nav.removeClass('active');
                add_carousel_index(idx, length);
            },
            onSlidePrev: function(){
                var idx = $('.js-carousel-nav.active').index(),
                length = $js_carousel_nav.length;
                $js_carousel_nav.removeClass('active');
                reduce_carousel_index(idx, length);
            }
        });

        $carousel_prev.click(function(e){            
            e.preventDefault();            
            $internal_carousel.swipePrev();
        });

        $carousel_next.click(function(e){            
            e.preventDefault();
            $internal_carousel.swipeNext();
        });

        $js_carousel_nav.click(function(e){
            var $this = $(this),
                idx = $this.index();

            $('.js-carousel-nav.active').removeClass('active');     
            e.preventDefault();
            $internal_carousel.swipeTo(idx);
            $this.addClass('active');       
        });
    };


    /**
     * Export module method
     */
    parent.articleCarousel = {
        setup: setup
    };

    return parent;

}(rr || {}, jQuery));

jQuery(function($){
    rr.articleCarousel.setup();
});/**
 *  RR Back to top 
 */

var rr = (function(parent, $) {

    var setup = function(){  

        var $window = $(window),
            $back_to_top = $('.back-to-top'),
            $back_to_top_btn = $('.js-back-to-top', $back_to_top);
        
        $back_to_top_btn.click(function(e){
            e.preventDefault();
            $('html,body').animate({
                scrollTop:0 
            });
        });

        $window.scroll(function(){
            if($window.scrollTop()>0 && !$back_to_top.hasClass('is-visible')){
                $back_to_top.addClass('is-visible');
            }else if ($window.scrollTop()===0 && $back_to_top.hasClass('is-visible')) {
                $back_to_top.removeClass('is-visible');
            }

        });
    };


    /**
     * Export module method
     */
    parent.backToTop = {
        setup: setup
    };

    return parent;

}(rr || {}, jQuery));

jQuery(function($){
    rr.backToTop.setup();
});/**
 *  RR UTILS - Banner Image Positioning
 *  Used to centre banner images horizontally.
 *
 *  Create a new Image() to get the actual width of the banner, the apply margin according to the width
 *
 */
var rr = (function(parent, $) {

    var align_images = function(image, $obj, window_width){
        if($obj.length>0){
            image.src = $obj.attr('src');

            image.onload = function(){

                // Only apply margin if the image is smaller than the viewport
                if( image.naturalWidth > window_width) {
                    $obj.css('margin-left', image.naturalWidth * -0.5 );
                    $obj.css('left', '50%');
                }else{

                    // Reset
                    $obj.css('margin-left', 0 );
                    $obj.css('left', 0);
                }
            }
        }
    }


    var setup = function(){
        var $featured_article = $('.featured-article'),
            $featured_images = $('.img', $featured_article),
            $header_banner = $('.header-banner > .img'),
            $window = $(window),
            image = null;

        // Initial process on load
        $featured_images.each(function(idx){
            var $this = $(this),
                image = new Image();

            align_images(image, $this, $window.width());
        });

        // Initial process on load
        var image_banner = new Image();
        align_images(image_banner, $header_banner, $window.width());

        //On resize adjust image alignment
        $window.on('resize', Foundation.utils.throttle(function(e){
            var window_width = $(this).width();

            $featured_images.each(function(idx){
                var $this = $(this),
                    image = new Image();

                align_images(image, $this, window_width);
            });

            var image_banner = new Image();
            align_images(image_banner, $header_banner, window_width);

        }, 500 ));

    };


    /**
     * Export module method
     */
    parent.bannerImagePositioning = {
        setup: setup
    };

    return parent;

}(rr || {}, jQuery));

jQuery(function($){
    rr.bannerImagePositioning.setup();
});/**
 *  RR UTILS - JS workaround for IE9 bg transition
 */
var rr = (function(parent, $) {
    var $main = $('#main'),
        hdb_red = '#cc0001',
        hdb_teal = '#0c8188',
        dark_red = '#a00a19',
        white = '#ffffff',
        bg_pos_y;

    var setup = function(){

         if($('.lt-ie10').length>0) {
            $('.btn').not('.faq-btn, .subscribe-btn')
                .on('mouseenter', function() {
                    
                    $(this).animate(
                        {backgroundColor: dark_red}, 100
                    );
                })
                .on('mouseleave' , function() {
                    
                    $(this).animate(
                        {backgroundColor: hdb_red}, 100
                    );
                });   

            $('.btn-white').on('mouseenter', function() {
                
                $(this).animate(
                    {backgroundColor: hdb_red}, 200
                );
            }).on('mouseleave' , function() {
                
                $(this).animate(
                    {backgroundColor: white}, 200
                );
            });

            $('.video-banner-link').on('mouseenter', function() {
                
                $('.btn-white', this).animate(
                    {backgroundColor: hdb_red}, 200
                );
            }).on('mouseleave' , function() {
                
                $('.btn-white', this).animate(
                    {backgroundColor: white}, 200
                );
            });

            $('.faq-btn').on('mouseenter', function() {
                
                $(this).animate(
                    {backgroundColor: white}, 300
                );
            }).on('mouseleave' , function() {
                
                $(this).animate(
                    {backgroundColor: hdb_teal}, 200
                );
            });

            $('.subscribe-btn').on('mouseenter', function() {
                
                $(this).animate(
                    {backgroundColor: dark_red}, 300
                );
            }).on('mouseleave' , function() {
                
                $(this).animate(
                    {backgroundColor: white}, 150
                );
            });

            $('.feature-tab-control-link').on('mouseenter', function() {
                

                $this = $(this);
                $icon = $(this).find('.feature-tab-control-icon');

                $icon.stop().animate(
                    {                         
                        backgroundColor: hdb_teal 
                    }, 300
                );
            }).on('mouseleave' , function() {
                

                $this = $(this);
                $icon = $(this).find('.feature-tab-control-icon');

                $icon.stop().animate(
                    {
                        backgroundColor: '#ffffff'
                    }, 300
                );
            });
        }

           
    };


    /**
     * Export module method
     */
    parent.bgTransitionIE = {
        setup: setup
    };

    return parent;

}(rr || {}, jQuery));

jQuery(function($){
    rr.bgTransitionIE.setup();
});/**
 *  RR UTILS - Composer
 *  Used to update components layout based on media queries
 */
var rr = (function(parent, $) {


    var mobile_composer = function(){
        var $side_listing = $('.side-listing'),
            $services_search = $('.full-screen-search'),
            $services_listing = $('.services-listing'),
            $interest_links = $('.interest-links'),
			$secondary_nav = $('.secondary-nav'),
            $content_section = $('.content-section');

        $interest_links.detach();
        $content_section.append($interest_links);
		
        $side_listing.detach();
        $content_section.append($side_listing);

        $services_search.detach();
        $services_search.insertBefore($secondary_nav);
	   
        

        $('.service-desc', $services_listing).addClass('is-stacked');
        $('.service-col', $services_listing).addClass('is-stacked');

    };

    var tablet_composer = function(){


        var $secondary_nav = $('.secondary-nav'),
            $side_listing = $('.side-listing'),
            $services_search = $('.full-screen-search'),
            $services_listing = $('.services-listing'),
            $interest_links = $('.interest-links'),
            $content_section = $('.content-section');

        $interest_links.detach();
        $content_section.append($interest_links);
		
        $side_listing.detach();
        $content_section.append($side_listing);

        $services_search.detach();
        $services_search.insertBefore($secondary_nav);
		
        $('.service-desc', $services_listing).addClass('is-stacked');
        $('.service-col', $services_listing).addClass('is-stacked');
    };

    var desktop_composer = function(){
        var $secondary_nav = $('.secondary-nav'),
            $side_listing = $('.side-listing'),
            $services_search = $('.full-screen-search'),
            $services_listing = $('.services-listing'),
            $interest_links = $('.interest-links');

        $secondary_nav.detach();
        $('.aside ').prepend($secondary_nav);

        $side_listing.detach();
        $('.aside').append($side_listing);

        $services_search.detach();
        $('.header-banner .wrapper').append($services_search);

        $interest_links.detach();
        $('.main-content').append($interest_links);

        $('.service-desc', $services_listing).removeClass('is-stacked');
        $('.service-col', $services_listing).removeClass('is-stacked');
    };

    var setup = function(){

    };


    /**
     * Export module method
     */
    parent.composer = {
        setup: setup,
        mobile_composer: mobile_composer,
        tablet_composer: tablet_composer,
        desktop_composer: desktop_composer
    };

    return parent;

}(rr || {}, jQuery));

jQuery(function($){
    rr.composer.setup();
});/**
 *  RR UTILS - eServices scripts
 */
var rr = (function(parent, $) {
    var $services_listing = $('.services-listing');


    var setup = function(){
        $('.js-bookmark').click(function(e){
            e.preventDefault();
            var $list_item = $(this).closest('.list-item'),
                $bookmark_icons = $list_item.find('.icon-bookmark');

            $bookmark_icons.toggleClass('is-bookmarked');
        });

        $('.js-service-expand', $services_listing).unbind().click(function(e){
            e.preventDefault();

            var $this = $(this),
                $list_item = $this.parent().parent().parent();

            if($list_item.hasClass('is-expanded')){
                $list_item.removeClass('is-expanded');
            }else{
                $('.list-item.is-expanded', $services_listing).removeClass('is-expanded');
                $list_item.addClass('is-expanded');
                $('html,body').animate({
                    scrollTop: $('.service-section-header', $list_item).offset().top
                });
            }
        });
    };


    /**
     * Export module method
     */
    parent.eservices = {
        setup: setup
    };

    return parent;

}(rr || {}, jQuery)); 
jQuery(function($){
    rr.eservices.setup();
});/**
 *  RR UTILS - Footer Carousel
 */
var rr = (function(parent, $) {
    var footer_carousel_instance,
        $footer_carousel = $('#main .multi-item-carousel');

    var setup = function(){  
        $('.js-carousel-prev', $footer_carousel).click(function(e){
            e.preventDefault();            
            footer_carousel_instance.swipePrev();
        });

        $('.js-carousel-next', $footer_carousel).click(function(e){
            e.preventDefault();
            footer_carousel_instance.swipeNext();
        });
    };

    var mobile = function(){        
        footer_carousel_instance = null;

        if($footer_carousel.length > 0) {
            footer_carousel_instance = $('.wrapper', $footer_carousel).swiper({
                mode:'horizontal',
                wrapperClass:'list',
                slideClass:'multi-item-carousel-item',
                loop:true,
                calculateHeight: true                
            });
        }
    };

    var small = function(){
        footer_carousel_instance=null;

        if($footer_carousel.length > 0) {
            footer_carousel_instance = $('.wrapper', $footer_carousel).swiper({
                mode:'horizontal',
                wrapperClass:'list',
                slideClass:'multi-item-carousel-item',
                slidesPerView:2,
                slidesPerGroup:2,
                loop:true,
                calculateHeight: true
            });
        }
    };

    var tablet = function(){
        footer_carousel_instance=null;

        if($footer_carousel.length > 0) {
            footer_carousel_instance = $('.wrapper', $footer_carousel).swiper({
                mode:'horizontal',
                wrapperClass:'list',
                slideClass:'multi-item-carousel-item',
                slidesPerView:4,
                slidesPerGroup:4,
                loop:true,
                calculateHeight: true
            });
        }

    };

    var desktop = function(){
        footer_carousel_instance=null;

        if($footer_carousel.length > 0) {
            footer_carousel_instance = $('.wrapper', $footer_carousel).swiper({
                mode:'horizontal',
                wrapperClass:'list',
                slideClass:'multi-item-carousel-item',
                slidesPerView:6,
                loop:true,
                slidesPerGroup: 6,
                calculateHeight: true
            });
        }
    };


    /**
     * Export module method
     */
    parent.footerCarousel = {
        setup: setup,
        mobile: mobile,
        small: small,
        tablet: tablet,
        desktop: desktop
    };

    return parent;

}(rr || {}, jQuery));

jQuery(function($){
    rr.footerCarousel.setup();
});/**
 *  RR UTILS - Homepage Features Tab
 *
 *  Plugin used for carousel: http://www.idangero.us/sliders/swiper/
 *  
 *  Carousel only initialized in mobile viewport. Tablet and desktop do not initialize carousel.
 *  
 */

var rr = (function(parent, $) {
    var feature_tab_carousel_option,
        $feature_tab_carousel,
        $feature_tab_toggle = $('.feature-tab .js-toggle-tab'),
        hdb_red = '#cc0001';

    var setup = function(){  
        feature_tab_carousel_option = {
            mode:'horizontal',
            wrapperClass:'list',
            slideClass:'feature-box'
        };
    };


    var feature_tabs_event_mobile = function($this,  $feature_tab_carousel, init, feature_reset){

        // Events codes include tablet view as well
        // In tablet view, carousel is not initialized

        var $parent = $this.parent().parent(),              
            $arrow_icon = $('.icon-chevron-down', $this),
            $feature_tab_active = $('.feature-tab.active'),
            $anchor_offset;

        $('.feature-tab-content', $feature_tab_active).stop().slideUp(function(){
            $feature_tab_active.removeClass('active');
        });
        

        if( $parent.hasClass('active')){
            
            $('.feature-tab-content', $parent).stop().slideUp(function(e){
                $parent.removeClass('active');
            });

            $arrow_icon.animateRotate(180,0);

        }else{
            
            // Initialize carousel only in mobile
            if(init){
                $feature_tab_carousel = $('.feature-box-list', $parent).swiper(feature_tab_carousel_option);    
            }
            $arrow_icon.animateRotate(0,180);

            $('.feature-tab-content', $parent).stop().slideDown(function(e){
                $parent.addClass('active');

                // Anchor newly opened tab to the top of the page                
                if(!feature_reset) {

                    $anchor_offset = $this.offset().top;
                    $(document).scrollTop($anchor_offset);
                }
                $(document).foundation('equalizer', 'reflow');
            });            
        }
        
    }

    var move_chevron = function($active_tab){
        // animate chevron movement on tab clicking
        var left_offset = $active_tab.offset().left,
            tab_width = $active_tab.outerWidth(),            
            $chevron = $('#main .chevron-wrapper');

        $chevron.stop().animate({
            left:  left_offset + (tab_width/2) - ($chevron.outerWidth()/2)
        },500, function(){         

        });
    }

    var feature_tabs_event = function($this,  $feature_tab_carousel){
        // Events triggered in desktop view

        var $parent = $this.parent().parent(),  
            $feature_tab_content_desktop = $('.feature-tabs .feature-tab-content-desktop'),
            $feature_tab_active = $('.feature-tab.active'),
            wrapper_content_clone;
        
        // Clone existing wrapper content 
        // Remove existing content from DOM
        // Fadein cloned content
        wrapper_content_clone = $('.wrapper',$feature_tab_content_desktop).clone().html($('.feature-tab-content', $parent).html());
        $('.wrapper',$feature_tab_content_desktop).remove();
        wrapper_content_clone.hide();
        wrapper_content_clone.appendTo( $feature_tab_content_desktop );
        wrapper_content_clone.fadeIn(700);

        // Initial load 
        if(!$feature_tab_content_desktop.hasClass('active')){
            $feature_tab_content_desktop.addClass('active');
        }
        

        if($('.lt-ie10').length>0) {

            $('.feature-tab-content-desktop .btn-white').on('mouseenter', function() {
                
                $(this).animate(
                    {backgroundColor: hdb_red}, 200
                );
            }).on('mouseleave' , function() {

                $(this).animate(
                    {backgroundColor: '#ffffff'}, 200
                );
            });    
        }

        // Reinitialize Foundation 5 equalizer script when tab content updated
        $(document).foundation('equalizer', 'reflow');
        
        $feature_tab_active.removeClass('active');
        $parent.addClass('active');

        move_chevron($parent);
    }

    var feature_tabs_reset = function(mobile){
        // Composer/Relayout
        // Called in the event of browser resizing, and the layout of Feature tabs changed.
        
        
        var $feature_tabs = $('#main .feature-tabs'),
            $feature_tab_content = $('.feature-tab-content', $feature_tabs),
            $feature_tab_content_desktop = $('.feature-tab-content-desktop', $feature_tabs),
            $active_feature_tab = $('.feature-tab.active');

        if(mobile){
            if($feature_tab_content_desktop.is(':visible')){
                $('.icon-chevron-down', $feature_tabs).animateRotate(180,0);
                $feature_tab_content_desktop.hide();
                $active_feature_tab.removeClass('active');
            }
            
        }else{

            if($feature_tab_content.is(':visible')){
                $feature_tab_content.hide(); 
                $active_feature_tab.removeClass('active');
            }

            if(!$feature_tab_content_desktop.is(':visible')) { 
                $feature_tab_toggle.eq(0).trigger('click');
            }

        }
    }

    var feature_tab_unbind = function(destroy){
        //Unbind and destroy carousel instances

        $feature_tab_toggle.unbind();
            
        if(destroy){
            if($feature_tab_carousel !=undefined && $feature_tab_carousel.destroy!=undefined) { 
                $feature_tab_carousel.destroy(); 
            }
        }
    };

    var mobile = function(){   
        feature_tab_carousel_option = {
            mode:'horizontal',
            wrapperClass:'list',
            slideClass:'feature-box',
            calculateHeight: true
        };
        $feature_tab_carousel = $('.feature-tab.active .feature-box-list').swiper(feature_tab_carousel_option); 

        $feature_tab_toggle.click(function(e){
            e.preventDefault();
            $this = $(this);

            feature_tabs_event_mobile($this, $feature_tab_carousel, true, false);
        });

        feature_tabs_reset(true);
       
    };

    var small = function(){
        feature_tab_carousel_option = {
            mode:'horizontal',
            wrapperClass:'list',
            slideClass:'feature-box',
            slidesPerView: 2,
            calculateHeight: true
        };

        $feature_tab_carousel = $('.feature-tab.active .feature-box-list').swiper(feature_tab_carousel_option); 
       
        $feature_tab_toggle.click(function(e){
            e.preventDefault();
            $this = $(this);
            feature_tabs_event_mobile($this, $feature_tab_carousel, true, false);
        });

        feature_tabs_reset(true);
    };

    var tablet = function(){
        
        $feature_tab_toggle.click(function(e){
            e.preventDefault();
            $this = $(this);
            feature_tabs_event_mobile($this, $feature_tab_carousel, false, false);
        });

        feature_tabs_reset(true);
        
    };

    var desktop = function(){
        
        $feature_tab_toggle.on('click', Foundation.utils.debounce(function(e){
            
            $this = $(this);

            if(!$this.parent().parent().hasClass('active')){
                feature_tabs_event($this, $feature_tab_carousel);
            }
            return false;
        }, 400, false));

        feature_tabs_reset(false);

        $(window).on('resize', Foundation.utils.throttle(function(e){
            if($('.feature-tab.active').length>0){
                move_chevron($('.feature-tab.active'));
            }
        }, 300 ));
    };


    /**
     * Export module method
     */
    parent.homepageFeaturesTab = {
        setup: setup,
        feature_tab_unbind: feature_tab_unbind,
        small: small,
        mobile: mobile,
        tablet: tablet,
        desktop: desktop
    };

    return parent;

}(rr || {}, jQuery));

jQuery(function($){
    rr.homepageFeaturesTab.setup();
});/**
 *  RR UTILS - Live Search
 */
var rr = (function(parent, $) {
    var $alphabetical_listing = $('.alphabetical-listing '),
        $result_list = $('.result-list', $alphabetical_listing);

    var populate = function(json_input){
        var html = '',
            ctr = 0,
            arr_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

        $.getJSON( json_input, function( data ) {
            var temp_id='',
                prev_id='';

            $.each( data.data, function( key, val ) {

                // Set ID for the first item in alphabet list
                for ( var i =0; i< arr_letters.length; i++ ){
                    if( val.title.toLowerCase().charAt(0) == arr_letters[i]){
                        temp_id = 'index' + arr_letters[i];

                        if( val.title.charAt(0) != prev_id.charAt(prev_id.length-1)){
                            temp_id = 'index' + arr_letters[i].toUpperCase();
                            prev_id = temp_id;
                        }else{
                            temp_id = '';
                        }
                    }
                }

                if(temp_id!=''){
                    html += '<li class="alphabetical-listing-item" id="'+temp_id+'">';
                }else{
                    html += '<li class="alphabetical-listing-item">';
                }

                html +=         '<h2 class="alphabetical-listing-item-title">';
                html +=             val.title;
                html +=         '</h2>';
                html +=         '<p class="alphabetical-listing-item-text">';
                html +=             val.text;
                html +=         '</p>';
                html +=     '</li>';
            });

            $result_list.html(html);
        });
    }

    var setup = function(){
        $('#inputLiveSearch').hideseek({
            list: '.alphabetical-listing .result-list',
            nodata :'No data available'
        });

    // populate(h_config.rschost+'/js/data.json');
    };


    /**
     * Export module method
     */
    parent.liveSearch = {
        setup: setup
    };

    return parent;

}(rr || {}, jQuery));

jQuery(function($){
    rr.liveSearch.setup();
});/**
 *  RR UTILS - Mega menu
 */
var rr = (function(parent, $) {
    var $primary_nav_item = $('.primary-nav .js-primary-nav'),
        myTimeout;

    var setup = function(){  
    };

    var desktop = function() {

        // Hover intent is used to make navigation in mega menu easier.
        // Mouse out movement will not hide the panel straight away.

        $primary_nav_item.hoverIntent({
            over: function(){

                var $this = $(this);                

                $this.addClass('on-hover')
                     .find('.megamenu-panel')
                     .stop().fadeIn(200,function(){

                        $(this).addClass('active');                
                });

            },
            out: function(){
                var $this = $(this);
                

                $this.removeClass('on-hover')
                     .find('.megamenu-panel')
                     .stop().fadeOut(100,function(){

                        $(this).removeClass('active');
                });
            },
            timeout: 300 
        });

        $('.js-mega-nav').hoverIntent({
            over: function(){
                var $this = $(this),
                    $tertiaries = $this.find('.megamenu-sub-panel'),
                    $preview = $this.parent().parent().parent().find('.preview');

                $this.addClass('on-hover');
                
                if($tertiaries.length>0){

                    $tertiaries.show().addClass('active');
                    $preview.removeClass('active');
                }
            },
            out: function(){
                var $this = $(this),
                    $tertiaries = $this.find('.megamenu-sub-panel'),
                    $preview = $this.parent().parent().parent().find('.preview');

                $this.removeClass('on-hover');
                $tertiaries.stop().fadeOut(200).removeClass('active');
                $preview.addClass('active');                
            },
            timeout: 250
        });
    };

    /**
     * Export module method
     */
    parent.megaMenu = {
        setup: setup,
        desktop: desktop
    };

    return parent;

}(rr || {}, jQuery));

jQuery(function($){
    rr.megaMenu.setup();
});/**
 *  RR UTILS - Mobile menu
 */
var rr = (function(parent, $) {
    var $navbar_toggle = $('.nav-bar .js-navbar-toggle'),
        $mobile_nav_close = $('.js-mobile-nav-close'),
        $mobile_nav_expand = $('.mobile-nav .js-mobile-nav-expand'),
        $mobile_nav_back = $('.mobile-nav .js-mobile-nav-back');


    var setup = function(){  
    };

    var mobile = function() {
        
        $navbar_toggle.click(function(e){
            if($mobile_nav_close.hasClass('active')){
                $mobile_nav_close.removeClass('active');
            }else{                
                $mobile_nav_close.addClass('active');
            }            
        });

        $mobile_nav_close.click(function(e){
            $mobile_nav_close.removeClass('active');
        });

        $mobile_nav_expand.click(function(e){
            var $mobile_nav_subpanel = $(this).next('.mobile-nav-subpanel');
            $mobile_nav_subpanel.show();

            $('.js-mobile-nav-expand', $mobile_nav_subpanel).each(function(index) {                
                var $this = $(this);
                $this.css('height', $this.parent().height() );
            });
            
            $mobile_nav_subpanel.animate({
                left:0
            },500);
        });

        $mobile_nav_back.click(function(e){
            var $mobile_nav_subpanel = $(this).parent().parent();
            $mobile_nav_subpanel.animate({
                left:'100%'
            },500,function(){
                $mobile_nav_subpanel.hide();
            });
        });

        $mobile_nav_expand.each(function(index) {
            var $this = $(this);
            $this.css('height', $this.parent().height() );
        });
    };

    /**
     * Export module method
     */
    parent.mobileMenu = {
        setup: setup,
        mobile: mobile
    };

    return parent;

}(rr || {}, jQuery));

jQuery(function($){
    rr.mobileMenu.setup();
});/**
 *  RR UTILS - Secondary Navigation
 */
var rr = (function(parent, $) {
    var $carousel = $('.carousel');

    var setup = function(){  


        // Desktop
        $('.secondary-nav').on('click','.js-secondary-nav-toggle',function(e){

            var $this = $(this),
                $subnav = $this.next('.list');
                
            e.preventDefault();

            if ( $subnav.hasClass('active') ){
                $this.animateRotate(180,0);
                $subnav.slideUp(function(){
                    $(this).removeClass('active');
                });
            }else{
                $this.animateRotate(0,180);
                $subnav.slideDown(function(){
                    $(this).addClass('active');
                });
            }
        });

        //Mobile
        $('.secondary-nav').on('click','.js-toggle-shortcut', function(e){
            e.preventDefault();
            $this = $(this);
            $secondary_nav_list = $this.parent().next('.list');

            if($secondary_nav_list.hasClass('active')){
                $('.icon',$this).animateRotate(180,0);
                $secondary_nav_list.slideUp(function(){
                    $secondary_nav_list.removeClass('active');                    
                });
            }else{
                $('.icon',$this).animateRotate(0,180);
                $secondary_nav_list.slideDown(function(){
                    $secondary_nav_list.addClass('active');                    
                });
            }
            

        });
        
    };


    /**
     * Export module method
     */
    parent.secondaryNavigation = {
        setup: setup
    };

    return parent;

}(rr || {}, jQuery));

jQuery(function($){
    rr.secondaryNavigation.setup();
});/**
 *  RR UTILS - Site Search module
 *  Events listener related to search
 */
var rr = (function(parent, $) {

    var $alert_bar = $('.header .alert-bar'),
        $clear_search = $('.js-clear-search'),
        $input_search = $('.js-input-search'),
        $mobile_search = $('.mobile-site-search-form');

    var setup = function(){

        $input_search.keyup(function(e){
            var $this = $(this),
                $clear_search = $this.next('.js-clear-search');

            if($this.val()!==''){
                $clear_search.show();
            }else{
                $clear_search.hide();
            }
        });

        $clear_search.click(function(e){
            e.preventDefault();
            var $this = $(this),
                $input_search = $this.parent().find('.js-input-search');

            $input_search.val('');
            $this.hide();
        });

        $('.mobile-site-search-toggle').click(function(e){
            e.preventDefault();

            if($alert_bar.is(':visible')){
                $alert_bar.slideUp(function(){
                    $('.alert.active').removeClass('active');
                });
            }

            if($mobile_search.is(':visible')){
                $mobile_search.slideUp();
            }else{
                $mobile_search.slideDown();
            }
        });
    };


    /**
     * Export module method
     */
    parent.siteSearch = {
        setup: setup
    };

    return parent;

}(rr || {}, jQuery));

jQuery(function($){
    rr.siteSearch.setup();
});