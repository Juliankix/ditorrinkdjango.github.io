// Validación básica del email
document.getElementById('id_email').addEventListener('blur', function() {
    const email = this.value;
    if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        alert('Por favor ingrese un email válido');
    }
});

// Mostrar nombre de archivos seleccionados
document.querySelectorAll('input[type="file"]').forEach(input => {
    input.addEventListener('change', function() {
        if (this.files.length > 0) {
            const fileName = this.files[0].name;
            const label = this.previousElementSibling;
            label.textContent += ` ✔️ (${fileName})`;
        }
    });
});

// Mostrar nombre del archivo seleccionado
document.querySelectorAll('.file-input').forEach(input => {
    input.addEventListener('change', function(e) {
        const label = this.nextElementSibling;
        const fileName = this.files[0]?.name || 'Ningún archivo seleccionado';
        
        // Actualizar texto
        label.querySelector('.file-text').textContent = fileName;
        label.querySelector('.file-hint').innerHTML = 
            `<span style="color: #6a11cb;">✔ Listo para subir</span>`;
        
        // Animación temporal
        label.parentElement.classList.add('uploading');
        setTimeout(() => {
            label.parentElement.classList.remove('uploading');
        }, 1500);
    });
});

// Efecto drag & drop
document.querySelectorAll('.file-label').forEach(label => {
    label.addEventListener('dragover', (e) => {
        e.preventDefault();
        label.style.backgroundColor = 'rgba(142, 84, 233, 0.2)';
    });
    
    label.addEventListener('dragleave', () => {
        label.style.backgroundColor = '';
    });
});