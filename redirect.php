<!DOCTYPE HTML>
<html>
	<head>A21 @ AC</head>
	<?php
	echo ("PHP RUNNING");
	if(array_key_exists("country", $_GET) and strlen($_GET["country"]) == 2){
		$africa = json_decode(file_get_contents('assets/redirector/africa.txt'), true);
		$europe = json_decode(file_get_contents('assets/redirector/europe.txt'), true);
		$nAmerica = json_decode(file_get_contents('assets/redirector/nAmerica.txt'), true);
		$asia = json_decode(file_get_contents('assets/redirector/asia.txt'), true);
		$sAmerica = json_decode(file_get_contents('assets/redirector/sAmerica.txt'), true);
		$oceania = json_decode(file_get_contents('assets/redirector/oceania.txt'), true);
		
		$requestedCountry = $_GET["country"];	
		$exists = false;
		
		function redirect($continent, $country){   
			header("HTTP/1.1 303 See Other");
			header("Location: http://".$_SERVER['HTTP_HOST']."/".$continent."/".$country.".html");
		}

		if (in_array($requestedCountry, $europe)){
			$continent = "europe";
		}
		if (in_array($requestedCountry, $africa)){
			$continent = "africa";
		}
		if (in_array($requestedCountry, $nAmerica)){
			$continent = "north-america";
		}
		if (in_array($requestedCountry, $sAmerica)){
			$continent = "south-america";
		}
		if (in_array($requestedCountry, $oceania)){
			$continent = "oceania";
		}
		if (in_array($requestedCountry, $asia)){
			$continent = "asia";
		}
		
		if (isset($continent)){
			$countryCodes = json_decode(file_get_contents('assets/redirector/countryCodes.txt'), true);
			redirect($continent, $countryCodes[$requestedCountry]);
		} else {
			echo ("No such country.");
		}
	} else {
		print_r("No such country.");
	}
	?>
</html>