// Add interactive effects
document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.container');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Add hover effect to container
    if (container) {
        container.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.02)';
        });
        
        container.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    }
    
    // Add click effect to nav links
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Don't prevent default for actual navigation
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });
    
    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});
