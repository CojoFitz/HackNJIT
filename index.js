var images = ["cat.jpg", "dog.jpg", "bird.jpg", "fox.jpg", "kangaroo.jpg", "koala.jpg", "panda.jpg", "racoon.jpg", "redpanda.jpg"];
var currentPos = 0;
var temp;

function updateImage(){
	document.getElementById("anchor").src = images[currentPos];
}

function moveRight(){
	if ((currentPos+1) >= images.length){
		currentPos = 0;
	}
	else{
		currentPos = currentPos + 1;
	}
	clearTimeout(temp);
	updateImage();
	reset();
}

function moveLeft(){
	if ((currentPos-1) < 0){
		currentPos = images.length-1;
	}
	else{
		currentPos = currentPos - 1;
	}
	clearTimeout(temp);
	updateImage();
	reset();
}

function reset(){
	temp = setInterval(moveRight, 4000);
}

reset();