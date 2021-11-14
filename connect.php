<?php
	//change database name if needed
	$con = mysqli_connect('localhost', 'root', '', 'leaderboard');
	
	if (mysqli_connect_errno()){
		echo "1";
		exit();
	}
	
	//connect to the score and user input of name from unity
	$username = $_POST["name"];
	$score = $_POST["score"];
	
	$query = "INSERT INTO scoreboard VALUES('" . $username . "', '" . $score . "');
	mysqli_query($con, $query);
	
?>