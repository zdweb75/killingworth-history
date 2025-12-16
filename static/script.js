// Simple JavaScript file for your Flask app
// This demonstrates how to include JavaScript in your project

document.addEventListener('DOMContentLoaded', function() {
    console.log('Flask app loaded successfully!');
    
    // Add a simple hover effect to the container
    const container = document.querySelector('.container');
    
    container.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-5px)';
        this.style.transition = 'transform 0.3s ease';
    });
    
    container.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
    });
});
