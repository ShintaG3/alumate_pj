import { FormGroup, FormControl } from '@angular/forms';
import { Component, OnInit, EventEmitter, Output, Input } from '@angular/core';
import { Options } from 'ng5-slider';

@Component({
  selector: 'app-slider',
  templateUrl: './slider.component.html',
  styleUrls: ['./slider.component.css']
})
export class SliderComponent implements OnInit {
  @Input() lowerBound = 1980;
  @Input() upperBound = 2030;
  @Input() sliderName: string;

  @Output() sliderFormChanged = new EventEmitter<FormGroup>();

  sliderForm: FormGroup = new FormGroup({
    range: new FormControl([this.lowerBound, this.upperBound])
  });

  sliderOptions: Options = {
    floor: this.lowerBound,
    ceil: this.upperBound,
    animate: false
  };

  constructor() { }

  ngOnInit(): void {
  }

  updateSlider() {
    this.sliderFormChanged.emit(this.sliderForm);
  }
}
