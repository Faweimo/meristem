// console.log('Hello world')

// bank details
$(document).ready(function(){
  
 
    $('#add_more_bank').hide()

    $('#more-line').click(function(){
        $('#add_more_bank').slideToggle(200)
    })
    let removeBtn = document.querySelector('#more-line')
    removeBtn.removeAttribute('more-line')
    

 
 
});

// adding extra bank fields 

let addBtn= document.querySelector('#more-line');
addBtn.setAttribute('class','extrafields');

console.log(addBtn)

$(document).ready(function(){
  
 
    $('#add_more_bank3').hide()

    $('.extrafields').click(function(){
        $('#add_more_bank3').slideToggle(200)
    })
    

 
 
});

// beneficiary details
$(document).ready(function(){
  
    // e.preventDefault();
//   alert("We are all set!");
    $('#more_beneficiary').hide()

    $('#more-beneficiary').click(function(){
        $('#more_beneficiary').slideToggle(200)
    })
    

 
 
});