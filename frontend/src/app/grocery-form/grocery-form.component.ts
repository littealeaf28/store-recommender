import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { from } from 'rxjs'

@Component({
  selector: 'app-grocery-form',
  templateUrl: './grocery-form.component.html',
  styleUrls: ['./grocery-form.component.scss']
})
export class GroceryFormComponent implements OnInit {
  endpoint = 'https://store-recommender.wn.r.appspot.com/';
  groceryList = '';
  err: null | string = null;

  constructor(public http: HttpClient) {
  }

  ngOnInit(): void {
  }

  onSubmit() {
    //first get location
    if(navigator.geolocation) {
      //get geolocation uses callbacks cause it's kind of old TnT
      navigator.geolocation.getCurrentPosition((location) => {
        const body = {
          location: {
            latitude: location.coords.latitude,
            longitude: location.coords.longitude
          },
          groceries: this.groceryList.split(',')
        }

        this.http.post(this.endpoint, body).subscribe((res) => {
          console.log(res)
        })
      })
    } else {
      this.err = 'Please activate geolocation'
    }
  }
}
