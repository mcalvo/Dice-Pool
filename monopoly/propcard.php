<!-- propcard.php
	This file manages the styles, elements, and functions related
	to the property card tooltip.
-->

<style type="text/css">
#propcard {
	background-color: white;
	padding: 10px;
	width: 240px;
	/*height: 300px;*/
	border: solid 2px;
	border-collapse: collapse;
}
#propcard #nameplate {
	background-color: yellow;
	margin: 0px 0px 7px;
	padding: 5px;
	border: 2px solid black;
	font-weight: bold;
	text-transform: uppercase;
}
#propcard p {
	margin: 2px;
	text-align: center;
}
#propcard table {
	margin-left: 7%;
	width: 80%;
}
#propcard td#rent1,td#rent2,td#rent3,td#rent4 {
	text-align: right;
}

</style>

<?php
function printPropcard(){
?>

<div class="tooltip" id="propcard" hidden="hidden"> 

  <div id="nameplate">
    <p style="font-family:monospace; font-size:0.8em; letter-spacing:3px;">
	Title Deed</p>
    <p id="name" style="font-family:sarif; font-size:1.0em;">
	Marvin Gardens</p>
  </div>

  <p id="rent0">RENT $24</p>

  <table>
    <colgroup>
      <col class="label" />
      <col class="rent" />
    </colgroup>
    <tr>
      <td>With 1 House</td>
      <td id="rent1">$ 120.</td>
    </tr>
    <tr>
      <td>With 2 Houses</td>
      <td id="rent2">  360.</td>
    </tr>
    <tr>
      <td>With 3 Houses</td>
      <td id="rent3">  850.</td>
    </tr>
    <tr>
      <td>With 4 Houses</td>
      <td id="rent4"> 1025.</td>
    </tr>
  </table>

  <div>
    <p id="rent5">With HOTEL $1200.</p>
    <p id="mortgage">Mortgage Value $140.</p>
    <p id="housecost">Houses cost $150. each<br>Hotels, $150. plus 4 houses</p>
    <p style="font-size:8px; margin-top:5px;">If a player owns ALL the Lots of any Color-Group, the rent is Doubled on Unimproved Lots in that group.</p>
  </div>

</div>

<?php } ?>

<script type="text/javascript">
function updatePropcard( index )
{
	// set nameplate props
	var tile = activeSkin.skin.tiles[index];  
	if( tile.group != null ){
		$("#nameplate").css("backgroundColor", propColors[ tile.group ] );
		if( tile.group==0 || tile.group==7 ){
			$("#nameplate").css("color", "white");
		}
		else {	
			$("#nameplate").css("color", "black");
		}
	}

	$("#name").text( tile.name );
	$("#rent0").text( "RENT $"+tile.rent[0]+"." );
	for(var i=1; i<=4; i++){
		$("#rent"+i).text( "$"+tile.rent[i]+"." );
	}
	$("#rent5").text( "With HOTEL $"+tile.rent[5]+"." );
	$("#mortgage").text( "Mortgage Value $"+tile.mortgage+"." );
	$("#housecost").html(
		"Houses cost $"+tile.housecost+". each<br>"
		+"Hotels, $"+tile.housecost+". plus 4 houses"
	);

}
</script>
