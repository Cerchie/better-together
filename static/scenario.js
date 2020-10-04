const btn = document.querySelector('#response');
const answer = document.querySelector('#answer');
const responseDiv = document.querySelector('.user-response');
const form = document.querySelector('#form-user-response');
const input = document.querySelector('#form-input');
const usefulInfo = document.querySelector('#conversationStarters');


form.addEventListener('submit', function (e) {
    console.log('click2');
    e.preventDefault();
    answer.classList.toggle('d-none');    
    usefulInfo.classList.toggle('d-none');
    responseDiv.innerText = input.value;
    input.value = '';
});