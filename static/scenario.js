const btn = document.querySelector('#response');
const answer = document.querySelector('#answer');
const responseDiv = document.querySelector('.user-response');
const form = document.querySelector('#form-user-response');
const input = document.querySelector('#form-input');

btn.addEventListener('click', function (e) {
    e.preventDefault();
    answer.classList.remove('.hidden');
    responseDiv.innerText = input.value;
});


form.addEventListener('submit', function (e) {
    console.log('click')
    e.preventDefault();


});