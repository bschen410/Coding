<!doctype html>
<html lang="zh-TW">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="google-site-verification" content="rZp7hpp4ubTGMjDooaGsumQ8ox3h_Q2FlZOpsYHyaO8" />
	<title>南山中學-國290-班網</title>
	<link rel="stylesheet" href="style.css">
	<link rel="Shortcut Icon" type="image/x-icon" href="media/icon.png">
	<meta name="google-site-verification" content="tazP7ipcOzaAthnz6tbQCwqWRdYtOE8UQrDpPnzLd9I" />	
</head>
<body bgcolor="black">
    <?php
        echo date("今天是Y年m月d日的H:m:s");
    ?>
	<?php
	// 資料庫伺服器IP或地址
	$mysql_server_name=`localhost`; 
	// 資料庫名
	$mysql_database=`pool`; 
	// 連線資料庫
	$conn=mysql_connect($mysql_server_name);
	// 判斷連線是否成功
	if (!$conn)
	{
	 die(“不能連線資料庫，錯誤是: ” . mysql_error());
	}
	// 資料庫輸出編碼，應該與你的資料庫編碼保持一致。建議用UTF-8國際標準編碼
	mysql_query(“set names `utf8`”); 
	// 開啟資料庫
	$db_selected = mysql_select_db($mysql_database, $conn);
	// 判斷開啟是否成功
	if (!$db_selected)
	{
	 die (“不能開啟資料庫，錯誤是: ” . mysql_error());
	}
	// SQL語句
	$sql = “insert into test (MyName) values (`111-111`)”;
	// 執行SQL語句
	if (mysql_query($sql,$conn))
	{
	echo “執行SQL語句完成”;
	}
	else
	{
	echo “不能執行SQL語句，錯誤是: ” . mysql_error();
	} 
	// 使用完畢關閉資料庫連線
	mysql_close(); 
	?>
</body>
</html>
