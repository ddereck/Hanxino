
'use strict';
 
(function ($) {

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");
    });

    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    /*------------------
		Navigation
	--------------------*/
    $(".mobile-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });
    
    /*--------------------------
        Event Slider
    ----------------------------*/
    $(".event__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: false,
        nav: true,
        navText: ["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        responsive: {
            992: {
                items: 3,
            },
            768: {
                items: 2,
            },
            0: {
                items: 1,
            },
        }
    });
    
/*--------------------------
        About Slider
    ----------------------------*/

    $(".about_pic__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 4,
        dots: false,
        nav: true,
        navText: ["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        responsive: {
            992: {
                items: 4,
            },
            768: {
                items: 3,
            },
            576: {
                items: 2,
            },
            0: {
                items: 1,
            }
        }
    });


    /*--------------------------
        Videos Slider
    ----------------------------*/
    $(".videos__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: false,
        nav: true,
        navText: ["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        responsive: {
            992: {
                items: 4,
            },
            768: {
                items: 3,
            },
            576: {
                items: 2,
            },
            0: {
                items: 1,
            }
        }
    });

    /*------------------
		Magnific
	--------------------*/
    $('.video').magnificPopup({
        type: 'iframe',
        iframe: {
            markup: '<div class="mfp-iframe-scaler">'+
                      '<div class="mfp-close"></div>'+
                      '<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>'+
                    '</div>', // HTML markup of popup, `mfp-close` will be replaced by the close button
          
            patterns: {
              youtube: {
                index: 'youtube.com/', // String that detects type of video (in this case YouTube). Simply via url.indexOf(index).
          
                id: 'v=', // String that splits URL in a two parts, second part should be %id%
                // Or null - full URL will be returned
                // Or a function that should return %id%, for example:
                // id: function(url) { return 'parsed id'; }
          
                src: 'https://www.youtube.com/embed/%id%?autoplay=1' // URL that will be set as a source for iframe.
              },
              vimeo: {
                index: 'vimeo.com/',
                id: '/',
                src: '//player.vimeo.com/video/%id%?autoplay=1'
              },
              gmaps: {
                index: '//maps.google.',
                src: '%id%&output=embed'
              }
          
              // you may add here more sources
          
            },
          
            srcAction: 'iframe_src', // Templating object key. First part defines CSS selector, second attribute. "iframe_src" means: find "iframe" and set attribute "src".
          }
    });


    $('.imagepop').magnificPopup({
        type:'image',
        gallery:{
            enabled:true
        },
        mainClass: 'mfp-with-zoom', // this class is for CSS animation below

        zoom: {
            enabled: true, // By default it's false, so don't forget to enable it

            duration: 300, // duration of the effect, in milliseconds
            easing: 'ease-in-out', // CSS transition easing function

            // The "opener" function should return the element from which popup will be zoomed in
            // and to which popup will be scaled down
            // By defailt it looks for an image tag:
            opener: function(openerElement) {
            // openerElement is the element on which popup was initialized, in this case its <a> tag
            // you don't need to add "opener" option if this code matches your needs, it's defailt one.
            return openerElement.is('img') ? openerElement : openerElement.find('img');
            }
        }
    });

    $('.image').magnificPopup({
        type:'image',
    });


    /*------------------
        CountDown
    --------------------*/

    // Use this for real timer date

    // Récupérer la date de l'objet prochain_concert
    document.addEventListener("DOMContentLoaded", function() {
    var concertDateElement = document.getElementById("concert-date");
    if (!concertDateElement) {
        console.error("Element with ID 'concert-date' not found.");
        return;
    }

    var concertDateStr = concertDateElement.dataset.concertDate;
    if (!concertDateStr) {
        console.error("Attribute 'data-concert-date' not found or empty.");
        return;
    }
    
    // Diviser la chaîne de date en parties (jour, mois, année, heure, minute)
    if (typeof concertDateStr !== "string") {
        console.error("concertDateStr is not a string:", concertDateStr);
        return;
    } else {
        console.log(concertDateStr)
        var parts = concertDateStr.split(" ");
        console.log(parts)
        var day = parseInt(parts[0]);
        var month = parts[1];
        var year = parseInt(parts[2]);
        var time = parts[3];
        var hour = parseInt(time.split(":")[0]);
        var minute = parseInt(time.split(":")[1]);
        console.log(parts)
    }
    // Convertir le mois en son équivalent numérique
    var months = {
        "janvier": 0,
        "février": 1,
        "mars": 2,
        "avril": 3,
        "mai": 4,
        "juin": 5,
        "juillet": 6,
        "août": 7,
        "septembre": 8,
        "octobre": 9,
        "novembre": 10,
        "décembre": 11
    };
    var monthIndex = months[month.toLowerCase()];

    // Créer un objet Date avec la date et l'heure extraites
    var concertDate = new Date(year, monthIndex, day, hour, minute);

    // Vérifier si la conversion a réussi
    if (isNaN(concertDate)) {
        console.error("Erreur de conversion de la date : " + concertDateStr);
        return;
    }

    console.log(concertDate);

    // Utiliser maintenant concertDate pour votre logique de minuterie JavaScript
    var x = setInterval(function() {
        var now = new Date().getTime();
        var distance = concertDate - now;

        // Calculer les jours, heures, minutes et secondes restantes
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Afficher le temps restant dans les éléments avec les ID correspondants
        document.getElementById("days").innerText = days;
        document.getElementById("hours").innerText = hours;
        document.getElementById("minutes").innerText = minutes;
        document.getElementById("seconds").innerText = seconds;
        
         
        // Si la distance est inférieure à 0, l'événement est passé
        if (distance < 0) {
            clearInterval(x);
            // Afficher le temps restant dans les éléments avec les ID correspondants
            document.getElementById("days").innerText = "00";
            document.getElementById("hours").innerText = "00";
            document.getElementById("minutes").innerText = "00";
            document.getElementById("seconds").innerText = "00";
            $(".pastevent").text("L'événement est en cours ou déjà terminé !");
            // Masquer ou désactiver les boutons d'achat ici
            $(".kkiapay-button").hide();
        }
    }, 1000);
});

    /*------------------
        CountDown End
    --------------------*/


    /*------------------
		Barfiller
	--------------------*/
    $('#bar1').barfiller({
        barColor: "#ffffff",
    });

    $('#bar2').barfiller({
        barColor: "#ffffff",
    });

    $('#bar3').barfiller({
        barColor: "#ffffff",
    });

    /*-------------------
		Nice Scroll
	--------------------- */
    $(".nice-scroll").niceScroll({
        cursorcolor: "#111111",
        cursorwidth: "5px",
        background: "#e1e1e1",
        cursorborder: "",
        autohidemode: false,
        horizrailenabled: false
    });

})(jQuery);