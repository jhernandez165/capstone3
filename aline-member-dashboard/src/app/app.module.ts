import {NgModule} from '@angular/core';

import {AppComponent} from './app.component';
import {AppRoutingModule} from './app-routing.module';
import {LoginModule} from '@login/login.module';
import {FontAwesomeModule} from '@fortawesome/angular-fontawesome';
import {RegistrationModule} from '@registration/registration.module';
import {CoreModule} from '@core/core.module';
import {GlobalModalModule} from '@app/global-modal/global-modal.module';
import {NotFoundComponent} from './not-found/not-found.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {ServiceWorkerModule} from '@angular/service-worker';
import {environment} from '@environments/environment';
import {CardModule} from '@app/card/card.module';
import { AuthInterceptor } from '@core/interceptors/auth.interceptor';
import { HTTP_INTERCEPTORS } from '@angular/common/http';

@NgModule({
    declarations: [
        AppComponent,
        NotFoundComponent
    ],
    imports: [
        BrowserAnimationsModule,
        CoreModule,
        AppRoutingModule,
        LoginModule,
        CardModule,
        RegistrationModule,
        FontAwesomeModule,
        GlobalModalModule,
        ServiceWorkerModule.register('ngsw-worker.js', {
            enabled: environment.production,
            registrationStrategy: 'registerWhenStable:30000'
        })
    ],
    providers: [{
        provide: HTTP_INTERCEPTORS,
        useClass: AuthInterceptor,
        multi: true,
    }],
    bootstrap: [AppComponent]
})
export class AppModule {}
