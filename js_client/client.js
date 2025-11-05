const loginForm = document.getElementById('login-form')
const baseEndpoint = "http://localhost:8000/api"

if (loginForm) {
  loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(e) {
  
  e.preventDefault();
  
  const loginEndpoint = `${baseEndpoint}/token/`;
  
  let loginFormData = new FormData(loginForm);
  
  let loginObjectData = Object.fromEntries(loginFormData)
  
  const options = {
    method: 'POST',
    headers: {
      'ContentType': 'application/json'
    },
    body: JSON.stringify(loginObjectData),
  };
  
  fetch(loginEndpoint, options) // like running requests.post
    .then(response => {
     console.log(response)
     return response.json()
   })
    .then(x => {
      console.log(x)
    })
    .catch(err => {
     console.log('err ', err) 
    }); 
}