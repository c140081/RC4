<script type = "text/javascript">
		function checkkeyvalue(){
			 var keyvalue = document.getElementById("keyvalue").value;
			 keyvalue = keyvalue.toString() ;
			 var keylen = keyvalue.length ;
			 // e.g.: <div class="vbox"><div class="velement">0</div><div>S<span class="sub">0</span></div></div>
			 var s1 = '<div class="vbox"><div class="velement">' ;
			 var s2 = '</div><div>K<span class="sub">' ;
			 var s3 = '</span></div></div>' ;
			 var li = '<li>' ;
			 var liend = '</li>' ;
			 var divclear = '<div class="clear"> </div>' ;
			 var tvector = '' ; 
			 if ( keylen < 17 ) {
			 	for (i=0 ; i<keylen ; i++){
				 	var keyelement = keyvalue[i] ;
				 	var telement = s1 + keyelement + s2 + i.toString() + s3 ;
				 	tvector = tvector + telement ;
			 	}
			 } 
			 else {
			 	for (i=0 ; i<keylen ; i++) {
				 	var keyelement = keyvalue[i] ;
				 	var telement = s1 + keyelement + s2 + i.toString() + s3 ;
			 		if ( i == 3 ) { tvector = tvector + '<div class="hscroll"><ul>' ; }
			 		if ( i == (keylen - 3)) { tvector = tvector + '</ul></div>' ; }
			 		if ( (i > 2) & (i < (keylen - 3) ) ) {	telement = li + telement + liend ; }
			 		tvector = tvector + telement ;
			 	}
			 }
			 
			 document.getElementById("showkey").innerHTML = tvector + divclear ;
			}


			function fillt(){
				document.getElementById("tvalue").innerHTML = 't value' ;
			}
		</script>
