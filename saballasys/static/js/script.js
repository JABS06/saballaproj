       		    function opendivlist() {
                            document.getElementById("Divlist").style.display = "block";
                        }

                        function closedivlist() {
                            document.getElementById("Divlist").style.display = "none";
                        }
                       

                        function computeprice(input){
                        var comp = document.querySelectorAll(".myBtn:checked");
                        var total = 0;
                        var cart =[];

                        items="";
                        comp.forEach(function(aa){
                           total += parseInt(aa.getAttribute('id'));
                           items += (aa.getAttribute('value'));
                       });
                        cart.push(items)
                        document.getElementById('tprice').value ="Total: ₱"+ total;
                        document.getElementById('listahan').innerHTML = cart ;
                        
                    } ;
                        document.getElementById("rstbtn").onclick =function(){
                        document.getElementById("listahan").innerHTML = deleteRow(1);
  
                    };
                      selectdiv("amdproc")
                      function selectdiv(c) {
                          var x, i;
                          x = document.getElementsByClassName("compDiv");
                          if (c == "amdproc") c = "amdproc";
                          for (i = 0; i < x.length; i++) {
                              next(x[i], "show");
                              if (x[i].className.indexOf(c) > -1) add(x[i], "show");
                          }
                      }

                      function add(element, name) {
                          var i, arr1, arr2;
                          arr1 = element.className.split(" ");
                          arr2 = name.split(" ");       
                          for (i = 0; i < arr2.length; i++) {
                              if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + 				arr2[i];}
                          }
                      }

                      function next(element, name) {
                          var i, arr1, arr2;
                          arr1 = element.className.split(" ");
                          arr2 = name.split(" ");
                          for (i = 0; i < arr2.length; i++) {
                              while (arr1.indexOf(arr2[i]) > -1) {
                                  arr1.splice(arr1.indexOf(arr2[i]), 1);     
                              }
                          }
                          element.className = arr1.join(" ");
                      }
