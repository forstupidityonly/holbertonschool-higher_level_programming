$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
                const res = data.results;
                const list = $('ul#list_movies');
                for (let i = 0; i < res.length; i++) {
                  list.append('<Li>${res[i].title}</li>');
                  }
                  });
