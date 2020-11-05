import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CalculadoraCambioComponent } from './calculadora-cambio.component';

const routes: Routes = [{ path: '', component: CalculadoraCambioComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CalculadoraCambioRoutingModule { }
