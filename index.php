<?php

?>

<!DOCTYPE html>

<html lang="en">
	<head>
		<title>Space-Animal Website</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1">
		<link rel="stylesheet" type="text/css" href="siteFormat.css">
		<script type="text/javascript" src="index.js"> </script>
		<meta charset="utf-8" />
	</head>

	<body id="forBody" >
		<div id="titleBox">
			<div id="titleText">
				<h1>HackNJIT 2021 - Website</h1>
			</div>	
			<div id="tabHolder">
				<a href="index.php" id="tab">Home</a> |
				<a href="game.php" id="tab">Game</a> |
				<a href="animalfacts.php" id="tab">Animal Facts</a> |
				<a href="aboutus.html" id="tab">About Us</a> 
			</div>
		</div>

		<div id="otterBox">

			<div id="picsReel">
				<button id="leftArrow" onclick="moveLeft()">
					<h1> < </h1>
				</button>
				
				<div id="middle">
					<img src="cat.jpg" id="anchor">
				</div>

				<button id="rightArrow" onclick="moveRight()">
					<h1> > </h1>
				</button>
			</div>
		</div>
	</body>
</html>