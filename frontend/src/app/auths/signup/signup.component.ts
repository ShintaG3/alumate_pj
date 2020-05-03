import { Component } from '@angular/core';
import { FormGroup, FormControl, FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent {
  constructor(private fb: FormBuilder) {}

  signupForm = this.fb.group({
    username: [''],
    email: [''],
    password1: [''],
    password2: ['']
  });
  agreeOnPrivacyPolicy = false;
  submitReady = false;

  updatePolicyAgreement(): void {
    this.agreeOnPrivacyPolicy = !this.agreeOnPrivacyPolicy;
    this.submitReady = this.signupForm.valid && this.agreeOnPrivacyPolicy;
  }

  onSubmit(): void {
    console.log(this.signupForm.value);
  }


  // let agree_to_policy = document.getElementById('customCheckRegister');
  // let registerUser = document.getElementById('registerUser');
  // const password2 = document.getElementById('id_password2');
  // const password1 = document.getElementById('id_password1');
  // password1.addEventListener('input', checkPasswordStrength);
  // password2.addEventListener('keyup', checkPasswordMatch);
  // let pwdStrengthText = document.getElementById('pwdStrength')

  // function checkPasswordMatch(e) {
  //     if (e.target.value.length == 0) {
  //       password2.style.backgroundColor = '#fff';
  //       password2.style.color = '#8898AA';
  //     }
  //     else if (e.target.value == password1.value) {
  //         password2.style.backgroundColor = '#2DCE89';
  //         password2.style.color = '#ffff';
  //     }
  //     else {
  //       password2.style.backgroundColor = '#F75676';
  //       password2.style.color = '#ffff';
  //     }
  // }

  // function checkPasswordStrength(e) {
  //     if (e.target.value.length >= 8) {
  //       $.ajax({
  //         url: 'ajax/checkpwdstrength/',
  //         data: {
  //           'password': e.target.value
  //         },
  //         dataType: 'json',
  //         success: function (data) {
  //           if (data.status == 'strong') {
  //             pwdStrengthText.style.color = '#2DCE89';
  //           }
  //           else {
  //             pwdStrengthText.style.color = '#F75676';
  //           }
  //           pwdStrengthText.innerHTML = data.status;
  //         }
  //       });
  //     }
  //   else if (e.target.value.length > 0 && e.target.value.length < 8){
  //       pwdStrengthText.style.color = '#F75676';
  //       pwdStrengthText.innerHTML = 'weak';

  //     }
  //   else {
  //       pwdStrengthText.innerHTML = '';
  //     }
  //   }



  // agree_to_policy.onclick = function (){
  //     if (agree_to_policy.checked == true) {
  //       registerUser.disabled = false;
  //     }
  //     else {
  //       registerUser.disabled = true;
  //     }
  // }
}
