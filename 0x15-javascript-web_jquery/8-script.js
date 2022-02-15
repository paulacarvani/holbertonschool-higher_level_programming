$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, textStatus) => {
  if (textStatus === 'success') {
    for (const i of data.results) {
      console.log(i.title);
      $('UL#list_movies').append('<li>' + i.title + '</li>');
    }
  }
});
