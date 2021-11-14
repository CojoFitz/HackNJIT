var questions = [["How many paws does a cat have?", "4"], ["Does cats have night vision?", "yes"], ["How many paws does a dog have?", "4"], ["What is a dog's best sense? (taste, smell, vision, hearing, touch)", "smell"], ["What country has koalas?", "australia"], ["What food does a koala eat? (eucalypt leaves or bamboo)", "eucalypt leaves"], ["What was the name of the fox in Dora?", "swiper"], ["Do foxes have whiskers?", "yes"], ["What continent does pandas reside in?", "asia"], ["What do pandas eat?", "bamboo"], ["How many paws does a racoon have?", "4"], ["Does raccoons have fur?", "yes"], ["What country has kangaroos?", "australia"], ["Does kangaroos have pouches?", "yes"], ["A group of cats is called a", "clowder"]];
var order = [];

function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}

function trivia(){
	let i = 0;
	let shuffledQuestions = shuffle(questions);

	while (i<shuffledQuestions.length){
		
		i++;
	}


}
