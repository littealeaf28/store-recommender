import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Validators} from '@angular/forms';

import { from } from 'rxjs'
import {Loader} from 'google-maps';

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



  onSubmit(){
    //first get location
    console.log("We are submitting");
    if(navigator.geolocation){
      //get geolocation uses callbacks cause it's kind of old TnT
      navigator.geolocation.getCurrentPosition((location)=>{
        //location.latitude, location.longitude
        console.log(location);
        const body = {
          location: location.coords,
          groceries : this.groceryList.split(',')
        }
        this.http.post(this.url,body).subscribe((optimal)=>{
          if(optimal){
            this.optimalStore = optimal;
          }
          else{
            this.err = {
              isErr: true,
              message: "There were no optimal stores found"
            }
          }
        },
        (err)=>{
          console.log(err);
        })
      })
    }
    else{
      this.err = {
        isErr: true,
        message: "Geolocation is not supported by this browser"
      }
    }

  }

  generateMap(res) {
    // Just make sure the res output looks right
    const user = res['user_geolocation'];
    const store = res['store'].geolocation;
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 4,
      center: user,
    });
    const marker = new google.maps.Marker({
      position: user,
      map: map,
    });
    const best_store = new google.maps.Marker({
      position: store,
      map: map,
    });
  }
}


