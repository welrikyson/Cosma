def loading_page():
    return """
<html>
	<head>
		<title>Loading</title>		
	</head>
	<style>
		html {
			height:90%;
		}
	
		body {
			background:#3F485B;
			display:flex;
			align-items:center;
			text-align: center; 
			padding: 40px 0;
			height:90%;
		}
		.back {
			margin:1em auto;
			font-family:"Roboto";
		}
		.back span {
			font-size:3em;
			color:#F2C640;
			background:#262B37;
			display:table-cell;
			box-shadow:inset 0 0 5px rgba(0,0,0,0.3), 0 5px 0 #ccc;
			padding: 0 15px;
			line-height: 100px;
			animation:jumb 2s infinite;
		}
		@keyframes jumb {
			0% {
				transform:translateY(0px)
			}
			50% {
				transform:translateY(-30px);
				box-shadow:0 15px 0 rgb(242, 198, 64);
			}
			100% {
				transform:translateY(0px)	
			}
		}
		.back span:nth-child(1) {
			animation-delay:0s;
		}
		.back span:nth-child(2) {
			animation-delay:.1s;	
		}
		.back span:nth-child(3) {
			animation-delay:.2s;
		}
		.back span:nth-child(4) {
			animation-delay:.3s;	
		}   
		.back span:nth-child(5) {
			animation-delay:.4s;
		}
		.back span:nth-child(6) {
			animation-delay:.5s;	
		}
		.back span:nth-child(7) {
			animation-delay:.6s;
		}
		
        h1 {
          color: #F2C640;
          font-family: "Nunito Sans", "Helvetica Neue", sans-serif;
          font-weight: 900;
          font-size: 40px;
          margin-bottom: 10px;
        }
        p {
          color: #404F5E;
          font-family: "Nunito Sans", "Helvetica Neue", sans-serif;
          font-size:20px;
          margin: 0;
        }
      i {
        color: #F2C640;;
        font-size: 100px;
        line-height: 200px;
        margin-left:-15px;
      }
      .card {
        background: #262B37;
        padding: 60px;
        border-radius: 4px;        
        display: inline-block;
        margin: 0 auto;
      }
    </style>
    <body>
        <span class="back">
            <span>N</span>
            <span>o</span>
            <span>t</span>
            <span>i</span>
            <span>f</span>
            <span>y</span>
            <span>i</span>
            <span>n</span>
            <span>g</span>
        </span>				
        <script>
            async function load(){
                const response = await fetch('http://localhost:8000/notify');            
                console.log('Hello')    
                const i = await response.json();
                var xmlString = `
                <div class="card">
                    <div style="border-radius:200px; height:200px; width:200px; background: #F8FAF5; margin:0 auto;">
                        <i class="checkmark">✓</i>
                    </div>      
                    <h1 style="font-size:30px"><b style="font-size:80px">${i}</b> <br> Activities notify</h1>        
                </div>`;            
                document.getElementsByTagName('body')[0].innerHTML = xmlString;
                document.title = 'Notify'                
            }            
            load();
        </script> 
    </body>
</html>
"""
