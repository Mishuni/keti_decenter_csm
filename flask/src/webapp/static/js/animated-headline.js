jQuery(document).ready(function($){

	// start the function
	initHeadline();

	function initHeadline() {
		//insert <i> element for each letter of a changing word
		singleLetters($('.box-headline.letters').find('b'));
		//initialise headline animation
		//animateHeadline($('.box-headline'));
		//intervalReq = setInterval(makeRequest,timeInterval);
	}

	function singleLetters($words) {
		$words.each(function(){
			let word = $(this),
				letters = word.text().split(''),
				selected = word.hasClass('is-visible');
			var idx = 0;  
			for (i in letters) {
				if(selected){
					if(word.parents('.rotate-2').length > 0) letters[i] = '<em>' + letters[i] + '</em>';
					letters[i] = '<i class="in">' + letters[i] + '</i>';
				}
				else{
					if(word.parents('.rotate-2').length > 0) letters[i] = (letters[i]=='A')?'<em><font color="red">' + letters[i] + '</font></em>'
																			:(letters[i]=='B')?'<em><font color="blue">' + letters[i] + '</font></em>'
																			:'<em>' + letters[i] + '</em>';
					letters[i] = '<i>' + letters[i] + '</i>';
				}
				
			}
			let newLetters = letters.join('');
			word.html(newLetters).css('opacity', 1);
		});
	}

});