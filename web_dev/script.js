// Smooth scroll for navigation links
const navLinks = document.querySelectorAll('.nav-links a');
navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href');
        if (targetId.startsWith('#')) {
            e.preventDefault();
            document.querySelector(targetId).scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Simple feedback for contact form submission
const contactForm = document.querySelector('#contact form');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Thank you for reaching out! I will get back to you soon.');
        contactForm.reset();
    });
}

// Civic authentication integration
const civicAppId = 'YOUR_CIVIC_APP_ID'; // Replace with your real Civic App ID
const loginBtn = document.getElementById('login-btn');

if (window.civic) {
    const civicSip = new window.civic.sip({
        appId: civicAppId
    });

    loginBtn.addEventListener('click', function() {
        civicSip.signup({ style: 'popup', scopeRequest: civicSip.ScopeRequests.BASIC_SIGNUP });
    });

    civicSip.on('auth-code-received', function(event) {
        // You get the JWT token here: event.response
        alert('Civic authentication successful!');
        // You can send event.response to your backend for verification
    });

    civicSip.on('user-cancelled', function() {
        alert('Civic authentication cancelled.');
    });

    civicSip.on('civic-sip-error', function(error) {
        alert('Civic authentication error: ' + error.type);
    });
}
