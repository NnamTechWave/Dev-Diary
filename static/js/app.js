

// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function() {
    // Select the message container
    const messageContainer = document.getElementById('message-container');
    
    // If there is a message container, hide it after 3 seconds (3000 ms)
    if (messageContainer) {
        setTimeout(function() {
            messageContainer.style.display = 'none';
        }, 3000);
    }
});

// post detail
gsap.from(".text-end button", {
    duration: 1,
    x: 20,
    opacity: 0,
    stagger: 0.2,
    ease: "power2.out",
    delay: 0.5
});
gsap.from(".list-none li", {
    duration: 1,
    x: -20,
    opacity: 0,
    stagger: 0.2,
    ease: "power2.out",
    delay: 0.5
});


 // Hero section animations
        // gsap.from(".bg-header-image", {
        //     duration: 1,
        //     y: 20,
        //     opacity: 0,
        //     stagger: 0.2,
        //     ease: "power2.out",
        //     scrollTrigger: {
        //         trigger: "#bg-header-image",
        //         start: "top top",
        //         end: "bottom top",
        //         toggleActions: "play none none reverse",
        //         markers: false // Set to true if you want to see debug markers
        //     }
        // });
        gsap.registerPlugin(ScrollTrigger);

        // Initial animation on page load
        gsap.from("#bg-header-image", {
                duration: 1,
                y: 30,
                opacity: 0,
                stagger: 0.2,
                ease: "power2.out",
                onComplete: function() {
                    // Ensure elements are styled correctly after initial animation
                    document.querySelectorAll("#bg-header-image").forEach(el => {
                        el.style.opacity = 1;
                        el.style.transform = 'translateY(0)';
                    });
                }
        });    

        // gsap.from(".text-end button", {
        //     duration: 1,
        //     x: 20,
        //     opacity: 0,
        //     stagger: 0.2,
        //     ease: "power2.out",
        //     delay: 0.5
        // });

        // gsap.from(".list-none li", {
        //     duration: 1,
        //     x: -20,
        //     opacity: 0,
        //     stagger: 0.2,
        //     ease: "power2.out",
        //     delay: 0.5
        // });
    
        gsap.registerPlugin(ScrollTrigger);

            gsap.utils.toArray(".post-card").forEach(card => {
                gsap.from(card, {
                duration: 0.5,
                y: 20, // Move from below
                opacity: 0, // Start as invisible
                stagger: 0.2, // Stagger the start times
                ease: "power2.out",
                scrollTrigger: {
                    trigger: card,
                    start: "top bottom", // Animation starts when the top of the card hits the bottom of the viewport
                    end: "bottom top", // Animation ends when the bottom of the card hits the top of the viewport
                    toggleActions: "play none none reverse", // Play animation when entering and reverse when leaving
                    markers: false // Set to true if you want to see debug markers
                }
            });
        });

        // Scroll-triggered animation for header content (after initial load)
        ScrollTrigger.create({
            trigger: "#bg-header-image",
            start: "top top",
            end: "bottom top",
            onEnter: () => {
                // Animate header elements after scrolling
                gsap.from("#bg-header-image ", {
                    duration: 1,
                    y: 20,
                    opacity: 0,
                    stagger: 0.2,
                    ease: "power2.out"
                });
                // gsap.from(".text-end button", {
                //     duration: 1,
                //     x: 30,
                //     opacity: 0,
                //     stagger: 0.2,
                //     ease: "power2.out",
                //     delay: 0.5
                // });
            },
            markers: false // Set to true if you want to see debug markers
        });

        gsap.registerPlugin(ScrollTrigger);

// Initial animation on page load
gsap.from("#about-section img", {
    duration: 1,
    y: 20,
    opacity: 1,
    ease: "power2.out",
    delay: 0.5
});

gsap.from("#about-section h1, #about-section p", {
    duration: 1,
    y: 30,
    opacity: 1,
    stagger: 0.2,
    scale: 0.8, // Scale down for a more dramatic effect
    rotate: -10, // Slight rotation for added effect
    ease: "power2.out",
    delay: 0.5
});
gsap.from("#about-section p", {
    duration: 1,
    y: 30,
    opacity: 1,
    stagger: 0.2,
    scale: 0.8, // Scale down for a more dramatic effect
    rotate: -5, // Slight rotation for added effect
    ease: "power2.out",
    delay: 0.5
});

// Scroll-triggered animation for the "About" section
ScrollTrigger.create({
    trigger: "#about-section",
    start: "top bottom",
    end: "bottom top",
    onEnter: () => {
        gsap.to("#about-section img", {
            duration: 1,
            y: 0,
            opacity: 1,
            ease: "power2.out",
            overwrite: "auto" // Ensures the animation is not overridden
        });

        gsap.to("#about-section h1, #about-section p", {
            duration: 1,
            y: 0,
            opacity: 1,
            scale: 1, // Scale down for a more dramatic effect
            rotate: 0, // Slight rotation for added effect
            stagger: 0.2,
            ease: "power2.out",
            overwrite: "auto" // Ensures the animation is not overridden
        });
    },
    onEnterBack: () => {
        // Reset the elements to their initial state when scrolling back into view
        gsap.to("#about-section img", {
            duration: 1,
            y: 0,
            opacity: 1,
            scale: 1,
            ease: "power2.out",
            overwrite: "auto"
        });

        gsap.to("#about-section h1, #about-section p", {
            duration: 1,
            y: 0,
            opacity: 1,
            scale: 1,
            rotate: 0,
            stagger: 0.2,
            ease: "power2.out",
            overwrite: "auto"
        });
    },
    onLeaveBack: () => {
        // Ensure that elements stay in their final state when scrolling out
        gsap.to("#about-section img", {
            duration: 1,
            y: 0,
            opacity: 1,
            scale: 1,
            rotate: 0,
            ease: "power2.out",
            overwrite: "auto"
        });

        gsap.to("#about-section h1, #about-section p", {
            duration: 1,
            y: 0,
            opacity: 1,
            stagger: 0.2,
            ease: "power2.out",
            overwrite: "auto"
        });
    },
    markers: false // Set to true if you want to see debug markers
});

// <script>
    gsap.registerPlugin(ScrollTrigger);

    // Function to split text into individual letters
    function splitTextIntoSpans(selector) {
        document.querySelectorAll(selector).forEach(element => {
            const text = element.innerText;
            // const splitText = text.split(' ').map(letter => `<span class="letter"> ${ letter }</span>`).join('');
            const splitText = text.split('').map(letter => letter === ' ' ? '&nbsp;' : `<span class="letter"> ${letter}</span>`).join('');
            element.innerHTML = splitText;
        });
    }

    // Split text into spans for individual letter animations
    splitTextIntoSpans('#about-heading');
    splitTextIntoSpans('#about-paragraph');

    // Initial animation on page load
    // gsap.from("#about-section img", {
    //     duration: 1,
    //     y: 20,
    //     opacity: 0,
    //     ease: "power2.out",
    //     delay: 0.5
    // });

    gsap.from(".letter", {
        duration: 1,
        y: 30,
        opacity: 0,
        scale: 1,
        rotate: -10,
        stagger: 0.05, // Staggered animation for each letter
        ease: "power2.out",
        delay: 0.05
    });

   // Scroll-triggered animation for the "About" section
   ScrollTrigger.create({
        trigger: "#about-section",
        start: "top bottom",
        end: "bottom top",
        onEnter: () => {
            gsap.to(".letter", {
                duration: 1,
                y: 0,
                opacity: 1,
                scale: 1,
                rotate: 0,
                stagger: 0.05,
                ease: "power2.out",
                overwrite: "auto"
            });
        },
        onEnterBack: () => {
            gsap.to(".letter", {
                duration: 1,
                y: 0,
                opacity: 1,
                scale: 1,
                rotate: 0,
                stagger: 0.05,
                ease: "power2.out",
                overwrite: "auto"
            });
        },
        onLeaveBack: () => {
            gsap.to(".letter", {
                duration: 1,
                y: 0,
                opacity: 1,
                scale: 1,
                rotate: 0,
                stagger: 0.05,
                ease: "power2.out",
                overwrite: "auto"
            });
        },
        markers: false
    });
