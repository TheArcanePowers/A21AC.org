# Templates
 ## Individual country pages
 **Structure of the folder:**
 - Continent
	- /images/
		 - [country]_map.png
		 - [country]_pic01.png
		 - [country]_pic02.png
	 - [country].html
	 - [country].html

Content is posted on Google Drive: `A21 @ AC\Events and Research\Detailed Website Document`
	
	```html
	<!DOCTYPE HTML>
	<html>
		<head>
			<title>[[COUNTRY NAME]]</title>
			<meta charset="utf-8" />
			<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
			<link rel="stylesheet" href="../assets/css/main.css" />
			<noscript><link rel="stylesheet" href="../assets/css/noscript.css" /></noscript>
		</head>
		<body class="is-preload">
			<!-- Wrapper -->
				<div id="wrapper" class="divided"> 
					<section class="wrapper style1 align-center">
					
					<!-- Spotlight -->
						<section class="spotlight onload-content-fade-left style1 orient-right content-align-left image-position-center">
							<div class="content">
							<h1>[[COUNTRY NAME]]</h1>
							<p>[[CONTENT]]</p>
							</div>
							<div class="image">
								<img src="images/[[COUNTRY NAME]]_map.png"/>
							</div>
						</section>
						<div class="inner">
							<hr>
							
							<!-- Helplines -->
							<section class="content align-left">
								<h1>Helplines</h1>
								<dl>
									<dt>[[PHONE]]</dt>
									<dd>
										<p>[[DESC]]</p>
									</dd>
									<dt>[[PHONE]]</dt>
									<dd>
										<p>[[DESC]]</p>
									</dd>
								</dl>
							</section>
							
							<!-- Things to watch out for -->
							<section class="content align-right">
								<h1>Things to watch out for</h1>
								<dl>
									<dt>[[THING]]</dt>
									<dd>
										<p>[[DESC]]</p>
									</dd>
									<dt>[[THING]]</dt>
									<dd>
										<p>[[DESC]]</p>
									</dd>
								</dl>
							</section>
							<br><hr><br>
							
							<!-- Statistics -->
							<section class="content align-left">
								<header>
									<h1>Statistics</h1>
									<p>[[WHERE FROM]]</p>
								</header>
								<p>[[STATISTICS]]</p>
							</section>
							
							<!-- image gallery -->
							<section class="content align-left onscroll-fade-in">
								<h2>[[IDK]]</h2>
								<p><span class="image left"><img src="../images/[[PIC01]].jpg"></span>[[TEXT]]</p>
								<br>
								<p><span class="image right"><img src="../images/[[PIC02]].jpg"></span>[[TEXT]]</p>
							</section>
							<br><hr>
							
							<!-- Citations -->
							<div class="index align-left">
								<section>
									<header><h3>Citations</h3></header>
									<div class="content">
										<ol>
											<li>[[CITATION 1]]</li>
											<li>[[CITATION 2]]</li>
										</ol>
									</div>
								</section>
							</div>
						</div>
					</section>
					
					<!-- Footer -->
					<footer class="wrapper style1 align-center">
							<div class="inner">
								<ul class="icons">
									<li><a href="#" class="icon brands style2 fa-twitter"><span class="label">Twitter</span></a></li>
									<li><a href="#" class="icon brands style2 fa-facebook-f"><span class="label">Facebook</span></a></li>
									<li><a href="#" class="icon brands style2 fa-instagram"><span class="label">Instagram</span></a></li>
									<li><a href="#" class="icon brands style2 fa-linkedin"><span class="label">LinkedIn</span></a></li>
									<li><a href="#" class="icon style2 fa-envelope"><span class="label">Email</span></a></li>
								</ul>
								<p>&copy; Untitled. Design: <a href="https://html5up.net">HTML5 UP</a>.</p>
							</div>
						</footer>

				</div>

			<!-- Scripts -->
				<script src="../assets/js/jquery.min.js"></script>
				<script src="../assets/js/jquery.scrollex.min.js"></script>
				<script src="../assets/js/jquery.scrolly.min.js"></script>
				<script src="../assets/js/browser.min.js"></script>
				<script src="../assets/js/breakpoints.min.js"></script>
				<script src="../assets/js/util.js"></script>
				<script src="../assets/js/main.js"></script>
		</body>
	</html>
	```
## To change map hover descriptions
Saved in `/assets/map/data.json`
**Structure:**

    {
	    "countries": {
		    "[[CountryCode]]": "[[STUFF]]
		    }
	}
Country code is 2 codes. Called [Alpha-2](https://www.nationsonline.org/oneworld/country_code_list.htm). This is posted on the google drive `A21 @ AC\Events and Research\Short description on map`


