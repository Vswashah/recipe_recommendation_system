document.getElementById('recipeForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent form from submitting in the traditional way

    const formData = new FormData(this);
    const recommendationsDiv = document.getElementById('recommendations');

    recommendationsDiv.innerHTML = `<p>Loading...</p>`;  // Show a loading message while the request is being processed

    fetch('/recommend', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        recommendationsDiv.innerHTML = '';  // Clear any previous results

        if (data.length === 0) {
            recommendationsDiv.innerHTML = '<p>No recommendations found.</p>';  // Display a message if no recipes are found
            return;
        }

        // Iterate over the recipes and create a separate container for each one
        data.forEach(recipe => {
            const recipeCard = document.createElement('div');
            recipeCard.className = 'recipe-card';  // Use the recipe-card class for styling

            recipeCard.innerHTML = `
                <h3>${recipe.title}</h3>
                <p><strong>Ingredients:</strong> ${recipe.items}</p>
                <p><strong>Instructions:</strong> ${recipe.instructions}</p>
            `;

            recommendationsDiv.appendChild(recipeCard);  // Add the recipe card to the recommendations div
        });
    })
    .catch(error => {
        console.error('Error:', error);
        recommendationsDiv.innerHTML = '<p>There was an error processing your request.</p>';  // Display an error message if the fetch fails
    });
});
