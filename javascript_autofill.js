// ==UserScript==
// @name        autofilljavascript
// @namespace   all
// @include     *
// @version     1
// @grant       none
// ==/UserScript==





(function() {
  'use strict'


  window.addEventListener('load', () => {
    addButton('benjamin', selectReadFn);
    var t=setInterval(populate,1000);
    console.log("asdadadsdassdasadsdasdsadasdasdasa");
  });
  
  
  function addButton(text, onclick, cssObj) {
    cssObj = cssObj || {
      position: 'absolute',
      bottom: '7%',
      left: '4%',
      'z-index': 3
    }
    let button = document.createElement('button'),
      btnStyle = button.style
    document.body.appendChild(button)
    button.innerHTML = text
    button.onclick = onclick
    Object.keys(cssObj).forEach(key => btnStyle[key] = cssObj[key])
    return button
  }
  function populate()
  {
    document.getElementById("account-firstName").value = "adadadas";
    document.getElementById("account-lastName").value = "adadadas";
    document.getElementById("account-email").value = "adadadas";
    document.getElementById("account-phone").value = "adadadas";
    document.getElementById("account-birthDate").value = "adadadas";
    document.getElementById("password-newPassword").value = "adadadas";
    document.getElementById("password-confirmPassword").value = "adadadas";
    document.getElementById("account-receiveEmail").checked = true;
    document.getElementById("account-receiveSms").checked = true;
    document.getElementByClassName("recaptha-checkbox-checkmark").checked = true;

  }


  function selectReadFn() {
	  window.location = "https://www.gratis.com/sign-up";	



  }
}())