let fileInput = document.querySelector('input[type=file]');
let fileLabel = document.querySelector('label[for=file]');
fileInput.addEventListener('change', (e) => {
	let filename = fileInput.files[0].name;
	fileLabel.innerHTML = filename;
});

let formContainer = document.querySelector('main');
let newImageBtn = document.querySelector('button[id=new-image]');
newImageBtn.addEventListener('click', (e) => {
	let formItem = document.querySelectorAll('form')[0].cloneNode(true);
	formContainer.appendChild(formItem);
	formContainer.appendChild(newImageBtn);
})
