import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CalculadoraCambioComponent } from './calculadora-cambio.component';

describe('CalculadoraCambioComponent', () => {
  let component: CalculadoraCambioComponent;
  let fixture: ComponentFixture<CalculadoraCambioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CalculadoraCambioComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CalculadoraCambioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
