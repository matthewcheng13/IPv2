function get_input() {
  console.log(document.getElementById('input').textContent)
  return document.getElementById('input').textContent
}

function call_all() {
  fetch('http://127.0.0.1:5000/call_all_info/7.7.7.7').then(response =>{
    return response.json(); 
  }).then(data =>{
    console.log(data);
  })
}

function call_hostname() {
  fetch('').then(response =>{
    return response.json(); 
  }).then(data =>{
    console.log(data);
  })
}

function call_ping() {
  fetch('').then(response =>{
    return response.json(); 
  }).then(data =>{
    console.log(data);
  })
}

function call_port() {
  fetch('').then(response =>{
    return response.json(); 
  }).then(data =>{
    console.log(data);
  })
}