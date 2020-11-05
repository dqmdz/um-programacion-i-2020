import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CalculadoraSimpleRoutingModule } from './calculadora-simple-routing.module';
import { CalculadoraSimpleComponent } from './calculadora-simple.component';
import { CalculadoraComponent } from './calculadora/calculadora.component';
import { FormsModule } from "@angular/forms";
@NgModule({
    declarations: [CalculadoraSimpleComponent, CalculadoraComponent],
    imports: [
        CommonModule,
        CalculadoraSimpleRoutingModule,
        FormsModule
    ]
})
export class CalculadoraSimpleModule { }