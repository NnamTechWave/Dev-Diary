

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
        // scale: 0.8, // Scale down for a more dramatic effect
        // rotate: -20, // Slight rotation for added effect
        ease: "power2.out",
        delay: 0.5
    });
    gsap.from("#about-section p", {
        duration: 1,
        y: 30,
        opacity: 1,
        stagger: 0.2,
        scale: 0.8, // Scale down for a more dramatic effect
        // rotate: -5, // Slight rotation for added effect
        ease: "power2.out",
        delay: 0.5
    });


