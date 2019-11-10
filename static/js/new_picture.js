let formArea = document.querySelector('form');
let fileInputFunc = document.querySelector('input[type=file]');
let fileInputLabl = document.querySelector('label[for=file]');
let resetButton = document.querySelector('button[type=reset]');

fileInputFunc.addEventListener('change', e => {
	let filename = fileInputFunc.files[0].name;
	fileInputLabl.innerHTML = filename;
});

resetButton.addEventListener('click', e => {
	fileInputLabl.innerHTML = "Escolha um arquivo";
});
