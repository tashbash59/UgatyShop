ibg();

function ibg() {

	let ibg = document.querySelectorAll(".ibg");
	for (var i = 0; i < ibg.length; i++) {
		if (ibg[i].querySelector('img')) {
			ibg[i].style.backgroundImage = 'url(' + ibg[i].querySelector('img').getAttribute('src') + ')';
		}
	}
}

// отслеживаем клик на странице 
window.addEventListener('click', function (event) {

	// проверяем что клик был совершен по кнопке добавить в корзину
	if (event.target.hasAttribute('data-cart')) {

		// находим блок внутри которого нужные данные
		const card = event.target.closest('.Product');

		// собираем данные с этого блока в объект productInfo
		const productInfo = {
			id: card.dataset.id,
			imgSrc: card.querySelector('.product-img').getAttribute('src'),
			title: card.querySelector('.product-title').innerText,
			itemsInBox: card.querySelector('.items-in-box').value,
		}

		console.log(productInfo);
	}

})
