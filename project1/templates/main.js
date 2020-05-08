var ids = document.getElementById("book");
      var buuton = document.getElementById("button");
      btn.addEventListener("click",function() {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.open("GET", "http://localhost:5000/api/Search/The" , true);
        xmlhttp.onload = function(){
          var data = JSON.parse(xmlhttp.responseText);
          renderHTML(data);
        };
        xmlhttp.send();
      });

      renderHTML(Data){
        var String = "";

        for(i=0;i< Data.length;i++){
          String += Data[i].isbn + "Book ISBN" + Data[i].tittle + "Tittle of the book" + Data[i].author;
        }
      };
