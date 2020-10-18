import { Component, OnInit } from '@angular/core';
import { Loader } from 'google-maps';

@Component({
  selector: 'app-store-map',
  templateUrl: './store-map.component.html',
  styleUrls: ['./store-map.component.scss']
})
export class StoreMapComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  initMap() {
    // const uluru = { lat: -25.344, lng: 131.036 };
    // // The map, centered at Uluru
    // const map = new google.maps.Map(document.getElementById("map"), {
    //   zoom: 4,
    //   center: uluru,
    // });
    // // The marker, positioned at Uluru
    // const marker = new google.maps.Marker({
    //   position: uluru,
    //   map: map,
    // });
  }
}
