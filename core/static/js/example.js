console.log('Hello world')

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
} 

 

// grab the preview button 
const previewBtn = document.querySelector('#myBtn');



// created dummy element to append the values of the input 
let para = document.querySelector('#textInput');




// adding eventlistener to the preview button 
previewBtn.addEventListener('click',modalsubmit,false)

// function after inputing the values 
function modalsubmit(e){
    e.preventDefault();
    
    // appending the values to the created dummy element
    const inputPost = document.getElementsByTagName('input');

    
    for (i = 1; i < inputPost.length; i++) {
        
            
        para.textContent += inputPost[i].value;
        
        console.log(para)
        
        

        
    }
    

}