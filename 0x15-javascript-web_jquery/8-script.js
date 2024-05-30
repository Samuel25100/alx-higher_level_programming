$.get('https://swapi-api.alx-tools.com/api/films/?format=json',function(response) {  
for (let line of response.results) {
	$('UL#list_movies').append('<li>'+ line.title +'</li>');
  }
});
