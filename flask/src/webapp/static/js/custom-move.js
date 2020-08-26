var socket = io.connect("http://"+document.domain+":"+location.port+"/socket.io/mynamespace");
// [True cnt, True conf, False cnt, False conf]
var listA = [0,0,0,0]
var listB = [0,0,0,0]

$(window).load(function () {

    // preloader
    $('#status').fadeOut(); // will first fade out the loading animation
    $('#preloader').delay(550).fadeOut('slow'); // will fade out the white DIV that covers the website.
    $('body').delay(550).css({
        'overflow': 'visible'
    });

    $('.portfolio_filter a').click(function () {
        $('.portfolio_filter .active').removeClass('active');
        $(this).addClass('active');

        var selector = $(this).attr('data-filter');
        $container.isotope({
            filter: selector,
            animationOptions: {
                duration: 500,
                animationEngine: "jquery"
            }
        });
        return false;
    });

    // back to top
    var offset = 300,
        offset_opacity = 1200,
        scroll_top_duration = 700,
        $back_to_top = $('.cd-top');

    //hide or show the "back to top" link
    $(window).scroll(function () {
        ($(this).scrollTop() > offset) ? $back_to_top.addClass('cd-is-visible'): $back_to_top.removeClass('cd-is-visible cd-fade-out');
        if ($(this).scrollTop() > offset_opacity) {
            $back_to_top.addClass('cd-fade-out');
        }
    });

    //smooth scroll to top
    $back_to_top.on('click', function (event) {
        event.preventDefault();
        $('body,html').animate({
            scrollTop: 0,
        }, scroll_top_duration);
    });

    // input
    $(".input-contact input, .textarea-contact textarea").focus(function () {
        $(this).next("span").addClass("active");
    });
    $(".input-contact input, .textarea-contact textarea").blur(function () {
        if ($(this).val() === "") {
            $(this).next("span").removeClass("active");
        }
    });

    /* Socket */
    socket.on('responseA', function(data) {
        if(data["result"]=="True"){
            listA[0]+=1
            listA[1]+=data["confidence"]
        }else{
            listA[2]+=1
            listA[3]+=(1-data["confidence"])
        }
    });

    socket.on('responseB', function(data) {
        if(data["result"]=="True"){
            listB[0]+=1
            listB[1]+=data["confidence"]
        }else{
            listB[2]+=1
            listB[3]+=(1-data["confidence"])
        }
    });
});