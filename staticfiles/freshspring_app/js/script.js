(function() {
	"use strict";

    // Preloader JS
    try {
        document.addEventListener('DOMContentLoaded', function() {
            setTimeout(function() {
                var container = document.getElementById('container');
                container.classList.add('loaded');
              
                if (container.classList.contains('loaded')) {
                    var preloader = document.getElementById('preloader');
                    setTimeout(function() {
                        preloader.parentNode.removeChild(preloader);
                    }, 1000);
                }
            }, 1000);
        });          
    } catch {}

    // Navbar JS
    try {
        const nav = document.querySelector('.navbar');
        let navTop = nav.offsetTop;
        
        function fixedNav() {
            if (window.scrollY >= navTop) {
                nav.classList.add('sticky');
            } else {
                nav.classList.remove('sticky');
            }
        }
        window.addEventListener('scroll', fixedNav);
    } catch (err) {}

    // Banner Slider JS
    try {
        var swiper = new Swiper(".myBannerSlider", {
            slidesPerView: 1,
            spaceBetween: 0,
            loop: true,
            speed: 1500,
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
            },
            autoplay: {
                delay: 3500,
                disableOnInteraction: false,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            breakpoints: {
                0: {
                    slidesPerView: 1
                },
                768: {
                    slidesPerView: 1
                },
                992: {
                    slidesPerView: 1
                },
                1200: {
                    slidesPerView: 1
                }
            }
        });
    } catch {}

    // Service Slider JS
    try {
        var swiper = new Swiper(".swiperServiceSliderItem", {
            slidesPerView: 1,
            spaceBetween: 20,
            loop: true,
            speed: 500,
            autoplay: {
                delay: 1000,
                disableOnInteraction: false,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            breakpoints: {
                0: {
                    slidesPerView: 1
                },
                576: {
                    slidesPerView: 2
                },
                768: {
                    slidesPerView: 2
                },
                992: {
                    slidesPerView: 3
                },
                1200: {
                    slidesPerView: 4
                },
                1400: {
                    slidesPerView: 5
                }
            }
        });
    } catch {}

    // Service Slider JS
    try {
        var swiper = new Swiper(".myServiceSliderItemTwo", {
            slidesPerView: 1,
            spaceBetween: 20,
            loop: true,
            speed: 600,
            autoplay: {
                delay: 1500,
                disableOnInteraction: false,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            breakpoints: {
                0: {
                    slidesPerView: 1
                },
                768: {
                    slidesPerView: 2
                },
                992: {
                    slidesPerView: 3
                },
                1200: {
                    slidesPerView: 5
                }
            }
        });
    } catch {}

    // Testimonials Thumb JS
    try {
        var swiper = new Swiper(".mySwiperButton", {
            loop: true,
            spaceBetween: 0,
            slidesPerView: 3,
            freeMode: true,
            watchSlidesProgress: true,
        });
        var swiper2 = new Swiper(".mySwiperContent", {
            loop: true,
            spaceBetween: 0,
            slidesPerView: 1,
            autoplay: {
                delay: 4000,
                disableOnInteraction: false,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            thumbs: {
                swiper: swiper,
            },
        });
    } catch {}

    // Testimonial Slide JS
    try {
        var swiper = new Swiper(".testimonialSlideContent", {
            loop: true,
            spaceBetween: 0,
            slidesPerView: 1,
            autoplay: {
                delay: 3500,
                disableOnInteraction: false,
            },
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
            },
        });
    } catch {}

    // Partner Slider JS
    try {
        var swiper = new Swiper(".partnerSlider", {
            slidesPerView: 1,
            spaceBetween: 50,
            loop: true,
            speed: 1000,
            autoplay: {
                delay: 2500,
                disableOnInteraction: false,
            },
            breakpoints: {
                0: {
                    slidesPerView: 2
                },
                576: {
                    slidesPerView: 3
                },
                768: {
                    slidesPerView: 3
                },
                992: {
                    slidesPerView: 4
                },
                1200: {
                    slidesPerView: 5
                },
                1400: {
                    slidesPerView: 6
                }
            }
        });
    } catch (err) {}

    // Portfolio Slider JS
    try {
        var swiper = new Swiper(".myPortfolioSlidersItems", {
            slidesPerView: 1,
            spaceBetween: 20,
            loop: true,
            speed: 1000,
            autoplay: {
                delay: 3000,
                disableOnInteraction: false,
            },
            scrollbar: {
                el: ".swiper-scrollbar",
                clickable: true,
            },
            breakpoints: {
                0: {
                    slidesPerView: 1
                },
                576: {
                    slidesPerView: 1
                },
                768: {
                    slidesPerView: 2
                },
                992: {
                    slidesPerView: 5
                }
            }
        });
    } catch {}

    // Portfolio Slider JS
    try {
        var swiper = new Swiper(".SwiperPortfolioSlide", {
            slidesPerView: 1,
            spaceBetween: 20,
            loop: true,
            speed: 1000,
            autoplay: {
                delay: 3500,
                disableOnInteraction: false,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            breakpoints: {
                0: {
                    slidesPerView: 1
                },
                576: {
                    slidesPerView: 1
                },
                768: {
                    slidesPerView: 2
                },
                992: {
                    slidesPerView: 3
                },
                1200: {
                    slidesPerView: 3
                },
                1400: {
                    slidesPerView: 4
                }
            }
        });
    } catch {}

    // Add To Cart Number JS
    try {
        function inc() {
            let number = document.querySelector('[name="number"]');
            number.value = parseInt(number.value) + 1;
        }

        function dec() {
            let number = document.querySelector('[name="number"]');
            if (parseInt(number.value) > 0) {
                number.value = parseInt(number.value) - 1;
            }
        }
    } catch (err) {}
    // End

    // // Counter Js
    try {
        if ("IntersectionObserver" in window) {
            let counterObserver = new IntersectionObserver(function (entries, observer) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                    let counter = entry.target;
                    let target = parseInt(counter.innerText);
                    let step = target / 200;
                    let current = 0;
                    let timer = setInterval(function () {
                        current += step;
                        counter.innerText = Math.floor(current);
                        if (parseInt(counter.innerText) >= target) {
                        clearInterval(timer);
                        }
                    }, 10);
                    counterObserver.unobserve(counter);
                    }
                });
            });

            let counters = document.querySelectorAll(".counter");
                counters.forEach(function (counter) {
                counterObserver.observe(counter);
            });
        }
    } catch {}

	// scrollCue Animate
	scrollCue.init();

    // // Select The Button Element Go Top
    try {
        var scrollTopBtn = document.getElementById("scrollTopBtn");
        // Show the button when the user scrolls down
        window.onscroll = function() {
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                scrollTopBtn.style.display = "block";
            } else {
                scrollTopBtn.style.display = "none";
            }
        };
        // Add a click event listener to the button
        scrollTopBtn.addEventListener("click", function() {
            window.scrollTo({
                top: 0,
                left: 0,
                behavior: "smooth"
            });
        });
    } catch (err) {}

})();

try {

    window.onload=function() {
        if(localStorage.darkMode=="true") {
        document.body.classList.toggle('dark');
        document.getElementById("chk").checked=true;
        }
        else {
        document.body.classList.toggle('light');
        }
    };
    document.getElementById("chk").addEventListener('change', () => {
        document.body.classList.toggle('dark');
        document.body.classList.toggle('light');
        localStorage.darkMode=(localStorage.darkMode=="true")?"false":"true";
    });

} catch {}