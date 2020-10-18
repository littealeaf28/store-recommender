import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Validators} from '@angular/forms';

import { from } from 'rxjs'
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'frontend';
  url='https://store-recommender.wn.r.appspot.com/';
  groceryList='';
  optimalStore : any;

  err = {
    isErr: false,
    message: ""
  };

  constructor(
    public fb : FormBuilder,
    public http : HttpClient
  ){}

  /*groceryForm = this.fb.group({
    list:['',Validators.required]
  });*/
}
