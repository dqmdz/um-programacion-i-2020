import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CalculadoraCambioRoutingModule } from './calculadora-cambio-routing.module';
import { CalculadoraCambioComponent } from './calculadora-cambio.component';
import { CalculadoraComponent } from './calculadora/calculadora.component';
import { FormsModule } from "@angular/forms";
@NgModule({
    declarations: [CalculadoraCambioComponent, CalculadoraComponent],
    imports: [
        CommonModule,
        CalculadoraCambioRoutingModule,
        FormsModule
    ]
})
export class CalculadoracambioModule { }