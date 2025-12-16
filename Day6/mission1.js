function fakeApiCall() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({ name: 'John Doe', age: 30 });
        }, 2000);
    });
}

// fetchUserData 함수 완성
async function fetchUserData(){
    const input = await fakeApiCall();
    console.log(input.name);
};

fetchUserData();