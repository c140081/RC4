@CHARSET "UTF-8";


* {
	text-align: center;
	margin:0;                 
	padding:0; 
	box-sizing: border-box;
}

h1 {
	margin-top:50px;    
}

h2 {
	height: 60px;
	text-align: left;
	margin-left: 10%;
	margin-top: 80px;
}

p {
	margin-left: 10%;
}

form {
	text-align: left;
	margin-left: 10%;
}

select {
	height: 30px;
	width: 160px;
	padding-left: 100px;
	margin-right: 20px;
}

input {
	height: 30px;
	width: 160px;
	margin-top: 30px;
	display: block;

}


.velement {
	border-style: solid;
	border-width: 5px;
	border-color: forestgreen;
	background-color: yellowgreen;
	width: 40px;
	height: 40px;
	line-height: 30px;
	display: inline-block;
	position: relative;
	float: left;
	right:-10%;	
}

.vbox {
	width: 50px;
	height: 80px;
	position: relative;
	float: left;
	right:-10%;
	display: inline-block;
}

ul {
	display: table;
}

li {
	display: table-cell;
}

.hscroll {
	display: inline-block;
	overflow-x: scroll;
	overflow-y: hidden;
	width: 40%;
	position: relative;
	float: left;
	right:-10%;
}


.super{
 	vertical-align: super;
 	font-size: xx-small;
 }

 .sub{
 	vertical-align: sub;
 	font-size: xx-small;
 }

 .italic {
 	font-style: italic;
}

.clear{
	clear:both;
	height:1px;
	margin-top:-1px;
	width:100%;
}  


