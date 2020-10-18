import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms'
import { HttpClient } from '@angular/common/http'

@Component({
  selector: 'app-grocery-form',
  templateUrl: './grocery-form.component.html',
  styleUrls: ['./grocery-form.component.scss']
})
export class GroceryFormComponent implements OnInit {
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

  ngOnInit(): void {
  }

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
}
