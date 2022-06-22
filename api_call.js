function get_input() {
  return document.getElementById('input').textContent
}

function call_all() {
  fetch('call_all_info/' + get_input()).then(response =>{
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