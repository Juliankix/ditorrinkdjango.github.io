 document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.btn');
    const cards = document.querySelectorAll('.card');
    const toast = document.getElementById('toast');

    // Efecto hover para cards (cambia el color de fondo)
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-5px)';
            card.style.boxShadow = '0 12px 20px rgba(0, 0, 0, 0.15)';
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = '';
            card.style.boxShadow = '0 8px 16px rgba(0, 0, 0, 0.1)';
        });
    });

    // Acciones al hacer clic en botones
    buttons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            const action = button.getAttribute('data-action');
            const cardTitle = button.closest('.card').querySelector('h2').textContent;

            // Feedback visual al hacer clic
            button.style.backgroundColor = '#f0f0f0';
            setTimeout(() => {
                button.style.backgroundColor = '';
            }, 200);

            // Mostrar toast
            showToast(`Acción: ${action} (${cardTitle})`);
        });
    });

    // Función para mostrar el toast
    function showToast(message) {
        toast.textContent = message;
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
        }, 3000);
    }
});