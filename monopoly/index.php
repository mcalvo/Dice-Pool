<?php

function getOpenGames()
{
	$name = 'localhost';
}
?>

<html>
  <head>
    <title>Monopoly Online!</title>
    <style type="text/css">
	table, th, td{
		border-style: solid;
		cell-padding: 10px;
	}
	td {
		vertical-align: top;
	}
    </style>
  </head>

  <body>
    <h1>Coming soon!</h1>
    <p>Monopoly Online is an educational project by Steven Vergenz.</p>

    <table>
      <tr>
        <td style='width: 50%;'>
          <p>Join an available game</p>
          <form action="">
            <select name="openGames">
              <? getOpenGames() ?>
            </select>
          </form>
        </td>
        <td>
          <p>Create a new game</p>
        </td>
      </tr>
    </table>
  </body>
</html>
