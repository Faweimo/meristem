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

 
/*
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

*/

// grab the all preview td 
let titleReview                   = document.querySelector('#person_title_review');
let surnameReview                 = document.querySelector('#person_surname_review');
let person_othername_review       = document.querySelector('#person_othername_review');
let person_phone_review           = document.querySelector('#person_phone_review');
let person_address_review         = document.querySelector('#person_address_review');
let person_companyName_review     = document.querySelector('#person_companyName_review');
let person_companyAddress_review  = document.querySelector('#person_companyAddress');
let person_idtype_review          = document.querySelector('#person_idtype_review');
let person_idnumber_review        = document.querySelector('#person_idnumber_review');
let person_pfa_review             = document.querySelector('#person_pfa_review');
let person_rsaNumber_review       = document.querySelector('#person_rsaNumber_review');
let person_firstname_review       = document.querySelector('#person_firstname_review');
let person_bankname_review = document.querySelector('#person_bankname_review');
let person_accountnumber_review = document.querySelector('#person_accountnumber_review');
let person_branch_review = document.querySelector('#person_branch_review');
// let titleReview = document.querySelector('#person_title_review');
// let titleReview = document.querySelector('#person_title_review');




// grab the all input  values 
let titleInput = document.querySelector('#person_title');
let person_surname = document.querySelector('#person_surname');
let person_othername = document.querySelector('#person_othername');
let person_phone = document.querySelector('#person_phone');
let person_address = document.querySelector('#person_address');
let person_company = document.querySelector('#person_company');
let person_companyAddress = document.querySelector('#person_companyAddress');
let means_of_id = document.querySelector('#means_of_id');
let person_idNumber = document.querySelector('#person_idNumber');
let person_pfa = document.querySelector('#person_pfa');
let person_rsaNumber = document.querySelector('#person_rsaNumber');
let person_firstname = document.querySelector('#person_firstname');
let bank_name = document.querySelector('#bank_name');
let person_accountNumber = document.querySelector('#person_accountNumber');
let person_accountBranch = document.querySelector('#person_accountBranch');



// grab the preview button 
let previewBtnAppend = document.querySelector('#myBtn');

previewBtnAppend.addEventListener('click',appendData,false);

function appendData(e) {
  e.preventDefault();
  
  // append the following input values 
  titleReview.textContent = titleInput.value;
  surnameReview.textContent = person_surname.value;
  person_othername_review.textContent = person_othername.value;
  person_phone_review.textContent = person_phone.value;
  person_address_review.textContent = person_address.value;
  person_companyName_review.textContent = person_company.value;
  person_companyAddress_review.textContent = person_companyAddress.value;
  person_idtype_review.textContent = means_of_id.value;

  person_pfa_review.textContent = person_pfa.value;
  person_rsaNumber_review.textContent = person_rsaNumber.value;
  person_firstname_review.textContent = person_firstname.value;
  person_idnumber_review.textContent = person_idNumber.value;

  person_bankname_review.textContent = bank_name.value;
  person_accountnumber_review.textContent = person_accountNumber.value;
  person_branch_review.textContent = person_accountBranch.value;

  console.log(person_firstname.value);
  console.log(person_idNumber.value);
  console.log(bank_name.value);
  console.log(person_accountNumber.value);
  console.log(person_accountBranch.value);
  console.log(person_companyAddress.value);




}