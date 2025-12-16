const API_URL = 'https://pokemon-api-ecru-eta.vercel.app';

async function fetchGreenPokemons(){
    try{
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error('API 요청 실패');
        }

        const data = await response.json();

        const greenPokemons = data.data.filter((pokemon)=> pokemon.color === "green");
        console.log(greenPokemons);
        } catch (error) {
    console.error(error.message);
  }
}

fetchGreenPokemons();