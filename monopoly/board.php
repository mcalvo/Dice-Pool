<!DOCTYPE html>

<html>
  <head>
    <title>Board</title>
    <style type="text/css">
	#gbcontainer {
		position: relative;
		height: 100%;
	}
	#gameboard {
		background: #b8ffb8;
		border: 3px solid;
		border-color: black;
		position: absolute;
		z-index: -1;
		max-width: 100%;
	}
	div#data {
		width: 300px;
		margin-left: 45%;
		float: right;
	}
	#debug {
		text-align: right;
	}
	
    </style>

    <script type="text/javascript" src="http://cdn.jquerytools.org/1.2.7/full/jquery.tools.min.js"></script>
    <script type="text/javascript" src="manageboard.js"></script>
    <script type="text/javascript" src="manageskins.js"></script>
    <?php include "propcard.php" ?>
    <script type="text/javascript">
	var ignoreHide = false;
	function debugPrint(str){
		console.log( str );
	}
	$(document).ready(function(){
		loadSkin("classic");
		initBoard("gameboard");
		debugPrint("stuff is ready...");
	});
    </script>
  </head>

  <body>

    <?php printPropcard(); ?>
    <div id="gbcontainer">
      <canvas id="gameboard" width="700" height="700">
        Your browser does not support the canvas element.
      </canvas>
    </div>

    <div id="data">
      <p id="debug"></p>
    </div>
  </body>
</html>

