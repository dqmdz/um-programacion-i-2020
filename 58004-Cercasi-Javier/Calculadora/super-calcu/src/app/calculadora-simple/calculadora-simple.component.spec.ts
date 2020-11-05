import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CalculadoraSimpleComponent } from './calculadora-simple.component';

describe('CalculadoraSimpleComponent', () => {
  let component: CalculadoraSimpleComponent;
  let fixture: ComponentFixture<CalculadoraSimpleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CalculadoraSimpleComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CalculadoraSimpleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
