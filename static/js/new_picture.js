let fileInput = document.querySelector('input[type=file]');
let fileLabel = document.querySelector('label[for=file]');
fileInput.addEventListener('change', (e) => {
	let filename = fileInput.files[0].name;
	fileLabel.innerHTML = filename;
});
