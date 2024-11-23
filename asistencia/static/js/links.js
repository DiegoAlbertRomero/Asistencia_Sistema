document.addEventListener('DOMContentLoaded', function() {
    // Obtener la ruta actual
    const currentPath = window.location.pathname;
    
    // Obtener todos los enlaces del menú
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    // Iterar sobre cada enlace
    navLinks.forEach(link => {
        // Obtener la URL del enlace
        const href = link.getAttribute('href');
        
        // Convertir las URLs de Django a rutas
        const cleanHref = href.replace(/\{% url '(.+)' %\}/g, '/$1');
        
        // Si la ruta actual coincide con la URL del enlace
        if (currentPath === cleanHref || 
            (currentPath === '/' && cleanHref === '/home') ||
            (currentPath.startsWith(cleanHref) && cleanHref !== '/')) {
            
            // Añadir la clase active y estilo
            link.classList.add('active');
            link.style.color = '#007bff'; // Color azul de Bootstrap
            link.style.fontWeight = 'bold';
        }
    });
});

document.querySelectorAll('.nav-item').forEach((item, index) => {
    item.style.setProperty('--item-number', index + 1);
});