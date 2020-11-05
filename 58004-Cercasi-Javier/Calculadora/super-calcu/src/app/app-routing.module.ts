import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [{ path: 'simple', loadChildren: () => import('./calculadora-simple/calculadora-simple.module').then(m => m.CalculadoraSimpleModule) }, { path: 'cambio', loadChildren: () => import('./calculadora-cambio/calculadora-cambio.module').then(m => m.CalculadoraCambioModule) }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
