import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CalculadoraSimpleComponent } from './calculadora-simple.component';

const routes: Routes = [{ path: '', component: CalculadoraSimpleComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CalculadoraSimpleRoutingModule { }
