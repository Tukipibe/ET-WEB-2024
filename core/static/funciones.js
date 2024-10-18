then(data => {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `
        <h3>Resultado del Análisis</h3>
        <p><strong>Calorías:</strong> ${data.calories}</p>
        <p><strong>Porciones:</strong> ${data.yield}</p>
        <h4>Ingredientes:</h4>
        <ul>
            ${data.ingredients.map(ingredient => `<li>${ingredient.text}</li>`).join('')}
        </ul>
        <h4>Etiquetas de Salud:</h4>
        <ul>
            ${data.healthLabels.map(label => `<li>${label}</li>`).join('')}
        </ul>
    `;
})
